#!/usr/bin/env python3
"""把文章 HTML 里的图片内嵌成 base64 data URI，产出「单文件、可整份复制」的产物。

为什么：外链图床会防盗链、会过期，本地图片复制到公众号后台时路径直接失效；内嵌后
图片跟着 HTML 走，粘贴时由公众号编辑器转存到自己的素材库。

本地图片的路径解析（重点）：
    依次按「HTML 所在目录 → 当前目录 → 各自往上两级 → --source-dir」查找；
    都找不到时，再按文件名在这些目录树里唯一定位（同名多份会报错让你写全路径）。
    所以 `images/1.png` 这种相对 docx/md 的路径，即使 HTML 存在别的目录也能命中。

处理规则：
  - `mmbiz.qpic.cn`（已在微信 CDN）默认保留原链接：它本来就是微信要的地址，
    再内嵌只是白白 +33% 体积；想强制内嵌用 --inline-all
  - 本地图片 / 其它外链默认内嵌（我们这边能下载 ≠ 微信粘贴时能取到，base64 才稳）
  - 图床稳定、想保留原链接：--keep-remote（全部远程）或 --keep-host 域名
  - 已经是 `data:` 的 src 跳过
  - `http(s)://` 链接 → 下载后内嵌（带 UA、超时、单图体积上限）
  - 本地路径 / `file://` → 读文件内嵌（自动 unquote、`\\` 转 `/`、去掉 `?v=1` 之类）
  - MIME 按文件头识别（png/jpeg/gif/webp/bmp/svg/ico），不靠扩展名
  - 占位符（`图片URL`、`{{图片URL}}`、`【…】`、空）单独计数并提示补真实路径
  - HTML 注释里的示例 `<img>` 不动

用法:
    inline_images.py 文章.html                  # 产出 文章_内嵌.html
    inline_images.py 文章.html -o out.html
    inline_images.py 文章.html --source-dir ./原稿目录
    inline_images.py 文章.html --check          # 只体检，不写文件

选项:
    --source-dir DIR    额外查找根目录，可重复（如 md / docx 所在目录）
    --max-image-mb N    单图上限，超限则跳过并保留原 src（默认 3）
    --timeout N         下载超时秒数（默认 15）
    --check             只打印结果，不写文件

退出码: 0 = 全部内嵌成功（或本就没有图片）; 1 = 有图片没内嵌成功（含占位图）。
"""

import argparse
import base64
import html as htmlmod
import os
import re
import sys
import urllib.parse
import urllib.request

IMG_SRC = re.compile(r"""(<img\b[^>]*?\bsrc\s*=\s*)(["'])(.*?)\2""", re.I | re.S)
COMMENT = re.compile(r"<!--.*?-->", re.S)
# 公众号后台对 webp / svg / ico 支持不稳定，提示换成 png/jpg
WECHAT_SAFE = {"image/png", "image/jpeg", "image/gif", "image/bmp"}
MAGIC = [
    (b"\x89PNG\r\n\x1a\n", "image/png"),
    (b"\xff\xd8\xff", "image/jpeg"),
    (b"GIF87a", "image/gif"),
    (b"GIF89a", "image/gif"),
    (b"BM", "image/bmp"),
    (b"\x00\x00\x01\x00", "image/x-icon"),
]
PLACEHOLDER = re.compile(
    r"^(?:|图片URL|图片地址|图片链接|图片|URL|url|#|about:blank"
    r"|\{\{.*\}\}|【.*】|\$.*)$", re.I)
SKIP_DIRS = {".git", "node_modules", "__pycache__", ".venv", "venv", ".idea", ".vscode"}
ROOT_ANCESTORS = 2


def sniff_mime(data):
    """按文件头识别 MIME；识别不出时回退到 svg / octet-stream。"""
    for magic, mime in MAGIC:
        if data.startswith(magic):
            return mime
    if data[:4] == b"RIFF" and data[8:12] == b"WEBP":
        return "image/webp"
    head = data[:512].lstrip().lower()
    if head.startswith(b"<svg") or (head.startswith(b"<?xml") and b"<svg" in head):
        return "image/svg+xml"
    return "application/octet-stream"


def shorten(path, limit=56):
    """中间省略，保留开头（哪个项目）和结尾（哪个文件）。"""
    p = path.replace(os.path.expanduser("~"), "~", 1)
    if len(p) <= limit:
        return p
    keep = limit - 1
    head = keep * 2 // 3
    return p[:head] + "…" + p[-(keep - head):]


def candidate_roots(base_dir, source_dirs):
    """HTML 目录、cwd、各自上两级、--source-dir，去重保序。"""
    roots = []

    def add(d):
        try:
            d = os.path.abspath(d)
        except (TypeError, ValueError):
            return
        if os.path.isdir(d) and d not in roots:
            roots.append(d)

    add(base_dir)
    add(os.getcwd())
    for base in (base_dir, os.getcwd()):
        p = os.path.abspath(base)
        for _ in range(ROOT_ANCESTORS):
            p = os.path.dirname(p)
            # 不把 / 或 /tmp 这类过浅的目录当搜索根，避免慢扫整盘
            if len(p.split(os.sep)) >= 3:
                add(p)
    for d in source_dirs or []:
        add(d)
    return roots


def normalize_src(src):
    p = htmlmod.unescape(src).strip()
    if p.lower().startswith("file://"):
        p = p[7:]
    p = p.split("?")[0].split("#")[0].replace("\\", "/")
    return urllib.parse.unquote(p)


def find_by_basename(name, roots, max_depth=3, max_files=8000):
    """在 roots 下按文件名找，返回命中列表（最多 2 个就够判定歧义）。

    嵌套的搜索根会让同一文件被走两次，按 realpath 去重。
    """
    hits, seen, scanned = [], set(), 0
    for root in roots:
        base_depth = root.rstrip(os.sep).count(os.sep)
        for dirpath, dirnames, filenames in os.walk(root):
            dirnames[:] = sorted(d for d in dirnames
                                 if d not in SKIP_DIRS and not d.startswith("."))
            if dirpath.rstrip(os.sep).count(os.sep) - base_depth >= max_depth:
                dirnames[:] = []
            scanned += len(filenames)
            if name in filenames:
                path = os.path.join(dirpath, name)
                real = os.path.realpath(path)
                if real not in seen:
                    seen.add(real)
                    hits.append(path)
                if len(hits) > 1:
                    return hits
            if scanned > max_files:
                return hits
    return hits


def resolve_local(src, roots):
    """返回 (绝对路径 | None, 说明)。"""
    p = normalize_src(src)
    if not p:
        return None, "空的 src"
    if os.path.isabs(p):
        return (p, "绝对路径") if os.path.isfile(p) else (None, f"文件不存在：{shorten(p)}")
    tried = []
    for root in roots:
        cand = os.path.normpath(os.path.join(root, p))
        tried.append(cand)
        if os.path.isfile(cand):
            tag = "本地" if root == roots[0] else f"本地（在 {shorten(root, 32)} 找到）"
            return cand, tag
    name = os.path.basename(p)
    hits = find_by_basename(name, roots) if name else []
    if len(hits) == 1:
        return hits[0], f"本地（按文件名匹配到 {shorten(hits[0])}）"
    if len(hits) > 1:
        return None, (f"文件名 {name} 在 {len(hits)} 处命中（"
                      + "、".join(shorten(h, 36) for h in hits[:3])
                      + "），请写完整相对路径")
    where = "、".join(shorten(t, 40) for t in tried[:2])
    more = " 等" if len(tried) > 2 else ""
    return None, f"找不到文件（试过 {where}{more}）"


def load_source(src, roots, timeout):
    if re.match(r"^https?://", src, re.I):
        url = htmlmod.unescape(src)
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 gzh-design"})
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.read(), "下载", url
    path, how = resolve_local(src, roots)
    if not path:
        raise FileNotFoundError(how)
    with open(path, "rb") as f:
        return f.read(), how, path


def human(n):
    if n >= 1024 * 1024:
        return f"{n / 1024 / 1024:.1f}MB"
    if n >= 1024:
        return f"{n / 1024:.0f}KB"
    return f"{n}B"


def inline(html, base_dir, max_image_mb, timeout, log=print,
           source_dirs=None, keep_remote=False, keep_hosts=None, inline_all=False):
    """把 HTML 里的 img src 换成 data URI；返回 (新 HTML, 统计)。

    keep_remote=True 保留所有 http(s) 链接；keep_hosts 指定额外保留的域名；
    inline_all=True 连微信 CDN 图也内嵌（完全离线单文件）。
    """
    comments = [(m.start(), m.end()) for m in COMMENT.finditer(html)]
    roots = candidate_roots(base_dir, source_dirs)
    keep_set = {"mmbiz.qpic.cn"} if not inline_all else set()
    keep_set |= {h.lower() for h in (keep_hosts or []) if h}
    stats = {"ok": 0, "kept": 0, "skipped": 0, "placeholder": 0,
             "failed": 0, "bytes": 0}
    limit = int(max_image_mb * 1024 * 1024)
    cache = {}

    def in_comment(pos):
        return any(a <= pos < b for a, b in comments)

    def repl(m):
        src = m.group(3).strip()
        if in_comment(m.start()):
            return m.group(0)
        if src.lower().startswith("data:"):
            stats["skipped"] += 1
            return m.group(0)
        if re.match(r"^https?:|^//", src, re.I) and not inline_all:
            host = (urllib.parse.urlparse(src).hostname or "").lower()
            if keep_remote or host in keep_set:
                stats["kept"] += 1
                why = "已在微信 CDN" if host in {"mmbiz.qpic.cn"} else "按 --keep-remote/--keep-host 保留"
                log(f"   ↔ 保留原链接（{why}）{shorten(src, 60)}")
                return m.group(0)
        if PLACEHOLDER.match(src):
            stats["placeholder"] += 1
            log(f"   ⚠ 占位图未替换「{src or '(空 src)'}」— 换成真实图片路径后重跑")
            return m.group(0)
        try:
            data, how, key = load_source(src, roots, timeout)
        except Exception as e:  # 网络/路径失败：保留原样，别让整篇排版报废
            stats["failed"] += 1
            log(f"   ✗ {shorten(src, 60)} — {str(e)[:100]}")
            return m.group(0)
        if key in cache:
            uri = cache[key]
            stats["ok"] += 1
            log(f"   ✓ {shorten(src, 60)} — 与前面同一张图，复用")
            return f"{m.group(1)}{m.group(2)}{uri}{m.group(2)}"
        if len(data) > limit:
            stats["failed"] += 1
            log(f"   ✗ {shorten(src, 60)} — {human(len(data))} 超过单图上限 "
                f"{max_image_mb}MB，保留原 src")
            return m.group(0)
        mime = sniff_mime(data)
        if not mime.startswith("image/"):
            # 多半是防盗链返回的 HTML、登录页或 404 页：内嵌成 data URI 只会得到裂图
            stats["failed"] += 1
            log(f"   ✗ {shorten(src, 60)} — 返回的不是图片（{mime}），保留原 src")
            return m.group(0)
        if mime not in WECHAT_SAFE:
            log(f"   ⚠ {shorten(src, 60)} — {mime}，公众号后台支持不稳定，建议先转 png/jpg")
        uri = f"data:{mime};base64,{base64.b64encode(data).decode('ascii')}"
        cache[key] = uri
        stats["ok"] += 1
        stats["bytes"] += len(data)
        log(f"   ✓ {human(len(data)):>6} {mime:<14} {how} {shorten(src, 56)}")
        return f"{m.group(1)}{m.group(2)}{uri}{m.group(2)}"

    return IMG_SRC.sub(repl, html), stats


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("file", help="要处理的 HTML")
    ap.add_argument("-o", "--out", help="输出路径（默认 <原名>_内嵌.html）")
    ap.add_argument("--in-place", action="store_true", help="覆盖原文件（留 .bak 备份）")
    ap.add_argument("--base-dir", default=None, help="相对路径图片的主根目录")
    ap.add_argument("--source-dir", action="append", default=[],
                    help="额外查找根目录，可重复（如 md / docx 所在目录）")
    ap.add_argument("--max-image-mb", type=float, default=3.0, help="单图上限（默认 3MB）")
    ap.add_argument("--timeout", type=int, default=15, help="下载超时秒数（默认 15）")
    ap.add_argument("--check", action="store_true", help="只体检，不写文件")
    ap.add_argument("--keep-remote", action="store_true",
                    help="保留所有 http(s) 图片链接（图床稳定时用，体积更小）")
    ap.add_argument("--keep-host", action="append", default=[], metavar="HOST",
                    help="额外保留这些域名的链接，可重复。默认已保留 mmbiz.qpic.cn")
    ap.add_argument("--inline-all", action="store_true",
                    help="连微信 CDN 图也内嵌，产出完全离线的单文件")
    args = ap.parse_args()

    if not os.path.isfile(args.file):
        print(f"✗ 找不到文件: {args.file}")
        sys.exit(2)
    src_path = os.path.abspath(args.file)
    base_dir = args.base_dir or os.path.dirname(src_path)
    text = open(src_path, encoding="utf-8").read()

    print(f"🖼  内嵌图片: {args.file}")
    roots = candidate_roots(base_dir, args.source_dir)
    print(f"   查找根目录: {' → '.join(shorten(r, 44) for r in roots[:4])}"
          + (" 等" if len(roots) > 4 else ""))
    out_html, stats = inline(text, base_dir, args.max_image_mb, args.timeout,
                             source_dirs=args.source_dir,
                             keep_remote=args.keep_remote,
                             keep_hosts=args.keep_host,
                             inline_all=args.inline_all)

    total = len(out_html.encode("utf-8"))
    print(f"\n   内嵌 {stats['ok']} 张（{human(stats['bytes'])} 原始数据），"
          f"保留链接 {stats['kept']}，跳过 {stats['skipped']}（已是 base64），"
          f"占位 {stats['placeholder']}，失败 {stats['failed']}")
    print(f"   产物大小 {human(total)}")
    if total > 8 * 1024 * 1024:
        print("   ⚠ 超过 8MB：公众号编辑器粘贴大段 HTML 可能卡顿甚至失败，"
              "建议压缩图片（长边 ≤ 1080px、jpg 质量 80）后重跑")
    if stats["placeholder"]:
        print("   ⚠ 还有占位图没换成真实路径：把原文的 ![](图片文件名) 换成实际文件再重跑")

    if args.check:
        print("   （--check：只体检，未写文件）")
        sys.exit(1 if stats["failed"] or stats["placeholder"] else 0)

    if args.in_place:
        import shutil
        shutil.copy2(args.file, args.file + ".bak")
        out = args.file
        print(f"   已覆盖原文件（备份 {os.path.basename(args.file)}.bak）")
    else:
        out = args.out or os.path.splitext(args.file)[0] + "_内嵌.html"
    open(out, "w", encoding="utf-8").write(out_html)
    print(f"✓ 已生成: {out}")
    sys.exit(1 if stats["failed"] or stats["placeholder"] else 0)


if __name__ == "__main__":
    main()

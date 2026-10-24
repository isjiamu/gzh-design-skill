#!/usr/bin/env python3
"""组件库源头检查器 —— 可验证循环的第一道关。

扫描 references/ 下所有组件库 .md 里的 ```html 代码块，检测会导致
排版问题的反模式。只看真实组件 HTML，不被说明文字干扰（grep 做不到）。

与 validate_gzh_html.py 配合构成闭环：
  改组件库 → component_lint.py 扫源头 → 生成产物 → validate_gzh_html.py 扫产物 → 修 → 重复

用法：
    component_lint.py [skill-dir]   # 默认当前目录
退出码：1 = 有 ERROR，0 = 通过。
"""

import glob
import os
import re
import sys

CJK = re.compile(r"[一-鿿㐀-䶿]")

# (正则, 级别, 说明) —— 在每个 ```html 组件块内检查
CHECKS = [
    (re.compile(r"white-space\s*:\s*pre", re.I), "ERROR",
     "用了 white-space:pre —— 会把 HTML 源码缩进/换行渲染成大左缩进+空行；"
     "代码块改成每行一个 <p style=\"margin:0\">，缩进用全角空格"),
    (re.compile(r"</?div[\s>]", re.I), "ERROR", "出现 <div>，应用 <section>"),
    (re.compile(r"\sclass\s*=", re.I), "ERROR", "出现 class 属性（会被公众号剥离）"),
    (re.compile(r"\sid\s*=", re.I), "ERROR", "出现 id 属性"),
    (re.compile(r"<style[\s>]", re.I), "ERROR", "出现 <style> 标签"),
    (re.compile(r"position\s*:\s*(fixed|absolute|sticky)", re.I), "ERROR",
     "position fixed/absolute/sticky 不被支持"),
    (re.compile(r"display\s*:\s*grid", re.I), "ERROR", "display:grid 不被支持"),
    (re.compile(r"var\s*\(\s*--", re.I), "ERROR", "用了 CSS 变量 var(--x)"),
    (re.compile(r"@(media|keyframes|import)", re.I), "ERROR", "@media/@keyframes/@import 不被支持"),
    # ---- 2026-10 公众号编辑器粘贴实测崩坏项（详见 SKILL.md 平台红线） ----
    (re.compile(r"<svg[\s>]", re.I), "ERROR",
     "<svg> 粘贴后被静默剥掉，图标改 Emoji/文字"),
    (re.compile(r"<video[\s>]", re.I), "ERROR",
     "视频无法粘贴带入，用占位框提示编辑器手动插入"),
    (re.compile(r"</?h[456][\s>]", re.I), "ERROR",
     "<h4>~<h6> 粘贴后样式丢失，小标题用带样式的 <p>"),
    (re.compile(r"<img[^>]+src\s*=\s*[\"'](?!https?://|\{\{)[^\"']*[\"']", re.I), "ERROR",
     "组件写死相对/本地图片地址，粘贴必丢——改 {{占位}} 并在实例化时填公网 URL"),
    (re.compile(r"display\s*:\s*flex", re.I), "WARN",
     "flex 布局粘贴不可靠（gap 必丢），建议垂直堆叠或 inline-block+margin"),
    (re.compile(r"(?<![\w-])gap\s*:", re.I), "WARN", "gap 粘贴时被丢弃，间距改 margin"),
    (re.compile(r"letter-spacing\s*:\s*-", re.I), "WARN", "负字距被规范化，去掉负值"),
    (re.compile(r"text-align\s*:\s*justify", re.I), "WARN", "中文 justify 粘贴后字距拉花，用左对齐"),
    (re.compile(r"overflow(?:-x)?\s*:\s*(?:scroll|auto)", re.I), "WARN",
     "滚动容器在公众号内不可用，改垂直堆叠"),
    (re.compile(r"<img[^>]+src\s*=\s*[\"']\{\{", re.I), "WARN",
     "图片 src 是占位符：实例化时必须填公网 http(s) URL，否则粘贴后图片静默消失"),
]

# 四周虚线框：border: ... dashed（不含方向，如 border-left dashed 不算）
FOURSIDE_DASHED = re.compile(r"border\s*:\s*[^;{}]*dashed", re.I)
CENTERED = re.compile(r"text-align\s*:\s*center", re.I)


def lint_file(path):
    text = open(path, encoding="utf-8", errors="replace").read()
    name = os.path.basename(path).replace("公众号排版组件库 —— ", "").replace(".md", "")
    found = []  # (level, msg)
    seen = set()

    def add(level, msg):
        if msg not in seen:
            seen.add(msg)
            found.append((level, msg))

    for m in re.finditer(r"```html\s*\n(.*?)```", text, re.S):
        html = m.group(1)
        for rx, level, msg in CHECKS:
            if rx.search(html):
                add(level, msg)
        # 四周虚线框：正文强调勿用；居中块视为"占位/素材"组件，豁免
        if FOURSIDE_DASHED.search(html) and not CENTERED.search(html):
            add("WARN", "四周虚线框 border:…dashed（正文强调请用左竖条；"
                        "仅居中的素材占位块可用 dashed）")
    return name, found


def main():
    root = sys.argv[1] if len(sys.argv) > 1 else "."
    refs = sorted(glob.glob(os.path.join(root, "references", "*.md")))
    if not refs:
        print(f"未找到 {root}/references/*.md")
        sys.exit(1)

    total_err = total_warn = clean = 0
    print(f"📐 组件库源头检查：{len(refs)} 个库\n")
    for path in refs:
        name, found = lint_file(path)
        if not found:
            clean += 1
            continue
        errs = [m for lv, m in found if lv == "ERROR"]
        warns = [m for lv, m in found if lv == "WARN"]
        total_err += len(errs)
        total_warn += len(warns)
        print(f"── {name} ──")
        for m in errs:
            print(f"   ❌ {m}")
        for m in warns:
            print(f"   ⚠️  {m}")

    print(f"\n汇总：{clean}/{len(refs)} 个库干净，ERROR×{total_err}，WARN×{total_warn}")
    if total_err == 0 and total_warn == 0:
        print("✅ 全部组件库源头无反模式")
    sys.exit(1 if total_err else 0)


if __name__ == "__main__":
    main()

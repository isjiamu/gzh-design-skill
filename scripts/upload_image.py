#!/usr/bin/env python3
"""图片上传图床，把本地图换成公众号能抓取的公网 URL。

公众号编辑器粘贴 HTML 时，<img src="https://公网URL"> 会被微信自动抓取转存；
但本地路径（./images/x.png）微信访问不到 → 图裂。本脚本把本地图上传到图床
（七牛/OSS/COS…），返回公网 URL，替换进排版产物即可。

用法:
    upload_image.py <图1> [图2 ...]      # 逐个上传，输出「本地路径<TAB>公网URL」
    upload_image.py --json <图...>        # 输出 JSON: {"本地路径": "URL", ...}
    upload_image.py --check               # 只检查配置（用哪个图床、密钥齐不齐），不上传

配置（密钥绝不进仓库）——两种来源，环境变量优先:
  A. 环境变量:
       GZH_IMAGE_HOST=qiniu                （可选，默认 qiniu）
       QINIU_ACCESS_KEY / QINIU_SECRET_KEY / QINIU_BUCKET / QINIU_DOMAIN
       QINIU_UP_HOST（可选，默认 https://up.qiniup.com；区域报错时按七牛控制台改）
  B. 本地配置文件 ~/.gzh-design/image-host.json（已在 .gitignore 忽略）:
       {"host":"qiniu","qiniu":{"access_key":"","secret_key":"","bucket":"","domain":"https://cdn.example.com"}}

行为:
  - 传入的是 http/https 远程 URL → 原样返回（不上传）
  - 本地图 → 按内容 sha256 命名 gzh-design/<hash>.<ext>，同图永远同 URL（幂等）
  - 本地缓存 ~/.gzh-design/upload-cache.json（hash→URL），重排同文不重复上传
  - 没配密钥 → stderr 明确提示 + 退出码 2（Agent 据此提醒用户去配置或手动上传）

退出码: 0 成功 / 2 未配置或密钥缺失 / 1 上传失败。
"""

import base64
import hashlib
import hmac
import json
import mimetypes
import os
import sys
import time
import urllib.request
import uuid

HOME_CFG = os.path.expanduser("~/.gzh-design")
CONFIG_FILE = os.path.join(HOME_CFG, "image-host.json")
CACHE_FILE = os.path.join(HOME_CFG, "upload-cache.json")


# ---------- 配置加载（环境变量优先，再读本地配置文件） ----------
def load_config():
    cfg = {}
    if os.path.isfile(CONFIG_FILE):
        try:
            cfg = json.load(open(CONFIG_FILE, encoding="utf-8"))
        except Exception:
            cfg = {}
    host = os.environ.get("GZH_IMAGE_HOST") or cfg.get("host") or "qiniu"
    q = cfg.get("qiniu", {})
    qiniu = {
        "access_key": os.environ.get("QINIU_ACCESS_KEY") or q.get("access_key"),
        "secret_key": os.environ.get("QINIU_SECRET_KEY") or q.get("secret_key"),
        "bucket": os.environ.get("QINIU_BUCKET") or q.get("bucket"),
        "domain": os.environ.get("QINIU_DOMAIN") or q.get("domain"),
        "up_host": os.environ.get("QINIU_UP_HOST") or q.get("up_host")
                   or "https://up.qiniup.com",
    }
    return host, {"qiniu": qiniu}


def missing_qiniu(q):
    return [k for k in ("access_key", "secret_key", "bucket", "domain") if not q.get(k)]


# ---------- 本地缓存 ----------
def load_cache():
    try:
        return json.load(open(CACHE_FILE, encoding="utf-8"))
    except Exception:
        return {}


def save_cache(cache):
    os.makedirs(HOME_CFG, exist_ok=True)
    json.dump(cache, open(CACHE_FILE, "w", encoding="utf-8"),
              ensure_ascii=False, indent=2)


# ---------- 七牛适配器（原生 API，无需第三方 SDK） ----------
def _b64(data):
    return base64.urlsafe_b64encode(data).decode()


def qiniu_upload_token(ak, sk, bucket, key, expires=3600):
    policy = {"scope": f"{bucket}:{key}", "deadline": int(time.time()) + expires}
    encoded_policy = _b64(json.dumps(policy).encode())
    sign = hmac.new(sk.encode(), encoded_policy.encode(), hashlib.sha1).digest()
    return f"{ak}:{_b64(sign)}:{encoded_policy}"


def qiniu_put(q, key, filepath):
    token = qiniu_upload_token(q["access_key"], q["secret_key"], q["bucket"], key)
    boundary = uuid.uuid4().hex
    ctype = mimetypes.guess_type(filepath)[0] or "application/octet-stream"
    with open(filepath, "rb") as f:
        content = f.read()

    def part(name, value):
        return (f'--{boundary}\r\nContent-Disposition: form-data; '
                f'name="{name}"\r\n\r\n{value}\r\n').encode()

    body = part("token", token) + part("key", key)
    body += (f'--{boundary}\r\nContent-Disposition: form-data; name="file"; '
             f'filename="{os.path.basename(filepath)}"\r\n'
             f'Content-Type: {ctype}\r\n\r\n').encode()
    body += content + b"\r\n" + f"--{boundary}--\r\n".encode()

    req = urllib.request.Request(
        q["up_host"], data=body,
        headers={"Content-Type": f"multipart/form-data; boundary={boundary}"})
    with urllib.request.urlopen(req, timeout=90) as resp:
        res = json.load(resp)
    domain = q["domain"].rstrip("/")
    if not domain.startswith("http"):
        domain = "https://" + domain
    return f"{domain}/{res['key']}"


# ---------- 主流程 ----------
def sha_key(filepath):
    h = hashlib.sha256(open(filepath, "rb").read()).hexdigest()[:16]
    ext = os.path.splitext(filepath)[1].lower() or ".png"
    return h, f"gzh-design/{h}{ext}"


def upload_one(path, host, cfg, cache):
    if path.startswith(("http://", "https://")):
        return path  # 远程图原样返回
    if not os.path.isfile(path):
        raise FileNotFoundError(path)
    h, key = sha_key(path)
    if h in cache:
        return cache[h]  # 命中缓存，不重复上传
    if host == "qiniu":
        url = qiniu_put(cfg["qiniu"], key, path)
    else:
        raise SystemExit(f"暂不支持的图床: {host}（目前实现 qiniu；OSS/COS 可加适配器）")
    cache[h] = url
    return url


def main():
    args = sys.argv[1:]
    as_json = "--json" in args
    check = "--check" in args
    files = [a for a in args if not a.startswith("--")]
    host, cfg = load_config()

    if check:
        print(f"图床: {host}")
        if host == "qiniu":
            miss = missing_qiniu(cfg["qiniu"])
            if miss:
                print(f"  ✗ 七牛密钥缺失: {', '.join(miss)}")
                print(f"  → 配置环境变量，或写 {CONFIG_FILE}（见 references/image-host.md）")
                sys.exit(2)
            print(f"  ✓ 七牛配置齐全 | bucket={cfg['qiniu']['bucket']} "
                  f"| domain={cfg['qiniu']['domain']}")
        print(f"缓存文件: {CACHE_FILE}")
        sys.exit(0)

    if not files:
        print("用法: upload_image.py <图片...> | --check | --json <图片...>",
              file=sys.stderr)
        sys.exit(2)

    cache = load_cache()

    # 只有当存在「本地、真实存在、未缓存」的图（真需要上传）时才要求密钥；
    # 远程 URL 直通、已缓存的图都不需要密钥。
    def needs_upload(p):
        if p.startswith(("http://", "https://")) or not os.path.isfile(p):
            return False
        return sha_key(p)[0] not in cache

    if host == "qiniu" and any(needs_upload(p) for p in files):
        miss = missing_qiniu(cfg["qiniu"])
        if miss:
            print(f"✗ 未配置图床（七牛密钥缺: {', '.join(miss)}）。"
                  f"请按 references/image-host.md 配置环境变量或 {CONFIG_FILE}，"
                  f"或改为手动上传图片后把 URL 填进 Markdown。", file=sys.stderr)
            sys.exit(2)
    result, failed = {}, []
    for p in files:
        try:
            result[p] = upload_one(p, host, cfg, cache)
        except Exception as e:  # 单张失败不影响其余
            failed.append((p, str(e)))
    save_cache(cache)

    if as_json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        for p, url in result.items():
            print(f"{p}\t{url}")
    for p, err in failed:
        print(f"✗ 上传失败 {p}: {err}", file=sys.stderr)
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()

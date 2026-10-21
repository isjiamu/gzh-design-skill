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
    (re.compile(r"!important", re.I), "ERROR",
     "用了 !important：平台不建议（官方规范 #4.5.2），会压掉平台公共样式与暗色模式覆盖"),
    (re.compile(r"<pre[\s>]", re.I), "ERROR",
     "用了 <pre>：普通正文不要 pre（官方规范 #1.8）；代码块请用 common-components 的"
     "「每行一个 <p style=\"margin:0\">」写法"),
]

# 官方规范 #3：不要设置自定义字体族（代码等宽字体可例外）
FONT_DECL = re.compile(r"font-family\s*:\s*([^;\"']*(?:'[^']*'[^;\"']*)*)", re.I)
FONT_OK = re.compile(r"^\s*(?:inherit|unset|initial|revert)\s*$", re.I)
FONT_OFFICIAL = re.compile(
    r'^\s*"?mp-quote"?,?\s*PingFang\s*SC,?\s*system-ui,?\s*-apple-system', re.I)
FONT_MONO = re.compile(r"monospace|courier|consolas|menlo|monaco|sf\s*mono", re.I)

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
        # 字体：主题/组件一律 inherit 或官方默认栈（等宽代码字体例外）
        for m in FONT_DECL.finditer(html):
            val = m.group(1).strip()
            if FONT_OK.match(val) or FONT_OFFICIAL.match(val) or FONT_MONO.search(val):
                continue
            add("ERROR", f"自定义 font-family「{val}」：官方规范 #3 不建议设置字体族，改 inherit")
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

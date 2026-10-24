#!/usr/bin/env python3
"""把已校验的公众号正文片段（纯 <section>）包成带「复制」按钮的浏览器预览页。

用户打开预览页 → 点右上角「复制到公众号」→ 按钮通过一次性 copy 事件处理器把
正文**源 HTML** 写入剪贴板（text/html，避免浏览器选中序列化注入 text-align:start
之类的杂质），粘贴效果等价手动 Ctrl+A/Ctrl+C → 到公众号编辑器 Ctrl+V 粘贴即可。

按钮和 JS 只存在于预览外壳里，**不在被复制的 section 内**，所以粘进公众号的
仍是干净合规的正文，不含 <script>/<button>。校验请对原始 section 文件跑
validate_gzh_html.py（本预览页含 script/style，不参与校验）。

实测注意（2026-10）：
- 复制按钮只在**真实用户点击**时可靠；脚本化 navigator.clipboard.write 会
  因页面未聚焦被浏览器拒绝（NotAllowedError），自动化场景不要依赖它。
- 粘贴时公众号会**静默剥掉相对路径/本地图片**（文字留下、图片消失）。
  正文里的 <img> src 必须是公网 http(s) URL（推荐素材库 mmbiz.qpic.cn 地址）。

用法:
    wrap_preview.py <section.html> [output.html]
    默认输出 <section去扩展名>_预览.html
"""

import os
import sys


def main():
    if len(sys.argv) < 2:
        print("用法: wrap_preview.py <section.html> [output.html]")
        sys.exit(1)
    src = sys.argv[1]
    if not os.path.isfile(src):
        print(f"✗ 找不到文件: {src}")
        sys.exit(1)

    content = open(src, encoding="utf-8").read().strip()
    tpl_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            "..", "assets", "preview-template.html")
    tpl = open(tpl_path, encoding="utf-8").read()

    title = os.path.splitext(os.path.basename(src))[0]
    out_html = tpl.replace("{{TITLE}}", title).replace("<!--GZH_CONTENT-->", content)

    out = sys.argv[2] if len(sys.argv) > 2 else os.path.splitext(src)[0] + "_预览.html"
    open(out, "w", encoding="utf-8").write(out_html)
    print(f"✓ 已生成带「复制」按钮的预览页: {out}")
    print("  用浏览器打开它，点右上角「复制到公众号」，再去公众号编辑器 Ctrl/⌘+V 粘贴。")


if __name__ == "__main__":
    main()

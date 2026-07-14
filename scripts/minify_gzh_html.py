#!/usr/bin/env python3
"""
微信公众号 HTML 压缩工具。

压缩规则：去掉标签之间的换行和缩进，防止手机端解析器
把 HTML 源码里的换行/空格误转成 &nbsp; 从而破坏排版。

用法：
    python3 minify_gzh_html.py <输入.html> [输出.html]

或作为模块导入：
    from minify_gzh_html import minify_html
    minified = minify_html(html_string)
"""
import re
import sys


def minify_html(html):
    """
    压缩公众号 HTML：去掉标签之间的换行和缩进，
    以及文字内容里的多余换行。

    原理：手机端解析器会把 HTML 源码里标签之间的换行和缩进，
    误读成文字内容里的空白并转换成 &nbsp;，导致排版错乱。
    压缩后手机解析器找不到"原料"，问题根治。

    同时，文字节点内的换行（如标签属性后的文字中间换行）
    也会被微信编辑器当作文本换行处理，必须去掉。

    注意：
    - 不动 <span leaf=""> 包裹的文字内容里的正常空格
    """
    # 移除 HTML 注释
    html = re.sub(r'<!--.*?-->', '', html, flags=re.DOTALL)

    # 去掉标签之间的空白（换行、空格、制表符）
    html = re.sub(r'>\s+<', '><', html)

    # 去掉标签属性后紧跟的文字内容里的换行
    # 例如: <p style="...">这里
    # 有换行</p>  →  <p style="...">这里有换行</p>
    # 通过把每行按 > 分割后 strip 再拼回来实现
    lines = html.split('\n')
    cleaned_lines = []
    for line in lines:
        # 每行首尾空白strip，但如果是纯空白行（标签间空行）则跳过
        stripped = line.strip()
        if stripped:
            cleaned_lines.append(stripped)
    html = ''.join(cleaned_lines)

    return html.strip()


def minify_file(input_path, output_path=None):
    """压缩 HTML 文件"""
    with open(input_path, 'r', encoding='utf-8') as f:
        html = f.read()

    minified = minify_html(html)

    if output_path:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(minified)
        print(f"压缩完成: {input_path} → {output_path}")
        print(f"  原始: {len(html)} 字符, 换行 {html.count(chr(10))} 个")
        print(f"  压缩: {len(minified)} 字符, 换行 {minified.count(chr(10))} 个")
    else:
        # 就地压缩
        backup = input_path + '.bak'
        with open(backup, 'w', encoding='utf-8') as f:
            f.write(html)
        with open(input_path, 'w', encoding='utf-8') as f:
            f.write(minified)
        print(f"压缩完成（原始备份: {backup}）")
        print(f"  原始: {len(html)} 字符, 换行 {html.count(chr(10))} 个")
        print(f"  压缩: {len(minified)} 字符, 换行 {minified.count(chr(10))} 个")

    return minified


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    minify_file(input_file, output_file)

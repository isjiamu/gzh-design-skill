#!/usr/bin/env python3
"""Word .docx → Markdown 提取器（零外部依赖）。

格式归一化层的确定性组件：把 docx 的标题层级 / 粗体 / 列表 / 图片
转成本 skill 排版流程认识的 Markdown。

用法：
    extract_docx.py 文章.docx [-o 输出.md]
    # 内嵌图片解包到 输出.md 同目录的 images/ 下，md 里用相对路径引用

退出码：0 成功；1 失败（文件不存在 / 不是合法 docx）。
提取不了的复杂结构（表格、文本框）会以「[表格：…]」占位并在 stderr 提示。
"""

import argparse
import os
import re
import sys
import zipfile
import xml.etree.ElementTree as ET

W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
R = "{http://schemas.openxmlformats.org/officeDocument/2006/relationships}"
A = "{http://schemas.openxmlformats.org/drawingml/2006/main}"


def load_styles(z):
    """styleId → 标题级别（1/2/3…）；非标题样式不入表。"""
    levels = {}
    try:
        root = ET.fromstring(z.read("word/styles.xml"))
    except KeyError:
        return levels
    for st in root.iter(f"{W}style"):
        sid = st.get(f"{W}styleId") or ""
        name_el = st.find(f"{W}name")
        name = (name_el.get(f"{W}val") if name_el is not None else "") or ""
        m = re.search(r"(?:heading|标题)\s*([1-6])", name, re.I) \
            or re.fullmatch(r"([1-6])", sid)
        if m:
            levels[sid] = int(m.group(1))
    return levels


def load_rels(z):
    """rId → 媒体文件路径（word/media/...）。"""
    rels = {}
    try:
        root = ET.fromstring(z.read("word/_rels/document.xml.rels"))
    except KeyError:
        return rels
    for rel in root:
        target = rel.get("Target") or ""
        if "media/" in target:
            rels[rel.get("Id")] = "word/" + target.lstrip("/").replace("../", "")
    return rels


def para_text(p):
    """段内 run → 行内 Markdown（粗体→**、下划线→<u>）。"""
    out = []
    for r_el in p.iter(f"{W}r"):
        rpr = r_el.find(f"{W}rPr")
        bold = rpr is not None and rpr.find(f"{W}b") is not None \
            and (rpr.find(f"{W}b").get(f"{W}val") or "1") not in ("0", "false")
        ul = rpr is not None and rpr.find(f"{W}u") is not None
        text = "".join(t.text or "" for t in r_el.iter(f"{W}t"))
        if not text:
            continue
        if bold:
            text = f"**{text}**"
        if ul:
            text = f"<u>{text}</u>"
        out.append(text)
    s = "".join(out)
    return re.sub(r"\*\*\*\*", "", s)  # 相邻粗体 run 合并的空标记


def extract(docx_path, out_md):
    try:
        z = zipfile.ZipFile(docx_path)
        doc = ET.fromstring(z.read("word/document.xml"))
    except (zipfile.BadZipFile, KeyError) as e:
        print(f"✗ 不是合法 docx：{e}", file=sys.stderr)
        return 1

    heading_of = load_styles(z)
    media_of = load_rels(z)
    out_dir = os.path.dirname(os.path.abspath(out_md)) or "."
    img_dir = os.path.join(out_dir, "images")
    lines, img_n, skipped = [], 0, 0

    body = doc.find(f"{W}body")
    for el in body:
        tag = el.tag
        if tag == f"{W}tbl":
            # 表格 → Markdown 表格，保住行列结构（合并单元格按普通格处理）
            rows = []
            for tr in el.findall(f"{W}tr"):
                cells = ["".join(t.text or "" for t in tc.iter(f"{W}t"))
                         .strip().replace("|", "\\|") or " "
                         for tc in tr.findall(f"{W}tc")]
                rows.append("| " + " | ".join(cells) + " |")
            if rows:
                lines.append(rows[0])
                ncols = rows[0].count("|") - 1
                lines.append("|" + "---|" * ncols)
                lines.extend(rows[1:])
                lines.append("")
                skipped += 1  # 计数改为"转换的表格数"
            continue
        if tag != f"{W}p":
            continue
        p = el
        # 图片
        for blip in p.iter(f"{A}blip"):
            rid = blip.get(f"{R}embed")
            src = media_of.get(rid)
            if not src:
                continue
            os.makedirs(img_dir, exist_ok=True)
            img_n += 1
            fname = f"{img_n:02d}-" + os.path.basename(src)
            with open(os.path.join(img_dir, fname), "wb") as f:
                f.write(z.read(src))
            lines.append(f"![](images/{fname})")
            lines.append("")
        text = para_text(p).strip()
        if not text:
            continue
        ppr = p.find(f"{W}pPr")
        style_el = ppr.find(f"{W}pStyle") if ppr is not None else None
        sid = style_el.get(f"{W}val") if style_el is not None else ""
        lvl = heading_of.get(sid)
        # 列表识别：直接编号(numPr) 或 列表类段落样式（List Bullet/Number/Paragraph/中文"列表"）
        is_list = (ppr is not None and ppr.find(f"{W}numPr") is not None) \
            or bool(re.search(r"list|列表", sid or "", re.I))
        if lvl:
            text_clean = re.sub(r"^\*\*(.*)\*\*$", r"\1", text)  # 标题不需要再加粗
            lines.append("#" * min(lvl + 0, 6) + " " + text_clean)
        elif is_list:
            lines.append("- " + text)
        else:
            lines.append(text)
        lines.append("")

    md = "\n".join(lines).rstrip() + "\n"
    with open(out_md, "w", encoding="utf-8") as f:
        f.write(md)
    print(f"✓ {os.path.basename(docx_path)} → {out_md}")
    print(f"  段落 {sum(1 for l in lines if l and not l.startswith(('#','-','![')))} · "
          f"标题 {sum(1 for l in lines if l.startswith('#'))} · "
          f"列表 {sum(1 for l in lines if l.startswith('- '))} · 图片 {img_n}"
          + (f" · 表格 {skipped}（已转 Markdown 表格）" if skipped else ""))
    return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("docx")
    ap.add_argument("-o", "--out", help="输出 md 路径（默认同名 .md）")
    args = ap.parse_args()
    if not os.path.isfile(args.docx):
        print(f"✗ 文件不存在: {args.docx}", file=sys.stderr)
        sys.exit(1)
    out = args.out or re.sub(r"\.docx$", "", args.docx, flags=re.I) + ".md"
    sys.exit(extract(args.docx, out))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""微信公众号 HTML 合规校验器（对齐官方《微信公众平台编辑器插件开发规范》）。

把 SKILL.md 里"必须遵守的平台限制"从模型自觉变成确定性兜底。
排版生成后必跑：检查禁用标签/属性/样式、官方规范 #1 的 CSS 属性红线、
#2 的节点结构约束、#3 的字体规范，并核查文字节点是否用 <span leaf=""> 包裹
（公众号编辑器粘贴后保持样式的关键）。

说明：本脚本是静态确定性检查；官方仓库 wechatjs/verify-article-structure-spec
用真实浏览器测布局（width/height/line-height/pre 的实际溢出与叠字）。两者互补：
本脚本保证"生成即不合规的写法"在源头被发现，官方 CLI 用于交付前的最终实测。

用法:
    validate_gzh_html.py <file.html>
    validate_gzh_html.py --stdin < file.html

退出码: 1 = 有 ERROR（会被公众号过滤或粘贴后样式丢失）; 0 = 通过。
"""

import argparse
import math
import re
import sys
from html.parser import HTMLParser

# (正则, 级别, 说明) —— ERROR 会被公众号编辑器过滤掉或导致样式失效
FORBIDDEN = [
    (re.compile(r"<style[\s>]", re.I), "ERROR", "<style> 标签会被过滤，样式必须内联"),
    (re.compile(r"<script[\s>]", re.I), "ERROR", "<script> 标签会被过滤"),
    (re.compile(r"</?div[\s>]", re.I), "ERROR", "<div> 会被改写，请用 <section>"),
    (re.compile(r"<link[\s>]", re.I), "ERROR", "外部 <link>（CSS/字体）会被过滤"),
    (re.compile(r"\sclass\s*=", re.I), "ERROR", "class 属性会被剥离，请用内联 style"),
    (re.compile(r"\sid\s*=", re.I), "ERROR", "id 属性会被剥离"),
    (re.compile(r"position\s*:\s*(fixed|absolute|sticky)", re.I), "ERROR",
     "position fixed/absolute/sticky 不被支持"),
    (re.compile(r"float\s*:", re.I), "ERROR", "float 不被支持"),
    (re.compile(r"@media", re.I), "ERROR", "@media 媒体查询不被支持"),
    (re.compile(r"@keyframes", re.I), "ERROR", "@keyframes 动画不被支持"),
    (re.compile(r"@import", re.I), "ERROR", "@import 不被支持"),
    (re.compile(r"display\s*:\s*grid", re.I), "ERROR", "display:grid 不被支持，请用 flex"),
    (re.compile(r"var\s*\(\s*--", re.I), "ERROR", "CSS 变量 var(--x) 不被支持，请写死值"),
    (re.compile(r"url\s*\(\s*['\"]?https?://[^)]*\.(woff2?|ttf|otf|eot)", re.I),
     "ERROR", "外部字体不被支持"),
]

CJK = re.compile(r"[一-鿿㐀-䶿]")
SKIP_TAGS = {"head", "title", "style", "script"}  # 不参与公众号正文粘贴的区域
# 中文字后紧跟半角逗号/分号/叹号/问号（应改全角）；只查"中文在前"避免中英混排误伤
HALF_PUNCT = re.compile(r"[一-鿿㐀-䶿][,;!?]")
ASCII_QUOTE = re.compile(r"[\"']")
# 代码区特征：等宽字体或 white-space:pre —— 其内半角符号是正常的
CODE_STYLE = re.compile(r"monospace|white-space\s*:\s*pre|courier|consolas|sf mono", re.I)
# 只检查内联背景声明，跳过 CSS 注释、字符串和图片 URL 中的示例文字。
CSS_NON_FUNCTION = re.compile(
    r"/\*.*?\*/|url\(\s*(?:\"(?:\\.|[^\"\\])*\"|'(?:\\.|[^'\\])*'|(?:\\.|[^)])*)\s*\)"
    r"|\"(?:\\.|[^\"\\])*\"|'(?:\\.|[^'\\])*'", re.I | re.S)
GRADIENT_BACKGROUND = re.compile(
    r"(?:^|;)\s*background(?:-image)?\s*:[^;]*\b"
    r"(?:repeating-)?(?:linear|radial|conic)-gradient\s*\(", re.I)

# ── 官方规范 #3：字体 ──────────────────────────────────────────────────────
# 允许列表：inherit（首选）或官方默认字体栈前缀；其余视为自定义字体
FONT_INHERIT = re.compile(r"^(?:inherit|unset|initial|revert)$", re.I)
FONT_OFFICIAL_PREFIX = re.compile(
    r'^"?mp-quote"?,?\s*PingFang\s*SC,?\s*system-ui,?\s*-apple-system', re.I)
# 等宽代码字体：代码块的可读性刚需，规范未点名禁用，按提示而非违规处理
FONT_MONOSPACE = re.compile(r"monospace|courier|consolas|menlo|monaco|sf\s*mono", re.I)

# ── 官方规范 #1：CSS 属性红线 ──────────────────────────────────────────────
BLOCK_LEVEL = {"section", "p", "div", "h1", "h2", "h3", "h4", "h5", "h6",
               "table", "thead", "tbody", "tr", "td", "th", "ul", "ol", "li",
               "figure", "figcaption", "blockquote", "pre", "hr"}
HEIGHT_ZERO = re.compile(r"(?:^|;)\s*height\s*:\s*0(?:px|r?em|%)?\s*(?:;|$)", re.I)
LINE_HEIGHT_SMALL = re.compile(r"(?:^|;)\s*line-height\s*:\s*([\d.]+)\s*(?:;|$)")
LINE_HEIGHT_PCT = re.compile(r"(?:^|;)\s*line-height\s*:\s*([\d.]+)%")
LINE_HEIGHT_LENGTH = re.compile(r"(?:^|;)\s*line-height\s*:\s*([\d.]+)\s*(px|em|rem)")
FONT_SIZE = re.compile(r"(?:^|;)\s*font-size\s*:\s*([\d.]+)\s*(px|em|rem|pt)")
TEXT_ALIGN_BAD = re.compile(r"(?:^|;)\s*text-align\s*:\s*(start|end)\b", re.I)
CARET_TRANSPARENT = re.compile(
    r"(?:^|;)\s*caret-color\s*:\s*"
    r"(?:transparent|rgba?\([^)]*,\s*0(?:\.0+)?\s*\))", re.I)
FIXED_WIDTH = re.compile(
    r"(?:^|;)\s*width\s*:\s*([\d.]+)(px|pt)(?![\w-])", re.I)
IMG_OPACITY_0 = re.compile(r"(?:^|;|\s)opacity\s*:\s*0(?:\.0+)?\s*(?:;|$)", re.I)
ANIMATE_BEGIN = re.compile(
    r"<animate(?:Transform|Motion)?\b[^>]*\bbegin\s*=\s*[\"']([^\"']*)[\"']", re.I)
# 空白/占位字符不算"内容"
BLANK = re.compile(r"^[\s　\u00a0\u200b]*$")
# 粗估一行能放多少字：正文按 16px、容器约 677px，中文 1em、其他 0.5em
CHARS_PER_LINE = 42
LINE_RATIO_MIN = 0.9


def decls(style):
    """把内联 style 拆成 dict（小写属性名），去掉 CSS 注释。"""
    style = re.sub(r"/\*.*?\*/", "", style or "", flags=re.S)
    out = {}
    for part in style.split(";"):
        if ":" not in part:
            continue
        prop, _, val = part.partition(":")
        out[prop.strip().lower()] = val.strip()
    return out


def as_decl_str(d):
    return ";" + ";".join(f"{k}:{v}" for k, v in d.items())


def text_em(text):
    """文本视觉宽度（em）：中文 1，其他 0.5。"""
    t = text.replace("\u00a0", " ").replace("​", "")
    cjk = len(CJK.findall(t))
    return cjk + (len(t) - cjk) * 0.5


def font_px(val):
    m = FONT_SIZE.search("font-size:" + (val or ""))
    if not m:
        return None
    num, unit = float(m.group(1)), m.group(2)
    return {"px": num, "pt": num * 4 / 3, "em": num * 16, "rem": num * 16}.get(unit, num)


def line_ratio(lh, fs_px):
    """line-height / font-size 的比值；无法比较时返回 None。"""
    if not lh:
        return None
    base = fs_px or 16.0
    m = LINE_HEIGHT_PCT.search("line-height:" + lh)
    if m:
        return float(m.group(1)) / 100
    m = LINE_HEIGHT_LENGTH.search("line-height:" + lh)
    if m:
        num, unit = float(m.group(1)), m.group(2)
        if unit == "em":
            return num
        if unit == "rem":
            return num * 16 / base
        return num / base
    m = LINE_HEIGHT_SMALL.search("line-height:" + lh)
    if m:
        return float(m.group(1))
    return 0.0  # "0" / "0px" 之类


class LeafChecker(HTMLParser):
    """逐元素检查：span leaf 包裹、官方 CSS 红线、结构约束、字体规范。"""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []           # 打开的元素节点（dict）
        self.leaf_depth = 0       # 处于 span[leaf] 内的嵌套计数
        self.code_depth = 0       # 处于代码区（等宽/pre）内的嵌套计数
        self.span_leaf_count = 0  # 全文 span leaf 总数
        self.unwrapped = []       # (文本片段, 父标签) —— 未被 leaf 包裹的中文文本
        self.half_punct = []      # 正文里疑似半角标点的片段
        self.gradient_backgrounds = []  # (行, 列, 标签) —— 内联渐变背景
        self.gradient_nodes = []  # 渐变元素（用于区分"文字背景"与"装饰"）
        self.font_families = []   # (行, 列, 标签, 值) —— font-family 声明
        self.bad_css = []         # (level, msg)
        self.bad_structure = []   # (level, msg)
        self._seen = set()

    # ── 工具 ──
    def _pos(self):
        line, col = self.getpos()
        return line, col + 1

    def _add(self, bucket, level, msg):
        key = (bucket, msg)
        if key not in self._seen:
            self._seen.add(key)
            (self.bad_css if bucket == "css" else self.bad_structure).append((level, msg))

    def _skip(self):
        return any(n["tag"] in SKIP_TAGS for n in self.stack)

    # ── 开标签 ──
    def handle_starttag(self, tag, attrs):
        ad = dict(attrs)
        style = ad.get("style", "") or ""
        smap = decls(style)
        line, col = self._pos()
        skip = self._skip()

        is_leaf = tag == "span" and "leaf" in ad
        is_code = bool(CODE_STYLE.search(style))
        if is_leaf:
            self.span_leaf_count += 1
            self.leaf_depth += 1
        if is_code:
            self.code_depth += 1

        gnode = None
        if not skip and GRADIENT_BACKGROUND.search(CSS_NON_FUNCTION.sub("", style)):
            self.gradient_backgrounds.append((line, col, tag))
            gnode = {"line": line, "col": col, "tag": tag, "has_text": False}
            self.gradient_nodes.append(gnode)

        if not skip:
            self._check_css(tag, ad, smap, line, col)
            self._check_structure(tag, is_leaf, line, col)

        self.stack.append({
            "tag": tag, "leaf": is_leaf, "code": is_code, "attrs": ad,
            "style": smap, "line": line, "col": col, "text": [], "gradient": gnode,
        })

    def _check_css(self, tag, attrs, smap, line, col):
        d = as_decl_str(smap)
        # #1.6 text-align: start/end 跨端不一致
        if TEXT_ALIGN_BAD.search(d):
            self._add("css", "ERROR",
                      f"text-align 不能写 start/end，请用 left/right（官方规范 #1.6）"
                      f"（第 {line} 行 {col} 列）")
        # #1.2 caret-color 透明会让编辑器光标不可见
        if CARET_TRANSPARENT.search(d):
            self._add("css", "WARNING",
                      f"caret-color 透明会让编辑器光标不可见（官方规范 #1.2）"
                      f"（第 {line} 行 {col} 列）")
        # #1.1 img 的 opacity:0（配合 SVG 背景图会锁死图片不可替换）
        if tag == "img" and IMG_OPACITY_0.search(d):
            self._add("css", "ERROR",
                      f"img 的 opacity 不能为 0，发布后将无法再改图（官方规范 #1.1）"
                      f"（第 {line} 行 {col} 列）")
        # #3 字体：不写 font-family，走平台默认字体栈
        if smap.get("font-family"):
            self.font_families.append((line, col, tag, smap["font-family"]))

    def _check_structure(self, tag, is_leaf, line, col):
        # #2.2 span[leaf] 是行内容器，其后代（任意层级）都不能是块级元素
        if not is_leaf and tag in BLOCK_LEVEL and any(n["leaf"] for n in self.stack):
            self._add("struct", "ERROR",
                      f"span[leaf] 里不能包块级元素 <{tag}>，只能放行内节点"
                      f"（官方规范 #2.2）（第 {line} 行 {col} 列）")
        # #1.8 pre 只应承载代码
        if tag == "pre":
            self._add("css", "WARNING",
                      f"用了 <pre>：只应包代码，且需 overflow-x 可横向滚动，"
                      f"否则窄屏内容会被截断（官方规范 #1.8）（第 {line} 行 {col} 列）")

    # ── 收标签 ──
    def handle_endtag(self, tag):
        idx = None
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i]["tag"] == tag:
                idx = i
                break
        if idx is None:
            return
        closing = self.stack[idx:]
        ancestors = self.stack[:idx]
        for node in closing:
            self._finish_node(node, ancestors)
        for node in closing:
            if node["leaf"]:
                self.leaf_depth -= 1
            if node["code"]:
                self.code_depth -= 1
        del self.stack[idx:]

    def _finish_node(self, node, ancestors=None):
        ancestors = ancestors or []
        text = "".join(node["text"])
        visible = bool(text.strip()) and not BLANK.match(text)
        smap = node["style"]
        d = as_decl_str(smap)
        parent_small = False
        if ancestors:
            ps = ancestors[-1]["style"]
            pr = line_ratio(ps.get("line-height"), font_px(ps.get("font-size")))
            parent_small = pr is not None and pr < LINE_RATIO_MIN

        mode = node["attrs"].get("data-mode", "")
        # #1.4 固定 px 宽度：只有"包着文字"才会破坏居中/溢出/宽度比；
        #     无文字的定宽元素（头像框、图标、装饰条）是刻意的固定尺寸，不报
        #     ≤120px 的定宽小件（编号圆点、标签胶囊、头像框）在窄屏也放得下，豁免
        if visible and node["tag"] not in ("img", "svg") \
                and "data-ignore-width" not in node["attrs"]:
            m = FIXED_WIDTH.search(d)
            if m and float(m.group(1)) > 120:
                self._add("css", "WARNING",
                          f"容器写了固定 {m.group(1)}px 宽度且内含文字，不同屏幕会居中不一致"
                          f"或溢出（官方规范 #1.4）；确有需要请加 data-ignore-width"
                          f"（第 {node['line']} 行 {node['col']} 列 <{node['tag']}>）")
        # #1.5.1 height:0 里真的有文字 → 移动端整段不可见（ERROR）；
        #     字 0 号 / 隐藏溢出 / 只有符号的装饰元素豁免
        if visible and node["tag"] != "svg" and mode != "svg" and HEIGHT_ZERO.search(d) \
                and not self._decorative(smap, text):
            self._add("css", "ERROR",
                      f"height:0 的容器里包着文字，移动端会整段不可见（官方规范 #1.5.1）"
                      f"（第 {node['line']} 行 {node['col']} 列）")

        # #1.3 真叠字判定：显式过小行高，或从上级继承过小行高，且文字会排成多行
        ratio = line_ratio(smap.get("line-height"), font_px(smap.get("font-size")))
        declared_small = ratio is not None and ratio < LINE_RATIO_MIN
        if not declared_small and not (parent_small and self._inherits_small_lh(ancestors)):
            return
        if not visible or self._decorative(smap, text):
            return
        lines = max(1, math.ceil(text_em(text) / CHARS_PER_LINE))
        if lines < 2:
            return  # 单行不会叠字（官方豁免）
        lh = smap.get("line-height")
        inherited = "" if declared_small else \
            f"（继承自上级的 line-height {self._ancestor_line_height(ancestors)}）"
        self._add("css", "WARNING",
                  f"行高过小（line-height {lh or '继承'}{inherited}）且元素内有成段文字，"
                  f"多行会叠字（官方规范 #1.3）（第 {node['line']} 行 {node['col']} 列 "
                  f"<{node['tag']}>）")

    @staticmethod
    def _inherits_small_lh(ancestors):
        """链上最近的显式 line-height 是否过小（且中间没有层重设字号）。"""
        for anc in reversed(ancestors):
            if anc["style"].get("font-size"):
                return False  # 字号由中间层重新定义，不会直接继承叠字
            r = line_ratio(anc["style"].get("line-height"),
                           font_px(anc["style"].get("font-size")))
            if r is not None:
                return r < LINE_RATIO_MIN
        return False

    @staticmethod
    def _ancestor_line_height(ancestors):
        for anc in reversed(ancestors):
            if anc["style"].get("line-height"):
                return anc["style"]["line-height"]
        return "?"

    @staticmethod
    def _decorative(smap, text):
        """装饰性元素（字 0 号、隐藏或透明、只有符号）不判叠字/不可见。"""
        fs = smap.get("font-size", "").strip()
        zero_font = bool(re.match(r"^0(?:px|r?em)?$", fs, re.I))
        clipped = bool(re.match(r"^(hidden|clip)$", smap.get("overflow", "").strip(), re.I))
        if zero_font or (zero_font and clipped):
            return True
        if smap.get("color", "").strip().lower() == "transparent":
            return True
        return not CJK.search(text) and not re.search(r"[A-Za-z0-9]", text)

    # ── 文本 ──
    def handle_data(self, data):
        text = data.strip()
        if not text or self._skip():
            return
        for node in self.stack:
            node["text"].append(data)
            if node["gradient"] is not None and CJK.search(text):
                node["gradient"]["has_text"] = True
        if not CJK.search(text):
            return
        if self.leaf_depth == 0:
            parent = self.stack[-1]["tag"] if self.stack else "(root)"
            snippet = text[:24] + ("…" if len(text) > 24 else "")
            self.unwrapped.append((snippet, parent))
        if self.code_depth == 0 and (HALF_PUNCT.search(text)
                                     or ASCII_QUOTE.search(text)):
            snippet = text[:24] + ("…" if len(text) > 24 else "")
            self.half_punct.append(snippet)


def check_fonts(checker):
    """官方规范 #3：不建议设置任何字体族；优先 inherit，其次官方默认栈。

    等宽代码字体是代码可读性的刚需、规范未点名，合并成一条"已豁免"提示，
    不逐行刷屏。
    """
    out, mono = [], set()
    for line, col, tag, ff in checker.font_families:
        norm = ff.replace('"', "").replace("'", "").strip()
        if FONT_INHERIT.match(norm) or FONT_OFFICIAL_PREFIX.match(norm):
            continue
        if FONT_MONOSPACE.search(norm):
            mono.add(norm)
            continue
        out.append(f"自定义 font-family「{ff}」在 iOS/安卓渲染不一致，应删掉改 inherit"
                   f"（官方规范 #3；第 {line} 行 {col} 列 <{tag}>）")
    if mono:
        out.append(f"等宽代码字体 {len(mono)} 种（{'、'.join(sorted(mono))}）已在代码块中"
                   f"豁免，交付时注明即可（官方规范 #3）")
    return out


def validate(html, name="<input>"):
    errors, warnings = [], []

    for rx, level, msg in FORBIDDEN:
        hits = len(rx.findall(html))
        if hits:
            (errors if level == "ERROR" else warnings).append(
                f"{msg}（命中 {hits} 处）")

    checker = LeafChecker()
    try:
        checker.feed(html)
        for pos, node in enumerate(checker.stack):  # 收尾未闭合的元素
            checker._finish_node(node, checker.stack[:pos])
    except Exception as e:  # 容错：解析失败不致命，只提示
        warnings.append(f"HTML 解析中断: {e}")

    for level, msg in checker.bad_css + checker.bad_structure:
        (errors if level == "ERROR" else warnings).append(msg)

    font_issues = check_fonts(checker)
    if font_issues:
        sample = "；".join(font_issues[:4])
        more = f" 等 {len(font_issues)} 处" if len(font_issues) > 4 else ""
        warnings.append(f"[font-family] {sample}{more}")

    # #1.7 SVG 动画 begin 只写 touchstart → PC 端不触发
    for begin in ANIMATE_BEGIN.findall(html):
        if re.search(r"\btouchstart\b", begin, re.I) and not re.search(r"\bclick\b", begin, re.I):
            warnings.append(f"[animate-begin] SVG 动画 begin=\"{begin.strip()}\" 只有 touchstart，"
                            f"PC 端需同时写 click（官方规范 #1.7）")
            break

    # #4.5.2 平台不建议 !important（会让平台公共样式与暗色模式覆盖失效）
    n_important = len(re.findall(r"!important", html, re.I))
    if n_important:
        warnings.append(f"[!important] {n_important} 处 !important，平台不建议使用"
                        f"（官方规范 #4.5.2），请直接写内联样式")

    if checker.gradient_backgrounds:
        grads = checker.gradient_backgrounds
        text_grads = [g for g in checker.gradient_nodes if g["has_text"]]
        sample = "；".join(f"第 {line} 行 {col} 列 <{tag}>" for line, col, tag in grads[:5])
        warnings.append(
            f"[darkmode-no-gradient] {len(grads)} 处渐变背景，"
            f"可能触发公众号内容结构检测；文字/卡片背景建议改为主题内纯色或 rgba 纯色，"
            f"装饰渐变也需人工确认。位置：{sample}")
        if text_grads:
            warnings.append(
                f"[darkmode-no-gradient:文字背景] {len(text_grads)} 处渐变上压着文字——"
                f"暗色模式会把渐变转纯色、渐变消失，官方规范 #4.1.2 明确不建议："
                + "；".join(f"第 {g['line']} 行 {g['col']} 列 <{g['tag']}>"
                            for g in text_grads[:5]))
        else:
            warnings.append(
                "[darkmode-no-gradient:装饰] 以上渐变下方均无文字：官方规范 #4.1.3 允许"
                "（暗色模式原样保留），可保留；对齐「纯色优先」原则时可改同类浅色/主色纯色")

    has_cjk = bool(CJK.search(html))
    if has_cjk and checker.span_leaf_count == 0:
        errors.append("全文没有任何 <span leaf=\"\"> 包裹——"
                      "粘贴到公众号后样式会大面积丢失")
    elif checker.unwrapped:
        sample = "；".join(f"「{s}」(在 <{p}> 内)"
                           for s, p in checker.unwrapped[:5])
        warnings.append(
            f"{len(checker.unwrapped)} 处中文文本未被 <span leaf> 包裹，"
            f"样式可能丢失。例：{sample}")

    if checker.half_punct:
        sample = "；".join(f"「{s}」" for s in checker.half_punct[:5])
        warnings.append(
            f"{len(checker.half_punct)} 处正文疑似半角标点/英文引号，应改中文全角"
            f"（代码块内不计）。例：{sample}")

    return errors, warnings, checker.span_leaf_count


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("file", nargs="?", help="HTML 文件路径")
    ap.add_argument("--stdin", action="store_true", help="从标准输入读取")
    args = ap.parse_args()

    if args.stdin or not args.file:
        html = sys.stdin.read()
        name = "<stdin>"
    else:
        with open(args.file, encoding="utf-8", errors="replace") as f:
            html = f.read()
        name = args.file

    errors, warnings, leaf_n = validate(html, name)

    print(f"📋 公众号 HTML 合规校验: {name}")
    print(f"   span leaf 包裹: {leaf_n} 处")
    if errors:
        print(f"\n❌ ERROR ×{len(errors)}（必须修复，否则粘贴后失效）:")
        for e in errors:
            print(f"   • {e}")
    if warnings:
        print(f"\n⚠️  WARNING ×{len(warnings)}（建议检查）:")
        for w in warnings:
            print(f"   • {w}")
    if not errors and not warnings:
        print("\n✅ 完全合规，可直接粘贴到公众号编辑器")
    elif not errors:
        print("\n✅ 无致命问题，可粘贴（warning 请人工确认）")

    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()

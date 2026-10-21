"""Regression for issue #21; run with unittest discovery or this file directly."""
import subprocess
import sys
import unittest
from pathlib import Path

from validate_gzh_html import validate

WARNING_ID = "[darkmode-no-gradient]"


def fragment(style):
    return f'<section style="{style}"><span leaf="">测试文字</span></section>'


class GradientBackgroundTests(unittest.TestCase):
    def test_background_styles(self):
        cases = [
            ("issue radial", fragment("background:radial-gradient(circle at 30% 0%,#FAFAFA,#FFFFFF)"), 1),
            ("linear", fragment("background:linear-gradient(180deg,transparent 60%,#E4E4E7 60%)"), 1),
            ("background-image", fragment("background-image:linear-gradient(red,blue)"), 1),
            ("conic", fragment("background:conic-gradient(red,blue)"), 1),
            ("repeating linear", fragment("background:repeating-linear-gradient(red,blue)"), 1),
            ("repeating radial", fragment("background:repeating-radial-gradient(red,blue)"), 1),
            ("vendor prefix", fragment("background:-webkit-linear-gradient(red,blue)"), 1),
            ("mixed case", fragment("color:red; BACKGROUND-IMAGE : LINEAR-GRADIENT(red,blue)"), 1),
            ("color fallback", fragment("background:#fff linear-gradient(red,blue)"), 1),
            ("layered image", fragment("background-image:url('photo.png'),linear-gradient(red,blue)"), 1),
            ("image-set", fragment("background-image:image-set(linear-gradient(red,blue) 1x)"), 1),
            ("decorative line", '<section style="height:1px;background:linear-gradient(red,blue)"><span leaf=""><br></span></section>', 1),
            ("solid", fragment("background:#FAFAFA"), 0),
            ("rgba", fragment("background:rgba(5,150,105,0.1)"), 0),
            ("background-color", fragment("background-color:#FAFAFA"), 0),
            ("unrelated property", fragment("border-image:linear-gradient(red,blue) 1"), 0),
            ("background-size", fragment("background-size:cover"), 0),
            ("CSS comment", fragment("background:#fff;/* background:linear-gradient(red,blue) */"), 0),
            ("quoted example", fragment("content:'background:linear-gradient(red,blue)';background:#fff"), 0),
            ("URL filename", fragment("background:url('linear-gradient(red,blue).png')"), 0),
            ("URL with parentheses", fragment("background:url('photo(size)/linear-gradient(red,blue).png')"), 0),
            ("URL with escaped parenthesis", fragment(r"background:url(photo\)linear-gradient\(red,blue\).png)"), 0),
            ("URL plus gradient", fragment("background:url('linear-gradient(red,blue).png'),radial-gradient(red,blue)"), 1),
            ("escaped code", '<section><span leaf="">&lt;section style=&quot;background:linear-gradient(red,blue)&quot;&gt;</span></section>', 0),
            ("HTML comment", '<!-- <section style="background:linear-gradient(red,blue)"> --><span leaf="">示例</span>', 0),
            ("head wrapper", '<head><meta style="background:linear-gradient(red,blue)"></head><span leaf="">正文</span>', 0),
            ("single quoted attribute", "<section style='background:linear-gradient(red,blue)'><span leaf=''>正文</span></section>", 1),
            ("empty style", '<section style><span leaf="">正文</span></section>', 0),
        ]
        for name, source, expected in cases:
            with self.subTest(name=name):
                errors, warnings, leaf_count = validate(source)
                self.assertEqual(errors, [])
                self.assertEqual(leaf_count, 1)
                self.assertEqual(sum(WARNING_ID in w for w in warnings), expected)

    def test_count_and_source_locations(self):
        source = fragment("background:linear-gradient(red,blue)")
        errors, warnings, leaf_count = validate(source + "\n" + source)
        self.assertEqual(errors, [])
        self.assertEqual(leaf_count, 2)
        # 文字压在渐变上时额外给出一条"[darkmode-no-gradient:文字背景]"提示
        grads = [w for w in warnings if w.startswith("[darkmode-no-gradient")]
        self.assertEqual(len(grads), 2)
        self.assertIn("2 处渐变背景", grads[0])
        self.assertIn("第 1 行 1 列 <section>", grads[0])
        self.assertIn("第 2 行 1 列 <section>", grads[0])
        self.assertIn("文字背景", grads[1])

    def test_cli_exit_codes(self):
        script = Path(__file__).with_name("validate_gzh_html.py")
        cases = [
            ("warning keeps exit 0", fragment("background:linear-gradient(red,blue)"), 0),
            ("error keeps exit 1", '<div style="background:linear-gradient(red,blue)"><span leaf="">正文</span></div>', 1),
        ]
        for name, source, expected in cases:
            with self.subTest(name=name):
                result = subprocess.run(
                    [sys.executable, str(script), "--stdin"], input=source,
                    text=True, encoding="utf-8", capture_output=True, check=False)
                self.assertEqual(result.returncode, expected, result.stdout)
                self.assertIn(WARNING_ID, result.stdout)


class OfficialSpecRuleTests(unittest.TestCase):
    """官方规范 #1/#2/#3 的规则回归。"""

    def _codes(self, source):
        errors, warnings, _ = validate(source)
        return errors, warnings

    def test_height_zero_with_text_is_error(self):
        errors, _ = self._codes(
            '<section style="height:0;overflow:hidden;"><p style="font-size:16px;">'
            '<span leaf="">height 为零却包着文字的段落。</span></p></section>')
        self.assertTrue(any("height:0" in e for e in errors), errors)

    def test_height_zero_decorative_span_ok(self):
        errors, _ = self._codes(
            '<section><span style="width:8px;height:8px;font-size:0;line-height:0;'
            'overflow:hidden;"><span leaf="">.</span></span></section>')
        self.assertEqual(errors, [])

    def test_span_leaf_with_block_is_error(self):
        errors, _ = self._codes(
            '<span leaf=""><section><span leaf="">块级元素塞进行内容器</span></section></span>')
        self.assertTrue(any("span[leaf]" in e for e in errors), errors)

    def test_text_align_start_is_error(self):
        errors, _ = self._codes(
            '<section style="text-align:start;"><span leaf="">文字左对齐</span></section>')
        self.assertTrue(any("text-align" in e for e in errors), errors)

    def test_img_opacity_zero_is_error(self):
        errors, _ = self._codes(
            '<span leaf=""><img src="a.png" style="opacity:0;width:100%;"></span>')
        self.assertTrue(any("opacity" in e for e in errors), errors)

    def test_custom_font_family_warns(self):
        errors, warnings = self._codes(
            '<section style="font-family:\'Noto Serif SC\',serif;">'
            '<span leaf="">用了自定义字体的正文</span></section>')
        self.assertEqual(errors, [])
        self.assertTrue(any("font-family" in w for w in warnings), warnings)

    def test_inherit_and_official_stack_pass(self):
        for stack in ("inherit", '"mp-quote", PingFang SC, system-ui, -apple-system, sans-serif'):
            with self.subTest(stack=stack):
                errors, warnings = self._codes(
                    f'<section style="font-family:{stack};">'
                    f'<span leaf="">正常字体的正文</span></section>')
                self.assertEqual(errors, [])
                self.assertFalse(any("font-family" in w for w in warnings), warnings)

    def test_important_warns(self):
        _, warnings = self._codes(
            '<section style="color:#333 !important;"><span leaf="">带感叹号的样式</span></section>')
        self.assertTrue(any("!important" in w for w in warnings), warnings)

    def test_line_height_overlap_needs_multiline(self):
        long_text = "这是一段很长很长的正文" * 6
        _, warnings = self._codes(
            f'<section style="font-size:16px;line-height:0.6;">'
            f'<span leaf="">{long_text}</span></section>')
        self.assertTrue(any("line-height" in w for w in warnings), warnings)
        _, warnings = self._codes(
            '<section style="font-size:42px;line-height:0.6;">'
            '<span leaf="">01</span></section>')
        self.assertFalse(any("line-height" in w for w in warnings), warnings)

    def test_small_fixed_width_chip_exempt_large_flagged(self):
        _, warnings = self._codes(
            '<section><span style="display:inline-block;width:22px;height:22px;">'
            '<span leaf="">1</span></span></section>')
        self.assertFalse(any("固定" in w for w in warnings), warnings)
        big = "很长的一段说明文字。" * 8
        _, warnings = self._codes(
            f'<section style="width:600px;"><span leaf="">{big}</span></section>')
        self.assertTrue(any("固定 600px" in w for w in warnings), warnings)


if __name__ == "__main__":
    unittest.main()

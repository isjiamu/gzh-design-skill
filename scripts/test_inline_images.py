"""inline_images.py 的回归测试：本地文件、已是 base64、注释、失败保留。"""
import base64
import pathlib
import tempfile
import unittest

from inline_images import inline, sniff_mime

PNG = base64.b64decode(
    "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNkYPhfDwAC"
    "hwGA60e6kgAAAABJRU5ErkJggg==")


class InlineImagesTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.dir = pathlib.Path(self.tmp.name)
        (self.dir / "a.png").write_bytes(PNG)
        (self.dir / "b.jpg").write_bytes(b"\xff\xd8\xff\xe0" + b"\x00" * 32)
        (self.dir / "c.gif").write_bytes(b"GIF89a" + b"\x00" * 16)

    def tearDown(self):
        self.tmp.cleanup()

    def run_inline(self, html):
        return inline(html, str(self.dir), 3, 5, log=lambda *_: None)

    def test_local_file_inlined(self):
        out, stats = self.run_inline('<img src="a.png" style="max-width:100%;">')
        self.assertEqual(stats["ok"], 1)
        self.assertIn("data:image/png;base64,", out)
        self.assertNotIn('src="a.png"', out)

    def test_mime_from_magic_not_extension(self):
        out, _ = self.run_inline('<img src="b.jpg">')
        self.assertIn("data:image/jpeg;base64,", out)

    def test_existing_data_uri_untouched(self):
        src = '<img src="data:image/png;base64,AAAA">'
        out, stats = self.run_inline(src)
        self.assertEqual(out, src)
        self.assertEqual(stats["skipped"], 1)

    def test_comment_example_untouched(self):
        src = '<!-- <img src="a.png"> 示例 --><img src="c.gif">'
        out, _ = self.run_inline(src)
        self.assertIn('<!-- <img src="a.png">', out)
        self.assertEqual(out.count("data:image/gif;base64,"), 1)

    def test_missing_file_keeps_src(self):
        out, stats = self.run_inline('<img src="nope.png">')
        self.assertIn('src="nope.png"', out)
        self.assertEqual(stats["failed"], 1)

    def test_size_limit_skips(self):
        out, stats = inline('<img src="a.png">', str(self.dir), 0.00001, 5, log=lambda *_: None)
        self.assertIn('src="a.png"', out)
        self.assertEqual(stats["failed"], 1)

    def test_sniff_svg_and_webp(self):
        self.assertEqual(sniff_mime(b'<svg xmlns="http://www.w3.org/2000/svg"></svg>'), "image/svg+xml")
        self.assertEqual(sniff_mime(b"RIFF\x00\x00\x00\x00WEBPVP8 "), "image/webp")

    # ── 本地图片路径解析（重点场景）──
    def test_relative_resolved_from_parent_root(self):
        sub = self.dir / "sub"
        sub.mkdir()
        (self.dir / "images").mkdir()
        (self.dir / "images" / "p.png").write_bytes(PNG)
        out, stats = inline('<img src="images/p.png">', str(sub), 3, 5, log=lambda *_: None)
        self.assertEqual(stats["ok"], 1, out)
        self.assertIn("data:image/png;base64,", out)

    def test_unique_basename_fallback(self):
        deep = self.dir / "deep" / "x"
        deep.mkdir(parents=True)
        (deep / "only-one.png").write_bytes(PNG)
        out, stats = inline('<img src="assets/only-one.png">', str(self.dir), 3, 5,
                            log=lambda *_: None)
        self.assertEqual(stats["ok"], 1, out)
        self.assertIn("data:image/png;base64,", out)

    def test_ambiguous_basename_keeps_src(self):
        for d in ("d1", "d2"):
            (self.dir / d).mkdir()
            (self.dir / d / "dup-name.png").write_bytes(PNG)
        out, stats = inline('<img src="dup-name.png">', str(self.dir), 3, 5,
                            log=lambda *_: None)
        self.assertEqual(stats["failed"], 1, out)
        self.assertIn('src="dup-name.png"', out)

    def test_placeholder_counted_separately(self):
        html = '<img src="图片URL"><img src="{{图片URL}}"><img src="">'
        out, stats = inline(html, str(self.dir), 3, 5, log=lambda *_: None)
        self.assertEqual(stats["placeholder"], 3)
        self.assertEqual(stats["failed"], 0)
        self.assertIn('src="图片URL"', out)

    def test_urlencoded_and_backslash_paths(self):
        (self.dir / "images").mkdir()
        (self.dir / "images" / "my photo.png").write_bytes(PNG)
        for src in ("images/my%20photo.png", "images\\my photo.png"):
            with self.subTest(src=src):
                out, stats = inline(f'<img src="{src}">', str(self.dir), 3, 5,
                                    log=lambda *_: None)
                self.assertEqual(stats["ok"], 1, out)

    def test_duplicate_image_reused(self):
        out, stats = inline('<img src="a.png"><img src="a.png">', str(self.dir), 3, 5,
                            log=lambda *_: None)
        self.assertEqual(stats["ok"], 2)
        self.assertEqual(out.count("data:image/png;base64,"), 2)

    def test_nested_roots_do_not_count_twice(self):
        # 文件同时落在多个搜索根下时，不能被判成"同名多份"
        sub = self.dir / "sub2"
        sub.mkdir()
        (sub / "nested.png").write_bytes(PNG)
        out, stats = inline('<img src="nope/nested.png">', str(sub), 3, 5,
                            log=lambda *_: None)
        self.assertEqual(stats["ok"], 1, out)

    def test_source_dir_as_extra_root(self):
        elsewhere = self.dir / "elsewhere"
        elsewhere.mkdir()
        (elsewhere / "s.png").write_bytes(PNG)
        sub = self.dir / "sub3"
        sub.mkdir()
        out, stats = inline('<img src="s.png">', str(sub), 3, 5, log=lambda *_: None,
                            source_dirs=[str(elsewhere)])
        self.assertEqual(stats["ok"], 1, out)
        self.assertIn("data:image/png;base64,", out)

    # ── 保留 / 内嵌策略 ──
    def test_mmbiz_kept_by_default(self):
        src = "https://mmbiz.qpic.cn/sz_mmbiz_png/abc/0?wx_fmt=png"
        out, stats = inline(f'<img src="{src}">', str(self.dir), 3, 1, log=lambda *_: None)
        self.assertEqual(stats["kept"], 1)
        self.assertEqual(stats["failed"], 0)
        self.assertIn(f'src="{src}"', out)

    def test_protocol_relative_mmbiz_kept(self):
        out, stats = inline('<img src="//mmbiz.qpic.cn/a/0">', str(self.dir), 3, 1,
                            log=lambda *_: None)
        self.assertEqual(stats["kept"], 1)
        self.assertIn('src="//mmbiz.qpic.cn/a/0"', out)

    def test_keep_remote_keeps_any_url_without_download(self):
        src = "https://example.invalid/x.png"
        out, stats = inline(f'<img src="{src}">', str(self.dir), 3, 1,
                            log=lambda *_: None, keep_remote=True)
        self.assertEqual(stats["kept"], 1)
        self.assertEqual(stats["failed"], 0)
        self.assertIn(f'src="{src}"', out)

    def test_keep_host_only_matches_hostname(self):
        keep = "https://cdn.myimg.cn/a.png"
        other = "https://other.invalid/b.png"
        html = f'<img src="{keep}"><img src="{other}">'
        out, stats = inline(html, str(self.dir), 3, 1, log=lambda *_: None,
                            keep_hosts=["cdn.myimg.cn"])
        self.assertEqual(stats["kept"], 1)
        self.assertEqual(stats["failed"], 1)  # other.invalid 下载失败
        self.assertIn(f'src="{keep}"', out)

    def test_inline_all_overrides_keep(self):
        # inline_all 时 keep_hosts 失效，走下载（.invalid 域名必然失败，不产生真实请求流量）
        src = "https://cdn.myimg.cn.invalid/a.png"
        _, stats = inline(f'<img src="{src}">', str(self.dir), 3, 1,
                          log=lambda *_: None,
                          keep_hosts=["cdn.myimg.cn.invalid"], inline_all=True)
        self.assertEqual(stats["kept"], 0)
        self.assertEqual(stats["failed"], 1)


if __name__ == "__main__":
    unittest.main()

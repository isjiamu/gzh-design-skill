#!/usr/bin/env python3
"""Regression checks for preview copying and malformed leaf attributes."""

import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
VALIDATE = ROOT / "scripts" / "validate_gzh_html.py"
WRAP = ROOT / "scripts" / "wrap_preview.py"


def run(*args):
    return subprocess.run(
        [sys.executable, *map(str, args)],
        capture_output=True,
        text=True,
        check=False,
    )


def main():
    valid = '<section><p><span leaf="">正常内容</span></p></section>'
    malformed = '<section><p><span leaf="损坏内容</span></p></section>'

    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)
        valid_path = tmp_path / "valid.html"
        malformed_path = tmp_path / "malformed.html"
        preview_path = tmp_path / "preview.html"
        valid_path.write_text(valid, encoding="utf-8")
        malformed_path.write_text(malformed, encoding="utf-8")

        valid_result = run(VALIDATE, valid_path)
        assert valid_result.returncode == 0, valid_result.stdout

        malformed_result = run(VALIDATE, malformed_path)
        assert malformed_result.returncode != 0
        assert "未闭合的 leaf 属性" in malformed_result.stdout

        wrap_result = run(WRAP, valid_path, preview_path)
        assert wrap_result.returncode == 0, wrap_result.stdout
        preview = preview_path.read_text(encoding="utf-8")
        assert preview.index("<script>") < preview.index('<div id="gzh-content">')
        assert "navigator.clipboard.write" in preview
        assert "document.execCommand('copy')" in preview

    print("preview regression checks passed")


if __name__ == "__main__":
    main()

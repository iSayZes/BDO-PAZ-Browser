"""Build the format docs wiki: a static site from docs/file-formats/.

    python build_wiki.py               # writes _site/
    python build_wiki.py --out ./wiki

The Wiki workflow (.github/workflows/wiki.yml) runs this on every push to
main that changes the docs or the generator, and publishes _site/ to GitHub
Pages. Open _site/index.html to preview a change locally. See "Format Docs
Wiki" in docs/format-docs.md.
"""

from __future__ import annotations

import argparse
import sys
from collections.abc import Sequence
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "PAZ-Parser"))

from wiki import build_site  # noqa: E402

DOCS_DIR = ROOT / "docs"
DEFAULT_OUT = ROOT / "_site"


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Build the format docs wiki from docs/file-formats/.")
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT, help=f"Output folder (default: {DEFAULT_OUT.name}/)")
    args = parser.parse_args(argv)
    try:
        result = build_site(DOCS_DIR, args.out)
    except OSError as ex:
        print(f"Error: could not write the wiki: {ex}", file=sys.stderr)
        return 1
    print(f"Done: {result.pages} pages, {result.converted} in the layout format, in {result.out_dir}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

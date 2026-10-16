from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

import pytest

from wiki import build_site
from wiki.format_list import game_totals
from wiki.markdown_html import render_inline, render_markdown

REPO_ROOT = Path(__file__).resolve().parents[2]
REPO_DOCS = REPO_ROOT / "docs"
CONVERTED_DOC = """# `test.bss` Format

## Purpose

Rows that point at [`other.dbss`](other_dbss.md).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

<!-- versions:end -->

## Companion Files

None.

## Layout 1

### File Layout

| Offset  | Type           | Field     | Notes |
| ------- | -------------- | --------- | ----- |
| `+0x00` | u32            | row_count |       |
| `+0x04` | Row[row_count] | rows      |       |

### Row (8 bytes)

| Offset  | Type | Field      | Notes      |
| ------- | ---- | ---------- | ---------- |
| `+0x00` | u32  | key        | Row key    |
| `+0x04` | u32  | unknown_04 | Always `0` |

## Open Questions

### What is unknown_04?

Always zero.
"""
PLAIN_DOC = "# `other.dbss` Format\n\n## Purpose\n\nOther rows. See [the handler guide](../handler.md#offset-tables).\n"
DOCUMENTED = (
    "| File | Description | Docs | Open Questions | In-Game Checks |\n| --- | --- | --- | --- | --- |\n"
    "| `test.bss` | Test rows | [test](file-formats/test_bss.md) | 1 | 0 |\n"
)


def _no_links(url: str) -> str:
    return url


@pytest.fixture
def docs_dir(tmp_path: Path) -> Path:
    formats = tmp_path / "docs" / "file-formats"
    formats.mkdir(parents=True)
    (formats / "test_bss.md").write_text(CONVERTED_DOC, encoding="utf-8")
    (formats / "other_dbss.md").write_text(PLAIN_DOC, encoding="utf-8")
    (formats / "_template.md").write_text("# `<filename.ext>` Format\n", encoding="utf-8")
    (tmp_path / "docs" / "documented-formats.md").write_text(DOCUMENTED, encoding="utf-8")
    return tmp_path / "docs"


def _formats(out: Path) -> dict[str, dict]:
    text = (out / "formats.js").read_text(encoding="utf-8")
    entries = json.loads(text.splitlines()[0].removeprefix("var FORMATS = ").rstrip(";"))
    return {entry["page"]: entry for entry in entries}


def test_inline_markdown_renders_code_links_and_bold() -> None:
    html = render_inline("**Use** `a<b` and [`x.dbss`](x_dbss.md)", lambda url: url.replace(".md", ".html"))

    assert html == '<b>Use</b> <code>a&lt;b</code> and <a href="x_dbss.html"><code>x.dbss</code></a>'


def test_block_markdown_renders_lists_tables_code_and_drops_comments() -> None:
    text = "- one\n  - nested\n- two\n\n| A | B |\n| - | - |\n| `1` | 2 |\n\n```text\n<raw>\n```\n\n<!-- hidden -->\n"

    html = render_markdown(text, _no_links)

    assert "<ul><li>one<ul><li>nested</li></ul></li><li>two</li></ul>" in html
    assert "<td><code>1</code></td><td>2</td>" in html
    assert "<pre><code>&lt;raw&gt;</code></pre>" in html
    assert "hidden" not in html


def test_the_site_has_an_index_a_page_per_doc_and_the_static_files(docs_dir: Path, tmp_path: Path) -> None:
    result = build_site(docs_dir, tmp_path / "site")

    names = {path.name for path in (tmp_path / "site").iterdir()}
    assert {"index.html", "formats.js", "static", "test_bss.html", "other_dbss.html"} <= names
    assert "_template.html" not in names
    assert (result.pages, result.converted) == (2, 1)
    assert {path.name for path in (tmp_path / "site" / "static").iterdir()} == {"wiki.css", "common.js", "index.js", "doc.js", "fonts", "favicon.ico"}
    for page_name in ("index.html", "test_bss.html"):
        assert '<link rel="icon" href="static/favicon.ico">' in (tmp_path / "site" / page_name).read_text(encoding="utf-8")


def test_pages_load_nothing_from_other_sites(docs_dir: Path, tmp_path: Path) -> None:
    build_site(docs_dir, tmp_path / "site")

    for page in (tmp_path / "site").glob("*.html"):
        text = page.read_text(encoding="utf-8")
        assert not re.search(r'<(?:link|script)[^>]+(?:href|src)="https?://', text), page.name


def test_formats_js_counts_known_bytes_of_converted_docs_only(docs_dir: Path, tmp_path: Path) -> None:
    build_site(docs_dir, tmp_path / "site")

    formats = _formats(tmp_path / "site")
    assert formats["test_bss.html"] | {"desc": ""} == {
        "page": "test_bss.html", "name": "test.bss", "others": [], "desc": "", "ext": "bss",
        "oq": 1, "ig": 0, "converted": True, "known": 8, "unknown": 4, "client": 0,
    }
    assert formats["other_dbss.html"]["converted"] is False
    summary = (tmp_path / "site" / "formats.js").read_text(encoding="utf-8").splitlines()[1]
    assert json.loads(summary.removeprefix("var SUMMARY = ").rstrip(";")) == {"documented": {"bss": 1, "dbss": 0}, "totals": {}}
    assert formats["other_dbss.html"]["desc"] == "Other rows."


def test_a_converted_page_shows_structures_and_links_docs_and_repo_files(docs_dir: Path, tmp_path: Path) -> None:
    build_site(docs_dir, tmp_path / "site")

    test_page = (tmp_path / "site" / "test_bss.html").read_text(encoding="utf-8")
    other_page = (tmp_path / "site" / "other_dbss.html").read_text(encoding="utf-8")
    assert 'id="l1-row"' in test_page and 'href="#l1-row"' in test_page
    assert 'href="other_dbss.html"' in test_page
    assert 'href="https://github.com/iSayZes/BDO-PAZ-Browser/blob/main/docs/handler.md#offset-tables"' in other_page
    assert "not in the layout format yet" in other_page


def test_a_doc_that_shares_a_layout_shows_the_linked_docs_structures(docs_dir: Path, tmp_path: Path) -> None:
    shared = CONVERTED_DOC.split("## Layout 1")[0].replace("test.bss", "shared.bss")
    shared += "## Observed Values\n\nSame layout as [`test.bss`](test_bss.md), with other rows.\n"
    (docs_dir / "file-formats" / "shared_bss.md").write_text(shared, encoding="utf-8")

    build_site(docs_dir, tmp_path / "site")

    page = (tmp_path / "site" / "shared_bss.html").read_text(encoding="utf-8")
    assert 'id="l1-row"' in page
    assert _formats(tmp_path / "site")["shared_bss.html"] | {"desc": ""} == {
        "page": "shared_bss.html", "name": "shared.bss", "others": [], "desc": "", "ext": "bss",
        "oq": 0, "ig": 0, "converted": True, "known": 8, "unknown": 4, "client": 0,
    }


VERSIONS_BLOCK = """<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File       | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | ---------- | ----- | ------- | --------- |
| 1      | 3464 and later | 3473    | `test.bss` | 804   | 100 Row | 8         |

| Layout | File       | Known         | Unknown       |
| ------ | ---------- | ------------- | ------------- |
| 1      | `test.bss` | 404 B (50.2%) | 400 B (49.8%) |

<!-- versions:end -->"""


def test_a_doc_with_versions_shows_them_and_shares_from_the_game_files(docs_dir: Path, tmp_path: Path) -> None:
    doc = docs_dir / "file-formats" / "test_bss.md"
    marker = "<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->"
    empty = f"{marker}\n\n<!-- versions:end -->"
    doc.write_text(CONVERTED_DOC.replace(empty, VERSIONS_BLOCK), encoding="utf-8")

    build_site(docs_dir, tmp_path / "site")

    page = (tmp_path / "site" / "test_bss.html").read_text(encoding="utf-8")
    entry = _formats(tmp_path / "site")["test_bss.html"]
    assert "client 3464 and later, sizes from client 3473" in page
    assert (entry["known"], entry["unknown"], entry["client"]) == (404, 400, 3473)


def test_game_totals_come_from_the_readme_supported_formats_lines() -> None:
    readme = (
        "- `.bss`: 83 of 402 files with a handler.\n"
        "- `.dbss`: 162 of 374 files with a handler.\n"
        "- Other formats: 31 with a handler.\n"
    )

    assert game_totals(readme) == {"bss": 402, "dbss": 374}


def test_the_repo_wiki_has_a_page_for_every_doc_and_no_dead_page_links(tmp_path: Path) -> None:
    build_site(REPO_DOCS, tmp_path / "site")

    docs = {path.stem for path in (REPO_DOCS / "file-formats").glob("*.md") if not path.name.startswith("_")}
    pages = {path.stem for path in (tmp_path / "site").glob("*.html")} - {"index"}
    assert pages == docs
    for page in (tmp_path / "site").glob("*.html"):
        text = page.read_text(encoding="utf-8")
        targets = set(re.findall(r'href="([a-z0-9_]+\.html)', text))
        assert targets <= {f"{name}.html" for name in pages | {"index"}}, page.name
        anchors = set(re.findall(r'href="#([a-z0-9-]+)"', text))
        assert all(f'id="{anchor}"' in text for anchor in anchors), page.name


def test_the_format_list_groups_read_the_loc_page_and_the_extension(tmp_path: Path) -> None:
    # common.js groups the list as the app's tree view: LOC pages, then .bss / .dbss, then Others.
    build_site(REPO_DOCS, tmp_path / "site")

    formats = _formats(tmp_path / "site")
    assert formats["languagedata_loc.html"]["ext"] == "other"
    assert {formats[page]["ext"] for page in ("buff_dbss.html", "buffsimply_bss.html")} == {"dbss", "bss"}
    assert formats["aiscript_ai.html"]["ext"] == "other"
    assert 'GROUP_LABELS = ["", "", "Others"]' in (REPO_ROOT / "PAZ-Parser" / "wiki" / "static" / "common.js").read_text(encoding="utf-8")


def test_build_wiki_script_writes_the_site(tmp_path: Path) -> None:
    script = REPO_ROOT / "build_wiki.py"

    done = subprocess.run([sys.executable, str(script), "--out", str(tmp_path / "site")], capture_output=True, text=True)

    assert done.returncode == 0, done.stderr
    assert (tmp_path / "site" / "index.html").exists()

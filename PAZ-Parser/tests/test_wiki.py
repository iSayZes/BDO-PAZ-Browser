from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

import pytest

from wiki import build_site, render_site
from wiki.format_list import game_totals
from wiki.markdown_html import render_inline, render_markdown
from format_docs import format_doc_paths
from format_docs.versions import ClientCheck
from wiki.timeline_model import LAYOUT, NO_FILE, NO_LAYOUT, UNDATED, TimelineLayout, build_timeline
from wiki.type_html import type_html

REPO_ROOT = Path(__file__).resolve().parents[2]
REPO_DOCS = REPO_ROOT / "docs"
CONVERTED_DOC = """# `test.bss` Format

## Purpose

Rows that point at [`other.dbss`](../dbss/other_dbss.md).

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
PLAIN_DOC = "# `other.dbss` Format\n\n## Purpose\n\nOther rows. See [the handler guide](../../handler.md#offset-tables).\n"
DOCUMENTED = (
    "| File | Description | Docs | Open Questions | In-Game Checks |\n| --- | --- | --- | --- | --- |\n"
    "| `test.bss` | Test rows | [test](file-formats/bss/test_bss.md) | 1 | 0 |\n"
)


def _no_links(url: str) -> str:
    return url


@pytest.fixture
def docs_dir(tmp_path: Path) -> Path:
    formats = tmp_path / "docs" / "file-formats"
    for group in ("bss", "dbss"):
        (formats / group).mkdir(parents=True)
    (formats / "bss" / "test_bss.md").write_text(CONVERTED_DOC, encoding="utf-8")
    (formats / "dbss" / "other_dbss.md").write_text(PLAIN_DOC, encoding="utf-8")
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


def test_a_code_span_that_is_a_number_or_text_type_gets_token_colors_and_others_stay_plain() -> None:
    html = render_inline("`u32` then `char16[count]`, `Row[count]` and `row_count`", _no_links)

    assert '<code><span class="tk-num">u32</span></code>' in html
    assert '<span class="tk-text">char16</span><span class="tk-punct">[</span><span class="tk-field">count</span>' in html
    assert "<code>Row[count]</code>" in html and "<code>row_count</code>" in html


def test_a_type_cell_becomes_tokens_that_spell_it_and_text_outside_the_grammar_is_none() -> None:
    cell = 'Tail if name ^= HH_ or kind = 2'
    html = type_html(cell)

    assert html is not None
    assert re.sub(r"<[^>]+>", "", html) == cell
    assert '<span class="tk-struct">Tail</span> <span class="tk-kw">if</span>' in html
    assert '<span class="tk-str">HH_</span>' in html and '<span class="tk-lit">2</span>' in html
    assert type_html("see Notes") is None
    assert type_html("Row[count]", allow_structures=False) is None


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
    assert '<a href="#l1-row"><span class="tk-struct">Row</span>' in test_page
    assert '<td class="mono"><span class="tk-num">u32</span></td>' in test_page
    assert "Current: Layout" not in test_page
    assert 'href="other_dbss.html"' in test_page
    assert 'href="https://github.com/iSayZes/BDO-PAZ-Browser/blob/main/docs/handler.md#offset-tables"' in other_page
    assert "not in the layout format yet" in other_page


def test_a_doc_that_shares_a_layout_shows_the_linked_docs_structures(docs_dir: Path, tmp_path: Path) -> None:
    shared = CONVERTED_DOC.split("## Layout 1")[0].replace("test.bss", "shared.bss")
    shared += "## Observed Values\n\nSame layout as [`test.bss`](test_bss.md), with other rows.\n"
    (docs_dir / "file-formats" / "bss" / "shared_bss.md").write_text(shared, encoding="utf-8")

    build_site(docs_dir, tmp_path / "site")

    page = (tmp_path / "site" / "shared_bss.html").read_text(encoding="utf-8")
    assert 'id="l1-row"' in page
    assert _formats(tmp_path / "site")["shared_bss.html"] | {"desc": ""} == {
        "page": "shared_bss.html", "name": "shared.bss", "others": [], "desc": "", "ext": "bss",
        "oq": 0, "ig": 0, "converted": True, "known": 8, "unknown": 4, "client": 0,
    }


VERSIONS_BLOCK = """<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File       | Bytes | Records | Row bytes |
| ------ | -------------- | ---------- | ----- | ------- | --------- |
| 1      | 3464 and later | `test.bss` | 804   | 100 Row | 8         |

| Layout | File       | Known         | Unknown       |
| ------ | ---------- | ------------- | ------------- |
| 1      | `test.bss` | 404 B (50.2%) | 400 B (49.8%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3473   | Layout 1 |
| 3464   | Layout 1 |
| 1230   | No file  |

<!-- versions:end -->"""


def test_a_doc_with_versions_shows_them_and_shares_from_the_game_files(docs_dir: Path, tmp_path: Path) -> None:
    doc = docs_dir / "file-formats" / "bss" / "test_bss.md"
    marker = "<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->"
    empty = f"{marker}\n\n<!-- versions:end -->"
    doc.write_text(CONVERTED_DOC.replace(empty, VERSIONS_BLOCK), encoding="utf-8")

    build_site(docs_dir, tmp_path / "site")

    page = (tmp_path / "site" / "test_bss.html").read_text(encoding="utf-8")
    entry = _formats(tmp_path / "site")["test_bss.html"]
    assert "client 3464 and later, sizes from client 3473" in page
    assert (entry["known"], entry["unknown"], entry["client"]) == (404, 400, 3473)


def test_a_versions_card_without_layout_rows_leaves_out_the_checked_against_column(docs_dir: Path, tmp_path: Path) -> None:
    doc = docs_dir / "file-formats" / "bss" / "test_bss.md"
    marker = "<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->"
    clients = (
        f"{marker}\n\nEvery client the doc check read, and the layout its files fit.\n\n"
        "| Client | Result  | Checked against |\n| ------ | ------- | --------------- |\n| 1230   | No file | `37e1249bfa22`  |\n\n"
        "<!-- versions:end -->"
    )
    doc.write_text(CONVERTED_DOC.replace(f"{marker}\n\n<!-- versions:end -->", clients), encoding="utf-8")

    build_site(docs_dir, tmp_path / "site")

    versions = (tmp_path / "site" / "test_bss.html").read_text(encoding="utf-8").split('aria-labelledby="versions"')[1].split("</section>")[0]
    assert "No file" in versions
    assert "Checked against" not in versions
    assert "37e1249bfa22" not in versions


def test_the_versions_card_opens_with_a_timeline_of_the_checked_clients(docs_dir: Path, tmp_path: Path) -> None:
    doc = docs_dir / "file-formats" / "bss" / "test_bss.md"
    marker = "<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->"
    doc.write_text(CONVERTED_DOC.replace(f"{marker}\n\n<!-- versions:end -->", VERSIONS_BLOCK), encoding="utf-8")

    build_site(docs_dir, tmp_path / "site")

    page = (tmp_path / "site" / "test_bss.html").read_text(encoding="utf-8")
    versions = page.split('aria-labelledby="versions"')[1].split("</section>")[0]
    assert versions.index('class="tl"') < versions.index('class="ver sel"')
    assert 'class="tl-band sel" data-layout="1"' in versions
    assert '<div class="tl-band absent" title="Not in client 1230."' in versions
    checked = versions.split('id="checkedVersions"')[1]
    assert '<option value="naeu" selected>NA / EU / OC</option>' in checked
    naeu, others = checked.split('data-region="naeu"')[1].split("</ul>", 1)
    assert [chip.split(">", 1)[0] for chip in naeu.split("<li><")[1:]] == [
        'button type="button" class="cv-chip" data-layout="1" title="Layout 1" aria-label="Client 3473, show layout 1"',
        'button type="button" class="cv-chip" data-layout="1" title="Layout 1" aria-label="Client 3464, show layout 1"',
        'span class="cv-chip absent" title="No file"',
    ]
    assert 'class="cv-chip' not in others
    assert "<table" not in versions
    assert 'id="layoutPill">Layout 1 · client 3464 and later</span>' in page and 'id="layoutTabs"' not in page


AXIS = (794, 1230, 1485, 1784, 2107, 2519, 3002, 3251, 3474)


def test_the_timeline_runs_live_to_oldest_with_no_documented_layout_and_no_file_bands_in_place() -> None:
    layouts = (TimelineLayout(2, 2519, None, True, 3474), TimelineLayout(1, 1485, 1784, False, 1784))
    clients = (
        ClientCheck(3474, 2, True), ClientCheck(2519, 2, True), ClientCheck(2107, None, True),
        ClientCheck(1784, 1, True), ClientCheck(1485, 1, True), ClientCheck(794, None, False),
    )

    model = build_timeline(layouts, clients, AXIS)

    assert [(band.kind, band.layout) for band in model.bands] == [(LAYOUT, 2), (NO_LAYOUT, None), (LAYOUT, 1), (NO_FILE, None)]
    assert (model.bands[0].left, model.bands[-1].right) == (0.0, 1.0)
    assert all(newer.right == older.left for newer, older in zip(model.bands, model.bands[1:]))
    assert model.bands[1].left == model.at[2107] and model.bands[3].left == model.at[794]
    assert model.ticks == (794, 1784, 2107, 3474)


def test_a_layout_with_no_checked_client_sits_between_the_layouts_numbered_around_it() -> None:
    layouts = (TimelineLayout(3, 3473, None, True, 3474), TimelineLayout(2, None, None, False, None), TimelineLayout(1, 1784, 1784, False, 1784))
    clients = (ClientCheck(3474, 3, True), ClientCheck(1784, 1, True))

    model = build_timeline(layouts, clients, AXIS)

    assert [(band.kind, band.layout) for band in model.bands] == [(LAYOUT, 3), (UNDATED, 2), (LAYOUT, 1)]
    assert (model.bands[1].left, model.bands[1].right) == (model.at[3473], model.at[1784])


def test_game_totals_come_from_the_readme_supported_formats_lines() -> None:
    readme = (
        "- `.bss`: 83 of 402 files with a handler.\n"
        "- `.dbss`: 162 of 374 files with a handler.\n"
        "- Other formats: 31 with a handler.\n"
    )

    assert game_totals(readme) == {"bss": 402, "dbss": 374}


def test_the_repo_wiki_has_a_page_for_every_doc_and_no_dead_page_links() -> None:
    # Rendered in memory: reading ~300 freshly written pages back took 2.3 s,
    # spent in the virus scanner on first open.
    html_pages = {name: text for name, text in render_site(REPO_DOCS).files.items() if name.endswith(".html")}

    docs = {path.stem for path in format_doc_paths(REPO_DOCS / "file-formats")}
    pages = {Path(name).stem for name in html_pages} - {"index"}
    assert pages == docs
    for name, text in html_pages.items():
        targets = set(re.findall(r'href="([a-z0-9_]+\.html)', text))
        assert targets <= {f"{page}.html" for page in pages | {"index"}}, name
        anchors = set(re.findall(r'href="#([a-z0-9-]+)"', text))
        assert all(f'id="{anchor}"' in text for anchor in anchors), name


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

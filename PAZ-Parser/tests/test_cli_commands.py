"""`--index`, `--render`, file lookup and the shared path matcher."""
from __future__ import annotations

import pytest

from api.bdo_api_helpers import path_matcher
from bdo_models import PazEntry
from cli.errors import CliError
from cli.index import entry_records, parse_id, parse_kind
from cli.parsed_file import find_entry
from cli.render import app_stylesheet, inline_icons, standalone_page
from _common.html import (
    PENDING_ICON_CELL_RE,
    PENDING_ICON_LABEL_RE,
    icon_cell,
    icon_html_label_cell,
    icon_label_cell,
    missing_icon_cell,
)
from _common.lookup_index import IndexKind, clear_indexes, init_index


def _entry(path: str) -> PazEntry:
    return PazEntry(
        archive_name="pad00001.paz",
        internal_path=path,
        offset=0,
        compressed_size=1,
        uncompressed_size=1,
        compression_type=0,
        encryption_type=0,
    )


# ── Path matching and file lookup ────────────────────────────────────────────

def test_path_matcher_globs_path_or_name_and_substrings_otherwise() -> None:
    assert path_matcher("*.BSS")("gamecommondata/binary/buffsimply.bss")
    assert path_matcher("gamecommondata/*/buff*")("gamecommondata/binary/buffsimply.bss")
    assert path_matcher("binary/buff")("gamecommondata/binary/buffsimply.bss")
    assert not path_matcher("buff*.dbss")("gamecommondata/binary/buffsimply.bss")


_ENTRIES = [_entry(path) for path in (
    "gamecommondata/binary/title.dbss",
    "gamecommondata/binary/subtitle.dbss",
    "gamecommondata/binary/buffoffset.dbss",
    "ui/a/same.xml",
    "ui/b/same.xml",
)]


def test_find_entry_prefers_an_exact_file_name() -> None:
    # As a substring, "title.dbss" also hits subtitle.dbss.
    assert find_entry(_ENTRIES, "TITLE.dbss").internal_path == _ENTRIES[0].internal_path


def test_find_entry_takes_a_single_pattern_hit() -> None:
    assert find_entry(_ENTRIES, "buffoff").internal_path == _ENTRIES[2].internal_path


@pytest.mark.parametrize("name", ["same.xml", "*title*", "missing.bss"])
def test_find_entry_rejects_ambiguous_or_missing(name: str) -> None:
    with pytest.raises(CliError):
        find_entry(_ENTRIES, name)


def test_find_entry_takes_a_full_path_among_same_names() -> None:
    assert find_entry(_ENTRIES, "ui\\b\\same.xml").internal_path == _ENTRIES[4].internal_path


# ── Index ────────────────────────────────────────────────────────────────────

def test_parse_kind_accepts_value_and_name() -> None:
    assert parse_kind("buff_icon") is IndexKind.BUFF_ICON
    assert parse_kind("BUFF_ICON") is IndexKind.BUFF_ICON
    with pytest.raises(CliError, match="buff_icon"):
        parse_kind("nope")


def test_parse_id() -> None:
    assert parse_id("0x10") == 16
    assert parse_id(None) is None
    with pytest.raises(CliError):
        parse_id("ten")


def test_entry_records_one_or_all_sorted() -> None:
    clear_indexes()
    try:
        init_index(IndexKind.KNOWLEDGE_CHARACTERS, {9: (1, 2), 3: (4,)})

        assert entry_records(IndexKind.KNOWLEDGE_CHARACTERS, 9, None) == [{"id": 9, "value": (1, 2)}]
        assert [r["id"] for r in entry_records(IndexKind.KNOWLEDGE_CHARACTERS, None, None)] == [3, 9]
        assert len(entry_records(IndexKind.KNOWLEDGE_CHARACTERS, None, 1)) == 1
        with pytest.raises(CliError):
            entry_records(IndexKind.KNOWLEDGE_CHARACTERS, 5, None)
    finally:
        clear_indexes()


# ── Render ───────────────────────────────────────────────────────────────────

def test_pending_icon_pattern_matches_icon_cell() -> None:
    path = 'ui/icon/a"&<b.dds'

    assert PENDING_ICON_CELL_RE.fullmatch(icon_cell(path))
    assert not PENDING_ICON_CELL_RE.search(icon_cell(path, "data:image/png;base64,AA"))


def test_inline_icons_embeds_found_icons_and_dashes_missing_ones() -> None:
    found, missing = "ui/icon/found.dds", 'ui/icon/"missing".dds'
    icons = {found: "data:image/png;base64,AA"}
    requests: list[str] = []

    def icon_url(path: str) -> str | None:
        requests.append(path)
        return icons.get(path)

    body = f"<td>{icon_cell(found)}</td><td>{icon_cell(missing)}</td>"

    result = inline_icons(body, icon_url)

    assert requests == [found, missing]
    assert icon_cell(found, "data:image/png;base64,AA") in result
    assert missing_icon_cell(missing) in result
    assert "icon-cell-placeholder" not in result


def test_pending_label_pattern_matches_icon_label_cell() -> None:
    path, label = 'ui/icon/a"&<b.dds', "Sap & <Knot>"

    assert PENDING_ICON_LABEL_RE.match(icon_label_cell(path, label))
    assert not PENDING_ICON_LABEL_RE.search(icon_label_cell(path, label, "data:image/png;base64,AA"))


def _missing_label_entry(path: str, label: str, tooltip: str | None = None) -> str:
    """What the GUI turns an unshipped `icon_label_cell` into: no swatch, label kept."""
    return (
        f'<span class="icon-cell icon-label-cell icon-cell-missing" title="{tooltip or path}" '
        f'data-icon-path="{path}"><span class="icon-cell-label">{label}</span></span>'
    )


def test_inline_icons_keeps_the_label_of_a_missing_list_entry() -> None:
    found, missing = "ui/icon/found.dds", "ui/icon/missing.dds"
    icons = {found: "data:image/png;base64,AA"}
    body = f"<td>{icon_label_cell(found, 'Sap')}, {icon_label_cell(missing, 'Knot & Bark')}</td>"

    result = inline_icons(body, icons.get)

    assert icon_label_cell(found, "Sap", "data:image/png;base64,AA") in result
    assert _missing_label_entry(missing, "Knot &amp; Bark") in result
    assert "icon-cell-placeholder" not in result


def test_inline_icons_keeps_a_coloured_label_intact() -> None:
    found, missing = "ui/icon/found.dds", "ui/icon/missing.dds"
    icons = {found: "data:image/png;base64,AA"}
    label = '1 <span class="pa-color" style="color: red">Sap</span> &amp; Knot'
    body = f"{icon_html_label_cell(found, label)}, {icon_html_label_cell(missing, label)}"

    result = inline_icons(body, icons.get)

    assert icon_html_label_cell(found, label, "data:image/png;base64,AA") in result
    assert _missing_label_entry(missing, label) in result


def test_standalone_page_carries_the_app_table_css() -> None:
    page = standalone_page("buff.dbss", "note", '<table class="data-table"></table>', app_stylesheet())

    assert page.startswith("<!doctype html>")
    assert ".data-table" in page
    assert "--color-raised" in page
    assert '<div id="preview-content"><table class="data-table"></table></div>' in page


def test_inline_icons_keeps_a_list_entry_tooltip() -> None:
    found, missing = "ui/icon/found.dds", "ui/icon/missing.dds"
    icons = {found: "data:image/png;base64,AA"}
    body = f"{icon_label_cell(found, 'Sap', tooltip='Buff 1')}, {icon_label_cell(missing, 'Knot', tooltip='Buff 2')}"

    result = inline_icons(body, icons.get)

    assert icon_label_cell(found, "Sap", "data:image/png;base64,AA", "Buff 1") in result
    assert _missing_label_entry(missing, "Knot", "Buff 2") in result

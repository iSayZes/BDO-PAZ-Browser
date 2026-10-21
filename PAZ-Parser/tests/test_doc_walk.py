"""The layout walk and the Versions section, on bytes the tests build."""
from __future__ import annotations

import struct
from pathlib import Path

import pytest

from format_docs import check_doc, read_layouts
from format_docs.check_run import Client, Status, check_doc_file
from format_docs.doc_fit import fit_layouts
from format_docs.versions import ClientCheck, VersionRow, merge_clients, merge_rows, read_clients, read_rows, render_rows, write_rows
from format_docs.walk_model import LayoutFit, LayoutMiss, Unwalkable

VERSIONS = (
    "## Versions\n\n"
    "<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->\n\n"
    "<!-- versions:end -->\n"
)


def _table(heading: str, *rows: tuple[str, str, str]) -> str:
    lines = [f"### {heading}", "", "| Offset | Type | Field | Notes |", "| --- | --- | --- | --- |"]
    lines += [f"| `{offset}` | {type_text} | {name} | note |" for offset, type_text, name in rows]
    return "\n".join(lines) + "\n"


def _doc(*structures: str, layouts: str | None = None) -> str:
    body = layouts if layouts is not None else "## Layout 1\n\n" + "\n".join(structures)
    return f"# `test.bss` Format\n\n## Purpose\n\nRows.\n\n{VERSIONS}\n{body}"


def _fit(text: str, files: dict[str, bytes]) -> LayoutFit | tuple[LayoutMiss, ...]:
    layouts, problems = read_layouts(text)
    assert problems == ()
    return fit_layouts(layouts, files)


def _str16(text: str) -> bytes:
    return struct.pack("<Q", len(text)) + text.encode("utf-16-le")


def _pstr(text: str) -> bytes:
    raw = text.encode("utf-8")
    return struct.pack("<BI", 0, len(raw)) + raw


COUNTED = _table("File Layout", ("+0x00", "u32", "count"), ("+0x04", "Row[count]", "rows"))
ROW = _table("Row (8 bytes)", ("+0x00", "u32", "key"), ("+0x04", "u32", "unknown_04"))


def test_a_file_that_walks_to_its_end_fits_with_known_and_unknown_bytes() -> None:
    data = struct.pack("<I", 2) + struct.pack("<II", 1, 0) * 2

    fit = _fit(_doc(COUNTED, ROW), {"test.bss": data})

    assert isinstance(fit, LayoutFit)
    file = fit.files[0]
    assert (file.known, file.unknown, file.size) == (12, 8, 20)
    assert file.rows["Row"].count == 2


def test_a_file_with_bytes_left_over_names_where_the_fields_end() -> None:
    data = struct.pack("<I", 1) + struct.pack("<II", 1, 0) + b"\x00"

    misses = _fit(_doc(COUNTED, ROW), {"test.bss": data})

    assert isinstance(misses, tuple)
    assert misses[0].error.message == "the fields end at 0xC, the file ends at 0xD"


def test_a_count_past_the_end_names_the_field_and_the_missing_bytes() -> None:
    misses = _fit(_doc(COUNTED, ROW), {"test.bss": struct.pack("<I", 2) + struct.pack("<II", 1, 0)})

    assert isinstance(misses, tuple)
    assert (misses[0].error.structure, misses[0].error.field) == ("Row", "key")


def test_strings_need_a_zero_high_word_and_follow_on_by_their_length() -> None:
    row = _table("Row (variable: 12 bytes + name)", ("+0x00", "u32", "key"), ("+0x04", "str16", "name_kr"), ("name_kr+0x00", "u8", "unknown_after_name_kr"))
    good = struct.pack("<I", 1) + struct.pack("<I", 7) + _str16("ab") + b"\x01"
    bad = struct.pack("<I", 1) + struct.pack("<I", 7) + struct.pack("<II", 2, 1) + b"a\x00b\x00\x01"

    assert isinstance(_fit(_doc(COUNTED, row), {"test.bss": good}), LayoutFit)
    misses = _fit(_doc(COUNTED, row), {"test.bss": bad})
    assert isinstance(misses, tuple) and "high word" in misses[0].error.message


def test_a_pabr_string_table_and_a_trailer_read_from_the_end() -> None:
    layout = _table(
        "File Layout",
        ("+0x00", "char[4]", "magic"), ("+0x04", "u32", "count"), ("+0x08", "Row[count]", "rows"),
        ("rows+0x00", "String Table", "string_table"), ("string_table+0x00", "u32", "table_start"), ("string_table+0x04", "u32", "zero"),
    )
    strings = _table("String Table (variable: 4 bytes + strings)", ("+0x00", "u32", "string_count"), ("+0x04", "pstr[string_count]", "strings"))
    data = b"PABR" + struct.pack("<I", 1) + struct.pack("<II", 5, 0)
    data += struct.pack("<I", 2) + _pstr("a") + _pstr("bc") + struct.pack("<II", len(data), 0)

    assert isinstance(_fit(_doc(layout, ROW, strings), {"test.bss": data}), LayoutFit)


def test_an_array_runs_up_to_a_field_read_from_the_end_of_the_file() -> None:
    layout = _table("File Layout", ("+0x00", "u32[..end_of_data]", "values"), ("EOF-0x08", "u32", "end_of_data"), ("EOF-0x04", "u32", "zero"))
    data = struct.pack("<III", 1, 2, 3) + struct.pack("<II", 12, 0)

    fit = _fit(_doc(layout), {"test.bss": data})

    assert isinstance(fit, LayoutFit) and fit.files[0].known == 20


def test_while_stops_before_the_row_that_holds_the_stop_value() -> None:
    layout = _table("File Layout", ("+0x00", "Row[while key != 200]", "rows"), ("rows+0x00", "Row[..end]", "slots"))
    data = struct.pack("<II", 1, 0) + struct.pack("<II", 2, 0) + struct.pack("<II", 200, 0)

    fit = _fit(_doc(layout, ROW), {"test.bss": data})

    assert isinstance(fit, LayoutFit) and fit.files[0].rows["Row"].count == 3


def test_conditions_and_a_union_pick_one_branch() -> None:
    row = _table(
        "Row (variable: 1 bytes + body)",
        ("+0x00", "u8", "kind"), ("+0x01", "u32 if kind = 2", "body_a"), ("body_a+0x00", "u16 if kind != 2", "body_b"),
    )
    data = struct.pack("<I", 2) + struct.pack("<BI", 2, 9) + struct.pack("<BH", 1, 9)

    fit = _fit(_doc(COUNTED, row), {"test.bss": data})

    assert isinstance(fit, LayoutFit) and fit.files[0].rows["Row"].smallest == 3


def test_a_clause_outside_the_grammar_is_reported() -> None:
    row = _table(
        "Row (variable: 9 bytes + name and tail)",
        ("+0x00", "u8", "kind"), ("+0x01", "str8", "name"),
        ("name+0x00", "u16 if name !^= HH_ and kind > 5", "unknown_other"),
    )

    messages = [problem.message for problem in check_doc(_doc(COUNTED, row))]
    assert any("is not `field = value`" in message for message in messages)


def test_or_conditions_pick_the_branch_for_each_row() -> None:
    row = _table(
        "Row (variable: 9 bytes + name and tail)",
        ("+0x00", "u8", "kind"), ("+0x01", "str8", "name"),
        ("name+0x00", "u32 if name ^= HH_ or kind = 5", "unknown_house"),
        ("unknown_house+0x00", "u16 if name !^= HH_ and kind != 5", "unknown_other"),
    )
    house = struct.pack("<B", 1) + struct.pack("<Q", 4) + b"HH_a" + struct.pack("<I", 7)
    empty = struct.pack("<B", 5) + struct.pack("<Q", 0) + struct.pack("<I", 7)
    other = struct.pack("<B", 1) + struct.pack("<Q", 1) + b"x" + struct.pack("<H", 7)
    data = struct.pack("<I", 3) + house + empty + other

    fit = _fit(_doc(COUNTED, row), {"test.bss": data})

    assert isinstance(fit, LayoutFit)
    assert (fit.files[0].rows["Row"].smallest, fit.files[0].rows["Row"].largest) == (12, 17)


def test_a_two_dimensional_array_takes_both_counts_from_fields() -> None:
    grid = _table(
        "File Layout", ("+0x00", "u8", "width"), ("+0x01", "u8", "height"), ("+0x02", "u16[height][width]", "cells"),
    )
    data = struct.pack("<BB", 3, 2) + struct.pack("<6H", *range(6))

    assert isinstance(_fit(_doc(grid), {"test.bss": data}), LayoutFit)


def test_a_structure_sized_by_its_offset_file_reads_rest_and_end_rows() -> None:
    main = _table("File Layout", ("+0x00", "u32", "count"), ("+0x04", "Payload[count]", "payloads"))
    payload = _table(
        "Payload (variable: 6 bytes, size from `testoffset.dbss`)",
        ("+0x00", "u32", "key"), ("+0x04", "bytes[rest]", "unknown_04"), ("end-0x02", "u16", "unknown_end"),
    )
    offsets = _table("`testoffset.dbss`", ("+0x00", "u32", "count"), ("+0x04", "Offset Row[count]", "rows"))
    offset_row = _table("Offset Row (8 bytes)", ("+0x00", "u32", "data_offset"), ("+0x04", "u32", "data_size"))
    data = struct.pack("<I", 2) + struct.pack("<I", 1) + b"xyz" + struct.pack("<H", 0) + struct.pack("<I", 2) + struct.pack("<H", 0)
    offset_file = struct.pack("<I", 2) + struct.pack("<II", 4, 9) + struct.pack("<II", 13, 6)

    fit = _fit(_doc(main, payload, offsets, offset_row), {"test.bss": data, "testoffset.dbss": offset_file})

    assert isinstance(fit, LayoutFit)
    assert fit.files[0].rows["Payload"].smallest == 6 and fit.files[0].rows["Payload"].largest == 9


def test_an_older_layout_fits_when_the_newest_does_not() -> None:
    old_row = _table("Row (6 bytes)", ("+0x00", "u16", "key"), ("+0x02", "u32", "unknown_04"))
    layouts = f"## Layout 2\n\n{COUNTED}\n{ROW}\n## Layout 1\n\n{old_row}"
    data = struct.pack("<I", 2) + struct.pack("<HI", 1, 0) * 2

    fit = _fit(_doc(layouts=layouts), {"test.bss": data})

    assert isinstance(fit, LayoutFit) and fit.layout == 1


def test_scanned_bytes_cannot_be_walked() -> None:
    row = _table("Row (variable: 4 bytes + scan)", ("+0x00", "bytes[scan]", "unknown_gap"), ("unknown_gap+0x00", "u32", "key"))

    with pytest.raises(Unwalkable):
        _fit(_doc(COUNTED, row), {"test.bss": struct.pack("<I", 1) + b"\x00" * 4})


def _version(layout: int, client: int, size: int) -> VersionRow:
    return VersionRow(layout, client, client, "test.bss", size, "2 Row", "8", size - 4, 4)


def test_a_client_widens_its_layouts_range_and_an_older_one_keeps_the_newer_sizes() -> None:
    merged = merge_rows([_version(2, 3464, 100)], [_version(2, 3473, 120)])
    older = merge_rows(merged, [_version(2, 3401, 90)])

    assert [(row.first, row.checked, row.size) for row in older] == [(3401, 3473, 120)]


def test_rows_of_other_layouts_are_never_dropped() -> None:
    merged = merge_rows([_version(1, 3401, 90)], [_version(2, 3464, 100)])

    assert [row.layout for row in merged] == [2, 1]


def test_the_versions_block_round_trips_and_names_the_newest_layout_and_later() -> None:
    rows = merge_rows([], [_version(2, 3464, 1_000), _version(1, 3401, 900)])
    clients = merge_clients([], [ClientCheck(3464, 2, True), ClientCheck(3401, 1, True), ClientCheck(2107, None, True), ClientCheck(1230, None, False)])
    text = write_rows(_doc(COUNTED, ROW), rows, clients, newest_layout=2)

    assert "3464 and later" in render_rows(rows, clients, 2)
    assert read_rows(text) == rows
    assert read_clients(text) == clients
    assert write_rows(text, read_rows(text), read_clients(text), newest_layout=2) == text


def test_a_client_read_again_keeps_only_its_new_result_and_the_newest_client_comes_first() -> None:
    merged = merge_clients([ClientCheck(1784, 1, True), ClientCheck(1230, None, False)], [ClientCheck(1230, 1, True), ClientCheck(3474, 2, True)])

    assert merged == (ClientCheck(3474, 2, True), ClientCheck(1784, 1, True), ClientCheck(1230, 1, True))


def test_check_doc_file_writes_versions_once_and_then_reports_ok(tmp_path: Path) -> None:
    doc = tmp_path / "test_bss.md"
    doc.write_text(_doc(COUNTED, ROW), encoding="utf-8")
    data = struct.pack("<I", 1) + struct.pack("<II", 1, 0)
    client = Client(3473, lambda name: data if name == "test.bss" else None)
    rows = {"test_bss.md": [("test.bss", "Rows")]}

    first = check_doc_file(doc, rows, client)
    second = check_doc_file(doc, rows, client)

    assert (first.status, second.status) == (Status.UPDATED, Status.OK)
    assert "| 1      | 3473 and later | 3473" in doc.read_text(encoding="utf-8")
    assert read_clients(doc.read_text(encoding="utf-8")) == (ClientCheck(3473, 1, True),)


def test_a_client_without_the_docs_files_is_recorded_as_no_file_once(tmp_path: Path) -> None:
    doc = tmp_path / "test_bss.md"
    doc.write_text(_doc(COUNTED, ROW), encoding="utf-8")
    client = Client(794, lambda name: None)
    rows = {"test_bss.md": [("test.bss", "Rows")]}

    first = check_doc_file(doc, rows, client)
    second = check_doc_file(doc, rows, client)

    assert (first.status, second.status) == (Status.UPDATED, Status.SKIPPED)
    assert read_clients(doc.read_text(encoding="utf-8")) == (ClientCheck(794, None, False),)
    assert read_rows(doc.read_text(encoding="utf-8")) == ()


def test_a_doc_not_in_the_layout_format_is_skipped_not_reported(tmp_path: Path) -> None:
    doc = tmp_path / "test_ai.md"
    doc.write_text("# `*.ai` Format\n\n## Purpose\n\nScripts.\n\n```text\n<state/>\n```\n", encoding="utf-8")

    outcome = check_doc_file(doc, {}, None)

    assert outcome.status is Status.NOT_CONVERTED
    assert not outcome.status.stops_commit


def test_check_doc_file_names_the_client_and_place_when_no_layout_fits(tmp_path: Path) -> None:
    doc = tmp_path / "test_bss.md"
    doc.write_text(_doc(COUNTED, ROW), encoding="utf-8")
    client = Client(3480, lambda name: struct.pack("<I", 1) + b"\x00" * 9)

    outcome = check_doc_file(doc, {"test_bss.md": [("test.bss", "Rows")]}, client)

    assert outcome.status is Status.NO_FIT
    assert outcome.messages[0] == "client 3480 fits no layout of test.bss"
    assert outcome.messages[1].startswith("Layout 1 breaks in test.bss: ")
    assert read_clients(doc.read_text(encoding="utf-8")) == (ClientCheck(3480, None, True),)
    assert "| 3480   | No documented layout |" in doc.read_text(encoding="utf-8")

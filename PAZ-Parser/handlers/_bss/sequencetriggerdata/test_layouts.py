"""Every documented layout reads back from a small built file, with the row size the doc gives."""

from __future__ import annotations

import struct

import pytest

from .parser import FLAG_FIELDS, LAYOUTS, TEXT_FIELDS, RowLayout, parse_sequencetriggerdata_records


# Row bytes per layout in docs/file-formats/bss/sequencetriggerdata_bss.md: the
# whole row for the one-key layouts, the fixed part before the region keys else.
_ROW_BYTES = {1: 63, 2: 67, 3: 68, 4: 69, 5: 70, 6: 75, 7: 81, 8: 83, 9: 82}
# String 0 is the empty string; each text field points at its own name.
_STRINGS = ("", *TEXT_FIELDS)
_REGION_KEY_SIZE = 2
_FILE_NAME_HASH = 0x1DB1F728
_POSITION = (6092.5, -7823.5, 93235.5)
_RESURRECT_POSITION = (1.0, 2.0, 3.0)
_RADIUS = 3140.0


def _pstr(text: str) -> bytes:
    raw = text.encode("utf-8")
    return struct.pack("<BI", 0, len(raw)) + raw


def _pabr(rows: list[bytes]) -> bytes:
    body = b"".join(rows)
    table = struct.pack("<I", len(_STRINGS)) + b"".join(_pstr(text) for text in _STRINGS)
    return b"PABR" + struct.pack("<I", len(rows)) + body + table + struct.pack("<II", 8 + len(body), 0)


def _row(layout: RowLayout, region_keys: list[int]) -> bytes:
    """One row of `layout` with every text field and flag set."""
    texts = struct.pack(f"<{len(layout.text_fields)}I", *(_STRINGS.index(field) for field in layout.text_fields))
    if layout.has_region_count:
        regions = struct.pack(f"<Q{len(region_keys)}H", len(region_keys), *region_keys)
    else:
        regions = struct.pack("<H", *region_keys)
    return b"".join((
        struct.pack("<I", _FILE_NAME_HASH),
        texts,
        struct.pack("<6f", *_POSITION, *_RESURRECT_POSITION),
        regions,
        struct.pack("<If", _FILE_NAME_HASH, _RADIUS),
        bytes([1] * len(layout.flag_fields)),
    ))


def _region_lists(layout: RowLayout) -> list[list[int]]:
    return [[1496, 1109], [1250]] if layout.has_region_count else [[1496], [1250]]


@pytest.mark.parametrize("layout", LAYOUTS, ids=lambda layout: f"Layout {layout.number}")
def test_row_size_matches_the_doc(layout: RowLayout) -> None:
    row = _row(layout, [1250])
    fixed = len(row) - _REGION_KEY_SIZE if layout.has_region_count else len(row)
    assert fixed == _ROW_BYTES[layout.number]


@pytest.mark.parametrize("layout", LAYOUTS, ids=lambda layout: f"Layout {layout.number}")
def test_each_layout_reads_back(layout: RowLayout) -> None:
    region_lists = _region_lists(layout)
    records = parse_sequencetriggerdata_records(_pabr([_row(layout, keys) for keys in region_lists]))

    assert [r["region_keys"] for r in records] == region_lists
    for record in records:
        assert record["file_name_hash"] == record["file_name_hash_dup"] == _FILE_NAME_HASH
        assert record["position"] == list(_POSITION)
        assert record["resurrect_position"] == list(_RESURRECT_POSITION)
        assert record["radius"] == _RADIUS
        assert record["region_count"] == len(record["region_keys"])
        for field in TEXT_FIELDS:
            assert record[field] == (field if field in layout.text_fields else ""), field
        for field in {*FLAG_FIELDS, *layout.flag_fields}:
            assert record[field] == (1 if field in layout.flag_fields else 0), field


def test_rows_that_fit_no_layout_fail() -> None:
    row = _row(LAYOUTS[-1], [1250])
    with pytest.raises(ValueError, match="fits no known layout"):
        parse_sequencetriggerdata_records(_pabr([row + b"\x00\x00"]))

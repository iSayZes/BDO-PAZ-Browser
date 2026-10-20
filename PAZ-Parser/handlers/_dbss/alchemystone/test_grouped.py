"""The alchemy stone rows on the grouped walk, and the helpers the alchemy stone table tests share."""
from __future__ import annotations

import struct

from tests.framework import CaseInput, DeclaredCount

from .grouped import parse_stone_offset_records, parse_stone_rows


ROW_SIZE = 12
_WORDS_PER_ROW = 3


def declared_grouped_rows() -> DeclaredCount:
    """Rows in a grouped file: its u32 words minus the group count and one
    row count per group, three words per row."""

    def read(source: CaseInput) -> int:
        raw = source.data
        group_count = int.from_bytes(raw[:4], "little")
        row_words = len(raw) // 4 - 1 - group_count
        if len(raw) % 4 or row_words < 0 or row_words % _WORDS_PER_ROW:
            raise AssertionError(f"{len(raw)} bytes do not hold {group_count} groups of 12-byte rows")
        return row_words // _WORDS_PER_ROW

    return read


def grouped_file(*groups: list[tuple[int, int, int]]) -> bytes:
    """A grouped file of the given groups of rows."""
    body = b"".join(
        struct.pack("<I", len(rows)) + b"".join(struct.pack("<III", *row) for row in rows) for rows in groups
    )
    return struct.pack("<I", len(groups)) + body


def check_rows_sit_in_their_stone_group(data: bytes, file_name: str) -> None:
    """Every main row's `stone_type` equals the index of the group holding it."""
    rows = parse_stone_rows(data, file_name)
    assert all(group == stone_type for group, (stone_type, _item, _value) in rows)


def check_offset_rows_point_at_main_rows(main: bytes, offset_records: list[dict]) -> None:
    """Every index row points at the main row with its stone type and item."""
    for row in offset_records:
        assert row["size"] == ROW_SIZE
        assert struct.unpack_from("<II", main, row["offset"]) == (row["stone_type"], row["item_id"])


def test_rows_carry_their_group_index() -> None:
    data = grouped_file([(0, 6601, 10)], [], [(2, 5301, 1)])
    assert parse_stone_rows(data, "test") == [(0, (0, 6601, 10)), (2, (2, 5301, 1))]


def test_an_offset_row_takes_its_group_as_stone_type() -> None:
    data = grouped_file([], [(6601, 8, 12)])
    assert parse_stone_offset_records(data, "test") == [
        {"stone_type": 1, "item_id": 6601, "offset": 8, "size": 12},
    ]


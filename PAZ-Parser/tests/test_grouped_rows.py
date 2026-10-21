"""The grouped walk of `_common/grouped_rows.py`."""
from __future__ import annotations

import struct

import pytest

from _common.grouped_rows import parse_grouped_rows

# A row that is not three u32 values, as in buildingbuff.dbss.
_ROW = struct.Struct("<HHq")


def _grouped_file(*groups: list[tuple[int, int, int]]) -> bytes:
    body = b"".join(struct.pack("<I", len(rows)) + b"".join(_ROW.pack(*row) for row in rows) for rows in groups)
    return struct.pack("<I", len(groups)) + body


def test_rows_carry_their_group_index() -> None:
    data = _grouped_file([(0, 52597, 10)], [], [(1, 52598, -1)])
    assert parse_grouped_rows(data, "test", _ROW) == [(0, (0, 52597, 10)), (2, (1, 52598, -1))]


def test_an_empty_file_of_empty_groups_has_no_rows() -> None:
    assert parse_grouped_rows(_grouped_file([], [], []), "test", _ROW) == []


def test_a_cut_group_raises() -> None:
    with pytest.raises(ValueError):
        parse_grouped_rows(_grouped_file([(0, 52597, 10)])[:-4], "test", _ROW)


def test_a_missing_row_count_raises() -> None:
    with pytest.raises(ValueError):
        parse_grouped_rows(struct.pack("<I", 2) + struct.pack("<I", 0), "test", _ROW)


def test_bytes_after_the_last_group_raise() -> None:
    with pytest.raises(ValueError):
        parse_grouped_rows(_grouped_file([(0, 52597, 10)]) + b"\0\0\0\0", "test", _ROW)

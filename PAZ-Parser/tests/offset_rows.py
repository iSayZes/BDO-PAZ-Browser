"""Checks that an `*offset.dbss` index points at every row of its table.

Fixed-row tables and their index are read independently: the parser walks
the rows from the count, the index lists key, offset and size per row.
`offset_row_problems()` checks that the two agree, so a test asserts both
readings at once without repeating the parser's walk.
"""
from __future__ import annotations

import struct
from collections.abc import Sequence

from _common.pabr_offset import PabrOffsetRow


def offset_row_problems(
    data: bytes,
    rows: Sequence[PabrOffsetRow],
    key: struct.Struct,
    *,
    rows_start: int = 4,
    lead: int = 0,
) -> list[str]:
    """What breaks the index: a row whose key differs from its index key, or rows that do not tile the file.

    The table's rows start at `rows_start`. Each index row points `lead`
    bytes into its row, past a key prefix that its size leaves out; `key` is
    read from the row start (`offset - lead`).
    """
    problems = []
    expected_offset = rows_start + lead
    for row in sorted(rows, key=lambda row: row.offset):
        (row_key,) = key.unpack_from(data, row.offset - lead)
        if row_key != row.entry_id:
            problems.append(f"key {row.entry_id} points at a row with key {row_key} (0x{row.offset:X})")
        if row.offset != expected_offset:
            problems.append(f"key {row.entry_id} starts at 0x{row.offset:X}, expected 0x{expected_offset:X}")
        expected_offset = row.offset + row.size + lead
    if expected_offset - lead != len(data):
        problems.append(f"the rows end at 0x{expected_offset - lead:X}, the file at 0x{len(data):X}")
    return problems

"""Tables that are a u32 row count followed by rows of one fixed size.

Most `.dbss` tables with an `*offset.dbss` index have this shape; the index
only says where each row sits, so the rows can be read from the count.
"""

from __future__ import annotations

import struct
from collections.abc import Sequence

from _common.binary import u32

COUNT_SIZE = 4


def counted_row_values(data: bytes, row: struct.Struct, file_name: str) -> list[tuple]:
    """The values `row` unpacks from every row, in file order.

    Raises ValueError when the rows do not end at the last byte of the file.
    """
    if len(data) < COUNT_SIZE:
        raise ValueError(f"{file_name} is too short to hold its row count")

    count = u32(data, 0)
    expected = COUNT_SIZE + count * row.size
    if len(data) != expected:
        raise ValueError(f"{file_name} is {len(data):,} bytes, {count:,} rows of {row.size} need {expected:,}")
    return list(row.iter_unpack(data[COUNT_SIZE:]))


def parse_counted_rows(data: bytes, row: struct.Struct, fields: Sequence[str], file_name: str) -> list[dict]:
    """Every row in file order, as `fields` -> the values `row` unpacks.

    Raises ValueError like `counted_row_values()`.
    """
    return [dict(zip(fields, values, strict=True)) for values in counted_row_values(data, row, file_name)]

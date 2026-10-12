"""The grouped walk of the alchemy stone material tables.

`alchemycharge.dbss`, `alchemyupgrade.dbss` and their `*offset.dbss` indexes
share one layout: a u32 group count, then per group a u32 row count and that
many rows of three u32 values. The group index is the alchemy stone type.
An index row is `(item_id, offset, size)`. Layout in
docs/file-formats/alchemycharge_dbss.md.
"""

from __future__ import annotations

import struct

_U32 = struct.Struct("<I")
_ROW = struct.Struct("<III")

GroupedRow = tuple[int, tuple[int, int, int]]


def parse_grouped_rows(data: bytes, file_name: str) -> list[GroupedRow]:
    """`(group index, row)` for every row, in file order.

    Raises ValueError when a group runs past the end of the file or bytes are
    left after the last group.
    """
    group_count = _read_u32(data, 0, file_name)
    cursor = _U32.size
    rows: list[GroupedRow] = []
    for group in range(group_count):
        row_count = _read_u32(data, cursor, file_name)
        cursor += _U32.size
        end = cursor + row_count * _ROW.size
        if end > len(data):
            raise ValueError(f"{file_name}: group {group} runs past the end of the file")
        rows.extend((group, _ROW.unpack_from(data, start)) for start in range(cursor, end, _ROW.size))
        cursor = end
    if cursor != len(data):
        raise ValueError(f"{file_name}: {len(data) - cursor} bytes left after group {group_count - 1}")
    return rows


def parse_stone_offset_records(data: bytes, file_name: str) -> list[dict]:
    """Every row of an `*offset.dbss` index, in file order; `stone_type` is the group index."""
    return [
        {"stone_type": group, "item_id": item_id, "offset": offset, "size": size}
        for group, (item_id, offset, size) in parse_grouped_rows(data, file_name)
    ]


def _read_u32(data: bytes, offset: int, file_name: str) -> int:
    if offset + _U32.size > len(data):
        raise ValueError(f"{file_name}: count at 0x{offset:X} runs past the end of the file")
    return _U32.unpack_from(data, offset)[0]

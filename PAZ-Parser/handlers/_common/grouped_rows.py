"""The grouped walk: a u32 group count, then per group a u32 row count and that many fixed-size rows.

Used by `alchemycharge.dbss`, `alchemyupgrade.dbss` (rows of three u32,
`_dbss/alchemystone/grouped.py`), `buildingbuff.dbss` and their `*offset.dbss`
indexes. Layouts in docs/file-formats/alchemycharge_dbss.md and
docs/file-formats/buildingbuff_dbss.md.
"""

from __future__ import annotations

import struct

_U32 = struct.Struct("<I")

GroupedRow = tuple[int, tuple[int, ...]]


def parse_grouped_rows(data: bytes, file_name: str, row: struct.Struct) -> list[GroupedRow]:
    """`(group index, row)` for every row, in file order; `row` unpacks one row.

    Raises ValueError when a count or a group runs past the end of the file, or
    bytes are left after the last group.
    """
    group_count = _read_u32(data, 0, file_name)
    cursor = _U32.size
    rows: list[GroupedRow] = []
    for group in range(group_count):
        row_count = _read_u32(data, cursor, file_name)
        cursor += _U32.size
        end = cursor + row_count * row.size
        if end > len(data):
            raise ValueError(f"{file_name}: group {group} runs past the end of the file")
        rows.extend((group, row.unpack_from(data, start)) for start in range(cursor, end, row.size))
        cursor = end
    if cursor != len(data):
        raise ValueError(f"{file_name}: {len(data) - cursor} bytes left after group {group_count - 1}")
    return rows


def _read_u32(data: bytes, offset: int, file_name: str) -> int:
    if offset + _U32.size > len(data):
        raise ValueError(f"{file_name}: count at 0x{offset:X} runs past the end of the file")
    return _U32.unpack_from(data, offset)[0]

"""The alchemy stone material tables on the grouped walk of `_common/grouped_rows.py`.

`alchemycharge.dbss`, `alchemyupgrade.dbss` and their `*offset.dbss` indexes
hold rows of three u32 values; the group index is the alchemy stone type.
An index row is `(item_id, offset, size)`. Layout in
docs/file-formats/alchemycharge_dbss.md.
"""

from __future__ import annotations

import struct

from _common.grouped_rows import GroupedRow, parse_grouped_rows

STONE_ROW = struct.Struct("<III")


def parse_stone_rows(data: bytes, file_name: str) -> list[GroupedRow]:
    """`(stone type, row)` for every row, in file order."""
    return parse_grouped_rows(data, file_name, STONE_ROW)


def parse_stone_offset_records(data: bytes, file_name: str) -> list[dict]:
    """Every row of an `*offset.dbss` index, in file order; `stone_type` is the group index."""
    return [
        {"stone_type": group, "item_id": item_id, "offset": offset, "size": size}
        for group, (item_id, offset, size) in parse_stone_rows(data, file_name)
    ]

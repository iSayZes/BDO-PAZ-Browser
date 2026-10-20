"""`employeeloyalismitem.dbss`: the items that restore a sailor's condition.

The main file is a u32 count and one 9-byte row per item:

    u8 loyalism_type | u32 item_id | u32 recovery_value

`employeeloyalismitemoffset.dbss` is a bare offset table of 12-byte
[u32 item_id][u32 offset][u32 size] rows; the offset points at
`loyalism_type`. Full layout in docs/file-formats/employeeloyalismitem_dbss.md.
"""

from __future__ import annotations

import struct
from enum import IntEnum

from _common.pabr_offset import parse_bare_u32_offset_rows


_ROW = struct.Struct("<BII")


class LoyalismType(IntEnum):
    """`__eEmployeeLoyalismType`: what a recovery item does."""

    LOYALTY = 0
    """Adds `recovery_value` condition points."""
    RESURRECTION = 1
    """Cures a sick sailor; `recovery_value` is the condition rate it sets."""


def parse_employeeloyalismitemoffset_records(data: bytes) -> list[dict]:
    return [
        {"item_id": row.entry_id, "data_offset": row.offset, "data_size": row.size}
        for row in parse_bare_u32_offset_rows(data)
    ]


def _recovery_item_record(data: bytes, offset_row: dict) -> dict:
    data_offset = offset_row["data_offset"]
    data_size = offset_row["data_size"]
    label = f"recovery item {offset_row['item_id']}"
    if data_size != _ROW.size:
        raise ValueError(f"{label}: row size {data_size}, expected {_ROW.size}")
    if data_offset + data_size > len(data):
        raise ValueError(f"{label}: row exceeds file size")

    loyalism_type, item_id, recovery_value = _ROW.unpack_from(data, data_offset)
    if item_id != offset_row["item_id"]:
        raise ValueError(f"{label}: row holds item {item_id}")

    return {
        "loyalism_type": loyalism_type,
        "item_id": item_id,
        "recovery_value": recovery_value,
    }


def parse_employeeloyalismitem_records(data: bytes, offset_data: bytes) -> list[dict]:
    """Every recovery item the offset companion points at, in its order.

    Raises ValueError when a row lies outside the file, has another size or
    holds an item other than the offset row's.
    """
    return [_recovery_item_record(data, row) for row in parse_employeeloyalismitemoffset_records(offset_data)]

"""`plantupgraderesource.bss`: upgrade costs of the worker system.

    PABR | u32 count | count x 58-byte entry | u32 0 (empty string table)
    | u32 string_table_start | u32 0

Each entry is keyed by (level group, level) and holds the time, contribution
points, silver and up to three items the upgrade takes. Full layout in
docs/file-formats/bss/plantupgraderesource_bss.md.
"""

from __future__ import annotations

import struct

from _common.pabr_strings import fixed_row_offsets


FILE_NAME = "plantupgraderesource.bss"
ROW_SIZE = 58

_HEAD = struct.Struct("<HhHhi")
_NEED_ITEM = struct.Struct("<Iq")
_NEED_ITEMS_AT = 0x0C
_NEED_ITEM_SLOTS = 3
_TAIL = struct.Struct("<hq")
_TAIL_AT = 0x30


def _need_items(data: bytes, pos: int) -> list[dict]:
    """The filled item slots; an item key of 0 marks an empty slot."""
    items: list[dict] = []
    for slot in range(_NEED_ITEM_SLOTS):
        item_key, count = _NEED_ITEM.unpack_from(data, pos + _NEED_ITEMS_AT + slot * _NEED_ITEM.size)
        if item_key:
            items.append({"item_key": item_key, "count": count})
    return items


def _parse_row(data: bytes, pos: int) -> dict:
    group, level, key_group, key_level, need_time = _HEAD.unpack_from(data, pos)
    need_point, need_money = _TAIL.unpack_from(data, pos + _TAIL_AT)
    return {
        "group": group,
        "level": level,
        "key_group": key_group,
        "key_level": key_level,
        "need_time": need_time,
        "need_items": _need_items(data, pos),
        "need_point": need_point,
        "need_money": need_money,
    }


def parse_plantupgraderesource_records(data: bytes) -> list[dict]:
    """Every entry in file order. Raises ValueError on a bad magic or row count."""
    return [_parse_row(data, pos) for pos in fixed_row_offsets(data, ROW_SIZE, FILE_NAME)]

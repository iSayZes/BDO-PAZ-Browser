"""`bartersubgroup.bss`: the barter sub groups, a trade item list and a material list.

    PABR | u32 group_count | group_count x group
    | u32 material_group_count | material_group_count x group
    | u32 0 (empty string table) | u32 string_table_start | u32 0
    group: u32 entry_count | entry_count x 72-byte entry
    entry: u32 barter_sub_group | u32 select_rate | u32 barter_cost
           | 56-byte Exchange | u32 barter_category (bit mask)

Full layout in docs/file-formats/bss/bartersubgroup_bss.md; the Exchange is read
by `_bss/barter/exchange.py`, the two lists by `_bss/barter/group_lists.py`.
"""

from __future__ import annotations

import struct

from _bss.barter.exchange import read_exchange
from _bss.barter.group_lists import group_spans
from _common.binary import u32

FILE_NAME = "bartersubgroup.bss"
ENTRY_SIZE = 72

# A group's head is its entry count alone.
_GROUP_HEAD = struct.Struct("<I")
_HEAD = struct.Struct("<III")
_EXCHANGE = 0x0C
_CATEGORY = 0x44


def _read_entry(data: bytes, pos: int, is_material: bool) -> dict:
    barter_sub_group, select_rate, barter_cost = _HEAD.unpack_from(data, pos)
    return {
        "barter_sub_group": barter_sub_group,
        "is_material": is_material,
        "select_rate": select_rate,
        "barter_cost": barter_cost,
        **read_exchange(data, pos + _EXCHANGE),
        "barter_category": u32(data, pos + _CATEGORY),
    }


def parse_bartersubgroup_records(data: bytes) -> list[dict]:
    """Every entry of the trade item list, then of the material list, in file order.

    Raises ValueError on a missing magic, a group that runs past the string
    table, or a material list that does not end where the string table starts.
    """
    return [
        _read_entry(data, pos, span.is_material)
        for span in group_spans(data, FILE_NAME, _GROUP_HEAD, ENTRY_SIZE)
        for pos in span.entries
    ]

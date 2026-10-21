"""`barter_normal.bss`: the barter slots of each barter region, a trade item list and a material list.

    PABR | u32 region_count | region_count x region
    | u32 material_region_count | material_region_count x region
    | u32 0 (empty string table) | u32 string_table_start | u32 0
    region: u16 region_key | u32 entry_count | entry_count x 70-byte entry
    entry: u16 barter_region_key | u32 select_rate | 56-byte Exchange
           | u32 barter_sub_group | u32 barter_category (bit mask)

An entry with a `barter_sub_group` names a `bartersubgroup.bss` group of the
same list and leaves its own Exchange zero. Full layout in
docs/file-formats/barter_normal_bss.md; the Exchange is read by
`_bss/barter/exchange.py`, the two lists by `_bss/barter/group_lists.py`.
"""

from __future__ import annotations

import struct

from _bss.barter.exchange import read_exchange
from _bss.barter.group_lists import GroupSpan, group_spans

FILE_NAME = "barter_normal.bss"
ENTRY_SIZE = 70

# A region's head: its key, then its entry count.
_REGION_HEAD = struct.Struct("<HI")
_HEAD = struct.Struct("<HI")
_EXCHANGE = 0x06
_TAIL = struct.Struct("<II")
_TAIL_OFFSET = 0x3E


def _read_entry(data: bytes, pos: int, span: GroupSpan, slot: int) -> dict:
    barter_region_key, select_rate = _HEAD.unpack_from(data, pos)
    barter_sub_group, barter_category = _TAIL.unpack_from(data, pos + _TAIL_OFFSET)
    (region_key,) = span.head
    return {
        "region_key": region_key,
        "is_material": span.is_material,
        "slot": slot,
        "barter_region_key": barter_region_key,
        "select_rate": select_rate,
        **read_exchange(data, pos + _EXCHANGE),
        "barter_sub_group": barter_sub_group,
        "barter_category": barter_category,
    }


def parse_barter_normal_records(data: bytes) -> list[dict]:
    """Every entry of the trade item list, then of the material list, in file order.

    `slot` is the entry's place in its region, from 1. Raises ValueError on a
    missing magic, a region that runs past the string table, or a material
    list that does not end where the string table starts.
    """
    return [
        _read_entry(data, pos, span, slot)
        for span in group_spans(data, FILE_NAME, _REGION_HEAD, ENTRY_SIZE)
        for slot, pos in enumerate(span.entries, start=1)
    ]

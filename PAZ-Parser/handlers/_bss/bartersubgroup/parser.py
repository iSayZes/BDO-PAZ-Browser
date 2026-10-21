"""`bartersubgroup.bss`: the barter sub groups, a trade item list and a material list.

    PABR | u32 group_count | group_count x group
    | u32 material_group_count | material_group_count x group
    | u32 0 (empty string table) | u32 string_table_start | u32 0
    group: u32 entry_count | entry_count x 72-byte entry
    entry: u32 barter_sub_group | u32 select_rate | u32 barter_cost
           | 56-byte Exchange | u32 barter_category (bit mask)

Full layout in docs/file-formats/bartersubgroup_bss.md; the Exchange is read
by `_bss/barter/exchange.py`.
"""

from __future__ import annotations

import struct

from _bss.barter.exchange import read_exchange
from _common.binary import u32
from _common.pabr_strings import U32_SIZE, check_pabr, check_rows_end, string_table_start

FILE_NAME = "bartersubgroup.bss"
ENTRY_SIZE = 72
# The first list's group count, after the PABR magic.
GROUP_COUNT_OFFSET = 4

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


def _read_list(data: bytes, pos: int, end: int, is_material: bool) -> tuple[list[dict], int]:
    """The entries of one list of groups starting at `pos`, and where the list ends."""
    group_count = _read_count(data, pos, end)
    pos += U32_SIZE
    entries: list[dict] = []
    for _ in range(group_count):
        entry_count = _read_count(data, pos, end)
        pos += U32_SIZE
        group_end = pos + entry_count * ENTRY_SIZE
        if group_end > end:
            raise ValueError(f"{FILE_NAME}: a group at 0x{pos - U32_SIZE:X} runs past the string table")
        entries.extend(_read_entry(data, start, is_material) for start in range(pos, group_end, ENTRY_SIZE))
        pos = group_end
    return entries, pos


def _read_count(data: bytes, pos: int, end: int) -> int:
    if pos + U32_SIZE > end:
        raise ValueError(f"{FILE_NAME}: the count at 0x{pos:X} runs past the string table")
    return u32(data, pos)


def parse_bartersubgroup_records(data: bytes) -> list[dict]:
    """Every entry of the trade item list, then of the material list, in file order.

    Raises ValueError on a missing magic, a group that runs past the string
    table, or a material list that does not end where the string table starts.
    """
    check_pabr(data, FILE_NAME)
    end = string_table_start(data)
    trade, pos = _read_list(data, GROUP_COUNT_OFFSET, end, is_material=False)
    material, pos = _read_list(data, pos, end, is_material=True)
    check_rows_end(data, pos, f"{FILE_NAME} groups")
    return trade + material

"""`buffsimply.bss`: a compact copy of `buff.dbss`, one fixed row per buff.

    PABR | u32 count | count x row | string table | u32 string_table_start | u32 0

Each row holds the buff ID, string-table indices for the icon path and
`effect_name`, `is_shown` and a few bytes copied from the `buff.dbss` stats and
tail blocks, among them `is_debuff`, `remove_on_dead` and the equipment type and
slot the buff needs. Rows are 32 bytes with a u32 `buff_id` in Layout 2 (client
3464 on) and 30 bytes with a u16 one in Layout 1 (clients 1311 to 3458); a file
is read with the first layout, in client order, whose rows end where the string
table starts. Full layout in docs/file-formats/bss/buffsimply_bss.md.
"""

from __future__ import annotations

import struct
from dataclasses import dataclass

from _common.buff import buff_icon_path
from _common.client_versions import ClientRange, client_order
from _common.pabr_strings import fixed_row_offsets, read_string_table, string_at

FILE_NAME = "buffsimply.bss"


# After buff_id: u8 need_equip_type | 2x | u8 unknown_07 | u8 unknown_08
# | u8 unknown_09 | x | u8 need_equip_slot | u8 unknown_0c | u32 effect_name_ref
# | u8 is_debuff | u32 unknown_12_ref | u8 remove_on_dead | u8 is_shown
# | u32 unknown_18 | u32 icon_ref
# The bytes from need_equip_type to unknown_0c copy the buff.dbss
# `_needEquipType`, an itemenchant.dbss equip type; 46 is the `equip_slot` of
# no slot. unknown_12_ref is a string-table index like icon_ref (the client
# 1784 reader reads both with its 8-bit string reader).
_AFTER_BUFF_ID = "B2xBBBxBBIBIBBII"


@dataclass(frozen=True)
class RowLayout:
    """One documented Buff Row shape; `number` is its Layout N in the doc."""

    number: int
    row: struct.Struct
    # Test clients this layout reads (the doc's Versions table, written by
    # check_docs); they only order the tries (`client_versions.py`).
    clients: tuple[ClientRange, ...] = ()


# Newest first. Client 3464 widened buff_id from u16 to u32.
LAYOUTS = (
    RowLayout(2, struct.Struct("<I" + _AFTER_BUFF_ID), (ClientRange(3464),)),
    RowLayout(1, struct.Struct("<H" + _AFTER_BUFF_ID), (ClientRange(1311, 3458),)),
)
assert [layout.row.size for layout in LAYOUTS] == [32, 30]


def _layout_offsets(data: bytes) -> tuple[RowLayout, range]:
    """The first layout, in client order, whose rows end where the string table starts."""
    breaks: list[str] = []
    for layout in client_order(LAYOUTS, lambda layout: layout.clients):
        try:
            return layout, fixed_row_offsets(data, layout.row.size, FILE_NAME)
        except ValueError as error:
            breaks.append(f"Layout {layout.number}: {error}")
    raise ValueError(f"{FILE_NAME} fits no known layout ({'; '.join(breaks)})")


def parse_buffsimply_records(data: bytes) -> list[dict]:
    """Every buff row in file order, with its strings resolved.

    Raises ValueError on a bad magic, or when no layout's rows end where the
    string table starts: then the row size has changed and every field is suspect.
    """
    layout, offsets = _layout_offsets(data)
    strings = read_string_table(data)
    records: list[dict] = []
    for offset in offsets:
        (
            buff_id, need_equip_type, unknown_07, unknown_08, unknown_09,
            need_equip_slot, unknown_0c, effect_name_ref, is_debuff, unknown_12_ref,
            remove_on_dead, is_shown, unknown_18, icon_ref,
        ) = layout.row.unpack_from(data, offset)
        records.append({
            "buff_id": buff_id,
            "icon_path": buff_icon_path(string_at(strings, icon_ref)),
            "is_shown": bool(is_shown),
            "is_debuff": bool(is_debuff),
            "remove_on_dead": bool(remove_on_dead),
            "effect_name": string_at(strings, effect_name_ref),
            "need_equip_type": need_equip_type,
            "need_equip_slot": need_equip_slot,
            "unknown_07": unknown_07,
            "unknown_08": unknown_08,
            "unknown_09": unknown_09,
            "unknown_0c": unknown_0c,
            "unknown_12": string_at(strings, unknown_12_ref),
            "unknown_18": unknown_18,
        })
    return records


def build_buff_icon_index(data: bytes) -> dict[int, str]:
    """Icon path by buff ID, for `IndexKind.BUFF_ICON`.

    Buffs without an icon, or with the `UNKNOWN` placeholder, are left out.
    """
    return {
        record["buff_id"]: record["icon_path"]
        for record in parse_buffsimply_records(data)
        if record["icon_path"]
    }

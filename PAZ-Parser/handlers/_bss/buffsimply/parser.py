"""`buffsimply.bss`: a compact copy of `buff.dbss`, one fixed row per buff.

    PABR | u32 count | count x 32-byte row | string table | u32 string_table_start | u32 0

Each row holds the buff ID, string-table indices for the icon path and
`unknown_str`, `is_shown` and a few bytes copied from the `buff.dbss` stats and
tail blocks. Full layout in docs/file-formats/buffsimply_bss.md.
"""

from __future__ import annotations

import struct

from _common.binary import u32
from _common.buff import buff_icon_path
from _common.pabr_strings import fixed_row_offsets, read_string_table, string_at, string_table_start


# u32 buff_id | u8 unknown_04 | 2x | u8 unknown_07 | u8 unknown_08
# | u8 unknown_09 | x | u8 unknown_0b | u8 unknown_0c | u32 unknown_str_ref
# | u8 unknown_11 | u8 unknown_12 | 3x | u8 unknown_16 | u8 is_shown
# | u32 unknown_18 | u32 icon_ref
_ROW = struct.Struct("<IB2xBBBxBBIBB3xBBII")
_ROW_SIZE = 32
assert _ROW.size == _ROW_SIZE


def _row_offsets(data: bytes) -> range:
    """Start of every row. Raises ValueError when the rows do not fill the file."""
    return fixed_row_offsets(data, _ROW_SIZE, "buffsimply.bss")


def parse_buffsimply_records(data: bytes) -> list[dict]:
    """Every buff row in file order, with its strings resolved.

    Raises ValueError on a bad magic, or when the rows do not end where the
    string table starts: then the row size has changed and every field is suspect.
    """
    offsets = _row_offsets(data)
    strings = read_string_table(data)
    records: list[dict] = []
    for offset in offsets:
        (
            buff_id, unknown_04, unknown_07, unknown_08, unknown_09,
            unknown_0b, unknown_0c, unknown_str_ref, unknown_11, unknown_12,
            unknown_16, is_shown, unknown_18, icon_ref,
        ) = _ROW.unpack_from(data, offset)
        records.append({
            "buff_id": buff_id,
            "icon_path": buff_icon_path(string_at(strings, icon_ref)),
            "is_shown": bool(is_shown),
            "unknown_str": string_at(strings, unknown_str_ref),
            "unknown_04": unknown_04,
            "unknown_07": unknown_07,
            "unknown_08": unknown_08,
            "unknown_09": unknown_09,
            "unknown_0b": unknown_0b,
            "unknown_0c": unknown_0c,
            "unknown_11": unknown_11,
            "unknown_12": unknown_12,
            "unknown_16": unknown_16,
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

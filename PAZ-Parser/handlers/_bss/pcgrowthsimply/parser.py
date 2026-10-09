"""`pcgrowthsimply.bss`: one fixed row per class type with its playable flag.

    PABR | u32 count | count x (u8 class_type | u32 name_index | u8 is_playable
    | u32 unknown_06) | string table | u32 string_table_start | u32 0

`name_index` points into the string table, which holds the Korean class names
(`pcgrowth.dbss` `name_kr`). Full layout in docs/file-formats/pcgrowthsimply_bss.md.
"""

from __future__ import annotations

import struct

from _common.pabr_strings import fixed_row_offsets, read_string_table, string_at


_DATA_FILE = "pcgrowthsimply.bss"
_ROW = struct.Struct("<BIBI")


def parse_pcgrowthsimply_records(data: bytes) -> list[dict]:
    """Every row in file order.

    Raises ValueError on a bad magic, or when the rows do not end where the
    string table starts.
    """
    strings = read_string_table(data)
    records: list[dict] = []
    for start in fixed_row_offsets(data, _ROW.size, _DATA_FILE):
        class_type, name_index, is_playable, unknown_06 = _ROW.unpack_from(data, start)
        records.append({
            "class_type": class_type,
            "name_index": name_index,
            "name_kr": string_at(strings, name_index),
            "is_playable": bool(is_playable),
            "unknown_06": unknown_06,
        })
    return records

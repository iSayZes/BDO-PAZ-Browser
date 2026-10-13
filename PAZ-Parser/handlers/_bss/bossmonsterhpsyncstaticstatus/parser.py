"""`bossmonsterhpsyncstaticstatus.bss`: boss characters with a world sector box.

    PABR | u32 count | count x 26-byte row | empty string table | u32 table_start | u32 0
    row: u16 key | u16 character_id | i32 min_x | i32 min_z | i32 max_x | i32 max_z
         | u16 | u32

One sector is 12,800 world units. Full layout in
docs/file-formats/bossmonsterhpsyncstaticstatus_bss.md.
"""

from __future__ import annotations

import struct

from _common.pabr_strings import fixed_row_offsets


FILE_NAME = "bossmonsterhpsyncstaticstatus.bss"

_ROW = struct.Struct("<HH4iHI")


def parse_bossmonsterhpsync_records(data: bytes) -> list[dict]:
    """Every row in file order.

    Raises ValueError on a bad magic, or when the rows do not end where the
    string table starts.
    """
    records: list[dict] = []
    for offset in fixed_row_offsets(data, _ROW.size, FILE_NAME):
        key, character_id, min_x, min_z, max_x, max_z, unknown_14, unknown_16 = _ROW.unpack_from(data, offset)
        records.append({
            "key": key,
            "character_id": character_id,
            "min_x": min_x,
            "min_z": min_z,
            "max_x": max_x,
            "max_z": max_z,
            "unknown_14": unknown_14,
            "unknown_16": unknown_16,
        })
    return records

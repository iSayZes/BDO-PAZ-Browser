"""`masterlessservantstaticstatus.bss`: the Traveler's Horse rows.

    PABR | u32 record_count | record_count x 14-byte Row | empty String Table
    | u32 string_table_start | u32 0
    Row: u32 unknown_00 | u32 unknown_04 | u32 unknown_08 | u16 character_id

What the three numbers set is open. Layout 1 in
docs/file-formats/masterlessservantstaticstatus_bss.md.
"""

from __future__ import annotations

import struct

from _common.pabr_strings import fixed_row_offsets


FILE_NAME = "masterlessservantstaticstatus.bss"

_ROW = struct.Struct("<IIIH")


def parse_masterlessservantstaticstatus_records(data: bytes) -> list[dict]:
    """Every row in file order.

    Raises ValueError on a missing magic or rows that do not end where the
    string table starts.
    """
    records = []
    for pos in fixed_row_offsets(data, _ROW.size, FILE_NAME):
        unknown_00, unknown_04, unknown_08, character_id = _ROW.unpack_from(data, pos)
        records.append(
            {
                "character_id": character_id,
                "unknown_00": unknown_00,
                "unknown_04": unknown_04,
                "unknown_08": unknown_08,
            }
        )
    return records

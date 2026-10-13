"""`guaranteeenchantss.dbss`: the Ancient Anvil, Agris Essences per enhancement type and level.

    u32 row_count | row_count x 7-byte row
    row = u32 enhancement_type | u8 enchant_level | u16 agris_count

No magic and no trailer. Full layout in docs/file-formats/guaranteeenchantss_dbss.md.
"""

from __future__ import annotations

import struct


FILE_NAME = "guaranteeenchantss.dbss"
COUNT = struct.Struct("<I")
ROW = struct.Struct("<IBH")


def parse_guaranteeenchantss_records(data: bytes) -> list[dict]:
    """One record per (enhancement type, level), sorted by type and then level.

    The file stores the rows in no order. Raises ValueError when the declared
    rows do not fill the file exactly: then the row size has changed and
    every field is suspect.
    """
    if len(data) < COUNT.size:
        raise ValueError(f"{FILE_NAME}: {len(data)} bytes is too short for the row count")
    (row_count,) = COUNT.unpack_from(data, 0)
    expected_size = COUNT.size + row_count * ROW.size
    if expected_size != len(data):
        raise ValueError(
            f"{FILE_NAME}: {row_count} rows of {ROW.size} bytes need {expected_size} bytes, "
            f"but the file holds {len(data)}"
        )
    records = [
        {"enhancement_type": enhancement_type, "enchant_level": enchant_level, "agris_count": agris_count}
        for enhancement_type, enchant_level, agris_count in ROW.iter_unpack(data[COUNT.size:])
    ]
    return sorted(records, key=lambda record: (record["enhancement_type"], record["enchant_level"]))

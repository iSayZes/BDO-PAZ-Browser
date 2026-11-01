"""`boss_spawn.bss`: the guild bosses of the Guild Boss Summon window.

    PABR | u32 count | count x 43-byte row | empty string table | u32 table_start | u32 0
    row: u32 key | u32 max_level | u32 | f32[3] position | u32 range | u32
         | u8 | u8 | 4 zero | u8 | zero | u8 | u8 | zero

The key is the `BossSpawnKey` that `boss_spawnlevel.bss` groups by. Full
layout in docs/file-formats/bss/boss_spawn_bss.md.
"""

from __future__ import annotations

import struct

from _common.pabr_strings import fixed_row_offsets


FILE_NAME = "boss_spawn.bss"

_ROW = struct.Struct("<III3fIIBB4xBxBBx")


def parse_boss_spawn_records(data: bytes) -> list[dict]:
    """Every row in file order.

    Raises ValueError on a bad magic, or when the rows do not end where the
    string table starts.
    """
    records: list[dict] = []
    for offset in fixed_row_offsets(data, _ROW.size, FILE_NAME):
        (
            key, max_level, unknown_08, x, y, z, spawn_range, unknown_1c,
            unknown_20, unknown_21, unknown_26, unknown_28, unknown_29,
        ) = _ROW.unpack_from(data, offset)
        records.append({
            "key": key,
            "max_level": max_level,
            "x": x,
            "y": y,
            "z": z,
            "range": spawn_range,
            "unknown_08": unknown_08,
            "unknown_1c": unknown_1c,
            "unknown_20": unknown_20,
            "unknown_21": unknown_21,
            "unknown_26": unknown_26,
            "unknown_28": unknown_28,
            "unknown_29": unknown_29,
        })
    return records

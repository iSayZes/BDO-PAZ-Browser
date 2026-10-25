"""`employeeclientspawn.dbss`: where the sailors stand on each ship.

    u32 count | count x (u16 character_key | u16 index
                         | f32 spawn_position_x, spawn_position_y, spawn_position_z
                         | f32 spawn_direction)

`employeeclientspawnoffset.dbss` (u32 count, then u16 character key, u16
index, u32 offset and u32 size per row) points at the row start. Layout 1
in docs/file-formats/dbss/employeeclientspawn_dbss.md.
"""

from __future__ import annotations

import struct

from _common.counted_rows import parse_counted_rows
from _common.pabr_offset import parse_bare_u32_offset_rows


FILE_NAME = "employeeclientspawn.dbss"
OFFSET_FILE = "employeeclientspawnoffset.dbss"

_ROW = struct.Struct("<HHffff")
_FIELDS = (
    "character_key",
    "index",
    "spawn_position_x",
    "spawn_position_y",
    "spawn_position_z",
    "spawn_direction",
)
# The index key is the row's first u32: character_key in the low half, index in the high.
_INDEX_SHIFT = 16
_CHARACTER_MASK = 0xFFFF


def parse_employeeclientspawn_records(data: bytes) -> list[dict]:
    """Every row in file order. Raises ValueError when the rows do not fill the file."""
    return parse_counted_rows(data, _ROW, _FIELDS, FILE_NAME)


def parse_employeeclientspawnoffset_records(data: bytes) -> list[dict]:
    """Every index row, its u32 key split into `character_key` and `index`.

    Raises ValueError on a count the file cannot hold.
    """
    return [
        {
            "character_key": row.entry_id & _CHARACTER_MASK,
            "index": row.entry_id >> _INDEX_SHIFT,
            "data_offset": row.offset,
            "data_size": row.size,
        }
        for row in parse_bare_u32_offset_rows(data)
    ]

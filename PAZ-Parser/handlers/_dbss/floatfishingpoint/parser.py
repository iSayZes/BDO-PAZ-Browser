"""`floatfishingpoint.dbss`: the fishing points that float on open water.

    u32 count | count x 42-byte row:
    u16 point_key | u32 point_size | f32 start x, y, z | f32 end x | 4 bytes |
    f32 end z | u16 fishing_group_key | 4 bytes | u16 spawn_character_key |
    u8 spawn_action_index | 3 bytes

`fishing_group_key` is a `floatfishing.dbss` row. `floatfishingpointoffset.dbss`
(u32 count, then u16 key, u32 offset and u32 size per row) points at the row
start. Layout 1 in docs/file-formats/dbss/floatfishingpoint_dbss.md.
"""

from __future__ import annotations

import struct

from _common.counted_rows import counted_row_values
from _common.pabr_offset import PabrOffsetRow, parse_bare_offset_rows


FILE_NAME = "floatfishingpoint.dbss"
OFFSET_FILE = "floatfishingpointoffset.dbss"
KEY_FIELD = "point_key"

_ROW = struct.Struct("<HI4f4sfH4sHB3s")
_FIELDS = (
    KEY_FIELD,
    "point_size",
    "start_position_x",
    "start_position_y",
    "start_position_z",
    "end_position_x",
    "unknown_16",
    "end_position_z",
    "fishing_group_key",
    "unknown_20",
    "spawn_character_key",
    "spawn_action_index",
    "unknown_27",
)


def parse_floatfishingpoint_records(data: bytes) -> list[dict]:
    """Every row in file order; byte runs become hex text.

    Raises ValueError when the rows do not fill the file.
    """
    return [
        {field: value.hex() if isinstance(value, bytes) else value for field, value in zip(_FIELDS, row, strict=True)}
        for row in counted_row_values(data, _ROW, FILE_NAME)
    ]


def parse_floatfishingpointoffset_rows(data: bytes) -> list[PabrOffsetRow]:
    """Every index row. Raises ValueError on a count the file cannot hold."""
    return parse_bare_offset_rows(data)

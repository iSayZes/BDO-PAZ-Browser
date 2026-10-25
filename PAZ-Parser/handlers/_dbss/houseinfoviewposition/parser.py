"""`houseinfoviewposition.dbss`: a world position and facing per house and house use type.

    PABR | u32 count | count x row | u32 string_count (0) | u32 table_start | u32 0
    row: u16 character_key | i16 padding_02 | u32 house_group_type
         | f32[3] position | f32[3] direction

The first 8 bytes are the row key (the 2016 `gc::HouseInfoViewPositionKey`).
`houseinfoviewpositionoffset.dbss` holds the same 8-byte key, then the
offset and size of the row, after a u32 count with no magic. Layout 1 in
docs/file-formats/dbss/houseinfoviewposition_dbss.md.
"""

from __future__ import annotations

import math
import struct

from _common.counted_rows import counted_row_values
from _common.pabr_strings import fixed_row_offsets


FILE_NAME = "houseinfoviewposition.dbss"
OFFSET_FILE = "houseinfoviewpositionoffset.dbss"
KEY_FIELD = "character_key"

_ROW = struct.Struct("<HhI3f3f")
_OFFSET_ROW = struct.Struct("<HhIII")
_OFFSET_FIELDS = (KEY_FIELD, "padding_02", "house_group_type", "data_offset", "data_size")
_FULL_TURN = 360.0


def _record(character_key: int, padding_02: int, house_group_type: int, *vectors: float) -> dict:
    return {
        KEY_FIELD: character_key,
        "padding_02": padding_02,
        "house_group_type": house_group_type,
        "position": list(vectors[:3]),
        "direction": list(vectors[3:]),
    }


def parse_houseinfoviewposition_records(data: bytes) -> list[dict]:
    """Every row in file order.

    Raises ValueError on a missing magic or rows that do not end where the
    string table starts.
    """
    return [_record(*_ROW.unpack_from(data, start)) for start in fixed_row_offsets(data, _ROW.size, FILE_NAME)]


def parse_houseinfoviewpositionoffset_records(data: bytes) -> list[dict]:
    """Every index row. Raises ValueError when the rows do not fill the file."""
    return [dict(zip(_OFFSET_FIELDS, values, strict=True)) for values in counted_row_values(data, _OFFSET_ROW, OFFSET_FILE)]


def yaw_degrees(direction: list[float]) -> float:
    """The facing as a yaw in degrees, 0 to 360: the direction is (-sin yaw, 0, -cos yaw)."""
    x, _y, z = direction
    return math.degrees(math.atan2(-x, -z)) % _FULL_TURN

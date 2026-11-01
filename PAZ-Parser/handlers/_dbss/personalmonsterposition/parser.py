"""`personalmonsterposition.dbss`: the spawn points of the Dark Rift bosses.

    u32 count | count x (u32 position_index | f32 x, y, z | f32 spawn_distance | u16 unknown_14)

`personalmonsterpositionoffset.dbss` (u32 count, then u32 index, offset and
size per row) points at the row start. Layout 2 in
docs/file-formats/dbss/personalmonsterposition_dbss.md.
"""

from __future__ import annotations

import struct

from _common.counted_rows import parse_counted_rows
from _common.pabr_offset import PabrOffsetRow, parse_bare_u32_offset_rows


FILE_NAME = "personalmonsterposition.dbss"
OFFSET_FILE = "personalmonsterpositionoffset.dbss"
KEY_FIELD = "position_index"

_ROW = struct.Struct("<IffffH")
_FIELDS = (KEY_FIELD, "x", "y", "z", "spawn_distance", "unknown_14")


def parse_personalmonsterposition_records(data: bytes) -> list[dict]:
    """Every row in file order. Raises ValueError when the rows do not fill the file."""
    return parse_counted_rows(data, _ROW, _FIELDS, FILE_NAME)


def parse_personalmonsterpositionoffset_rows(data: bytes) -> list[PabrOffsetRow]:
    """Every index row. Raises ValueError on a count the file cannot hold."""
    return parse_bare_u32_offset_rows(data)

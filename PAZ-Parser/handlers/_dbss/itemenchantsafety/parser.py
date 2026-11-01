"""`itemenchantsafety.dbss`: the enhancement safety limits per gear type.

    u32 count | count x (u8 type | u8 min_level | u8 max_level
                         | u32 stack | u32 caution_stack | u32 caution_rate)

`itemenchantsafetyoffset.dbss` (u32 count, then u32 type, offset and size
per row) points at the row start. Layout 1 in
docs/file-formats/dbss/itemenchantsafety_dbss.md.
"""

from __future__ import annotations

import struct

from _common.counted_rows import parse_counted_rows
from _common.pabr_offset import PabrOffsetRow, parse_bare_u32_offset_rows


FILE_NAME = "itemenchantsafety.dbss"
OFFSET_FILE = "itemenchantsafetyoffset.dbss"
KEY_FIELD = "type"

_ROW = struct.Struct("<BBBIII")
_FIELDS = (KEY_FIELD, "min_level", "max_level", "stack", "caution_stack", "caution_rate")


def parse_itemenchantsafety_records(data: bytes) -> list[dict]:
    """Every row in file order. Raises ValueError when the rows do not fill the file."""
    return parse_counted_rows(data, _ROW, _FIELDS, FILE_NAME)


def parse_itemenchantsafetyoffset_rows(data: bytes) -> list[PabrOffsetRow]:
    """Every index row. Raises ValueError on a count the file cannot hold."""
    return parse_bare_u32_offset_rows(data)

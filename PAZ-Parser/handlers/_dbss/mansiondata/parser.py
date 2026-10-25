"""`mansiondata.dbss`: the furniture characters that belong to the manor.

    u32 count | count x (u16 character_key | u16 character_key_dup
                         | u8 unknown_04 | u8 unknown_05)

`mansiondataoffset.dbss` (u32 count, then u16 key, offset and size per
row) points 2 bytes into a row, at `character_key_dup`. Layout 1 in
docs/file-formats/dbss/mansiondata_dbss.md.
"""

from __future__ import annotations

import struct

from _common.counted_rows import parse_counted_rows
from _common.pabr_offset import PabrOffsetRow, parse_bare_offset_rows


FILE_NAME = "mansiondata.dbss"
OFFSET_FILE = "mansiondataoffset.dbss"
KEY_FIELD = "character_key"

_ROW = struct.Struct("<HHBB")
_FIELDS = (KEY_FIELD, "character_key_dup", "unknown_04", "unknown_05")


def parse_mansiondata_records(data: bytes) -> list[dict]:
    """Every row in file order. Raises ValueError when the rows do not fill the file."""
    return parse_counted_rows(data, _ROW, _FIELDS, FILE_NAME)


def parse_mansiondataoffset_rows(data: bytes) -> list[PabrOffsetRow]:
    """Every index row. Raises ValueError on a count the file cannot hold."""
    return parse_bare_offset_rows(data)

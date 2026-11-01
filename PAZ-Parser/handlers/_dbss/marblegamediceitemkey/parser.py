"""`marblegamediceitemkey.dbss`: the keys of the Black Spirit's Adventure dice items.

    u32 count | count x u32 dice_item_key

`marblegamediceitemkeyoffset.dbss` (u32 count, then u32 key, offset and size
per row) points at each key. Layout 1 in
docs/file-formats/dbss/marblegamediceitemkey_dbss.md.
"""

from __future__ import annotations

import struct

from _common.counted_rows import parse_counted_rows
from _common.pabr_offset import PabrOffsetRow, parse_bare_u32_offset_rows


FILE_NAME = "marblegamediceitemkey.dbss"
OFFSET_FILE = "marblegamediceitemkeyoffset.dbss"
KEY_FIELD = "dice_item_key"

ROW = struct.Struct("<I")


def parse_marblegamediceitemkey_records(data: bytes) -> list[dict]:
    """Every key in file order. Raises ValueError when the rows do not fill the file."""
    return parse_counted_rows(data, ROW, (KEY_FIELD,), FILE_NAME)


def parse_marblegamediceitemkeyoffset_rows(data: bytes) -> list[PabrOffsetRow]:
    """Every index row. Raises ValueError on a count the file cannot hold."""
    return parse_bare_u32_offset_rows(data)

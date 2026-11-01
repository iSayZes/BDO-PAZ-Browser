"""`restrictcontentsregion.dbss`: the functions a region turns off.

    u32 count | count x (u16 region_key | u16 region_key_dup | u8 x 9)

The first eight bytes are the `Ban_*` flags of the `Ban_Function` sheet, the
ninth is unknown. `restrictcontentsregionoffset.dbss` (u32 count, then u16
region key, offset and size per row) points 2 bytes into each row, at
`region_key_dup`. Layout 2 in docs/file-formats/dbss/restrictcontentsregion_dbss.md.
"""

from __future__ import annotations

import struct

from _common.counted_rows import parse_counted_rows
from _common.pabr_offset import PabrOffsetRow, parse_bare_offset_rows


FILE_NAME = "restrictcontentsregion.dbss"
OFFSET_FILE = "restrictcontentsregionoffset.dbss"
KEY_FIELD = "region_key"

# The functions in file order: `Ban_Maid` to `Ban_MiniMap` of the sheet.
BAN_FIELDS = (
    "ban_maid",
    "ban_world_map",
    "ban_character_change",
    "ban_muster",
    "ban_camp",
    "ban_compass",
    "ban_item_map",
    "ban_mini_map",
)

_ROW = struct.Struct("<HH9B")
_FIELDS = (KEY_FIELD, "region_key_dup", *BAN_FIELDS, "unknown_0c")


def parse_restrictcontentsregion_records(data: bytes) -> list[dict]:
    """Every row in file order. Raises ValueError when the rows do not fill the file."""
    return parse_counted_rows(data, _ROW, _FIELDS, FILE_NAME)


def parse_restrictcontentsregionoffset_rows(data: bytes) -> list[PabrOffsetRow]:
    """Every index row. Raises ValueError on a count the file cannot hold."""
    return parse_bare_offset_rows(data)

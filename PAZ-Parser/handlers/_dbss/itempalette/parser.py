"""`itempalette.dbss`: the dye colour each dye item applies.

    u32 count | count x (u32 item_key | u8 palette_type | u8 palette_index)

`palette_type` is a row of `dyeingpalette.dbss` and `palette_index` a colour
in it. `itempaletteoffset.dbss` (u32 count, then u32 item key, offset and
size per row) points at the row start. Layout 1 in
docs/file-formats/dbss/itempalette_dbss.md.
"""

from __future__ import annotations

import struct

from _common.counted_rows import parse_counted_rows
from _common.pabr_offset import PabrOffsetRow, parse_bare_u32_offset_rows


FILE_NAME = "itempalette.dbss"
OFFSET_FILE = "itempaletteoffset.dbss"
KEY_FIELD = "item_key"

_ROW = struct.Struct("<IBB")
_FIELDS = (KEY_FIELD, "palette_type", "palette_index")


def parse_itempalette_records(data: bytes) -> list[dict]:
    """Every row in file order. Raises ValueError when the rows do not fill the file."""
    return parse_counted_rows(data, _ROW, _FIELDS, FILE_NAME)


def parse_itempaletteoffset_rows(data: bytes) -> list[PabrOffsetRow]:
    """Every index row. Raises ValueError on a count the file cannot hold."""
    return parse_bare_u32_offset_rows(data)

"""`servnatmarkettax.dbss`: the Horse Market silver bonus per Training level.

    u32 count | count x (u32 life_level | u32 horse_market_tax_percent)

`horse_market_tax_percent` is on the 1,000,000 = 100% scale: the Lua divides
`ToClient_GetServantMarketTaxPercent()` by 10,000 for the percent it shows.
`servnatmarkettaxoffset.dbss` (u32 count, then u32 level, offset and size
per row) points at the row start. Layout 1 in
docs/file-formats/dbss/servnatmarkettax_dbss.md.
"""

from __future__ import annotations

import struct

from _common.counted_rows import parse_counted_rows
from _common.pabr_offset import PabrOffsetRow, parse_bare_u32_offset_rows


FILE_NAME = "servnatmarkettax.dbss"
OFFSET_FILE = "servnatmarkettaxoffset.dbss"
KEY_FIELD = "life_level"

_ROW = struct.Struct("<II")
_FIELDS = (KEY_FIELD, "horse_market_tax_percent")


def parse_servnatmarkettax_records(data: bytes) -> list[dict]:
    """Every row in file order. Raises ValueError when the rows do not fill the file."""
    return parse_counted_rows(data, _ROW, _FIELDS, FILE_NAME)


def parse_servnatmarkettaxoffset_rows(data: bytes) -> list[PabrOffsetRow]:
    """Every index row. Raises ValueError on a count the file cannot hold."""
    return parse_bare_u32_offset_rows(data)

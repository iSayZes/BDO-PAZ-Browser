"""`floatfishing.dbss`: the fish drop groups of the floating fishing points.

    u32 count | count x 70-byte row:
    u16 fishing_group_key | 28 bytes | u32 drop_ids[5] | u32 drop_rates[5]

The five slots are treasure, rare, large, general and junk; a rate is on the
1,000,000 = 100% scale, `0` with an empty slot. `floatfishingoffset.dbss`
(u32 count, then u16 key, u32 offset and u32 size per row) points at the
row start. Layout 2 in docs/file-formats/floatfishing_dbss.md.
"""

from __future__ import annotations

import struct

from _common.counted_rows import counted_row_values
from _common.pabr_offset import PabrOffsetRow, parse_bare_offset_rows


FILE_NAME = "floatfishing.dbss"
OFFSET_FILE = "floatfishingoffset.dbss"
KEY_FIELD = "fishing_group_key"
DROP_SLOT_COUNT = 5

_ROW = struct.Struct(f"<H28s{DROP_SLOT_COUNT}I{DROP_SLOT_COUNT}I")


def _record(values: tuple) -> dict:
    key, unknown_02, *drops = values
    return {
        KEY_FIELD: key,
        "unknown_02": unknown_02.hex(),
        "drop_ids": list(drops[:DROP_SLOT_COUNT]),
        "drop_rates": list(drops[DROP_SLOT_COUNT:]),
    }


def parse_floatfishing_records(data: bytes) -> list[dict]:
    """Every row in file order. Raises ValueError when the rows do not fill the file."""
    return [_record(values) for values in counted_row_values(data, _ROW, FILE_NAME)]


def parse_floatfishingoffset_rows(data: bytes) -> list[PabrOffsetRow]:
    """Every index row. Raises ValueError on a count the file cannot hold."""
    return parse_bare_offset_rows(data)

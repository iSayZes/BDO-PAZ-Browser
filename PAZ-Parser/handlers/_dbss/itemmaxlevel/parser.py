"""`itemmaxlevel.dbss`: the highest enhancement level of each enhanceable item.

A `PABR` table of 5-byte rows (u32 item ID, u8 level) with an empty string
table. `itemmaxleveloffset.dbss` points at each row, so reading the rows in
order needs no index. Layout in docs/file-formats/itemmaxlevel_dbss.md.
"""

from __future__ import annotations

import struct

from _common.pabr_strings import fixed_row_offsets


FILE_NAME = "itemmaxlevel.dbss"
OFFSET_FILE = "itemmaxleveloffset.dbss"

_ROW = struct.Struct("<IB")  # item_id, max_enchant_level


def parse_itemmaxlevel_records(data: bytes) -> list[dict]:
    """Every row, in file order.

    Raises ValueError on a missing magic or rows that do not end where the
    string table starts.
    """
    return [_record(*_ROW.unpack_from(data, start)) for start in fixed_row_offsets(data, _ROW.size, FILE_NAME)]


def _record(item_id: int, max_enchant_level: int) -> dict:
    return {"item_id": item_id, "max_enchant_level": max_enchant_level}

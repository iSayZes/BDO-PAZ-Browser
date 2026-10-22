"""`buffitemautousestaticstatus.bss`: the items the Fairy's auto-use of buff items can use, by category.

    PABR | u32 row_count | row_count x row (9 bytes) | string table
    | u32 table_start | u32 0
    row: u32 category_key | u32 item_key | u8 unknown_08

Layout 2 in docs/file-formats/buffitemautousestaticstatus_bss.md; clients
2107 to 2519 have no `unknown_08` (Layout 1), which this parser does not
read.
"""

from __future__ import annotations

import struct

from _common.pabr_strings import fixed_row_offsets


FILE_NAME = "buffitemautousestaticstatus.bss"
KEY_FIELD = "item_key"

_ROW = struct.Struct("<IIB")
_FIELDS = ("category_key", KEY_FIELD, "unknown_08")


def parse_buffitemautouse_records(data: bytes) -> list[dict]:
    """Every row in file order.

    Raises ValueError on a bad magic or when the rows do not end where the
    string table starts.
    """
    return [
        dict(zip(_FIELDS, _ROW.unpack_from(data, start), strict=True))
        for start in fixed_row_offsets(data, _ROW.size, FILE_NAME)
    ]

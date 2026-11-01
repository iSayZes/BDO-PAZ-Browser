"""`monsterbuffzone.bss`: one row per monster buff zone key.

    u32 count | count x (u32 key | u32 unknown_04 | u32 unknown_08 | u32 unknown_0c
                         | u32 unknown_10 | u8 unknown_14 | u8 unknown_15)

`unknown_14` and `unknown_15` repeat the key's second and first byte. Layout 1
in docs/file-formats/bss/monsterbuffzone_bss.md.
"""

from __future__ import annotations

import struct

from _common.counted_rows import parse_counted_rows


FILE_NAME = "monsterbuffzone.bss"

_ROW = struct.Struct("<5I2B")
_FIELDS = ("key", "unknown_04", "unknown_08", "unknown_0c", "unknown_10", "unknown_14", "unknown_15")


def parse_monsterbuffzone_records(data: bytes) -> list[dict]:
    """Every row in file order. Raises ValueError when the rows do not fill the file."""
    return parse_counted_rows(data, _ROW, _FIELDS, FILE_NAME)

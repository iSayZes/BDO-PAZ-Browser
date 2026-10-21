"""`simplesequence.bss`: one row per u32 key.

    u32 count | count x (u32 key | u16 unknown_04 | u16 unknown_06 | u16 unknown_08
                         | u16 unknown_0a | u8 unknown_0c)

The two u16 halves of `key` repeat as `unknown_04` and `unknown_06`, then in
swapped order as `unknown_08` and `unknown_0a`. Layout 1 in
docs/file-formats/simplesequence_bss.md.
"""

from __future__ import annotations

import struct

from _common.counted_rows import parse_counted_rows


FILE_NAME = "simplesequence.bss"

_ROW = struct.Struct("<I4HB")
_FIELDS = ("key", "unknown_04", "unknown_06", "unknown_08", "unknown_0a", "unknown_0c")


def parse_simplesequence_records(data: bytes) -> list[dict]:
    """Every row in file order. Raises ValueError when the rows do not fill the file."""
    return parse_counted_rows(data, _ROW, _FIELDS, FILE_NAME)

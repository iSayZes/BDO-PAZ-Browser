"""`servanttransformdata.dbss`: the ship appearance changes offered at a wharf.

    u32 count | count x (u16 form_key | u16 form_key_dup | u16 from_character_key | u16 to_character_key)

`servanttransformdataoffset.dbss` points at each row's `form_key_dup`, so
the walk from the start needs no index. Layout 1 in
docs/file-formats/servanttransformdata_dbss.md.
"""

from __future__ import annotations

import struct

from _common.binary import u32


FILE_NAME = "servanttransformdata.dbss"
OFFSET_FILE = "servanttransformdataoffset.dbss"

_COUNT_SIZE = 4
# form_key, form_key_dup, from_character_key, to_character_key
_ROW = struct.Struct("<HHHH")


def parse_servanttransformdata_records(data: bytes) -> list[dict]:
    """Every row, in file order.

    Raises ValueError when the file is not the row count followed by exactly
    that many rows.
    """
    if len(data) < _COUNT_SIZE:
        raise ValueError(f"{FILE_NAME} is too short to hold its row count")

    count = u32(data, 0)
    end = _COUNT_SIZE + count * _ROW.size
    if end != len(data):
        raise ValueError(f"{count:,} rows of {_ROW.size} bytes end at 0x{end:X}, the file is {len(data):,} bytes")

    return [
        {
            "form_key": form_key,
            "form_key_dup": form_key_dup,
            "from_character_key": from_character_key,
            "to_character_key": to_character_key,
        }
        for form_key, form_key_dup, from_character_key, to_character_key in _ROW.iter_unpack(data[_COUNT_SIZE:end])
    ]

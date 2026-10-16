"""`fieldboss.dbss`: the character IDs listed as field bosses.

A u32 row count, then 33-byte rows with no `PABR` magic and no string
table: the key, a byte, the character ID, 12 zero bytes, a byte and 15 zero
bytes.
`fieldbossoffset.dbss` points at each row's first byte after the key.
Layout in docs/file-formats/fieldboss_dbss.md.
"""

from __future__ import annotations

import struct

from _common.binary import u32


FILE_NAME = "fieldboss.dbss"
OFFSET_FILE = "fieldbossoffset.dbss"

_COUNT_SIZE = 4
# key, unknown_02, character_id, unknown_05, unknown_11, unknown_12
_ROW = struct.Struct("<HBH12xB15x")


def parse_fieldboss_records(data: bytes) -> list[dict]:
    """Every row, in file order.

    Raises ValueError when the file is not exactly the count and its rows.
    """
    if len(data) < _COUNT_SIZE:
        raise ValueError(f"{FILE_NAME} is too short to hold its row count")

    count = u32(data, 0)
    expected_size = _COUNT_SIZE + count * _ROW.size
    if len(data) != expected_size:
        raise ValueError(
            f"{FILE_NAME} declares {count:,} rows ({expected_size:,} bytes) but holds {len(data):,} bytes"
        )

    return [
        {
            "key": key,
            "character_id": character_id,
            "unknown_02": unknown_02,
            "unknown_11": unknown_11,
        }
        for key, unknown_02, character_id, unknown_11 in _ROW.iter_unpack(data[_COUNT_SIZE:])
    ]

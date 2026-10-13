"""`weatheractor.dbss`: the characters tied to the weather system.

A u32 row count, then 75-byte rows with no `PABR` magic and no string
table: a u16 key, the character key, a type byte, floats and small integers
whose meaning is open, and on a few rows a skill key. `weatheractoroffset.dbss`
points 2 bytes into each row, past its key. Layout in
docs/file-formats/weatheractor_dbss.md.
"""

from __future__ import annotations

import struct

from _common.binary import u32


FILE_NAME = "weatheractor.dbss"
OFFSET_FILE = "weatheractoroffset.dbss"

_COUNT_SIZE = 4
_ROW = struct.Struct("<HBHB6f4sIIIf12sHfH4sB")
_FIELDS = (
    "key",
    "unknown_02",
    "character_key",
    "unknown_05",
    "unknown_06",
    "unknown_0a",
    "unknown_0e",
    "unknown_12",
    "unknown_16",
    "unknown_1a",
    "unknown_1e",
    "skill_key",
    "unknown_26",
    "unknown_2a",
    "unknown_2e",
    "unknown_32",
    "unknown_3e",
    "unknown_40",
    "unknown_44",
    "unknown_46",
    "unknown_4a",
)


def parse_weatheractor_records(data: bytes) -> list[dict]:
    """Every row, in file order; byte runs become hex text.

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
        {field: value.hex() if isinstance(value, bytes) else value for field, value in zip(_FIELDS, row)}
        for row in _ROW.iter_unpack(data[_COUNT_SIZE:])
    ]

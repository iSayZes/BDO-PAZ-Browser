"""`instancedungeonskillstatic.dbss`: the instance dungeon skill table.

    u32 count | count x (u32 key | str16 unknown_04 | u32 unknown_04_00)

Client 3473 ships the count `0` and no records; client 1784 holds 157 records
(Layout 1), each a key and a Korean text with `<PAColor>` tags.
`instancedungeonskillstaticoffset.dbss` holds bare u32-keyed index rows that
point just past each record's key. Layout in
docs/file-formats/instancedungeonskillstatic_dbss.md.
"""

from __future__ import annotations

import struct

from _common.binary import u32
from _common.record_reader import RecordReader


FILE_NAME = "instancedungeonskillstatic.dbss"
OFFSET_FILE = "instancedungeonskillstaticoffset.dbss"

COUNT_SIZE = 4
_U32 = struct.Struct("<I")


def parse_instancedungeonskillstatic_records(data: bytes) -> list[dict]:
    """Every record in file order; none for the empty table of the live client.

    Raises ValueError when a record runs past the file or bytes follow the last one.
    """
    if len(data) < COUNT_SIZE:
        raise ValueError(f"{FILE_NAME} is too short to hold its record count")
    reader = RecordReader(data, COUNT_SIZE, len(data), FILE_NAME)
    records: list[dict] = []
    for _ in range(u32(data, 0)):
        (key,) = reader.unpack(_U32)
        unknown_04 = reader.text(wide=True)
        (unknown_04_00,) = reader.unpack(_U32)
        records.append({"key": key, "unknown_04": unknown_04, "unknown_04_00": unknown_04_00})
    if not reader.at_end():
        raise ValueError(f"{FILE_NAME} records end at 0x{reader.pos:X} but the file holds {len(data):,} bytes")
    return records

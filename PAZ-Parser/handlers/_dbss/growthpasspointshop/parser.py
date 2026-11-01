"""`growthpasspointshop.dbss`: the Growth Pass point shop table.

    u32 count | count x 28-byte record (u32 key | u32 key_dup | 5 x u32 unknown)

Client 3473 ships the count `0` and no records; client 1784 holds 15 records
(Layout 1). `growthpasspointshopoffset.dbss` holds bare u32-keyed index rows
that point just past each record's key. Layout in
docs/file-formats/dbss/growthpasspointshop_dbss.md.
"""

from __future__ import annotations

import struct

from _common.binary import u32


FILE_NAME = "growthpasspointshop.dbss"
OFFSET_FILE = "growthpasspointshopoffset.dbss"

COUNT_SIZE = 4
# u32 key | u32 key_dup | u32 unknown_08 | u32 unknown_0c | u32 unknown_10
# | u32 unknown_14 | u32 unknown_18
RECORD = struct.Struct("<7I")
_FIELDS = ("key", "key_dup", "unknown_08", "unknown_0c", "unknown_10", "unknown_14", "unknown_18")


def parse_growthpasspointshop_records(data: bytes) -> list[dict]:
    """Every record in file order; none for the empty table of the live client.

    Raises ValueError when the file is not exactly its count and that many records.
    """
    if len(data) < COUNT_SIZE:
        raise ValueError(f"{FILE_NAME} is too short to hold its record count")
    count = u32(data, 0)
    expected = COUNT_SIZE + count * RECORD.size
    if len(data) != expected:
        raise ValueError(f"{FILE_NAME} declares {count:,} records ({expected:,} bytes) but holds {len(data):,} bytes")
    return [dict(zip(_FIELDS, values)) for values in RECORD.iter_unpack(data[COUNT_SIZE:])]

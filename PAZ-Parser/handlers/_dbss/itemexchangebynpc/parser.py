"""`itemexchangebynpc.dbss`: the item exchanges NPC dialogs list by key.

A u32 row count, then 28-byte rows: the u16 exchange key the index stores,
then the 2016 `gc::ItemExchangeByNpcStaticStatus` packed (the key again, the
u32 need item key, i64 need count, u32 result item key, i64 result count).
`itemexchangebynpcoffset.dbss` points 2 bytes into a row, at the key copy, so
the walk from the start needs no index. Layout 1 in
docs/file-formats/itemexchangebynpc_dbss.md.
"""

from __future__ import annotations

import struct

from _common.binary import u32


FILE_NAME = "itemexchangebynpc.dbss"
OFFSET_FILE = "itemexchangebynpcoffset.dbss"

_COUNT_SIZE = 4
_ROW = struct.Struct("<HHIqIq")
_FIELDS = (
    "item_exchange_key",
    "item_exchange_key_dup",
    "need_item_key",
    "need_item_count",
    "result_item_key",
    "result_item_count",
)


def parse_itemexchangebynpc_records(data: bytes) -> list[dict]:
    """Every row, in file order.

    Raises ValueError when the file is not the row count followed by exactly
    that many rows.
    """
    if len(data) < _COUNT_SIZE:
        raise ValueError(f"{FILE_NAME} is too short to hold its row count")

    count = u32(data, 0)
    expected = _COUNT_SIZE + count * _ROW.size
    if expected != len(data):
        raise ValueError(f"{count:,} rows of {_ROW.size} bytes need {expected:,} bytes, the file is {len(data):,}")
    return [
        dict(zip(_FIELDS, _ROW.unpack_from(data, _COUNT_SIZE + index * _ROW.size), strict=True))
        for index in range(count)
    ]

"""`itemtrade.dbss`: the character keys of every NPC that buys trade goods.

A u32 count, then `count` u16 character keys and nothing else: no `PABR`
magic and no string table. `itemtradeoffset.dbss` points at each key, so
reading the keys in order needs no index. Layout in
docs/file-formats/dbss/itemtrade_dbss.md.
"""

from __future__ import annotations

import struct

from _common.binary import u32


FILE_NAME = "itemtrade.dbss"
OFFSET_FILE = "itemtradeoffset.dbss"

_COUNT_SIZE = 4
_KEY = struct.Struct("<H")


def parse_itemtrade_records(data: bytes) -> list[dict]:
    """Every character key, in file order.

    Raises ValueError when the file is not exactly the count and its keys.
    """
    if len(data) < _COUNT_SIZE:
        raise ValueError(f"{FILE_NAME} is too short to hold its row count")

    count = u32(data, 0)
    expected_size = _COUNT_SIZE + count * _KEY.size
    if len(data) != expected_size:
        raise ValueError(
            f"{FILE_NAME} declares {count:,} keys ({expected_size:,} bytes) but holds {len(data):,} bytes"
        )

    return [
        {"character_id": character_id}
        for (character_id,) in _KEY.iter_unpack(data[_COUNT_SIZE:expected_size])
    ]

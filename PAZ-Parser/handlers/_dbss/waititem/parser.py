"""`waititem.dbss`: the item keys the Central Market puts in its Registration Queue.

A u32 row count, then 17-byte rows with no `PABR` magic and no string
table: the key, the packed item key, the item ID and level split out, and
the u32 `wait_second` (the client 1784 sheet's `WaitSecond`). `waititemoffset.dbss` points at each row's `item_key`, 4
bytes past its key. Layout in docs/file-formats/dbss/waititem_dbss.md.
"""

from __future__ import annotations

import struct

from _common.binary import u32


FILE_NAME = "waititem.dbss"
OFFSET_FILE = "waititemoffset.dbss"

_COUNT_SIZE = 4
_ROW = struct.Struct("<IIIBI")


def parse_waititem_records(data: bytes) -> list[dict]:
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
            "item_key": item_key,
            "item_id": item_id,
            "enchant_level": enchant_level,
            "wait_second": wait_second,
        }
        for key, item_key, item_id, enchant_level, wait_second in _ROW.iter_unpack(data[_COUNT_SIZE:])
    ]

"""`itemnakmessage.dbss`: the screen-wide message shown when a rare item is found.

    u32 count | count x (u32 item_key | str16 main_message_key | str16 sub_message_key)

Both strings are `GAME` sheet keys of `stringtable.bss`.
`itemnakmessageoffset.dbss` is a `PABR` index (u32 item key, offset and size
per row) that points at the row start. Layout 1 in
docs/file-formats/dbss/itemnakmessage_dbss.md.
"""

from __future__ import annotations

import struct

from _common.binary import u32
from _common.record_reader import RecordReader


FILE_NAME = "itemnakmessage.dbss"
OFFSET_FILE = "itemnakmessageoffset.dbss"

COUNT_SIZE = 4
_ITEM_KEY = struct.Struct("<I")


def _read_row(reader: RecordReader) -> dict:
    (item_key,) = reader.unpack(_ITEM_KEY)
    return {
        "item_key": item_key,
        "main_message_key": reader.text(wide=True),
        "sub_message_key": reader.text(wide=True),
    }


def parse_itemnakmessage_records(data: bytes) -> list[dict]:
    """Every row in file order.

    Raises ValueError when a row runs past the file or the rows do not end at
    its last byte.
    """
    if len(data) < COUNT_SIZE:
        raise ValueError(f"{FILE_NAME} is too short to hold its row count")

    count = u32(data, 0)
    reader = RecordReader(data, COUNT_SIZE, len(data), FILE_NAME)
    records = [_read_row(reader) for _ in range(count)]
    if not reader.at_end():
        raise ValueError(f"{FILE_NAME} has {reader.remaining():,} bytes after its {count:,} rows")
    return records

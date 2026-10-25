"""`houseinfoneeditem.dbss`: the items and time each house level costs, per need item group.

A u32 row count, then the rows back to back with no `PABR` magic and no
string table. A row is a u16 group key (the `need_item_key` of
`houseinforeceipe.dbss`) and six level slots, the 2016
`pa::Array<gc::HouseInfoNeedItemLevelGroup,6>`: an i32 level, an i32 transfer
time in seconds and a u32-counted list of (u32 item key, i64 count) pairs.
Slot 0 holds level 0 and no items; slots 1 to 5 are the house levels.
`houseinfoneeditemoffset.dbss` points at each row's key. Layout in
docs/file-formats/dbss/houseinfoneeditem_dbss.md.
"""

from __future__ import annotations

import struct

from _common.binary import u32
from _common.record_reader import RecordReader


FILE_NAME = "houseinfoneeditem.dbss"
OFFSET_FILE = "houseinfoneeditemoffset.dbss"
# Level slots per row; slot 0 is level 0, the others the house levels 1 to 5.
LEVEL_SLOTS = 6

_COUNT_SIZE = 4
_KEY = struct.Struct("<H")
# level, transfer_time, item_count
_LEVEL_HEAD = struct.Struct("<iiI")
# item_key, count
_NEED_ITEM = struct.Struct("<Iq")


def parse_houseinfoneeditem_records(data: bytes) -> list[dict]:
    """Every need item row, in file order.

    Raises ValueError when a row runs past the end of the file or bytes are
    left after the last row.
    """
    if len(data) < _COUNT_SIZE:
        raise ValueError(f"{FILE_NAME} is too short to hold its row count")

    count = u32(data, 0)
    reader = RecordReader(data, _COUNT_SIZE, len(data), FILE_NAME)
    records = [_read_row(reader) for _ in range(count)]
    if not reader.at_end():
        raise ValueError(f"{FILE_NAME}: {reader.remaining()} bytes left after row {count - 1}")
    return records


def _read_row(reader: RecordReader) -> dict:
    (need_item_key,) = reader.unpack(_KEY)
    return {
        "need_item_key": need_item_key,
        "levels": [_read_level(reader) for _ in range(LEVEL_SLOTS)],
    }


def _read_level(reader: RecordReader) -> dict:
    level, transfer_time, item_count = reader.unpack(_LEVEL_HEAD)
    if item_count * _NEED_ITEM.size > reader.remaining():
        raise ValueError(f"list of {item_count:,} need items runs past the end of {FILE_NAME}")
    items = [
        {"item_key": item_key, "count": count}
        for item_key, count in (reader.unpack(_NEED_ITEM) for _ in range(item_count))
    ]
    return {"level": level, "transfer_time": transfer_time, "items": items}

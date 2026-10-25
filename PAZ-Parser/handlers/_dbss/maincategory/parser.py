"""`maincategory.dbss`: the Pearl Shop main categories.

    u32 count | count x (u16 category_id | u32 display_order | u32 tab_image_no
                         | u32 category_type | str8 icon_path
                         | u32 event_category | u8 is_display)

`maincategoryoffset.dbss` (no magic, no trailer) holds a u16 category ID, the
absolute u32 offset of its record, a u16 size and a u16 that is always 0 per
row. Layout in docs/file-formats/dbss/maincategory_dbss.md.
"""

from __future__ import annotations

import struct

from _common.binary import u32
from _common.record_reader import RecordReader


FILE_NAME = "maincategory.dbss"
OFFSET_FILE = "maincategoryoffset.dbss"

_COUNT_SIZE = 4
# u16 category_id | u32 record_offset | u16 record_size | u16 unknown_08
_OFFSET_ROW = struct.Struct("<HIHH")
# u16 category_id | u32 display_order | u32 tab_image_no | u32 category_type
_HEAD = struct.Struct("<HIII")
# u32 event_category | u8 is_display
_TAIL = struct.Struct("<IB")


def parse_maincategoryoffset_records(data: bytes) -> list[dict]:
    """Every index row in file order.

    Raises ValueError when the file is shorter than its declared rows.
    """
    if len(data) < _COUNT_SIZE:
        raise ValueError(f"{OFFSET_FILE} is too short to hold its row count")
    count = u32(data, 0)
    rows_end = _COUNT_SIZE + count * _OFFSET_ROW.size
    if rows_end > len(data):
        raise ValueError(f"{OFFSET_FILE} declares {count:,} rows past the end of the file")
    return [
        {"category_id": category_id, "record_offset": offset, "record_size": size, "unknown_08": unknown_08}
        for category_id, offset, size, unknown_08 in _OFFSET_ROW.iter_unpack(data[_COUNT_SIZE:rows_end])
    ]


def parse_maincategory_records(data: bytes, offset_data: bytes) -> list[dict]:
    """Every category in offset table order.

    Raises ValueError when a record runs past its offset row, names another
    category than its row, or leaves bytes over.
    """
    return [_read_category(data, row) for row in parse_maincategoryoffset_records(offset_data)]


def _read_category(data: bytes, row: dict) -> dict:
    start = row["record_offset"]
    label = f"{FILE_NAME} category {row['category_id']}"
    reader = RecordReader(data, start, start + row["record_size"], label)
    category_id, display_order, tab_image_no, category_type = reader.unpack(_HEAD)
    if category_id != row["category_id"]:
        raise ValueError(f"{label}: the record at 0x{start:X} names category {category_id}")
    icon_path = reader.text(wide=False)
    event_category, is_display = reader.unpack(_TAIL)
    if not reader.at_end():
        raise ValueError(f"{label}: {reader.remaining()} bytes left after the record")
    return {
        "category_id": category_id,
        "display_order": display_order,
        "tab_image_no": tab_image_no,
        "category_type": category_type,
        "icon_path": icon_path,
        "event_category": event_category,
        "is_display": bool(is_display),
    }

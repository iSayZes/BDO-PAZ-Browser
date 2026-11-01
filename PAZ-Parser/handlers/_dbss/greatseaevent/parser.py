"""`greatseaevent.dbss`: the result messages of the Great Ocean sailing events.

    u32 group_count | group_count x Group
    Group: u32 event_count | event_count x Event
    Event: u16 group_key | u8 select_index | str16 result_string_kr
           | str16 image_path | u32 unknown_image_path_00

`greatseaeventoffset.dbss` holds the same groups: u32 group_count, then per
group u16 group_key, u32 count and count x (u32 select_index, u32 offset,
u32 size), each pointing at the event start with the event's whole size.
Layout 1 in docs/file-formats/dbss/greatseaevent_dbss.md.
"""

from __future__ import annotations

import struct

from _common.binary import u32
from _common.record_reader import RecordReader


FILE_NAME = "greatseaevent.dbss"
OFFSET_FILE = "greatseaeventoffset.dbss"

_COUNT_SIZE = 4
_HEAD = struct.Struct("<HB")
_U32 = struct.Struct("<I")
_OFFSET_GROUP = struct.Struct("<HI")
_OFFSET_ROW = struct.Struct("<III")


def _read_event(reader: RecordReader) -> dict:
    group_key, select_index = reader.unpack(_HEAD)
    result = reader.text(wide=True)
    image_path = reader.text(wide=True)
    (unknown_tail,) = reader.unpack(_U32)
    return {
        "group_key": group_key,
        "select_index": select_index,
        "result_string_kr": result,
        "image_path": image_path,
        "unknown_image_path_00": unknown_tail,
    }


def parse_greatseaevent_records(data: bytes) -> list[dict]:
    """Every event of every group, in file order.

    Raises ValueError when an event runs past the file or the groups do not
    end at its last byte.
    """
    if len(data) < _COUNT_SIZE:
        raise ValueError(f"{FILE_NAME} is too short to hold its group count")

    reader = RecordReader(data, _COUNT_SIZE, len(data), FILE_NAME)
    records = []
    for _ in range(u32(data, 0)):
        (event_count,) = reader.unpack(_U32)
        records.extend(_read_event(reader) for _ in range(event_count))
    if not reader.at_end():
        raise ValueError(f"{FILE_NAME} has {reader.remaining():,} bytes after its last group")
    return records


def parse_greatseaeventoffset_records(data: bytes) -> list[dict]:
    """Every index row as group_key, select_index, data_offset and data_size.

    Raises ValueError when a group runs past the file or the groups do not
    end at its last byte.
    """
    if len(data) < _COUNT_SIZE:
        raise ValueError(f"{OFFSET_FILE} is too short to hold its group count")

    reader = RecordReader(data, _COUNT_SIZE, len(data), OFFSET_FILE)
    records = []
    for _ in range(u32(data, 0)):
        group_key, count = reader.unpack(_OFFSET_GROUP)
        for _ in range(count):
            select_index, offset, size = reader.unpack(_OFFSET_ROW)
            records.append({
                "group_key": group_key,
                "select_index": select_index,
                "data_offset": offset,
                "data_size": size,
            })
    if not reader.at_end():
        raise ValueError(f"{OFFSET_FILE} has {reader.remaining():,} bytes after its last group")
    return records

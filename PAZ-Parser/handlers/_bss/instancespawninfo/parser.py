"""`instancespawninfo.bss`: the private monster zones of the Personal Field window.

    u32 count | count x Row
    Row: u16 key | i32 max_x | i32 max_z | i32 min_x | i32 min_z | u16 unknown_12
         | f32 x | f32 y | f32 z | f32 radius | str16 area_name_kr
         | f32 offense_point | u16 unknown_area_name_kr_04 | u32 enter_item_key
         | u32 unknown_area_name_kr_0a | u32 unknown_area_name_kr_0e | u8 enter_type
         | u32 unknown_item_key | u8 unknown_area_name_kr_17

The box is in world units, the centre and radius in centimetres. Layout 6
(client 3454 and later) in docs/file-formats/instancespawninfo_bss.md.
"""

from __future__ import annotations

import struct
from typing import Any

from _common.counted_rows import read_counted_records
from _common.record_reader import RecordReader


FILE_NAME = "instancespawninfo.bss"

_HEAD = struct.Struct("<H4iH4f")
_HEAD_FIELDS = ("key", "max_x", "max_z", "min_x", "min_z", "unknown_12", "x", "y", "z", "radius")
_TAIL = struct.Struct("<fHIIIBIB")
_TAIL_FIELDS = (
    "offense_point",
    "unknown_area_name_kr_04",
    "enter_item_key",
    "unknown_area_name_kr_0a",
    "unknown_area_name_kr_0e",
    "enter_type",
    "unknown_item_key",
    "unknown_area_name_kr_17",
)


def _read_row(reader: RecordReader) -> dict:
    record: dict[str, Any] = dict(zip(_HEAD_FIELDS, reader.unpack(_HEAD), strict=True))
    record["area_name_kr"] = reader.text(wide=True)
    record.update(zip(_TAIL_FIELDS, reader.unpack(_TAIL), strict=True))
    return record


def parse_instancespawninfo_records(data: bytes) -> list[dict]:
    """Every row in file order. Raises ValueError when the rows do not end at the last byte."""
    return read_counted_records(data, _read_row, FILE_NAME)

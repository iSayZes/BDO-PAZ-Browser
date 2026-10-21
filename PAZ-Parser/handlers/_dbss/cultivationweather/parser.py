"""`cultivationweather.dbss`: how weather changes the growth speed of each crop.

    u32 count | count x record:
    u32 key_prefix | u32 exchange_key | u32 weather_count | weather_count x
        (u8 weather_kind | u32 range_count | range_count x
            (f32 weather_start_rate | f32 weather_end_rate | i32 product_speed_rate))

`exchange_key` is the crop's `itemexchangesource.bss` key and
`product_speed_rate` is on the 1,000,000 = 100% scale.
`cultivationweatheroffset.dbss` (u32 count, then u32 key, u32 offset and u32
size per row) points past the key prefix. Layout 2 in
docs/file-formats/cultivationweather_dbss.md.
"""

from __future__ import annotations

import struct

from _common.binary import u32
from _common.pabr_offset import PabrOffsetRow, parse_bare_u32_offset_rows
from _common.record_reader import RecordReader


FILE_NAME = "cultivationweather.dbss"
OFFSET_FILE = "cultivationweatheroffset.dbss"
KEY_FIELD = "exchange_key"

_COUNT_SIZE = 4
_HEAD = struct.Struct("<III")
_WEATHER = struct.Struct("<BI")
_RANGE = struct.Struct("<ffi")


def _read_weather(reader: RecordReader) -> dict:
    weather_kind, range_count = reader.unpack(_WEATHER)
    ranges = []
    for _ in range(range_count):
        start, end, speed = reader.unpack(_RANGE)
        ranges.append({"weather_start_rate": start, "weather_end_rate": end, "product_speed_rate": speed})
    return {"weather_kind": weather_kind, "ranges": ranges}


def _read_record(reader: RecordReader) -> dict:
    key_prefix, exchange_key, weather_count = reader.unpack(_HEAD)
    if key_prefix != exchange_key:
        raise ValueError(f"{FILE_NAME} record {exchange_key} follows the key prefix {key_prefix}")
    return {KEY_FIELD: exchange_key, "weathers": [_read_weather(reader) for _ in range(weather_count)]}


def parse_cultivationweather_records(data: bytes) -> list[dict]:
    """Every record in file order.

    Raises ValueError when a record runs past the file, its key prefix
    differs from its key, or the records do not end at the last byte.
    """
    if len(data) < _COUNT_SIZE:
        raise ValueError(f"{FILE_NAME} is too short to hold its record count")

    reader = RecordReader(data, _COUNT_SIZE, len(data), FILE_NAME)
    records = [_read_record(reader) for _ in range(u32(data, 0))]
    if not reader.at_end():
        raise ValueError(f"{FILE_NAME} has {reader.remaining():,} bytes after its last record")
    return records


def parse_cultivationweatheroffset_rows(data: bytes) -> list[PabrOffsetRow]:
    """Every index row. Raises ValueError on a count the file cannot hold."""
    return parse_bare_u32_offset_rows(data)

"""`fieldwalkingcameradata.bss`: the camera paths of the field walking camera events.

    PABR | u32 row_count | rows | String Table | u32 string_table_start | u32 0
    row: u32 event_name_hash | u32 event_name | u16 region_key
         | u32 point_count | Point[point_count] points | u32 unknown_points_00
    Point: f32[3] position | f32[4] rotation | f32 fov | f32 speed_or_time
           | u8 is_speed_mode | u8 is_spline

`event_name` indexes the string table; `event_name_hash` is its `key_hash()`.
The file is compiled from `fieldwalkingcamera/fieldwalkingcameradata.xml`.
Layout 1 in docs/file-formats/fieldwalkingcameradata_bss.md.
"""

from __future__ import annotations

import struct

from _bss.sequence_scripts.reader import check_rows_end, open_table, read_position, read_string_refs
from _common.record_reader import RecordReader


FILE_NAME = "fieldwalkingcameradata.bss"

_HASH = struct.Struct("<I")
_REGION_AND_COUNT = struct.Struct("<HI")
_POINT_TAIL = struct.Struct("<4fffBB")
_U32 = struct.Struct("<I")


def _read_point(reader: RecordReader) -> dict:
    position = read_position(reader)
    *rotation, fov, speed_or_time, is_speed_mode, is_spline = reader.unpack(_POINT_TAIL)
    return {
        "position": position,
        "rotation": rotation,
        "fov": fov,
        "speed_or_time": speed_or_time,
        "is_speed_mode": is_speed_mode,
        "is_spline": is_spline,
    }


def parse_fieldwalkingcameradata_rows(data: bytes) -> list[dict]:
    """Every event in file order with its points.

    Raises ValueError on a bad magic, a string index past the table, a point
    list that runs past the rows, or rows that do not end where the string
    table starts.
    """
    table = open_table(data, FILE_NAME)
    rows: list[dict] = []
    for index in range(table.row_count):
        (event_name_hash,) = table.reader.unpack(_HASH)
        texts = read_string_refs(table, ("event_name",), f"{FILE_NAME} row {index}")
        region_key, point_count = table.reader.unpack(_REGION_AND_COUNT)
        points = [_read_point(table.reader) for _ in range(point_count)]
        (unknown_points_00,) = table.reader.unpack(_U32)
        rows.append({
            "event_name_hash": event_name_hash,
            **texts,
            "region_key": region_key,
            "point_count": point_count,
            "points": points,
            "unknown_points_00": unknown_points_00,
        })
    check_rows_end(table, FILE_NAME)
    return rows

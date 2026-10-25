"""`videotriggerdata.bss`: where a video plays when the player walks in, and the scripts it runs.

    PABR | u32 row_count | row_count x 45-byte row | String Table
    | u32 string_table_start | u32 0
    row: u32 video_name_hash | u32 video_name | u32 start_condition
         | u32 start_execute | u32 end_execute | f32[3] position
         | u32 video_name_hash_dup | f32 radius | u32 contents_group_open
         | u8 unknown_2c

The text fields are indexes into the string table
(`_bss/sequence_scripts/reader.py`). Layout 1 in
docs/file-formats/bss/videotriggerdata_bss.md.
"""

from __future__ import annotations

import struct

from _bss.sequence_scripts.reader import SCRIPT_FIELDS, check_rows_end, open_table, read_position, read_string_refs


FILE_NAME = "videotriggerdata.bss"

_HASH = struct.Struct("<I")
_AREA = struct.Struct("<If")
_FLAG = struct.Struct("<B")
_HEAD_TEXT = ("video_name", *SCRIPT_FIELDS)
_TAIL_TEXT = ("contents_group_open",)


def parse_videotriggerdata_records(data: bytes) -> list[dict]:
    """Every row in file order, its text fields resolved.

    Raises ValueError on a bad magic, a string index past the table, or rows
    that do not end where the string table starts.
    """
    table = open_table(data, FILE_NAME)
    records: list[dict] = []
    for index in range(table.row_count):
        label = f"{FILE_NAME} row {index}"
        (video_name_hash,) = table.reader.unpack(_HASH)
        head = read_string_refs(table, _HEAD_TEXT, label)
        position = read_position(table.reader)
        video_name_hash_dup, radius = table.reader.unpack(_AREA)
        tail = read_string_refs(table, _TAIL_TEXT, label)
        (unknown_2c,) = table.reader.unpack(_FLAG)
        records.append({
            "video_name_hash": video_name_hash,
            **head,
            "position": position,
            "video_name_hash_dup": video_name_hash_dup,
            "radius": radius,
            **tail,
            "unknown_2c": unknown_2c,
        })
    check_rows_end(table, FILE_NAME)
    return records

"""`specialpass.bss`: the Special Pass events and the reward steps of each.

    PABR | u32 row_count | row_count x row
    | u32 track_count | track_count x (u32 step_count | step_count x step)
    | u32 unknown_after_tracks[..table_start] | string table
    | u32 table_start | u32 0
    row (43 bytes): u16 pass_key | u64 start_time | u64 end_time
         | u64 sale_end_time | u32 title_index | u32 period_index
         | u32 description_index | u32 content_type | u8 unknown_2a
    step (34 bytes): u16 pass_key | u32 basic_item_key | u64 basic_item_count
         | u32 pass_item_key | u64 pass_item_count | u64 reward_point

The three indices point into the string table. Clients 2107 to 2765 have a
42-byte row without `content_type` and a 26-byte step without
`reward_point` (Layout 1). Layout 2 in docs/file-formats/bss/specialpass_bss.md.
"""

from __future__ import annotations

import struct
from typing import NamedTuple

from _common.counted_rows import read_counted_structs
from _common.pabr_strings import HEADER_SIZE, U32_SIZE, checked_string_table_start, read_string_table, string_at
from _common.record_reader import RecordReader


FILE_NAME = "specialpass.bss"
KEY_FIELD = "pass_key"

_COUNT = struct.Struct("<I")
_ROW = struct.Struct("<HQQQIIIIB")
_ROW_FIELDS = (
    KEY_FIELD,
    "start_time",
    "end_time",
    "sale_end_time",
    "title_index",
    "period_index",
    "description_index",
    "content_type",
    "unknown_2a",
)
_STEP = struct.Struct("<HIQIQQ")
_STEP_FIELDS = (KEY_FIELD, "basic_item_key", "basic_item_count", "pass_item_key", "pass_item_count", "reward_point")
_TEXT_FIELDS = ("title_kr", "period_kr", "description_kr")
# The row fields of a step whose pass_key has no row.
_NO_ROW: dict = {**dict.fromkeys(_ROW_FIELDS), **dict.fromkeys(_TEXT_FIELDS, "")}


class SpecialPassFile(NamedTuple):
    rows: list[dict]
    # One list of steps per reward track, in file order.
    tracks: list[list[dict]]
    unknown_after_tracks: list[int]
    strings: list[str]


def parse_specialpass_file(data: bytes) -> SpecialPassFile:
    """The rows, the reward tracks, the u32 values after them and the string table.

    Raises ValueError on a bad magic or trailer, when a count runs past the
    string table, or when the bytes before it are not whole u32 values.
    """
    end = checked_string_table_start(data, FILE_NAME)
    reader = RecordReader(data, HEADER_SIZE - U32_SIZE, end, FILE_NAME)
    rows = read_counted_structs(reader, _ROW, _ROW_FIELDS, f"{FILE_NAME} row")
    (track_count,) = reader.unpack(_COUNT)
    tracks = [read_counted_structs(reader, _STEP, _STEP_FIELDS, f"{FILE_NAME} step") for _ in range(track_count)]
    if reader.remaining() % U32_SIZE:
        raise ValueError(f"{FILE_NAME} has {reader.remaining()} bytes after the tracks, not whole u32 values")
    unknown = list(reader.unpack(struct.Struct(f"<{reader.remaining() // U32_SIZE}I")))
    return SpecialPassFile(rows, tracks, unknown, read_string_table(data))


def parse_specialpass_records(data: bytes) -> list[dict]:
    """One record per reward step, in file order, with its pass row's fields and texts.

    `step_no` is the step's 1-based position in its track. A step whose
    `pass_key` has no row gets None row fields and empty texts. Raises
    ValueError like `parse_specialpass_file`.
    """
    parsed = parse_specialpass_file(data)
    rows = {
        row[KEY_FIELD]: {
            **row,
            "title_kr": string_at(parsed.strings, row["title_index"]),
            "period_kr": string_at(parsed.strings, row["period_index"]),
            "description_kr": string_at(parsed.strings, row["description_index"]),
        }
        for row in parsed.rows
    }
    return [
        {**rows.get(step[KEY_FIELD], _NO_ROW), **step, "step_no": step_no}
        for track in parsed.tracks
        for step_no, step in enumerate(track, start=1)
    ]

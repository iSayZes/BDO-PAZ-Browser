"""`snowboard.bss`: the Snowfall Crasher snowboard courses and their checkpoints.

    PABR | 56-byte head | u32 course_count | courses | u32 item_count | items
    | u32 effect_count | effects | u32 string_count | strings | u32 table_start | u32 0
    Course: u32 course_key | u32 name_ref | u8 mode | 32 bytes | u32 checkpoint_count | checkpoints
    Checkpoint: u32 checkpoint_index | u32 next_checkpoint_index | 40 bytes | u8 | u8

The menu reads each course with `ToClient_GetSnowBoardStaticStatusByIndex`
(`getKeyRaw()`, `getMode()`, `getName()`, `getCheckPointCount()`). Every
`*_ref` is a string-table index: the course names are Korean, the effect
names `effectbin/<name>.pae` files.

Layout 1 in docs/file-formats/snowboard_bss.md.
"""

from __future__ import annotations

import struct

from _common.pabr_strings import checked_string_table_start, read_string_table, string_at
from _common.record_reader import RecordReader


FILE_NAME = "snowboard.bss"

_HEAD_START = 4
# u16, u32, u32, u32 item key, f32[3], u32 effect_ref, u16 region_key, f32[3], bytes[8], u32.
_HEAD = struct.Struct("<HIII3fIH3f8sI")
_COUNT = struct.Struct("<I")
# course_key, name_ref, mode, f32[3], f32, f32, u32, u32, checkpoint_count.
_COURSE = struct.Struct("<IIB3fffIII")
# checkpoint_index, next_checkpoint_index, f32[3], f32, f32[6], u8, u8.
_CHECKPOINT = struct.Struct("<II3ff6fBB")
# unknown_00, first_effect_ref, second_effect_ref, f32[3], f32[3].
_ITEM = struct.Struct("<III3f3f")
# first_effect_ref, second_effect_ref, f32[3], f32[3], f32[3].
_EFFECT = struct.Struct("<II3f3f3f")


def _read_head(reader: RecordReader, strings: list[str]) -> dict:
    values = reader.unpack(_HEAD)
    head = {
        "unknown_04": values[0],
        "unknown_06": values[1],
        "unknown_0a": values[2],
        "unknown_item_key": values[3],
        "unknown_12": list(values[4:7]),
        "effect_ref": values[7],
        "region_key": values[8],
        "unknown_24": list(values[9:12]),
        "unknown_30": values[12].hex(" "),
        "unknown_38": values[13],
    }
    head["effect_name"] = string_at(strings, head["effect_ref"])
    return head


def _read_checkpoint(reader: RecordReader) -> dict:
    values = reader.unpack(_CHECKPOINT)
    return {
        "checkpoint_index": values[0],
        "next_checkpoint_index": values[1],
        "unknown_08": list(values[2:5]),
        "unknown_14": values[5],
        "unknown_18": list(values[6:12]),
        "unknown_30": values[12],
        "unknown_31": values[13],
    }


def _read_course(reader: RecordReader, strings: list[str]) -> dict:
    values = reader.unpack(_COURSE)
    course = {
        "course_key": values[0],
        "name_ref": values[1],
        "name_kr": string_at(strings, values[1]),
        "mode": values[2],
        "unknown_09": list(values[3:6]),
        "unknown_15": values[6],
        "unknown_19": values[7],
        "unknown_1d": values[8],
        "unknown_21": values[9],
        "checkpoint_count": values[10],
    }
    course["checkpoints"] = [_read_checkpoint(reader) for _ in range(course["checkpoint_count"])]
    return course


def _read_list(reader: RecordReader, item: struct.Struct, what: str) -> list[tuple]:
    """A u32 count, then that many `item` structs as raw value tuples."""
    (count,) = reader.unpack(_COUNT)
    if count * item.size > reader.remaining():
        raise ValueError(f"{FILE_NAME} {what} count {count:,} at 0x{reader.pos - _COUNT.size:X} runs past the end")
    return [reader.unpack(item) for _ in range(count)]


def _item(values: tuple, strings: list[str]) -> dict:
    return {
        "unknown_00": values[0],
        "first_effect_ref": values[1],
        "first_effect_name": string_at(strings, values[1]),
        "second_effect_ref": values[2],
        "second_effect_name": string_at(strings, values[2]),
        "unknown_0c": list(values[3:6]),
        "unknown_18": list(values[6:9]),
    }


def _effect(values: tuple, strings: list[str]) -> dict:
    return {
        "first_effect_ref": values[0],
        "first_effect_name": string_at(strings, values[0]),
        "second_effect_ref": values[1],
        "second_effect_name": string_at(strings, values[1]),
        "unknown_08": list(values[2:5]),
        "unknown_14": list(values[5:8]),
        "unknown_20": list(values[8:11]),
    }


def parse_snowboard(data: bytes) -> dict:
    """The head, the courses with their checkpoints, the items and the effects.

    Raises ValueError on a bad PABR magic or trailer, or when a count runs
    past the string table or the lists stop short of it.
    """
    table_start = checked_string_table_start(data, FILE_NAME)
    strings = read_string_table(data)
    reader = RecordReader(data, _HEAD_START, table_start, FILE_NAME)
    head = _read_head(reader, strings)
    (course_count,) = reader.unpack(_COUNT)
    courses = [_read_course(reader, strings) for _ in range(course_count)]
    items = [_item(values, strings) for values in _read_list(reader, _ITEM, "item")]
    effects = [_effect(values, strings) for values in _read_list(reader, _EFFECT, "effect")]
    if not reader.at_end():
        raise ValueError(f"{FILE_NAME} lists end at 0x{reader.pos:X}, but the string table starts at 0x{table_start:X}")
    return {"head": head, "courses": courses, "items": items, "effects": effects}


def parse_checkpoint_records(data: bytes) -> list[dict]:
    """One record per checkpoint, course by course, with its course's key, name and mode.

    Raises ValueError like `parse_snowboard()`.
    """
    parsed = parse_snowboard(data)
    records: list[dict] = []
    for course in parsed["courses"]:
        course_fields = {key: value for key, value in course.items() if key != "checkpoints"}
        records.extend({**course_fields, **checkpoint} for checkpoint in course["checkpoints"])
    return records

"""`eventmanagement.bss`: the scheduled world events and the event contents they set.

    PABR | u32 event_count | event_count x 15-byte Event Row
    | u32 contents_count | contents_count x 22-byte Contents Row
    | string table | u32 string_table_start | u32 0

Every text of both tables is a string table index (`*_ref`); the records
carry the index and its text. Layout 1 in
docs/file-formats/bss/eventmanagement_bss.md.
"""

from __future__ import annotations

import struct
from typing import NamedTuple

from _common.counted_rows import COUNT_SIZE, read_counted_structs
from _common.pabr_strings import HEADER_SIZE, checked_string_table_start, read_string_table, string_at
from _common.record_reader import RecordReader


FILE_NAME = "eventmanagement.bss"

# Separates the `event_contents_no` values of `setted_event`.
SETTED_EVENT_SEPARATOR = ","

_EVENT_FIELDS = ("event_no", "event_name_ref", "condition_ref", "setted_event_ref", "unknown_0e")
_EVENT_ROW = struct.Struct("<HIIIB")
_CONTENTS_FIELDS = (
    "event_contents_no",
    "function_ref",
    "param_1_ref",
    "param_2_ref",
    "param_3_ref",
    "param_4_ref",
)
_CONTENTS_ROW = struct.Struct("<HIIIII")

# Each string index field and the record field that holds its text.
_EVENT_TEXTS = (
    ("event_name_ref", "event_name"),
    ("condition_ref", "condition"),
    ("setted_event_ref", "setted_event"),
)
_CONTENTS_TEXTS = (
    ("function_ref", "function"),
    ("param_1_ref", "param_1"),
    ("param_2_ref", "param_2"),
    ("param_3_ref", "param_3"),
    ("param_4_ref", "param_4"),
)


class EventManagementTables(NamedTuple):
    events: list[dict]
    contents: list[dict]


def parse_eventmanagement(data: bytes) -> EventManagementTables:
    """Both tables in file order, each string index joined with its text.

    Raises ValueError on a bad magic or trailer, a count the rows cannot
    hold, or rows that do not end where the string table starts.
    """
    rows_end = checked_string_table_start(data, FILE_NAME)
    # The event count sits right after the magic, inside the 8-byte header.
    reader = RecordReader(data, HEADER_SIZE - COUNT_SIZE, rows_end, f"{FILE_NAME} rows")
    events = read_counted_structs(reader, _EVENT_ROW, _EVENT_FIELDS, "event rows")
    contents = read_counted_structs(reader, _CONTENTS_ROW, _CONTENTS_FIELDS, "contents rows")
    if not reader.at_end():
        raise ValueError(f"{FILE_NAME} rows end at 0x{reader.pos:X} but the string table starts at 0x{rows_end:X}")

    strings = read_string_table(data)
    return EventManagementTables(
        [_with_texts(event, _EVENT_TEXTS, strings) for event in events],
        [_with_texts(row, _CONTENTS_TEXTS, strings) for row in contents],
    )


def setted_contents_keys(setted_event: str) -> list[int]:
    """The `event_contents_no` values of a `setted_event` text, in order.

    Raises ValueError on an entry that is not a number.
    """
    entries = [entry.strip() for entry in setted_event.split(SETTED_EVENT_SEPARATOR)]
    try:
        return [int(entry) for entry in entries if entry]
    except ValueError as ex:
        raise ValueError(f"{FILE_NAME}: setted event list {setted_event!r} is not a list of numbers") from ex


def _with_texts(record: dict, texts: tuple[tuple[str, str], ...], strings: list[str]) -> dict:
    return {**record, **{text_field: string_at(strings, record[ref_field]) for ref_field, text_field in texts}}

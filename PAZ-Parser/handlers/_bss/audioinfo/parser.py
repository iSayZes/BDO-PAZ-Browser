"""`audioinfo.bss`: the world's background music and ambience by audio map colour.

    PABR | u32 row_count | row_count x row | 10 x state entry
    | u32 radio_count | radio_count x radio entry
    | u32 unknown_tail_count | unknown_tail_count x u8 unknown_tail
    | String Table | u32 string_table_start | u32 0
    row: u32 color | u32 color_dup | u32 bgm_states[4] | u32 bank_no_environment
    state entry: u8 unknown_00 | u8 unknown_01 | u32 state_group | u32 state_name
    radio entry: u32 unknown_00 | u32 unknown_04 | u32 channel_name | u32 event_name | u8 unknown_10

No field counts the state entries; Layout 6 of
docs/file-formats/audioinfo_bss.md has 10, older clients fewer, and the
parser fails on them when the rest does not end at the string table. Every
string field indexes the string table; the record carries its text as
`<field>_text`. Each record has a `section`: an area row, a state entry or
a radio entry.
"""

from __future__ import annotations

import struct

from _common.binary import u32
from _common.pabr_strings import HEADER_SIZE, checked_string_table_start, read_string_table, string_at
from _common.record_reader import RecordReader
from .bgm_states import BGM_TAIL, bgm_fields


FILE_NAME = "audioinfo.bss"
SECTION_AREA = "area"
SECTION_STATE = "state"
SECTION_RADIO = "radio"
STATE_ENTRY_COUNT = 10

_COUNT_OFFSET = 4
_COLORS = struct.Struct("<II")
_STATE_ENTRY = struct.Struct("<BBII")
_RADIO_ENTRY = struct.Struct("<IIIIB")
_U32 = struct.Struct("<I")


def _read_area(reader: RecordReader, strings: list[str]) -> dict:
    color, color_dup = reader.unpack(_COLORS)
    return {
        "section": SECTION_AREA,
        "color": color,
        "color_dup": color_dup,
        **bgm_fields(reader.unpack(BGM_TAIL), strings),
    }


def _read_state(reader: RecordReader, strings: list[str]) -> dict:
    unknown_00, unknown_01, state_group, state_name = reader.unpack(_STATE_ENTRY)
    return {
        "section": SECTION_STATE,
        "unknown_00": unknown_00,
        "unknown_01": unknown_01,
        "state_group": state_group,
        "state_group_text": string_at(strings, state_group),
        "state_name": state_name,
        "state_name_text": string_at(strings, state_name),
    }


def _read_radio(reader: RecordReader, strings: list[str]) -> dict:
    unknown_00, unknown_04, channel_name, event_name, unknown_10 = reader.unpack(_RADIO_ENTRY)
    return {
        "section": SECTION_RADIO,
        "unknown_00": unknown_00,
        "unknown_04": unknown_04,
        "unknown_04_text": string_at(strings, unknown_04),
        "channel_name": channel_name,
        "channel_name_text": string_at(strings, channel_name),
        "event_name": event_name,
        "event_name_text": string_at(strings, event_name),
        "unknown_10": unknown_10,
    }


def _skip_tail(reader: RecordReader) -> None:
    (count,) = reader.unpack(_U32)
    reader.skip(count)


def parse_audioinfo_records(data: bytes) -> list[dict]:
    """The area rows, then the state entries, then the radio entries, each in file order.

    Raises ValueError on a missing magic, a part that runs into the string
    table, or a tail that does not end where the string table starts.
    """
    table_start = checked_string_table_start(data, FILE_NAME)
    strings = read_string_table(data)
    reader = RecordReader(data, HEADER_SIZE, table_start, FILE_NAME)
    records = [_read_area(reader, strings) for _ in range(u32(data, _COUNT_OFFSET))]
    records += [_read_state(reader, strings) for _ in range(STATE_ENTRY_COUNT)]
    (radio_count,) = reader.unpack(_U32)
    records += [_read_radio(reader, strings) for _ in range(radio_count)]
    _skip_tail(reader)
    if not reader.at_end():
        raise ValueError(f"{FILE_NAME} tail ends at 0x{reader.pos:X}, the string table starts at 0x{table_start:X}")
    return records

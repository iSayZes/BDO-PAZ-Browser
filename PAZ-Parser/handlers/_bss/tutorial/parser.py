"""`tutorial.bss`: the Black Spirit guide steps of the in-game tutorials.

    PABR | u32 row_count | row_count x row | string table | u32 table_start | u32 0
    row: u16 tutorial_index | u16 tutorial_type | u32 start_condition_ref
         | u32 complete_condition_ref | u64 start_event_count
         | u32[start_event_count] start_event_keys
         | u32 title_ref | u32 desc_ref | u32 image_path_ref | u32 base_pos_panel_hash
         | f32[2] pos | f32[2] pan | u32 attr | u8 unknown_start_event_keys_24
         | u8 accept_tutorial_type | bytes[10] unknown_start_event_keys_26
         | u8 use_popup

The `*_ref` fields index the string table; the records hold their text.
`tutorial_type` and `tutorial_index` are the Lua `TutorialKey(type, index)`;
a tutorial runs its steps from index 0 up. Layout 4 in docs/file-formats/bss/tutorial_bss.md.
"""

from __future__ import annotations

import struct

from _common.binary import u32
from _common.pabr_strings import HEADER_SIZE, check_rows_end, checked_string_table_start, read_string_table, string_at
from _common.record_reader import RecordReader


FILE_NAME = "tutorial.bss"

_ROW_COUNT_AT = 4
_HEAD = struct.Struct("<HHIIQ")
_BODY = struct.Struct("<IIII2f2fIBB10sB")
_EVENT_KEY_SIZE = 4


def _read_row(reader: RecordReader, strings: list[str]) -> dict:
    tutorial_index, tutorial_type, start_condition, complete_condition, event_count = reader.unpack(_HEAD)
    if event_count * _EVENT_KEY_SIZE > reader.remaining():
        raise ValueError(f"{FILE_NAME} start event count {event_count:,} at 0x{reader.pos - 8:X} runs past the rows")
    start_event_keys = list(reader.unpack(struct.Struct(f"<{event_count}I")))
    (
        title, desc, image_path, base_pos_panel_hash, pos_x, pos_y, pan_x, pan_y, attr,
        unknown_24, accept_tutorial_type, unknown_26, use_popup,
    ) = reader.unpack(_BODY)
    return {
        "tutorial_type": tutorial_type,
        "tutorial_index": tutorial_index,
        "start_condition": string_at(strings, start_condition),
        "complete_condition": string_at(strings, complete_condition),
        "start_event_keys": start_event_keys,
        "title_kr": string_at(strings, title),
        "desc_kr": string_at(strings, desc),
        "image_path": string_at(strings, image_path),
        "base_pos_panel_hash": base_pos_panel_hash,
        "pos": [pos_x, pos_y],
        "pan": [pan_x, pan_y],
        "attr": attr,
        "unknown_start_event_keys_24": unknown_24,
        "accept_tutorial_type": accept_tutorial_type,
        "unknown_start_event_keys_26": unknown_26.hex(" "),
        "use_popup": use_popup,
    }


def parse_tutorial_records(data: bytes) -> tuple[list[dict], list[str]]:
    """Every step in file order, and the string table.

    Raises ValueError on a bad magic, or when a row runs past or ends before
    the string table.
    """
    rows_end = checked_string_table_start(data, FILE_NAME)
    strings = read_string_table(data)
    reader = RecordReader(data, HEADER_SIZE, rows_end, FILE_NAME)
    records = [_read_row(reader, strings) for _ in range(u32(data, _ROW_COUNT_AT))]
    check_rows_end(data, reader.pos, f"{FILE_NAME} rows")
    return records, strings

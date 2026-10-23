"""`tutorial_startevent.bss`: what a Black Spirit guide step highlights when it starts.

    PABR | u32 row_count | row_count x 101-byte row | String Table
    | u32 string_table_start | u32 0
    row: u32 key | u8 item_where_type | u32 item_key | Highlight black_bg
         | Highlight white_bg | u8 white_ignore | u32 selected_panel_hash
         | Selected Control[5] selected_controls | u8 snapping_effect_on
         | u32 do_lua
    Highlight: u8 use_bg | u32 panel_hash | u32 child_control_hash
               | u32 child_control_index | f32[2] offset
    Selected Control: u32 child_control_hash | u32 child_control_index

Panel and control names are stored as their `ascii_key_hash()`; `do_lua`
indexes the string table. `tutorial.bss` steps name these rows by `key`.
Layout 1 in docs/file-formats/tutorial_startevent_bss.md.
"""

from __future__ import annotations

import struct

from _common.binary import u32
from _common.pabr_strings import HEADER_SIZE, check_rows_end, checked_string_table_start, read_string_table, string_at
from _common.record_reader import RecordReader


FILE_NAME = "tutorial_startevent.bss"
SELECTED_CONTROL_COUNT = 5

_ROW_COUNT_AT = 4
_HEAD = struct.Struct("<IBI")
_HIGHLIGHT = struct.Struct("<BIII2f")
_WHITE_IGNORE_AND_SELECTED_PANEL = struct.Struct("<BI")
_SELECTED_CONTROL = struct.Struct("<II")
_TAIL = struct.Struct("<BI")


def _read_highlight(reader: RecordReader) -> dict:
    use_bg, panel_hash, child_control_hash, child_control_index, offset_x, offset_y = reader.unpack(_HIGHLIGHT)
    return {
        "use_bg": use_bg,
        "panel_hash": panel_hash,
        "child_control_hash": child_control_hash,
        "child_control_index": child_control_index,
        "offset": [offset_x, offset_y],
    }


def _read_selected_control(reader: RecordReader) -> dict:
    child_control_hash, child_control_index = reader.unpack(_SELECTED_CONTROL)
    return {"child_control_hash": child_control_hash, "child_control_index": child_control_index}


def _read_row(reader: RecordReader, strings: list[str]) -> dict:
    key, item_where_type, item_key = reader.unpack(_HEAD)
    black_bg = _read_highlight(reader)
    white_bg = _read_highlight(reader)
    white_ignore, selected_panel_hash = reader.unpack(_WHITE_IGNORE_AND_SELECTED_PANEL)
    selected_controls = [_read_selected_control(reader) for _ in range(SELECTED_CONTROL_COUNT)]
    snapping_effect_on, do_lua = reader.unpack(_TAIL)
    return {
        "key": key,
        "item_where_type": item_where_type,
        "item_key": item_key,
        "black_bg": black_bg,
        "white_bg": white_bg,
        "white_ignore": white_ignore,
        "selected_panel_hash": selected_panel_hash,
        "selected_controls": selected_controls,
        "snapping_effect_on": snapping_effect_on,
        "do_lua": string_at(strings, do_lua),
    }


def parse_tutorial_startevent_records(data: bytes) -> list[dict]:
    """Every start event in file order.

    Raises ValueError on a bad magic, or when the rows do not end where the
    string table starts.
    """
    rows_end = checked_string_table_start(data, FILE_NAME)
    strings = read_string_table(data)
    reader = RecordReader(data, HEADER_SIZE, rows_end, FILE_NAME)
    records = [_read_row(reader, strings) for _ in range(u32(data, _ROW_COUNT_AT))]
    check_rows_end(data, reader.pos, f"{FILE_NAME} rows")
    return records

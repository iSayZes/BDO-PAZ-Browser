"""`edaniaetcoptionstaticstatus.bss`: the Edania options, one row per castle, then six settings.

    PABR | rows | settings (22 bytes) | string table | u32 table_start | u32 0
    Row (71 bytes + list): u32 contents_group_hash | 4 x f32 min AP and DP
        | 2 x (u8 min_item_grade | u32) | u32 tax_rate | u8 | 3 bytes
        | u32 throne_quest | 3 x f32 | u64 tax_base_amount
        | u32 boss_clear_item_key | u8 | u32 count | count x u32 item ID
    Settings: u8 | u8 | u32 | u32 drop_buff_count | u32 drop_buff_rate
        | u32 drop_buff_minutes | u32

The file stores no row count: one row per `__eEdaniaRegion` castle, in enum
order, up to the settings. Full layout in
docs/file-formats/bss/edaniaetcoptionstaticstatus_bss.md.
"""

from __future__ import annotations

import struct

from _common.binary import whole_float
from _common.pabr_strings import checked_string_table_start
from _common.record_reader import RecordReader


FILE_NAME = "edaniaetcoptionstaticstatus.bss"

_VALUES_START = 0x04
_ROW_HEAD = struct.Struct("<I4fBIBIIB3sI3fQIB")
_COUNT = struct.Struct("<I")
_ITEM_ID = struct.Struct("<I")
_SETTINGS = struct.Struct("<BB5I")
_ROW_HEAD_FIELDS = (
    "contents_group_hash",
    "min_ap_1",
    "min_dp_1",
    "min_ap_2",
    "min_dp_2",
    "min_item_grade_1",
    "unknown_15",
    "min_item_grade_2",
    "unknown_1a",
    "tax_rate",
    "unknown_22",
    "unknown_23",
    "throne_quest",
    "unknown_2a",
    "unknown_2e",
    "unknown_32",
    "tax_base_amount",
    "boss_clear_item_key",
    "unknown_42",
)
_SETTINGS_FIELDS = (
    "unknown_rows_00",
    "unknown_rows_01",
    "unknown_rows_02",
    "drop_buff_count",
    "drop_buff_rate",
    "drop_buff_minutes",
    "unknown_rows_12",
)


def _value(raw: object) -> object:
    """A byte run as `71 0b 00` hex text, a float without a trailing `.0`; other numbers as read."""
    if isinstance(raw, bytes):
        return raw.hex(" ")
    return whole_float(raw) if isinstance(raw, float) else raw


def _read_row(reader: RecordReader, edania_region: int) -> dict:
    head = dict(zip(_ROW_HEAD_FIELDS, (_value(raw) for raw in reader.unpack(_ROW_HEAD))))
    (count,) = reader.unpack(_COUNT)
    if count * _ITEM_ID.size > reader.remaining():
        raise ValueError(f"{FILE_NAME} row {edania_region} item count {count:,} runs past the settings")
    item_ids = [reader.unpack(_ITEM_ID)[0] for _ in range(count)]
    return {"edania_region": edania_region, **head, "unknown_item_ids": item_ids}


def parse_etc_option_records(data: bytes) -> list[dict]:
    """One record per castle row, in file order, each with the settings after the rows.

    The row number is the castle's `__eEdaniaRegion` value. Raises ValueError
    on a bad magic or trailer, or when the rows do not end where the
    settings start, 22 bytes before the string table.
    """
    end = checked_string_table_start(data, FILE_NAME)
    rows_end = end - _SETTINGS.size
    if rows_end < _VALUES_START:
        raise ValueError(f"{FILE_NAME} string table offset 0x{end:X} leaves no room for the settings")
    # The rows run up to the settings; a row that does not end there raises in the reader.
    reader = RecordReader(data, _VALUES_START, rows_end, FILE_NAME)
    rows: list[dict] = []
    while not reader.at_end():
        rows.append(_read_row(reader, len(rows)))
    settings = dict(zip(_SETTINGS_FIELDS, _SETTINGS.unpack_from(data, rows_end)))
    return [{**row, **settings} for row in rows]

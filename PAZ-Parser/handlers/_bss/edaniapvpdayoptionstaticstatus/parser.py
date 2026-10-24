"""`edaniapvpdayoptionstaticstatus.bss`: the Edania schedule, three lists of time pairs.

    PABR | ROW_COUNT x Row | u8 unknown_rows_00 | string table
    | u32 table_start | u32 0
    Row: u32 entry_count | entry_count x Entry
    Entry (25 bytes): u8 unknown_00 | 2 x (u32 day_of_week | u32 hour | u32 minute)

Full layout in docs/file-formats/edaniapvpdayoptionstaticstatus_bss.md.
"""

from __future__ import annotations

import struct

from _common.pabr_strings import checked_string_table_start, check_rows_end
from _common.record_reader import RecordReader


FILE_NAME = "edaniapvpdayoptionstaticstatus.bss"
# The file stores no row count; every client checked has three rows.
ROW_COUNT = 3
TIMES_PER_ENTRY = 2

_VALUES_START = 0x04
_COUNT = struct.Struct("<I")
_ENTRY = struct.Struct("<B6I")
_END_FLAG = struct.Struct("<B")


def _read_entries(reader: RecordReader, row: int) -> list[dict]:
    (count,) = reader.unpack(_COUNT)
    if count * _ENTRY.size > reader.remaining():
        raise ValueError(f"{FILE_NAME} row {row} entry count {count:,} runs past the string table")
    entries: list[dict] = []
    for _ in range(count):
        unknown_00, *times = reader.unpack(_ENTRY)
        entries.append({"row": row, "unknown_00": unknown_00, "times": [times[0:3], times[3:6]]})
    return entries


def parse_pvp_day_records(data: bytes) -> list[dict]:
    """One record per entry, in file order, with its row number and the u8 after the rows.

    Raises ValueError on a bad magic or trailer, or when the rows and the u8
    do not end where the string table starts.
    """
    end = checked_string_table_start(data, FILE_NAME)
    reader = RecordReader(data, _VALUES_START, end, FILE_NAME)
    entries = [entry for row in range(ROW_COUNT) for entry in _read_entries(reader, row)]
    (unknown_rows_00,) = reader.unpack(_END_FLAG)
    check_rows_end(data, reader.pos, f"{FILE_NAME} rows")
    return [{**entry, "unknown_rows_00": unknown_rows_00} for entry in entries]

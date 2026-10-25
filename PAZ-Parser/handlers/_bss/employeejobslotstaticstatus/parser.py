"""`employeejobslotstaticstatus.bss`: sailor preset job slots per ship, then an unnamed entry table.

    PABR | u32 record_count | record_count x 18-byte Row | Entry up to table_start
    | u32 0 (empty string table) | u32 table_start | u32 0
    Row:   u16 character_key | u16[8] job_slot_counts
    Entry: u16 unknown_00 | u8 unknown_02

No count gives the number of entries; they run up to the string table.
Layout 1 in docs/file-formats/bss/employeejobslotstaticstatus_bss.md.
"""

from __future__ import annotations

import struct
from typing import NamedTuple

from _common.binary import u32
from _common.pabr_strings import HEADER_SIZE, checked_string_table_start


FILE_NAME = "employeejobslotstaticstatus.bss"
JOB_COUNT = 8

_COUNT_OFFSET = 4
_ROW = struct.Struct(f"<H{JOB_COUNT}H")
_ENTRY = struct.Struct("<HB")


class JobSlotFile(NamedTuple):
    rows: list[dict]
    entries: list[dict]


def parse_employeejobslot_file(data: bytes) -> JobSlotFile:
    """The ship rows and the entries after them.

    Raises ValueError on a bad magic or trailer, rows that run past the
    string table, or entries that do not fill the space up to it.
    """
    end = checked_string_table_start(data, FILE_NAME)
    rows_end = HEADER_SIZE + u32(data, _COUNT_OFFSET) * _ROW.size
    if rows_end > end:
        raise ValueError(f"{FILE_NAME} rows end at 0x{rows_end:X}, past the string table at 0x{end:X}")
    if (end - rows_end) % _ENTRY.size:
        raise ValueError(f"{FILE_NAME} entries from 0x{rows_end:X} do not fill the space up to 0x{end:X}")

    rows = []
    for character_key, *counts in _ROW.iter_unpack(data[HEADER_SIZE:rows_end]):
        rows.append({"character_key": character_key, "job_slot_counts": counts})
    entries = [
        {"unknown_00": unknown_00, "unknown_02": unknown_02}
        for unknown_00, unknown_02 in _ENTRY.iter_unpack(data[rows_end:end])
    ]
    return JobSlotFile(rows, entries)

"""`cashproduct_instant.bss`: the cost to finish a timed task at once, per remaining time.

    PABR | INSTANT_TYPE_COUNT x group | string table | u32 table_start | u32 0
    group: u8 unknown_00 | u64 entry_count | entry_count x entry
    entry: u16 minute | bytes[6] padding_02 | i64 pearl_count

The groups follow `CppEnums.InstantCashType` in order; the file stores no
group count. An entry is the 2016 `gc::InstantCashItem::value_type`, its
padding left as the server wrote it. Layout 1 in
docs/file-formats/cashproduct_instant_bss.md.
"""

from __future__ import annotations

import struct

from _common.pabr_strings import HEADER_SIZE, checked_string_table_start
from _common.record_reader import RecordReader


FILE_NAME = "cashproduct_instant.bss"
# CppEnums.InstantCashType, without the `eInstant_` prefix; eInstant_Count is 4.
INSTANT_TYPE_NAMES = (
    "ChangeHouseUseType",
    "CompleteServantMating",
    "CompleteNpcWorking",
    "CompleteNpcWorkerUpgrade",
)
INSTANT_TYPE_COUNT = len(INSTANT_TYPE_NAMES)
# The PABR magic only: the groups start where other PABR files keep their row count.
GROUPS_START = HEADER_SIZE - 4

_GROUP_HEAD = struct.Struct("<BQ")
_ENTRY = struct.Struct("<H6sq")


def parse_cashproduct_instant_records(data: bytes) -> list[dict]:
    """One record per entry, group by group, in file order.

    Raises ValueError on a bad PABR magic or trailer, or when the groups do
    not end where the string table starts.
    """
    end = checked_string_table_start(data, FILE_NAME)
    reader = RecordReader(data, GROUPS_START, end, FILE_NAME)
    records = []
    for instant_type in range(INSTANT_TYPE_COUNT):
        unknown_00, entry_count = reader.unpack(_GROUP_HEAD)
        if entry_count * _ENTRY.size > reader.remaining():
            raise ValueError(f"{FILE_NAME} group {instant_type} declares {entry_count:,} entries past the rows")
        for _ in range(entry_count):
            minute, padding, pearl_count = reader.unpack(_ENTRY)
            records.append(
                {
                    "instant_type": instant_type,
                    "unknown_00": unknown_00,
                    "minute": minute,
                    "padding_02": padding.hex(),
                    "pearl_count": pearl_count,
                }
            )
    if not reader.at_end():
        raise ValueError(f"{FILE_NAME} groups end at 0x{reader.pos:X}, the string table starts at 0x{end:X}")
    return records

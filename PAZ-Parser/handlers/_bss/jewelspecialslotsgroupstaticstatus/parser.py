"""`jewelspecialslotsgroupstaticstatus.bss`: crystal groups per special preset slot.

    PABR | u32 count | count x row | string table
    | u32 string_table_start | u32 0

    row: u8 slot | u32 group_count | group_count x u16 group

The groups are `jewelgroupstaticstatus.bss` group numbers. Layout in
docs/file-formats/jewelspecialslotsgroupstaticstatus_bss.md.
"""

from __future__ import annotations

import struct

from _common.binary import u32
from _common.pabr_strings import HEADER_SIZE, checked_string_table_start
from _common.record_reader import RecordReader


FILE_NAME = "jewelspecialslotsgroupstaticstatus.bss"
# The row count follows the PABR magic.
_COUNT_OFFSET = 4

# u8 slot | u32 group_count
_ROW_HEAD = struct.Struct("<BI")


def _read_row(reader: RecordReader) -> dict:
    slot, group_count = reader.unpack(_ROW_HEAD)
    groups = list(reader.unpack(struct.Struct(f"<{group_count}H")))
    return {"slot": slot, "groups": groups}


def parse_special_slot_records(data: bytes) -> list[dict]:
    """Every slot row in file order.

    Raises ValueError on a bad magic, when a row runs into the string table,
    or when the rows end before it: then the layout has changed.
    """
    rows_end = checked_string_table_start(data, FILE_NAME)
    reader = RecordReader(data, HEADER_SIZE, rows_end, f"{FILE_NAME} rows")
    records = [_read_row(reader) for _ in range(u32(data, _COUNT_OFFSET))]
    if not reader.at_end():
        raise ValueError(f"{FILE_NAME} rows end {reader.remaining()} bytes before the string table")
    return records

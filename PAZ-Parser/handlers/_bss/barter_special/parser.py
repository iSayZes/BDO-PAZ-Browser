"""`barter_special.bss`: the special barter offers, one 70-byte row each.

    PABR | u32 row_count | row_count x row | u32 0 (empty string table)
    | u32 string_table_start | u32 0
    row: u16 barter_region_key | u32 select_rate | 56-byte Exchange
         | u32 barter_sub_group | u32 barter_category (bit mask)

Full layout in docs/file-formats/bss/barter_special_bss.md; the Exchange is read
by `_bss/barter/exchange.py`.
"""

from __future__ import annotations

import struct

from _bss.barter.exchange import read_exchange
from _common.pabr_strings import HEADER_SIZE, fixed_row_offsets

FILE_NAME = "barter_special.bss"
ROW_SIZE = 70

_HEAD = struct.Struct("<HI")
_EXCHANGE = 0x06
_TAIL = struct.Struct("<II")
_TAIL_OFFSET = 0x3E


def parse_barter_special_records(data: bytes) -> list[dict]:
    """Every row in file order, with `index` its place in the file from 1.

    Raises ValueError on a missing magic or rows that do not end where the
    trailer says the string table starts.
    """
    records = []
    for pos in fixed_row_offsets(data, ROW_SIZE, FILE_NAME):
        barter_region_key, select_rate = _HEAD.unpack_from(data, pos)
        barter_sub_group, barter_category = _TAIL.unpack_from(data, pos + _TAIL_OFFSET)
        records.append({
            "index": (pos - HEADER_SIZE) // ROW_SIZE + 1,
            "barter_region_key": barter_region_key,
            "select_rate": select_rate,
            **read_exchange(data, pos + _EXCHANGE),
            "barter_sub_group": barter_sub_group,
            "barter_category": barter_category,
        })
    return records

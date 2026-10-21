"""`eventcategory.dbss`: the pearl shop discount events of the event cart.

    u32 count | count x Row
    Row: u16 index | i16 cash_coupon_category_main | i16 cash_coupon_category_middle
         | i16 cash_coupon_category_small | str16 discount_start_period
         | str16 discount_end_period | u8 unknown_discount_end_period_00
         | 10 x (i64 discount_ceiling, i64 discount_price) | u8 unknown_discount_end_period_a1
         | i64 max_discount_pearl | u8 event_type

`eventcategoryoffset.dbss` (u32 count, then u16 index, offset and size per
row) points at the row start with the whole row's size. Layout 1 in
docs/file-formats/eventcategory_dbss.md.
"""

from __future__ import annotations

import struct

from _common.binary import u32
from _common.pabr_offset import PabrOffsetRow, parse_bare_offset_rows
from _common.record_reader import RecordReader


FILE_NAME = "eventcategory.dbss"
OFFSET_FILE = "eventcategoryoffset.dbss"
KEY_FIELD = "index"

DISCOUNT_STEP_COUNT = 10
_COUNT_SIZE = 4
_HEAD = struct.Struct("<Hhhh")
_U8 = struct.Struct("<B")
_STEPS = struct.Struct(f"<{DISCOUNT_STEP_COUNT * 2}q")
_TAIL = struct.Struct("<BqB")


def _read_row(reader: RecordReader) -> dict:
    key, category_main, category_middle, category_small = reader.unpack(_HEAD)
    start = reader.text(wide=True)
    end = reader.text(wide=True)
    (unknown_discount_end_period_00,) = reader.unpack(_U8)
    steps = reader.unpack(_STEPS)
    unknown_discount_end_period_a1, max_discount_pearl, event_type = reader.unpack(_TAIL)
    return {
        KEY_FIELD: key,
        "cash_coupon_category_main": category_main,
        "cash_coupon_category_middle": category_middle,
        "cash_coupon_category_small": category_small,
        "discount_start_period": start,
        "discount_end_period": end,
        "unknown_discount_end_period_00": unknown_discount_end_period_00,
        "discount_steps": [
            {"discount_ceiling": steps[i], "discount_price": steps[i + 1]}
            for i in range(0, len(steps), 2)
        ],
        "unknown_discount_end_period_a1": unknown_discount_end_period_a1,
        "max_discount_pearl": max_discount_pearl,
        "event_type": event_type,
    }


def parse_eventcategory_records(data: bytes) -> list[dict]:
    """Every row in file order.

    Raises ValueError when a row runs past the file or the rows do not end at
    its last byte.
    """
    if len(data) < _COUNT_SIZE:
        raise ValueError(f"{FILE_NAME} is too short to hold its row count")

    reader = RecordReader(data, _COUNT_SIZE, len(data), FILE_NAME)
    records = [_read_row(reader) for _ in range(u32(data, 0))]
    if not reader.at_end():
        raise ValueError(f"{FILE_NAME} has {reader.remaining():,} bytes after its last row")
    return records


def parse_eventcategoryoffset_rows(data: bytes) -> list[PabrOffsetRow]:
    """Every index row. Raises ValueError on a count the file cannot hold."""
    return parse_bare_offset_rows(data)

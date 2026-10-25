"""`coupon.dbss`: the Pearl Shop discount coupons.

    u32 count | count x row
    row: u16 coupon_key | u8 unknown_02 | u64 max_discount_pearl
         | u64 min_product_pearl | str16 name_kr | u32 expiration_days
         | u32 discount_rate | u64 discount_pearl | str16 icon_path
         | str16 category_expression_kr | u16 category_main
         | u16 category_middle | u16 category_small
         | u32 unknown_category_expression_kr_06

`couponoffset.dbss` (u32 count, then u16 key, u32 offset and u32 size per
row, no PABR magic) points at the row start. The category keys are
`cashproductcategory.dbss` keys, `65535` where the coupon stops at a higher
level. Layout 1 in docs/file-formats/dbss/coupon_dbss.md.
"""

from __future__ import annotations

import struct

from _common.counted_rows import read_counted_records
from _common.pabr_offset import PabrOffsetRow, parse_bare_offset_rows
from _common.record_reader import RecordReader


FILE_NAME = "coupon.dbss"
OFFSET_FILE = "couponoffset.dbss"
KEY_FIELD = "coupon_key"
# A category level the coupon does not narrow down to.
NO_CATEGORY = 0xFFFF

_HEAD = struct.Struct("<HBqq")
_DISCOUNT = struct.Struct("<IIq")
_CATEGORY = struct.Struct("<HHHI")


def _read_row(reader: RecordReader) -> dict:
    coupon_key, unknown_02, max_discount_pearl, min_product_pearl = reader.unpack(_HEAD)
    name_kr = reader.text(wide=True)
    expiration_days, discount_rate, discount_pearl = reader.unpack(_DISCOUNT)
    icon_path = reader.text(wide=True)
    category_expression_kr = reader.text(wide=True)
    category_main, category_middle, category_small, unknown_06 = reader.unpack(_CATEGORY)
    return {
        KEY_FIELD: coupon_key,
        "unknown_02": unknown_02,
        "max_discount_pearl": max_discount_pearl,
        "min_product_pearl": min_product_pearl,
        "name_kr": name_kr,
        "expiration_days": expiration_days,
        "discount_rate": discount_rate,
        "discount_pearl": discount_pearl,
        "icon_path": icon_path,
        "category_expression_kr": category_expression_kr,
        "category_main": category_main,
        "category_middle": category_middle,
        "category_small": category_small,
        "unknown_category_expression_kr_06": unknown_06,
    }


def parse_coupon_records(data: bytes) -> list[dict]:
    """Every coupon in file order. Raises ValueError when a row runs past the file or the rows end early."""
    return read_counted_records(data, _read_row, FILE_NAME)


def parse_couponoffset_rows(data: bytes) -> list[PabrOffsetRow]:
    """Every index row: coupon key, row offset and row size. Raises ValueError on a count the file cannot hold."""
    return parse_bare_offset_rows(data)

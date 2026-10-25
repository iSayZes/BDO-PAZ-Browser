"""`purchaselimitgroup.dbss`: Pearl Shop purchase limits shared by a group of products.

A u32 row count, then 9-byte rows packed with no padding: the u32 group
number, the u8 limit type (`CppEnums.CashPurchaseLimitType`) and the i32
number of purchases the group allows. `purchaselimitgroupoffset.dbss`
points at the start of each row. Layout 1 in
docs/file-formats/dbss/purchaselimitgroup_dbss.md.
"""

from __future__ import annotations

import struct


FILE_NAME = "purchaselimitgroup.dbss"
OFFSET_FILE = "purchaselimitgroupoffset.dbss"

_COUNT = struct.Struct("<I")
# group_no, purchase_type, purchase_count
_ROW = struct.Struct("<IBi")
ROW_SIZE = _ROW.size


def parse_purchaselimitgroup_records(data: bytes) -> list[dict]:
    """Every row, in file order.

    Raises ValueError when the file is not the row count followed by exactly
    that many rows.
    """
    if len(data) < _COUNT.size:
        raise ValueError(f"{FILE_NAME} is too short to hold its row count")

    (count,) = _COUNT.unpack_from(data, 0)
    expected = _COUNT.size + count * ROW_SIZE
    if len(data) != expected:
        raise ValueError(f"{count:,} rows of {ROW_SIZE} bytes need {expected:,} bytes, the file has {len(data):,}")

    return [
        {"group_no": group_no, "purchase_type": purchase_type, "purchase_count": purchase_count}
        for group_no, purchase_type, purchase_count in _ROW.iter_unpack(data[_COUNT.size :])
    ]

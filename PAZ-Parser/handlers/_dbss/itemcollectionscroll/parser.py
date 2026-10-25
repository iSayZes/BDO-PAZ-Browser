"""`itemcollectionscroll.dbss`: the levels of the Item Collection Increase gauge.

A u32 row count, then 16-byte rows: the u32 gauge level (`grade`), then the
Item Drop Rate bonus, the Item Drop Amount bonus and the charged time used
per real second, each an i32 on the 1,000,000 = 100% scale.
`itemcollectionscrolloffset.dbss` points at the start of each row. Layout 1
in docs/file-formats/dbss/itemcollectionscroll_dbss.md.
"""

from __future__ import annotations

import struct


FILE_NAME = "itemcollectionscroll.dbss"
OFFSET_FILE = "itemcollectionscrolloffset.dbss"

_COUNT = struct.Struct("<I")
# grade, drop_rate, count_rate, cost_percent
_ROW = struct.Struct("<Iiii")
ROW_SIZE = _ROW.size


def parse_itemcollectionscroll_records(data: bytes) -> list[dict]:
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
        {"grade": grade, "drop_rate": drop_rate, "count_rate": count_rate, "cost_percent": cost_percent}
        for grade, drop_rate, count_rate, cost_percent in _ROW.iter_unpack(data[_COUNT.size :])
    ]

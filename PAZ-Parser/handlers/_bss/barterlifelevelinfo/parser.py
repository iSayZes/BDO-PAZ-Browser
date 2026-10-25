"""`barterlifelevelinfo.bss`: the parley discount per Barter level.

    PABR | u32 count | count x (u32 level, u32 discount_point)
    | u32 0 (empty string table) | u32 string_table_start | u32 0

`discount_point` is in units of 0.0001% (`CppDefine.e1Percent` = 10000).
Full layout in docs/file-formats/bss/barterlifelevelinfo_bss.md.
"""

from __future__ import annotations

import struct

from _common.pabr_strings import fixed_row_offsets


FILE_NAME = "barterlifelevelinfo.bss"
# `CppDefine.e1Percent`: discount points per 1%.
DISCOUNT_POINTS_PER_PERCENT = 10_000

_ROW = struct.Struct("<II")  # level, discount_point


def parse_barterlifelevelinfo_records(data: bytes) -> list[dict]:
    """Every level row in file order.

    Raises ValueError on a missing magic or a row count that does not end
    where the trailer says the string table starts.
    """
    records = []
    for pos in fixed_row_offsets(data, _ROW.size, FILE_NAME):
        level, discount_point = _ROW.unpack_from(data, pos)
        records.append({"level": level, "discount_point": discount_point})
    return records

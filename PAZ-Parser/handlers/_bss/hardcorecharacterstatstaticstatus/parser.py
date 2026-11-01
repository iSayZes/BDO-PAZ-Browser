"""`hardcorecharacterstatstaticstatus.bss`: the stat body per class type.

    PABR | row* | string table | u32 string_table_start | u32 0
    row = u8 class_type | 200-byte stat body

There is no row count: the rows fill the space up to the string table. The
stat body is the one of `experience.bss` level records (`_bss/experience/
stat_body.py`). Layout in docs/file-formats/bss/hardcorecharacterstatstaticstatus_bss.md.
"""

from __future__ import annotations

import struct

from _bss.experience.stat_body import STAT_BODY, STAT_BODY_SIZE, stat_fields
from _common.pabr_strings import checked_string_table_start


FILE_NAME = "hardcorecharacterstatstaticstatus.bss"
FIRST_ROW = 0x04
_CLASS_TYPE = struct.Struct("<B")
ROW_SIZE = _CLASS_TYPE.size + STAT_BODY_SIZE


def parse_hardcore_stat_records(data: bytes) -> list[dict]:
    """Every row in file order.

    Raises ValueError on a missing magic, when the rows do not fill the space
    before the string table, or when a row's class type is not its index.
    """
    rows_end = checked_string_table_start(data, FILE_NAME)
    if rows_end < FIRST_ROW or (rows_end - FIRST_ROW) % ROW_SIZE:
        raise ValueError(
            f"{FILE_NAME} string table starts at 0x{rows_end:X}, "
            f"not after whole {ROW_SIZE}-byte rows from 0x{FIRST_ROW:X}"
        )
    records: list[dict] = []
    for index, offset in enumerate(range(FIRST_ROW, rows_end, ROW_SIZE)):
        (class_type,) = _CLASS_TYPE.unpack_from(data, offset)
        if class_type != index:
            raise ValueError(f"{FILE_NAME} row {index} holds class type {class_type}")
        body = STAT_BODY.unpack_from(data, offset + _CLASS_TYPE.size)
        records.append({"class_type": class_type, **stat_fields(body)})
    return records

"""`skillquickslotinfo.bss`: the skills of each class's quick slots 0 to 19.

    PABR | Class Rows up to table_start | string table
    | u32 table_start | u32 0
    Class Row (80 bytes): 20 x (u16 skill_no | u16 unknown_02)

No row count: the rows run to the string table, one per class type from `0`
(`80` bytes each). An empty slot is all zero. Full layout in
docs/file-formats/skillquickslotinfo_bss.md.
"""

from __future__ import annotations

import struct

from _common.pabr_strings import checked_string_table_start


FILE_NAME = "skillquickslotinfo.bss"
# pa::Array<gc::QuickSlot::value_type, 20> in the 2016 gc::QuickSlot.
SLOT_COUNT = 20

_SLOT = struct.Struct("<HH")
CLASS_ROW_SIZE = SLOT_COUNT * _SLOT.size
_ROWS_AT = 4


def parse_skillquickslotinfo(data: bytes) -> list[dict]:
    """One record per filled slot, class row by class row, in slot order.

    `class_type` is the row's index and `slot` the slot's index in it. Raises
    ValueError on a bad magic or when the rows do not fill the space before
    the string table.
    """
    rows_end = checked_string_table_start(data, FILE_NAME)
    row_bytes = rows_end - _ROWS_AT
    if row_bytes % CLASS_ROW_SIZE:
        raise ValueError(f"{FILE_NAME} rows take {row_bytes:,} bytes, not a whole number of {CLASS_ROW_SIZE}-byte rows")

    records: list[dict] = []
    for class_type in range(row_bytes // CLASS_ROW_SIZE):
        row_start = _ROWS_AT + class_type * CLASS_ROW_SIZE
        for slot in range(SLOT_COUNT):
            skill_no, unknown_02 = _SLOT.unpack_from(data, row_start + slot * _SLOT.size)
            if skill_no or unknown_02:
                records.append({"class_type": class_type, "slot": slot, "skill_no": skill_no, "unknown_02": unknown_02})
    return records

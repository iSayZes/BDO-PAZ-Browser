"""`skillfusionslotlist.bss`: the Skill Enhancement choices of each class, slot by slot.

    PABR | Class Rows up to table_start | string table
    | u32 table_start | u32 0
    Class Row: 5 x Slot
    Slot: u32 skill_fusion_key_count | skill_fusion_key_count x u32 skill_fusion_key

No row count: the rows run to the string table, one per class type from `0`.
Each key is a `skillfusion.dbss` key, a skill key `skill_no << 16 | level`.
Full layout in docs/file-formats/skillfusionslotlist_bss.md.
"""

from __future__ import annotations

from _common.counted_rows import read_counted_u32s
from _common.pabr_strings import checked_string_table_start
from _common.record_reader import RecordReader


FILE_NAME = "skillfusionslotlist.bss"
SLOT_COUNT = 5
# Right after the PABR magic: the file has no row count.
_ROWS_AT = 4


def parse_skillfusionslotlist(data: bytes) -> list[dict]:
    """One record per slot that holds keys: `class_type`, `slot` and `skill_fusion_keys`.

    Raises ValueError on a bad magic, or when a list runs past the string
    table or the last class row ends before it.
    """
    rows_end = checked_string_table_start(data, FILE_NAME)
    reader = RecordReader(data, _ROWS_AT, rows_end, FILE_NAME)
    records: list[dict] = []
    class_type = 0
    while not reader.at_end():
        for slot in range(SLOT_COUNT):
            keys = read_counted_u32s(reader, f"{FILE_NAME} class {class_type} slot {slot}")
            if keys:
                records.append({"class_type": class_type, "slot": slot, "skill_fusion_keys": keys})
        class_type += 1
    return records

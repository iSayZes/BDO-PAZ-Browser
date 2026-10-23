"""`privateskill.bss`: the active and passive skills and the classes that learn them.

    PABR | u32 active_count | active_count x Row | u32 passive_count
    | passive_count x Row | string table | u32 table_start | u32 0
    Row: u32 skill_key | u64 class_mask

`class_mask` has bit `n` set for class type `n`. Layout 2 in
docs/file-formats/privateskill_bss.md; the 36-byte rows of Layout 1
(clients before 1267) are not read.
"""

from __future__ import annotations

import struct

from _common.counted_rows import read_counted_structs
from _common.pabr_offset import PABR_MAGIC
from _common.pabr_strings import checked_string_table_start
from _common.record_reader import RecordReader


FILE_NAME = "privateskill.bss"
# The skillsimply.dbss `kind` of every key in each list, in file order.
ACTIVE_KIND = 1
PASSIVE_KIND = 2
LIST_KINDS = {"active": ACTIVE_KIND, "passive": PASSIVE_KIND}

_ROW = struct.Struct("<IQ")
_ROW_FIELDS = ("skill_key", "class_mask")


def parse_privateskill_records(data: bytes) -> list[dict]:
    """Every row, the active list then the passive list, each with the list's `kind`.

    Raises ValueError on a bad PABR magic or trailer, a count that runs past
    the rows, or rows that do not end where the string table starts.
    """
    end = checked_string_table_start(data, FILE_NAME)
    reader = RecordReader(data, len(PABR_MAGIC), end, FILE_NAME)
    records = [
        {**row, "kind": kind}
        for list_name, kind in LIST_KINDS.items()
        for row in read_counted_structs(reader, _ROW, _ROW_FIELDS, f"{FILE_NAME} {list_name}_count")
    ]
    if not reader.at_end():
        raise ValueError(f"{FILE_NAME} rows end at 0x{reader.pos:X}, the string table starts at 0x{end:X}")
    return records

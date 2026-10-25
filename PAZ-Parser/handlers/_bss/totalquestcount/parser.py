"""`totalquestcountregion.bss` and `totalquestcounttype.bss`: quests per category.

    PABR | u32 quest_count per value | u32 string_count (0) | u32 table_start | u32 0

No count is stored: the array runs up to the string table. Value N of the
region file counts the quests of `eQuestRegionType` N, value N of the type
file the quests of `__eQuestType` N. Full layout in
docs/file-formats/bss/totalquestcountregion_bss.md.
"""

from __future__ import annotations

import struct

from _common.pabr_strings import checked_string_table_start


FIRST_VALUE = 0x04
_U32 = struct.Struct("<I")


def parse_quest_counts(data: bytes, file_name: str) -> list[int]:
    """The quest count of every enum value, in value order.

    Raises ValueError on a missing magic, a trailer outside the file, or an
    array end that leaves part of a u32 before the string table.
    """
    table_start = checked_string_table_start(data, file_name)
    if (table_start - FIRST_VALUE) % _U32.size:
        raise ValueError(
            f"{file_name} string table starts at 0x{table_start:X}, "
            f"not after whole u32 values from 0x{FIRST_VALUE:X}"
        )
    return [count for (count,) in _U32.iter_unpack(data[FIRST_VALUE:table_start])]

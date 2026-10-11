"""`traininglevelskillstat.bss`: the two mount bonuses a Training level gives.

    PABR | entry per level, from level 1 | u32 0 (empty string table)
    | u32 string_table_start | u32 0

    entry: u32 add_vehicle_skill_owner_rate | u32 add_servant_stat_rate

The layout of `commonlifestatdata.bss` with 8-byte entries. Rates use
1,000,000 = 100%. Full layout in docs/file-formats/traininglevelskillstat_bss.md.
"""

from __future__ import annotations

import struct

from _bss.commonlifestatdata.parser import parse_level_entries

_FILE_NAME = "traininglevelskillstat.bss"
_ENTRY = struct.Struct("<II")


def parse_traininglevelskillstat_records(data: bytes) -> list[dict]:
    """One record per Training level.

    Raises ValueError on a missing magic or when the entries do not fill the
    space before the string table.
    """
    return [
        {
            "level": level,
            "add_vehicle_skill_owner_rate": skill_rate,
            "add_servant_stat_rate": stat_rate,
        }
        for level, (skill_rate, stat_rate) in parse_level_entries(data, _ENTRY, _FILE_NAME)
    ]

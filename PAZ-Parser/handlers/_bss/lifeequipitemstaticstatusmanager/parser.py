"""`lifeequipitemstaticstatusmanager.bss`: the buff effect types of each Life Skill tab.

    PABR | Life Stat List[..table_start] life_stat_lists | u32 string_count | strings | u32 table_start | u32 0
    Life Stat List: u32 effect_type_count | effect_type_count x u8 effect_type

The lists have no count: they run up to the string table, which holds no
strings, and list `n` is `__ePlayerLifeStatType` `n` (`0` Collecting to
`9` Sail, empty lists up to `14`). Each value is a `buff.dbss` effect type.

Layout 1 in docs/file-formats/bss/lifeequipitemstaticstatusmanager_bss.md.
"""

from __future__ import annotations

import struct

from _common.counted_rows import read_counted_structs
from _common.pabr_strings import checked_string_table_start
from _common.record_reader import RecordReader


FILE_NAME = "lifeequipitemstaticstatusmanager.bss"

# The lists follow the PABR magic.
_LISTS_START = 4
_EFFECT_TYPE = struct.Struct("<B")
_EFFECT_TYPE_FIELDS = ("effect_type",)


def parse_life_stat_lists(data: bytes) -> list[list[int]]:
    """The effect types of every life stat type, in type order (list `n` is type `n`).

    Raises ValueError on a bad PABR magic or trailer, or when a count runs
    past the string table.
    """
    table_start = checked_string_table_start(data, FILE_NAME)
    reader = RecordReader(data, _LISTS_START, table_start, FILE_NAME)
    lists: list[list[int]] = []
    while not reader.at_end():
        what = f"{FILE_NAME} life stat type {len(lists)} effect type"
        entries = read_counted_structs(reader, _EFFECT_TYPE, _EFFECT_TYPE_FIELDS, what)
        lists.append([entry["effect_type"] for entry in entries])
    return lists


def parse_life_equip_records(data: bytes) -> list[dict]:
    """One record per effect type, life stat type by life stat type, in list order.

    Raises ValueError like `parse_life_stat_lists()`.
    """
    return [
        {"life_stat_type": life_stat_type, "effect_index": effect_index, "effect_type": effect_type}
        for life_stat_type, effect_types in enumerate(parse_life_stat_lists(data))
        for effect_index, effect_type in enumerate(effect_types)
    ]

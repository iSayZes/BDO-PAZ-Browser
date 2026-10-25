"""`classcooltimeuilist.bss`: the skills of the skill cooldown slot window, per class type.

    PABR | Class List[..table_start] class_lists | u32 string_count | strings | u32 table_start | u32 0
    Class List: u32 skill_count | skill_count x (u16 show_type | u16 skill_no)

The lists have no count: they run up to the string table, which holds no
strings, and list `n` is class type `n`
(`ToClient_getSkillCoolTimeUIListCount`, `..._SkillNo(idx)` and
`..._ShowType(idx)` read the list of the player's class).

Layout 1 in docs/file-formats/bss/classcooltimeuilist_bss.md.
"""

from __future__ import annotations

import struct

from _common.counted_rows import read_counted_structs
from _common.pabr_strings import checked_string_table_start
from _common.record_reader import RecordReader


FILE_NAME = "classcooltimeuilist.bss"

# The lists follow the PABR magic.
_LISTS_START = 4
_SKILL = struct.Struct("<HH")
_SKILL_FIELDS = ("show_type", "skill_no")


def parse_class_lists(data: bytes) -> list[list[dict]]:
    """The skill list of every class type, in class type order (list `n` is class type `n`).

    Raises ValueError on a bad PABR magic or trailer, or when a skill count
    runs past the string table.
    """
    table_start = checked_string_table_start(data, FILE_NAME)
    reader = RecordReader(data, _LISTS_START, table_start, FILE_NAME)
    lists: list[list[dict]] = []
    while not reader.at_end():
        what = f"{FILE_NAME} class type {len(lists)} skill"
        lists.append(read_counted_structs(reader, _SKILL, _SKILL_FIELDS, what))
    return lists


def parse_cooltime_records(data: bytes) -> list[dict]:
    """One record per skill, class type by class type; `skill_index` is the getters' `idx`.

    Raises ValueError like `parse_class_lists()`.
    """
    return [
        {"class_type": class_type, "skill_index": skill_index, **skill}
        for class_type, skills in enumerate(parse_class_lists(data))
        for skill_index, skill in enumerate(skills)
    ]

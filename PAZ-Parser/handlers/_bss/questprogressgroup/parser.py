"""`questprogressgroup.bss`: groups of quest chains, each chain with its final quest.

    PABR | u32 count | count x group | string table | u32 string_table_start | u32 0

    group: u32 group_key | u32 quest_count | quest_count x entry
    entry: u32 group_key | u16 quest_chain_id | u16 quest_id | u16 final_quest_id

Each entry repeats its group's key. The string table is empty. Layout in
docs/file-formats/questprogressgroup_bss.md.
"""

from __future__ import annotations

import struct

from _common.binary import u32
from _common.pabr_strings import HEADER_SIZE, check_rows_end, checked_string_table_start


FILE_NAME = "questprogressgroup.bss"

# u32 group_key | u32 quest_count
GROUP_HEAD = struct.Struct("<II")
# u32 group_key | u16 quest_chain_id | u16 quest_id | u16 final_quest_id
ENTRY = struct.Struct("<IHHH")


def parse_questprogressgroup_records(data: bytes) -> list[dict]:
    """One record per entry, in file order. `group_key` is the entry's own copy.

    Raises ValueError on a bad magic, a group that runs past the string
    table, or groups that do not end where the string table starts.
    """
    end = checked_string_table_start(data, FILE_NAME)
    count = u32(data, 4)
    pos = HEADER_SIZE
    records: list[dict] = []
    for index in range(count):
        if pos + GROUP_HEAD.size > end:
            raise ValueError(f"{FILE_NAME} group {index} at 0x{pos:X} runs past the string table")
        group_key, quest_count = GROUP_HEAD.unpack_from(data, pos)
        pos += GROUP_HEAD.size
        if pos + quest_count * ENTRY.size > end:
            raise ValueError(f"{FILE_NAME} group {group_key} lists {quest_count} quests past the string table")
        for _ in range(quest_count):
            entry_group_key, quest_chain_id, quest_id, final_quest_id = ENTRY.unpack_from(data, pos)
            pos += ENTRY.size
            records.append({
                "group_key": entry_group_key,
                "quest_chain_id": quest_chain_id,
                "quest_id": quest_id,
                "final_quest_id": final_quest_id,
            })
    check_rows_end(data, pos, f"{FILE_NAME} groups")
    return records

"""`branchquest.bss`: the crossroad quest groups.

    PABR | u32 group_count | group_count x group
    | string table (empty) | u32 string_table_start | u32 0

    group: u32 row_count | row_count x row
    row:   u32 group_key | u16 quest_chain_id | u16 quest_id | u8 is_root_quest

Layout in docs/file-formats/bss/branchquest_bss.md.
"""

from __future__ import annotations

import struct
from typing import TypedDict

from _common.binary import u32
from _common.pabr_strings import HEADER_SIZE, check_rows_end, checked_string_table_start
from _common.record_reader import RecordReader


FILE_NAME = "branchquest.bss"

# `is_root_quest`: the quest's place in its branch group.
ROLE_OPENS_CROSSROAD = 0
ROLE_CROSSROAD_CHOICE = 1
ROLE_LATER_QUEST = 2

_U32 = struct.Struct("<I")
# u32 group_key | u16 quest_chain_id | u16 quest_id | u8 is_root_quest
_ROW = struct.Struct("<IHHB")


class BranchQuestRecord(TypedDict):
    group: int
    group_key: int
    row: int
    quest_chain_id: int
    quest_id: int
    packed_quest_id: int
    is_root_quest: int


def parse_branchquest_records(data: bytes) -> list[BranchQuestRecord]:
    """Every quest reference in file order, with its group's index and its row in the group.

    Raises ValueError on a bad magic, when a group runs into the string
    table, or when the groups end anywhere but where the string table
    starts: then the row layout has changed and every field is suspect.
    """
    groups_end = checked_string_table_start(data, FILE_NAME)
    records: list[BranchQuestRecord] = []
    pos = HEADER_SIZE
    for group in range(u32(data, 4)):
        reader = RecordReader(data, pos, groups_end, f"{FILE_NAME} group {group}")
        (row_count,) = reader.unpack(_U32)
        for row in range(row_count):
            group_key, quest_chain_id, quest_id, is_root_quest = reader.unpack(_ROW)
            records.append({
                "group": group,
                "group_key": group_key,
                "row": row,
                "quest_chain_id": quest_chain_id,
                "quest_id": quest_id,
                "packed_quest_id": (quest_id << 16) | quest_chain_id,
                "is_root_quest": is_root_quest,
            })
        pos = reader.pos
    check_rows_end(data, pos, f"{FILE_NAME} groups")
    return records

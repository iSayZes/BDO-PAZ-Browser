"""`specialquestinfo.bss`: special quest groups, each a list of packed quest IDs.

    PABR | u32 count | count x group | string table | u32 string_table_start | u32 0

    group: u32 group_key | u64 quest_count | quest_count x u32 packed_quest_id

`alreadyclearspecialquest(group)` in `quest.dbss` action scripts names a
group by its key. A packed quest ID is `(quest_id << 16) | quest_chain_id`.
The string table is empty. Layout in docs/file-formats/bss/specialquestinfo_bss.md.
"""

from __future__ import annotations

import struct

from _common.binary import u32
from _common.pabr_strings import HEADER_SIZE, check_rows_end, checked_string_table_start


FILE_NAME = "specialquestinfo.bss"

# u32 group_key | u64 quest_count
_GROUP_HEAD = struct.Struct("<IQ")
_QUEST_ID_SIZE = 4


def parse_specialquestinfo_records(data: bytes) -> list[dict]:
    """Every group in file order.

    Raises ValueError on a bad magic, a group that runs past the string
    table, or groups that do not end where the string table starts.
    """
    end = checked_string_table_start(data, FILE_NAME)
    count = u32(data, 4)
    pos = HEADER_SIZE
    records: list[dict] = []
    for index in range(count):
        if pos + _GROUP_HEAD.size > end:
            raise ValueError(f"{FILE_NAME} group {index} at 0x{pos:X} runs past the string table")
        group_key, quest_count = _GROUP_HEAD.unpack_from(data, pos)
        quests_start = pos + _GROUP_HEAD.size
        pos = quests_start + quest_count * _QUEST_ID_SIZE
        if pos > end:
            raise ValueError(f"{FILE_NAME} group {group_key} lists {quest_count} quests past the string table")
        records.append({
            "group_key": group_key,
            "quest_count": quest_count,
            "packed_quest_ids": list(struct.unpack_from(f"<{quest_count}I", data, quests_start)),
        })
    check_rows_end(data, pos, f"{FILE_NAME} groups")
    return records

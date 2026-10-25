"""`acceptquest.bss` and `completequest.bss`: the NPC dialog that gives or takes each quest.

    PABR | u32 count | count x 8-byte row | u32 0 | u32 rows_end | u32 0

The tail is the PABR string table of `exploration.bss` with no strings. Each
row is u16 npc_id | u16 quest_chain_id | u16 quest_id | u16 dialog_index;
`dialog_index << 16 | npc_id` is a `detail_dialog.dbss` key. Full layout in
docs/file-formats/bss/acceptquest_bss.md and completequest_bss.md.
"""

from __future__ import annotations

import struct
from typing import TypedDict

from _common.pabr_strings import fixed_row_offsets


# u16 npc_id | u16 quest_chain_id | u16 quest_id | u16 dialog_index
_ROW = struct.Struct("<HHHH")


class QuestNpcRecord(TypedDict):
    packed_quest_id: int
    quest_chain_id: int
    quest_id: int
    npc_id: int
    dialog_index: int


def parse_quest_npc_records(data: bytes, file_name: str) -> list[QuestNpcRecord]:
    """Every row in file order, raw: `npc_id` 0 means the quest names no NPC.

    Raises ValueError on a bad magic, or when the rows do not end where the
    trailer says: then the row size has changed and every field is suspect.
    """
    records: list[QuestNpcRecord] = []
    for offset in fixed_row_offsets(data, _ROW.size, file_name):
        npc_id, quest_chain_id, quest_id, dialog_index = _ROW.unpack_from(data, offset)
        records.append({
            "packed_quest_id": quest_id << 16 | quest_chain_id,
            "quest_chain_id": quest_chain_id,
            "quest_id": quest_id,
            "npc_id": npc_id,
            "dialog_index": dialog_index,
        })
    return records

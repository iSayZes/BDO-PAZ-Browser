from __future__ import annotations

from typing import TypedDict


class NpcGiftOffsetRecord(TypedDict):
    npc_id: int
    data_offset: int
    data_size: int
    unknown_08: int


class NpcGiftFlatRecord(TypedDict):
    npc_id: int
    npc_name: str
    item_id: int
    item_name: str
    amity: int


class NpcGiftDataRecord(TypedDict):
    npc_id: int
    npc_name: str
    unknown_02: int
    dialogue: str
    dialogue_source: str

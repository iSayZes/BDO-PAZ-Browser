"""`knowledgelearningcharacterkey.bss`: every character that teaches each knowledge card.

`knowledgelearning.dbss` table 0 grouped by card, no PABR magic:

    u32 count | count x (u32 character_count | u32 card_id | u16 character_ids[character_count])

Full layout in docs/file-formats/bss/knowledgelearningcharacterkey_bss.md.
"""

from __future__ import annotations

import struct
from dataclasses import dataclass

from _common.binary import u32

_ENTRY_HEAD = struct.Struct("<II")
_CHARACTER_ID_SIZE = 2


@dataclass(frozen=True)
class KnowledgeCharacterKeyEntry:
    card_id: int
    character_ids: tuple[int, ...]


def parse_knowledgelearningcharacterkey(data: bytes) -> list[KnowledgeCharacterKeyEntry]:
    """Every card entry in file order.

    Raises ValueError when an entry runs past the end, or when the entries do
    not end exactly at the end of the file.
    """
    if len(data) < 4:
        raise ValueError("knowledgelearningcharacterkey.bss is too short for its count")

    entries: list[KnowledgeCharacterKeyEntry] = []
    pos = 4
    for index in range(u32(data, 0)):
        if pos + _ENTRY_HEAD.size > len(data):
            raise ValueError(f"knowledgelearningcharacterkey.bss entry {index} runs past the end")
        character_count, card_id = _ENTRY_HEAD.unpack_from(data, pos)
        start = pos + _ENTRY_HEAD.size
        pos = start + character_count * _CHARACTER_ID_SIZE
        if pos > len(data):
            raise ValueError(f"knowledgelearningcharacterkey.bss card {card_id} runs past the end")
        entries.append(KnowledgeCharacterKeyEntry(card_id, struct.unpack_from(f"<{character_count}H", data, start)))

    if pos != len(data):
        raise ValueError("knowledgelearningcharacterkey.bss has bytes after its last entry")
    return entries

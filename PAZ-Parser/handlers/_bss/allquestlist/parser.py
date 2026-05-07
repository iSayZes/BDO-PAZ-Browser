from __future__ import annotations

from _common.binary import u32 as _u32
from .model import AllQuestListRecord


_MAGIC = b"PABR"
_HEADER_SIZE = 8
_ENTRY_SIZE = 4
_TRAILER_SIZE = 12


def parse_allquestlist_records(data: bytes) -> list[AllQuestListRecord]:
    if len(data) < _HEADER_SIZE:
        return []

    if data[:4] != _MAGIC:
        raise ValueError("allquestlist.bss has invalid magic.")

    count = _u32(data, 4)
    entries_start = _HEADER_SIZE
    entries_end = entries_start + count * _ENTRY_SIZE
    trailer_end = entries_end + _TRAILER_SIZE

    if trailer_end > len(data):
        count = max(0, (len(data) - entries_start - _TRAILER_SIZE) // _ENTRY_SIZE)
        entries_end = entries_start + count * _ENTRY_SIZE

    records: list[AllQuestListRecord] = []
    for slot in range(count):
        packed_quest_id = _u32(data, entries_start + slot * _ENTRY_SIZE)
        records.append({
            "slot": slot,
            "packed_quest_id": packed_quest_id,
            "quest_chain_id": packed_quest_id & 0xFFFF,
            "quest_id": packed_quest_id >> 16,
        })

    return records

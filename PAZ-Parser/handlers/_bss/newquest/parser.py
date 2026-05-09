from __future__ import annotations

from _common.binary import u8, u16, u32
from .model import NewQuestRecord


_MAGIC = b"PABR"
_HEADER_SIZE = 8
_FIRST_GROUP_HEADER_SIZE = 10
_GROUP_HEADER_SIZE = 23
_ROW_SIZE = 17


def _row_count(data: bytes, offset: int, group: int) -> int:
    if group == 0:
        return u8(data, offset + 7)
    return u16(data, offset + 0x14)


def _header_size(group: int) -> int:
    if group == 0:
        return _FIRST_GROUP_HEADER_SIZE
    return _GROUP_HEADER_SIZE


def parse_newquest_records(data: bytes) -> list[NewQuestRecord]:
    if len(data) < _HEADER_SIZE:
        return []

    if data[:4] != _MAGIC:
        raise ValueError("newquest.bss has invalid magic.")

    group_count = u32(data, 4)
    offset = _HEADER_SIZE
    records: list[NewQuestRecord] = []

    for group in range(group_count):
        header_size = _header_size(group)
        if offset + header_size > len(data):
            break

        count = _row_count(data, offset, group)
        offset += header_size

        for row in range(count):
            if offset + _ROW_SIZE > len(data):
                return records

            quest_chain_id = u16(data, offset + 1)
            quest_id = u16(data, offset + 3)
            records.append({
                "group": group,
                "row": row,
                "flags": u8(data, offset),
                "quest_chain_id": quest_chain_id,
                "quest_id": quest_id,
                "packed_quest_id": (quest_id << 16) | quest_chain_id,
                "sequence_a": u32(data, offset + 5),
                "sequence_b": u32(data, offset + 9),
                "sequence_c": u32(data, offset + 13),
            })
            offset += _ROW_SIZE

    return records

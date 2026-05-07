from __future__ import annotations

from _common.binary import f32 as _f32, u16 as _u16, u32 as _u32
from .model import NpcPersonalityOffsetRecord, NpcPersonalityRecord

_RECORD_SIZE = 34
_OFFSET_RECORD_SIZE = 10


def parse_npcpersonality_records(data: bytes) -> list[NpcPersonalityRecord]:
    records: list[NpcPersonalityRecord] = []

    if len(data) < 4:
        return records

    count = _u32(data, 0)
    expected_size = 4 + count * _RECORD_SIZE

    if len(data) < expected_size:
        count = (len(data) - 4) // _RECORD_SIZE

    for index in range(count):
        base = 4 + index * _RECORD_SIZE

        group_a = _u32(data, base + 0x02)
        group_b = _u32(data, base + 0x06)
        group_c = _u32(data, base + 0x0A)

        records.append(NpcPersonalityRecord(
            row=index,
            personality_id=_u16(data, base + 0x00),
            group_a_id=group_a & 0xFFFF,
            group_a_count=(group_a >> 16) & 0xFFFF,
            group_b_id=group_b & 0xFFFF,
            group_b_count=(group_b >> 16) & 0xFFFF,
            group_c_id=group_c & 0xFFFF,
            group_c_count=(group_c >> 16) & 0xFFFF,
            interest_min=_f32(data, base + 0x10),
            interest_max_excl=_f32(data, base + 0x14),
            favor_min=_f32(data, base + 0x18),
            favor_max_excl=_f32(data, base + 0x1C),
            personality_type=_u16(data, base + 0x20),
        ))

    return records


def parse_npcpersonalityoffset_records(data: bytes) -> list[NpcPersonalityOffsetRecord]:
    records: list[NpcPersonalityOffsetRecord] = []

    if len(data) < 4:
        return records

    count = _u32(data, 0)
    expected_size = 4 + count * _OFFSET_RECORD_SIZE

    if len(data) < expected_size:
        count = (len(data) - 4) // _OFFSET_RECORD_SIZE

    for index in range(count):
        base = 4 + index * _OFFSET_RECORD_SIZE

        records.append(NpcPersonalityOffsetRecord(
            row=index,
            personality_id=_u16(data, base + 0x00),
            data_offset=_u32(data, base + 0x02),
            data_size=_u16(data, base + 0x06),
        ))

    return records

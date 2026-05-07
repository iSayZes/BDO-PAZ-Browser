from __future__ import annotations

from _common.binary import u8 as _u8, u16 as _u16, u32 as _u32
from .model import (
    ZodiacSignOffsetRecord,
    ZodiacSignOrderOffsetRecord,
    ZodiacSignOrderRecord,
)


def parse_zodiacsignoffset_records(data: bytes) -> list[ZodiacSignOffsetRecord]:
    if len(data) < 4:
        return []

    count = _u32(data, 0)
    record_size = 9  # u8 zodiac_id + u32 data_offset + u32 data_size
    if len(data) < 4 + count * record_size:
        count = (len(data) - 4) // record_size

    records: list[ZodiacSignOffsetRecord] = []
    for i in range(count):
        base = 4 + i * record_size
        records.append(
            ZodiacSignOffsetRecord(
                row=i,
                zodiac_id=_u8(data, base),
                data_offset=_u32(data, base + 1),
                data_size=_u32(data, base + 5),
            )
        )

    return records


def parse_zodiacsignorder_records(
    data: bytes, offset_data: bytes
) -> list[ZodiacSignOrderRecord]:
    """Parse zodiacsignorder.dbss using its offset companion to locate records."""
    if len(offset_data) < 4:
        return []

    count = _u32(offset_data, 0)
    offset_record_size = 10  # u16 + u32 + u16 + u16
    if len(offset_data) < 4 + count * offset_record_size:
        count = (len(offset_data) - 4) // offset_record_size

    records: list[ZodiacSignOrderRecord] = []
    for i in range(count):
        base = 4 + i * offset_record_size
        personality_type = _u16(offset_data, base)
        data_offset = _u32(offset_data, base + 2)

        # data_offset points 2 bytes past record start (skips leading u16 personality_type)
        rec_start = data_offset - 2
        if rec_start < 0 or rec_start + 12 > len(data):
            continue

        pos = rec_start + 2  # skip personality_type already known
        trigger_count = _u16(data, pos)
        pos += 2
        pos += 8  # reserved_a (u32) + reserved_b (u32)

        step_count = max(0, trigger_count - 1)
        step_indices: list[int] = []
        for _ in range(step_count):
            if pos + 2 > len(data):
                break
            step_indices.append(_u16(data, pos))
            pos += 2

        zodiac_id = _u8(data, pos)
        trigger_order = [0] + step_indices

        records.append(
            ZodiacSignOrderRecord(
                row=i,
                personality_type=personality_type,
                zodiac_id=zodiac_id,
                trigger_count=trigger_count,
                trigger_order=trigger_order,
            )
        )

    return records


def parse_zodiacsignorderoffset_records(data: bytes) -> list[ZodiacSignOrderOffsetRecord]:
    if len(data) < 4:
        return []

    count = _u32(data, 0)
    record_size = 10  # u16 + u32 + u16 + u16
    if len(data) < 4 + count * record_size:
        count = (len(data) - 4) // record_size

    records: list[ZodiacSignOrderOffsetRecord] = []
    for i in range(count):
        base = 4 + i * record_size
        records.append(
            ZodiacSignOrderOffsetRecord(
                row=i,
                personality_type=_u16(data, base),
                data_offset=_u32(data, base + 2),
                data_size=_u16(data, base + 6),
                padding=_u16(data, base + 8),
            )
        )

    return records

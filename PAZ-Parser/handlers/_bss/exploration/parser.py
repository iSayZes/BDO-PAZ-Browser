from __future__ import annotations

import struct

from _common.binary import u16, u32


_MAGIC = b"PABR"
_HEADER_SIZE = 8
_MIN_RECORD_SIZE = 48
_MAX_KNOWLEDGE_ID = 100_000


def _f32(data: bytes, offset: int) -> float:
    if offset < 0 or offset + 4 > len(data):
        return 0.0
    return struct.unpack_from("<f", data, offset)[0]


def _is_record_anchor(data: bytes, offset: int, count: int) -> bool:
    if offset + _MIN_RECORD_SIZE > len(data):
        return False

    knowledge_id = u32(data, offset)
    duplicate_id = u32(data, offset + 0x06)
    group_id = u32(data, offset + 0x0A)

    return (
        0 < knowledge_id < _MAX_KNOWLEDGE_ID
        and duplicate_id == knowledge_id
        and group_id < count
        and data[offset + 0x0E] in (0, 1)
        and data[offset + 0x0F] in (0, 1)
    )


def _record_offsets(data: bytes, count: int) -> list[int]:
    offsets: list[int] = []

    for offset in range(_HEADER_SIZE, len(data) - _MIN_RECORD_SIZE + 1):
        if _is_record_anchor(data, offset, count):
            offsets.append(offset)
            if len(offsets) == count:
                break

    return offsets


def parse_exploration_records(data: bytes) -> list[dict]:
    if len(data) < _HEADER_SIZE:
        return []

    if data[:4] != _MAGIC:
        raise ValueError("exploration.bss has invalid magic.")

    count = u32(data, 4)
    offsets = _record_offsets(data, count)
    records: list[dict] = []

    for slot, offset in enumerate(offsets):
        next_offset = offsets[slot + 1] if slot + 1 < len(offsets) else len(data)
        records.append({
            "slot": slot,
            "file_offset": offset,
            "record_size": next_offset - offset,
            "knowledge_id": u32(data, offset),
            "unknown_flags": u16(data, offset + 0x04),
            "duplicate_knowledge_id": u32(data, offset + 0x06),
            "group_id": u32(data, offset + 0x0A),
            "enabled": data[offset + 0x0E],
            "unknown_flag_a": data[offset + 0x10],
            "unknown_flag_b": data[offset + 0x11],
            "unknown_flag_c": data[offset + 0x12],
            "unknown_marker": data[offset + 0x13],
            "anchor_id_a": u32(data, offset + 0x17),
            "anchor_id_b": u32(data, offset + 0x1B),
            "radius": _f32(data, offset + 0x1F),
            "radius_squared": _f32(data, offset + 0x23),
        })

    return records

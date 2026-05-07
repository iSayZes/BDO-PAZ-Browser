from __future__ import annotations

import struct


def u8(data: bytes, offset: int) -> int:
    return data[offset] if 0 <= offset < len(data) else 0


def u16(data: bytes, offset: int) -> int:
    if offset < 0 or offset + 2 > len(data):
        return 0

    return struct.unpack_from("<H", data, offset)[0]


def u32(data: bytes, offset: int) -> int:
    if offset < 0 or offset + 4 > len(data):
        return 0

    return struct.unpack_from("<I", data, offset)[0]


def u64(data: bytes, offset: int) -> int:
    if offset < 0 or offset + 8 > len(data):
        return 0

    return struct.unpack_from("<Q", data, offset)[0]


def f32(data: bytes, offset: int) -> float:
    if offset < 0 or offset + 4 > len(data):
        return 0.0

    return struct.unpack_from("<f", data, offset)[0]


def u32_hi(value: int) -> int:
    return (value >> 16) & 0xFFFF


def u32_lo(value: int) -> int:
    return value & 0xFFFF


def debug_u32_fields(block: bytes, count: int = 16) -> dict[str, int]:
    fields: dict[str, int] = {}

    for index in range(count):
        offset = index * 4
        fields[f"u32_{offset:02X}"] = u32(block, offset)

    return fields


def parse_offset_table(data: bytes) -> dict[int, tuple[int, int]]:
    """Return {entry_id: (byte_offset, block_size)} for offset-style files."""
    count = u32(data, 0)
    result: dict[int, tuple[int, int]] = {}

    for index in range(count):
        base = 4 + index * 12
        entry_id = u32(data, base)
        offset = u32(data, base + 4)
        size = u32(data, base + 8)

        result[entry_id] = (offset, size)

    return result

from __future__ import annotations

import struct

from .model import (
    ZodiacSignOffsetRecord,
    ZodiacSignOrderOffsetRecord,
    ZodiacSignOrderRecord,
    ZodiacSignRecord,
)

# UTF-16LE bytes for "자리" (U+C790 U+B9AC)
_ZARI = b"\x90\xC7\xAC\xB9"


def _u8(data: bytes, offset: int) -> int:
    return data[offset] if 0 <= offset < len(data) else 0


def _u16(data: bytes, offset: int) -> int:
    if offset + 2 > len(data):
        return 0
    return struct.unpack_from("<H", data, offset)[0]


def _u32(data: bytes, offset: int) -> int:
    if offset + 4 > len(data):
        return 0
    return struct.unpack_from("<I", data, offset)[0]


def _u64(data: bytes, offset: int) -> int:
    if offset + 8 > len(data):
        return 0
    return struct.unpack_from("<Q", data, offset)[0]


def _read_utf16_block(data: bytes, offset: int) -> tuple[str, int]:
    """Read u32 char_count + u32 pad + char16[char_count]. Returns (text, new_offset)."""
    if offset + 8 > len(data):
        return "", offset
    char_count = _u32(data, offset)
    offset += 8  # skip char_count (4B) + pad (4B)
    byte_len = char_count * 2
    if offset + byte_len > len(data):
        return "", offset
    text = data[offset : offset + byte_len].decode("utf-16-le", errors="replace")
    return text, offset + byte_len


def _read_text_block(data: bytes, offset: int) -> tuple[str, str, int]:
    """Parse text_block. Returns (constellation_name, trait_text, new_offset).

    Layout: u32 reserved_a (4B) + u16 reserved_b (2B) + char16[?] constellation_name
    (scan for 자리) + u64 trait_len (8B) + char16[trait_len] trait_text.
    """
    name_start = offset + 6  # skip reserved_a (4B) + reserved_b (2B)

    zari_pos = data.find(_ZARI, name_start)
    if zari_pos == -1:
        return "", "", name_start

    name_end = zari_pos + 4  # inclusive of 자리
    constellation_name = data[name_start:name_end].decode("utf-16-le", errors="replace")

    pos = name_end
    trait_len = _u64(data, pos)
    pos += 8
    byte_len = trait_len * 2
    if pos + byte_len > len(data):
        return constellation_name, "", pos
    trait_text = data[pos : pos + byte_len].decode("utf-16-le", errors="replace")
    return constellation_name, trait_text, pos + byte_len


def _parse_one_zodiacsign(
    data: bytes, offset: int, row: int
) -> tuple[ZodiacSignRecord | None, int]:
    pos = offset
    if pos >= len(data):
        return None, pos

    zodiac_id = _u8(data, pos)
    pos += 1
    float_count = _u32(data, pos)
    pos += 4

    if float_count > 64:
        return None, pos

    pos += float_count * 12  # skip f32×3×float_count star_positions

    pairs_count = _u32(data, pos)
    pos += 4
    pos += 2  # u16 padding

    if pairs_count > 64:
        return None, pos

    pos += pairs_count * 4  # skip u16×2×pairs_count star_pairs

    constellation_name, trait_text, pos = _read_text_block(data, pos)
    icon_small, pos = _read_utf16_block(data, pos)
    icon_large, pos = _read_utf16_block(data, pos)

    # tail: zodiac_id_tail (u8) + zodiac_id_dup2 (u8) + pad0 (u8) + next_zodiac_id (u16)
    #       + const1 (u8) + const0a (u8) + const1b (u8) + const0b (u8) + reserved (u32)
    pos += 3  # zodiac_id_tail + zodiac_id_dup2 + pad0
    next_zodiac_id = _u16(data, pos)
    pos += 2
    pos += 4  # 4 constant u8 bytes
    pos += 4  # reserved u32

    return ZodiacSignRecord(
        row=row,
        zodiac_id=zodiac_id,
        float_count=float_count,
        pairs_count=pairs_count,
        constellation_name=constellation_name,
        trait_text=trait_text,
        icon_small=icon_small,
        icon_large=icon_large,
        next_zodiac_id=next_zodiac_id,
    ), pos


def parse_zodiacsign_records(data: bytes) -> list[ZodiacSignRecord]:
    if len(data) < 4:
        return []

    count = _u32(data, 0)
    if count > 64:
        count = 12  # always 12 zodiac signs

    records: list[ZodiacSignRecord] = []
    pos = 4
    for i in range(count):
        record, pos = _parse_one_zodiacsign(data, pos, row=i)
        if record is None:
            break
        records.append(record)

    return records


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

from __future__ import annotations

from _common.binary import u8 as _u8, u16 as _u16, u32 as _u32, u64 as _u64
from .model import ZodiacSignRecord

# UTF-16LE bytes for "자리" (U+C790 U+B9AC)
_ZARI = b"\x90\xC7\xAC\xB9"


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

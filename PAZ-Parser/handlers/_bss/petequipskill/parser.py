from __future__ import annotations

from _common.binary import u16, u32


_MAGIC = b"PABR"
_HEADER_SIZE = 4
_SECTION1_RECORD_SIZE = 12
_SECTION2_RECORD_SIZE = 16
# [u32 0][u32 data_end][u32 0], the same trailer as fairyequipskill.bss.
_TRAILER_SIZE = 12
_NULL_EQUIP_SKILL_ID = 200


def _parse_section1(data: bytes) -> tuple[list[dict], int]:
    """Read Section 1 and return its records and the offset right after it.

    Section 1 stores record `n` for `equip_skill_id = n` and declares no count,
    so it ends at the first record whose ID is not its slot. That is the first
    null placeholder (ID 200) of the slot table that follows.
    """
    records: list[dict] = []
    pos = _HEADER_SIZE
    end = len(data) - _TRAILER_SIZE

    while pos + _SECTION1_RECORD_SIZE <= end:
        equip_skill_id = u32(data, pos)
        slot = len(records)
        if equip_skill_id != slot:
            break

        records.append({
            "slot": slot,
            "section": "S1",
            "equip_skill_id": equip_skill_id,
            "skill_type": u32(data, pos + 0x04),
            "skill_level": u16(data, pos + 0x08),
            "skill_no": u16(data, pos + 0x0A),
            "unknown_0c": None,
            "unknown_10": None,
        })
        pos += _SECTION1_RECORD_SIZE

    return records, pos


def _parse_section2(data: bytes, start: int) -> list[dict]:
    """Walk the slot table after Section 1; slot `n` holds `equip_skill_id = n` or a null (200)."""
    records: list[dict] = []
    pos = start
    end = len(data) - _TRAILER_SIZE
    slot = 0

    while pos + _SECTION2_RECORD_SIZE <= end:
        equip_skill_id = u32(data, pos)
        skill_type = u32(data, pos + 0x04)
        skill_level = u16(data, pos + 0x08)
        skill_no = u16(data, pos + 0x0A)
        # 0 or 1; each record with 1 carries one more u32 after the 16 bytes.
        unknown_0c = u32(data, pos + 0x0C)
        pos += _SECTION2_RECORD_SIZE

        if equip_skill_id == _NULL_EQUIP_SKILL_ID:
            slot += 1
            continue

        unknown_10 = None
        if unknown_0c == 1 and pos + 4 <= end:
            unknown_10 = u32(data, pos)
            pos += 4

        records.append({
            "slot": slot,
            "section": "S2",
            "equip_skill_id": equip_skill_id,
            "skill_type": skill_type,
            "skill_level": skill_level,
            "skill_no": skill_no,
            "unknown_0c": unknown_0c,
            "unknown_10": unknown_10,
        })
        slot += 1

    return records


def parse_petequipskill_records(data: bytes) -> list[dict]:
    if len(data) < _HEADER_SIZE:
        return []

    if data[:4] != _MAGIC:
        raise ValueError("petequipskill.bss has invalid magic.")

    section1, section2_start = _parse_section1(data)
    return section1 + _parse_section2(data, section2_start)

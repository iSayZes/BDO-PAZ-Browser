from __future__ import annotations

from _common.binary import u8, u16, u32


_MAGIC = b"PABR"
_HEADER_SIZE = 4
_RECORD_SIZE = 12
_TRAILER_SIZE = 12

# Sentinel written into the reserved block that follows the live catalog.
# The catalog has no count field, so this value terminates parsing.
_NULL_EQUIP_SKILL_ID = 200


def _catalog_end(data: bytes) -> int:
    """Last byte position a catalog record may occupy, excluding the trailer."""
    return max(_HEADER_SIZE, len(data) - _TRAILER_SIZE)


def parse_fairyequipskill_records(data: bytes) -> list[dict]:
    """Parse the fairy skill catalog into plain dicts.

    The file stores 12-byte records starting at 0x04 with no count field; the
    catalog ends at the first record whose equip_skill_id is the null sentinel.
    """
    if len(data) < _HEADER_SIZE:
        return []

    if data[:_HEADER_SIZE] != _MAGIC:
        raise ValueError("fairyequipskill.bss has invalid magic.")

    records: list[dict] = []
    end = _catalog_end(data)
    pos = _HEADER_SIZE

    while pos + _RECORD_SIZE <= end:
        equip_skill_id = u32(data, pos)

        if equip_skill_id == _NULL_EQUIP_SKILL_ID:
            break

        records.append({
            "equip_skill_id": equip_skill_id,
            "skill_type": u32(data, pos + 0x04),
            "tier": u8(data, pos + 0x08),
            "padding": u8(data, pos + 0x09),
            "loc_id": u16(data, pos + 0x0A),
        })
        pos += _RECORD_SIZE

    return records

from __future__ import annotations

from _common.binary import u32


_HEADER_SIZE = 4
_RECORD_SIZE = 12

# The offset companion addresses the payload that follows the record's key.
_KEY_PREFIX_SIZE = 4


def _record_count(data: bytes, filename: str) -> int:
    if len(data) < _HEADER_SIZE:
        raise ValueError(f"{filename} is truncated: missing record count.")

    count = u32(data, 0)
    available = (len(data) - _HEADER_SIZE) // _RECORD_SIZE

    # Trust whichever is smaller so a short or padded file cannot over-read.
    return min(count, available)


def parse_fairyskillchange_records(data: bytes) -> list[dict]:
    """Parse the fairy level -> skill-reroll orb cost table."""
    count = _record_count(data, "fairyskillchange.dbss")

    records: list[dict] = []
    for index in range(count):
        pos = _HEADER_SIZE + index * _RECORD_SIZE
        records.append({
            "key": u32(data, pos),
            "level": u32(data, pos + 0x04),
            "orb_cost": u32(data, pos + 0x08),
        })

    return records


def parse_fairyskillchangeoffset_records(data: bytes) -> list[dict]:
    """Parse the level-keyed index into fairyskillchange.dbss."""
    count = _record_count(data, "fairyskillchangeoffset.dbss")

    records: list[dict] = []
    for index in range(count):
        pos = _HEADER_SIZE + index * _RECORD_SIZE
        data_offset = u32(data, pos + 0x04)
        records.append({
            "level": u32(data, pos),
            "data_offset": data_offset,
            "data_size": u32(data, pos + 0x08),
            "record_start": data_offset - _KEY_PREFIX_SIZE,
        })

    return records

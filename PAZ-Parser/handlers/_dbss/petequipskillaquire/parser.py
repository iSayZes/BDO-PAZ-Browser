from __future__ import annotations

from _common.equipskill_roll import (
    parse_roll_offset_records,
    parse_roll_records,
)


_LABEL = "petequipskillaquire"


def _group(acquire_type_id: int) -> int:
    """Leading digit of the key, e.g. 401 -> 4. Keys 0-4 have group 0."""
    return acquire_type_id // 100


def _tier(acquire_type_id: int) -> int:
    """Trailing digits of the key, e.g. 401 -> 1."""
    return acquire_type_id % 100


def parse_petequipskillaquireoffset_records(data: bytes) -> list[dict]:
    return parse_roll_offset_records(data, f"{_LABEL}offset")


def parse_petequipskillaquire_records(data: bytes, offset_data: bytes) -> list[dict]:
    records = parse_roll_records(data, offset_data, _LABEL)

    for record in records:
        acquire_type_id = record["acquire_type_id"]
        record["group"] = _group(acquire_type_id)
        record["tier"] = _tier(acquire_type_id)

    return records

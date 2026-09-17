from __future__ import annotations

from _common.equipskill_roll import (
    parse_roll_offset_records,
    parse_roll_records,
)


_LABEL = "fairyequipskillaquire"

# Acquire type IDs are the four fairy grades, ascending.
FAIRY_GRADES: dict[int, tuple[int, str]] = {
    501: (1, "Faint"),
    502: (2, "Glimmering"),
    503: (3, "Brilliant"),
    504: (4, "Radiant"),
}


def parse_fairyequipskillaquireoffset_records(data: bytes) -> list[dict]:
    return parse_roll_offset_records(data, f"{_LABEL}offset")


def parse_fairyequipskillaquire_records(data: bytes, offset_data: bytes) -> list[dict]:
    records = parse_roll_records(data, offset_data, _LABEL)

    for record in records:
        grade, grade_name = FAIRY_GRADES.get(record["acquire_type_id"], (0, ""))
        record["fairy_grade"] = grade
        record["grade_name"] = grade_name

    return records

"""`petupgraderesult.bss`: the Tier 5 Pet Training result of each Tier 4 pet.

Two maps with no PABR magic and no trailer:

    u32 result_count | Result[result_count]
        (u16 pet_id | u16 pet_id_dup | u16 result_pet_id | u32 leader_base_skill_id)
    u32 leader_skill_count | Leader Skill[leader_skill_count]
        (u16 pet_id | u32 leader_base_skill_id)

Layout 1 in docs/file-formats/petupgraderesult_bss.md.
"""

from __future__ import annotations

import struct

from _common.binary import u32


FILE_NAME = "petupgraderesult.bss"
SECTION_RESULT = 1
SECTION_LEADER_SKILL = 2

_COUNT_SIZE = 4
_RESULT = struct.Struct("<HHHI")
_LEADER_SKILL = struct.Struct("<HI")


def _section(data: bytes, start: int, row: struct.Struct, label: str) -> tuple[list[tuple], int]:
    """The rows of one counted section and the offset past it.

    Raises ValueError when the count or the rows run past the end.
    """
    if start + _COUNT_SIZE > len(data):
        raise ValueError(f"{label} count at 0x{start:X} is past the end of {len(data):,} bytes")
    count = u32(data, start)
    rows_start = start + _COUNT_SIZE
    rows_end = rows_start + count * row.size
    if rows_end > len(data):
        raise ValueError(f"{label} declares {count:,} rows but {len(data):,} bytes hold fewer")
    return list(row.iter_unpack(data[rows_start:rows_end])), rows_end


def parse_petupgraderesult_records(data: bytes) -> list[dict]:
    """The Result rows, then the Leader Skill rows, each tagged with its `section`.

    A Leader Skill row has `None` in the Result-only fields. Raises ValueError
    when a section runs past the end or bytes are left over.
    """
    results, results_end = _section(data, 0, _RESULT, "Result")
    leader_skills, end = _section(data, results_end, _LEADER_SKILL, "Leader Skill")
    if end != len(data):
        raise ValueError(f"{len(data) - end:,} bytes left after the Leader Skill rows")

    return [
        {
            "section": SECTION_RESULT,
            "pet_id": pet_id,
            "pet_id_dup": pet_id_dup,
            "result_pet_id": result_pet_id,
            "leader_base_skill_id": leader_base_skill_id,
        }
        for pet_id, pet_id_dup, result_pet_id, leader_base_skill_id in results
    ] + [
        {
            "section": SECTION_LEADER_SKILL,
            "pet_id": pet_id,
            "pet_id_dup": None,
            "result_pet_id": None,
            "leader_base_skill_id": leader_base_skill_id,
        }
        for pet_id, leader_base_skill_id in leader_skills
    ]

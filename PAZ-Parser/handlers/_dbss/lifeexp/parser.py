"""`lifeexp.dbss`: the EXP table of every life skill.

The main file holds one block per life skill:

    u32 skill_count | skill_count x (u32 level_count | level_count x 13-byte row)

Each row is:

    u8 life_skill | u32 level | u64 exp

`lifeexpoffset.dbss` has the same shape with 12-byte
[u32 level][u32 offset][u32 size] rows; its block index is the life skill.
Full layout in docs/file-formats/lifeexp_dbss.md.
"""

from __future__ import annotations

import struct


_U32 = struct.Struct("<I")
_OFFSET_ROW = struct.Struct("<III")
_LEVEL_ROW = struct.Struct("<BIQ")


def _skill_count(data: bytes, file_name: str) -> int:
    if len(data) < _U32.size:
        raise ValueError(f"{file_name} is too small for its life skill count")
    return _U32.unpack_from(data)[0]


def parse_lifeexpoffset_records(data: bytes) -> list[dict]:
    """Every offset row, with the life skill taken from its block index.

    Raises ValueError when a block runs past the end of the file or the blocks
    do not fill it exactly.
    """
    skill_count = _skill_count(data, "lifeexpoffset.dbss")
    records: list[dict] = []
    cursor = _U32.size
    for life_skill in range(skill_count):
        if cursor + _U32.size > len(data):
            raise ValueError(f"lifeexpoffset block {life_skill} header exceeds file size")
        (level_count,) = _U32.unpack_from(data, cursor)
        cursor += _U32.size
        if cursor + level_count * _OFFSET_ROW.size > len(data):
            raise ValueError(f"lifeexpoffset block {life_skill} rows exceed file size")
        for _ in range(level_count):
            level, data_offset, data_size = _OFFSET_ROW.unpack_from(data, cursor)
            cursor += _OFFSET_ROW.size
            records.append({
                "life_skill": life_skill,
                "level": level,
                "data_offset": data_offset,
                "data_size": data_size,
            })
    if cursor != len(data):
        raise ValueError(f"lifeexpoffset blocks end at {cursor}, file holds {len(data)} bytes")
    return records


def _level_record(data: bytes, offset_row: dict) -> dict:
    data_offset = offset_row["data_offset"]
    data_size = offset_row["data_size"]
    label = f"life skill {offset_row['life_skill']} level {offset_row['level']}"
    if data_size != _LEVEL_ROW.size:
        raise ValueError(f"{label}: row size {data_size}, expected {_LEVEL_ROW.size}")
    if data_offset + data_size > len(data):
        raise ValueError(f"{label}: row exceeds file size")

    life_skill, level, exp = _LEVEL_ROW.unpack_from(data, data_offset)
    if (life_skill, level) != (offset_row["life_skill"], offset_row["level"]):
        raise ValueError(f"{label}: row holds life skill {life_skill} level {level}")
    return {"life_skill": life_skill, "level": level, "exp": exp}


def parse_lifeexp_records(data: bytes, offset_data: bytes) -> list[dict]:
    """Every level row the offset companion points at, in its order.

    Raises ValueError when the two files count different life skills, or a
    row lies outside the file or holds another life skill or level than the
    offset row that points at it.
    """
    skill_count = _skill_count(data, "lifeexp.dbss")
    offset_skill_count = _skill_count(offset_data, "lifeexpoffset.dbss")
    if skill_count != offset_skill_count:
        raise ValueError(
            f"lifeexp.dbss counts {skill_count} life skills, lifeexpoffset.dbss {offset_skill_count}"
        )
    return [_level_record(data, row) for row in parse_lifeexpoffset_records(offset_data)]

"""`fitnesslevel.dbss`: Breath, Strength and Health level tables.

The main file holds one block per fitness type:

    u32 type_count | type_count x (u32 level_count | level_count x 29-byte row)

Each row is:

    u8 fitness_type | u32 level | u64 exp
    | f32 max_stamina | f32 weight_limit | f32 max_hp | f32 max_mp

`fitnessleveloffset.dbss` repeats the block shape with 12-byte
[u32 level][u32 offset][u32 size] rows; its block index is the fitness type.
Full layout in docs/file-formats/dbss/fitnesslevel_dbss.md.
"""

from __future__ import annotations

import struct


_U32 = struct.Struct("<I")
_OFFSET_ROW = struct.Struct("<III")
_LEVEL_ROW = struct.Struct("<BIQffff")
# Weight is stored in ten-thousandths of an LT: 800000 is 80 LT.
_WEIGHT_PER_LT = 10_000


def parse_fitnessleveloffset_records(data: bytes) -> list[dict]:
    """Every offset row, with the fitness type taken from its block index."""
    records: list[dict] = []
    cursor = 0
    fitness_type = 0
    while cursor < len(data):
        if cursor + _U32.size > len(data):
            raise ValueError(f"fitnessleveloffset block {fitness_type} header exceeds file size")
        (level_count,) = _U32.unpack_from(data, cursor)
        cursor += _U32.size
        if cursor + level_count * _OFFSET_ROW.size > len(data):
            raise ValueError(f"fitnessleveloffset block {fitness_type} rows exceed file size")
        for _ in range(level_count):
            level, data_offset, data_size = _OFFSET_ROW.unpack_from(data, cursor)
            cursor += _OFFSET_ROW.size
            records.append({
                "fitness_type": fitness_type,
                "level": level,
                "data_offset": data_offset,
                "data_size": data_size,
            })
        fitness_type += 1
    return records


def _level_record(data: bytes, offset_row: dict) -> dict:
    data_offset = offset_row["data_offset"]
    data_size = offset_row["data_size"]
    label = f"fitness type {offset_row['fitness_type']} level {offset_row['level']}"
    if data_size != _LEVEL_ROW.size:
        raise ValueError(f"{label}: row size {data_size}, expected {_LEVEL_ROW.size}")
    if data_offset + data_size > len(data):
        raise ValueError(f"{label}: row exceeds file size")

    fitness_type, level, exp, max_stamina, weight, max_hp, max_mp = _LEVEL_ROW.unpack_from(data, data_offset)
    if (fitness_type, level) != (offset_row["fitness_type"], offset_row["level"]):
        raise ValueError(f"{label}: row holds fitness type {fitness_type} level {level}")

    return {
        "fitness_type": fitness_type,
        "level": level,
        "exp": exp,
        "max_stamina": max_stamina,
        "weight_limit": weight / _WEIGHT_PER_LT,
        "max_hp": max_hp,
        "max_mp": max_mp,
    }


def parse_fitnesslevel_records(data: bytes, offset_data: bytes) -> list[dict]:
    """Every level row the offset companion points at, in its order.

    Raises ValueError when a row lies outside the file or its type and level
    differ from the offset row that points at it.
    """
    return [_level_record(data, row) for row in parse_fitnessleveloffset_records(offset_data)]

"""Skill point EXP tables: combat skill points, guild points and life skill points.

`skillexperience.dbss`, `guildskillexperience.dbss` and `productexperience.dbss`
share one container and differ only in the row tail:

    u32 row_count | row_count x row, every row opening with its u32 level

Each `*offset.dbss` companion is the bare u16 offset table of
`_common/pabr_offset.py` (`parse_bare_offset_rows`): a u32 count, then
[u16 level][u32 offset][u32 size] rows, the offset pointing at the row's
u32 level. Neither file stores the rows in level order; the parser returns
them by level. Full layouts in docs/file-formats/skillexperience_dbss.md,
guildskillexperience_dbss.md and productexperience_dbss.md.
"""

from __future__ import annotations

import struct
from dataclasses import dataclass

from _common.offset_table import offset_records
from _common.pabr_offset import parse_bare_offset_rows


_U32 = struct.Struct("<I")


@dataclass(frozen=True)
class LevelTable:
    """One skill point EXP table: its files and the fields after the row's u32 level."""

    file_name: str
    offset_file: str
    row: struct.Struct
    fields: tuple[str, ...]


# Combat skill points: u32 level | u64 exp | u32 unknown_0c (16 bytes).
SKILL_EXPERIENCE = LevelTable(
    "skillexperience.dbss",
    "skillexperienceoffset.dbss",
    struct.Struct("<IQI"),
    ("exp", "unknown_0c"),
)
# Guild points: u32 level | u64 exp | u8 unknown_0c (13 bytes).
GUILD_SKILL_EXPERIENCE = LevelTable(
    "guildskillexperience.dbss",
    "guildskillexperienceoffset.dbss",
    struct.Struct("<IQB"),
    ("exp", "unknown_0c"),
)
# Life skill points: u32 level | u16 unknown_04 | u8 unknown_06 (7 bytes).
PRODUCT_EXPERIENCE = LevelTable(
    "productexperience.dbss",
    "productexperienceoffset.dbss",
    struct.Struct("<IHB"),
    ("unknown_04", "unknown_06"),
)

LEVEL_TABLES: tuple[LevelTable, ...] = (SKILL_EXPERIENCE, GUILD_SKILL_EXPERIENCE, PRODUCT_EXPERIENCE)

# Every offset companion: level, then the row's offset and size.
parse_level_offset_records = offset_records(parse_bare_offset_rows, "level", "data_offset", "data_size")


def _level_record(table: LevelTable, data: bytes, offset_row: dict) -> dict:
    data_offset = offset_row["data_offset"]
    data_size = offset_row["data_size"]
    label = f"{table.file_name} level {offset_row['level']}"
    if data_size != table.row.size:
        raise ValueError(f"{label}: row size {data_size}, expected {table.row.size}")
    if data_offset < _U32.size or data_offset + data_size > len(data):
        raise ValueError(f"{label}: row lies outside the file")

    level, *values = table.row.unpack_from(data, data_offset)
    if level != offset_row["level"]:
        raise ValueError(f"{label}: row holds level {level}")
    return {"level": level, **dict(zip(table.fields, values))}


def parse_level_records(table: LevelTable, data: bytes, offset_data: bytes) -> list[dict]:
    """Every row the offset companion points at, sorted by level.

    Raises ValueError when the two files count different rows, or a row lies
    outside the file, has another size or holds another level than the offset
    row that points at it.
    """
    if len(data) < _U32.size:
        raise ValueError(f"{table.file_name} is too small for its row count")
    (row_count,) = _U32.unpack_from(data)
    offset_rows = parse_level_offset_records(offset_data)
    if row_count != len(offset_rows):
        raise ValueError(f"{table.file_name} counts {row_count} rows, {table.offset_file} {len(offset_rows)}")
    records = [_level_record(table, data, row) for row in offset_rows]
    return sorted(records, key=lambda record: record["level"])

"""Skill point EXP tables: combat skill points, guild points and life skill points.

`skillexperience.dbss`, `guildskillexperience.dbss` and `productexperience.dbss`
share one container and differ only in the row tail:

    u32 row_count | row_count x row, every row opening with its u16 level

The row fields follow the client 1784 server dump, which reads each row into
its static status and fills the same members from the developer sheets
(`SkillPointEXP_Table_New`, `GuildSkillPointEXP_Table`, `ProductExp_Table`).
`is_exp_defined` is the flag the server sets once every EXP field of the row
is at least 0.

Each `*offset.dbss` companion is the bare u16 offset table of
`_common/pabr_offset.py` (`parse_bare_offset_rows`): a u32 count, then
[u16 level][u32 offset][u32 size] rows, the offset pointing at the row's
u32 level. Neither file stores the rows in level order; the parser returns
them by level. Full layouts in docs/file-formats/dbss/skillexperience_dbss.md,
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
    """One skill point EXP table: its files and the fields after the row's u16 level."""

    file_name: str
    offset_file: str
    row: struct.Struct
    fields: tuple[str, ...]


# Combat skill points (16 bytes): u16 level | u16 acquired_point | u32 exp |
# u32 require_exp_limit | u32 quest_require_exp_limit.
SKILL_EXPERIENCE = LevelTable(
    "skillexperience.dbss",
    "skillexperienceoffset.dbss",
    struct.Struct("<HHIII"),
    ("acquired_point", "exp", "require_exp_limit", "quest_require_exp_limit"),
)
# Guild points (13 bytes): u16 level | u16 acquired_point | u32 exp |
# u32 require_exp_limit | u8 is_exp_defined.
GUILD_SKILL_EXPERIENCE = LevelTable(
    "guildskillexperience.dbss",
    "guildskillexperienceoffset.dbss",
    struct.Struct("<HHIIB"),
    ("acquired_point", "exp", "require_exp_limit", "is_exp_defined"),
)
# Life skill points (7 bytes): u16 level | u32 exp | u8 is_exp_defined.
PRODUCT_EXPERIENCE = LevelTable(
    "productexperience.dbss",
    "productexperienceoffset.dbss",
    struct.Struct("<HIB"),
    ("exp", "is_exp_defined"),
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

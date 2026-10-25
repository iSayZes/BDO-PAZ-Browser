"""`cronenchant.bss`: the Caphras enhancement table.

    PABR | u32 category_count
    | category_count x (u32 grade_count | grade_count x (u32 step_count | step_count x 39-byte step))
    | u32 0 (empty string table) | u32 string_table_start | u32 0

One step per gear category, grade (TRI, TET, PEN) and Caphras level: the total
Caphras Stones to reach the level and the stats the item has at it. Full
layout in docs/file-formats/bss/cronenchant_bss.md.
"""

from __future__ import annotations

import struct

from _common.binary import whole_float
from _common.pabr_strings import checked_string_table_start
from _common.record_reader import RecordReader


_FILE_NAME = "cronenchant.bss"
_COUNT = struct.Struct("<I")
# The category count follows the PABR magic.
_CATEGORY_COUNT = 0x04

# category, enchant_level, total_stones, seven f32 stats, mp.
_STEP = struct.Struct("<HBI7fI")
_FLOAT_STATS = (
    "ap",
    "accuracy",
    "evasion",
    "hidden_evasion",
    "damage_reduction",
    "hidden_damage_reduction",
    "hp",
)


def _read_count(reader: RecordReader) -> int:
    (count,) = reader.unpack(_COUNT)
    return count


def _read_grade(reader: RecordReader, label: str) -> list[dict]:
    """The steps of one grade block, Caphras levels 1 to step_count.

    Raises ValueError when a step names another category or grade than the
    first step of the block, which means the step size or order is misread.
    """
    steps: list[dict] = []
    previous_total = 0
    for caphras_level in range(1, _read_count(reader) + 1):
        category, enchant_level, total_stones, *stats, mp = reader.unpack(_STEP)
        if steps and (category, enchant_level) != (steps[0]["category"], steps[0]["enchant_level"]):
            raise ValueError(
                f"{label} step {caphras_level} is category {category} level {enchant_level}, "
                f"the block started with {steps[0]['category']} level {steps[0]['enchant_level']}"
            )
        steps.append({
            "category": category,
            "enchant_level": enchant_level,
            "caphras_level": caphras_level,
            "stones": total_stones - previous_total,
            "total_stones": total_stones,
            # Every stat is a whole number on client 3464.
            **{name: whole_float(value) for name, value in zip(_FLOAT_STATS, stats)},
            "mp": mp,
        })
        previous_total = total_stones
    return steps


def parse_cronenchant_records(data: bytes) -> list[dict]:
    """Every step in file order.

    Raises ValueError on a missing magic, a block that runs past the string
    table, or blocks that stop short of it.
    """
    end = checked_string_table_start(data, _FILE_NAME)
    reader = RecordReader(data, _CATEGORY_COUNT, end, _FILE_NAME)
    records: list[dict] = []
    for category_index in range(_read_count(reader)):
        for grade_index in range(_read_count(reader)):
            records.extend(_read_grade(reader, f"{_FILE_NAME} category {category_index} grade {grade_index}"))
    if not reader.at_end():
        raise ValueError(
            f"{_FILE_NAME} categories end at 0x{reader.pos:X} but the string table starts at 0x{end:X}"
        )
    return records

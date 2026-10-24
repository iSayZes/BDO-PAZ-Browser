"""`skillcomboguide.bss`: the skill combos the combo guide shows, per class.

    PABR | u32 class_count | class_count x Class Combos | string table
    | u32 table_start | u32 0
    Class Combos: u32 combo_count | combo_count x Combo
    Combo: u8 class_type | u32 combo_skill_count | u32 step_count
           | step_count x (u16 skill_no | u32 command_index)

`command_index` points into the string table: the key binding text of the
step, such as `<{KeyBind:MoveBack}> + <{KeyBind:Kick}>`. Full layout in
docs/file-formats/skillcomboguide_bss.md.
"""

from __future__ import annotations

import struct
from dataclasses import dataclass

from _common.pabr_strings import HEADER_SIZE, check_rows_end, checked_string_table_start, read_string_table, string_at
from _common.record_reader import RecordReader


FILE_NAME = "skillcomboguide.bss"

_U32 = struct.Struct("<I")
_COMBO_HEAD = struct.Struct("<BII")
_STEP = struct.Struct("<HI")
_CLASS_COUNT_AT = 4


@dataclass(frozen=True)
class ComboStep:
    skill_no: int
    command_index: int
    command: str


@dataclass(frozen=True)
class Combo:
    class_type: int
    # Position of the combo in its class list, from 1, as the sheet's ComboIndex.
    combo_no: int
    combo_skill_count: int
    steps: tuple[ComboStep, ...]


def _read_combo(reader: RecordReader, combo_no: int, strings: list[str]) -> Combo:
    class_type, combo_skill_count, step_count = reader.unpack(_COMBO_HEAD)
    if step_count * _STEP.size > reader.remaining():
        raise ValueError(f"{FILE_NAME} combo step count {step_count:,} at 0x{reader.pos - 4:X} runs past the rows")
    steps = []
    for _ in range(step_count):
        skill_no, command_index = reader.unpack(_STEP)
        steps.append(ComboStep(skill_no, command_index, string_at(strings, command_index)))
    return Combo(class_type, combo_no, combo_skill_count, tuple(steps))


def parse_skillcomboguide(data: bytes) -> list[Combo]:
    """Every combo, class list by class list in file order.

    Raises ValueError on a bad magic, or when a list runs past or ends before
    the string table.
    """
    rows_end = checked_string_table_start(data, FILE_NAME)
    strings = read_string_table(data)
    reader = RecordReader(data, HEADER_SIZE, rows_end, FILE_NAME)
    (class_count,) = _U32.unpack_from(data, _CLASS_COUNT_AT)
    combos: list[Combo] = []
    for _ in range(class_count):
        (combo_count,) = reader.unpack(_U32)
        combos.extend(_read_combo(reader, combo_no, strings) for combo_no in range(1, combo_count + 1))
    check_rows_end(data, reader.pos, f"{FILE_NAME} combos")
    return combos

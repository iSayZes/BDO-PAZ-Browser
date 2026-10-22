"""`uipracticeskilltreelayout.bss`: a skill tree grid per class, in the 2016 cell format.

    PABR | u32 class_count | class_count x Class Grid | string table
    | u32 table_start | u32 0
    Class Grid: u8 class_type | u32 width | u32 height | width * height x Cell
    Cell (4 bytes): u8 cell_type | u8 arrow_type | u16 skill_no

The cell is the 2016 `ge::UISkillTreeLayout_CellValue`; cell type `2` holds a
skill. Full layout in docs/file-formats/uipracticeskilltreelayout_bss.md.
"""

from __future__ import annotations

import struct
from dataclasses import dataclass

from _common.pabr_strings import HEADER_SIZE, check_rows_end, checked_string_table_start
from _common.record_reader import RecordReader


FILE_NAME = "uipracticeskilltreelayout.bss"
# ge::UISkillTreeLayout_CellValueType_Blank and _Skill (2016 PDB).
CELL_TYPE_BLANK = 1
CELL_TYPE_SKILL = 2

_U32 = struct.Struct("<I")
_GRID_HEAD = struct.Struct("<BII")
_CELL = struct.Struct("<BBH")
_CLASS_COUNT_AT = 4


@dataclass(frozen=True)
class ClassGrid:
    class_type: int
    width: int
    height: int
    blank_cells: int
    # Skill numbers of the skill cells, in cell order.
    skill_nos: tuple[int, ...]


def _read_grid(reader: RecordReader) -> ClassGrid:
    class_type, width, height = reader.unpack(_GRID_HEAD)
    cell_count = width * height
    if cell_count * _CELL.size > reader.remaining():
        raise ValueError(f"{FILE_NAME} class {class_type} grid of {width} x {height} runs past the rows")
    cells = [reader.unpack(_CELL) for _ in range(cell_count)]
    return ClassGrid(
        class_type=class_type,
        width=width,
        height=height,
        blank_cells=sum(1 for cell_type, _, _ in cells if cell_type == CELL_TYPE_BLANK),
        skill_nos=tuple(skill_no for cell_type, _, skill_no in cells if cell_type == CELL_TYPE_SKILL),
    )


def parse_uipracticeskilltreelayout(data: bytes) -> list[ClassGrid]:
    """Every class grid in file order.

    Raises ValueError on a bad magic, or when a grid runs past or the grids
    end before the string table.
    """
    rows_end = checked_string_table_start(data, FILE_NAME)
    reader = RecordReader(data, HEADER_SIZE, rows_end, FILE_NAME)
    (class_count,) = _U32.unpack_from(data, _CLASS_COUNT_AT)
    grids = [_read_grid(reader) for _ in range(class_count)]
    check_rows_end(data, reader.pos, f"{FILE_NAME} grids")
    return grids

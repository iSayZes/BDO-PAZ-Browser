"""One skill tree grid in the 2016 cell format of `ge::UISkillTreeLayout_CellValue`.

`uiguildskilltreelayout.bss`, `uifusionskilltreelayout.bss`,
`uiproductskilltreelayout.bss` and the five
`ui_territorypolicyskilltree_*.bss` files hold one grid each:

    PABR | u32 width | u32 height | width * height x Cell | string table
    | u32 table_start | u32 0
    Cell (4 bytes): u8 cell_type | u8 arrow_type | u16 skill_no

Cells run column by column (cell index = column * height + row); cell type
`2` holds a skill. `uipracticeskilltreelayout.bss` keeps one such grid per
class and reads its cells with `read_cells`. Full layout in
docs/file-formats/bss/uiguildskilltreelayout_bss.md.
"""

from __future__ import annotations

import struct
from dataclasses import dataclass

from _common.pabr_strings import check_rows_end, checked_string_table_start
from _common.record_reader import RecordReader


TERRITORY_POLICY_FILES = tuple(
    f"ui_territorypolicyskilltree_{territory}.bss"
    for territory in ("balenos", "serendia", "calpheon", "media", "valencia")
)
SKILL_TREE_FILES = (
    "uiguildskilltreelayout.bss",
    "uifusionskilltreelayout.bss",
    "uiproductskilltreelayout.bss",
    *TERRITORY_POLICY_FILES,
)

# ge::UISkillTreeLayout_CellValueType_Blank and _Skill (2016 PDB).
CELL_TYPE_BLANK = 1
CELL_TYPE_SKILL = 2

_CELL = struct.Struct("<BBH")
_GRID_SIZE = struct.Struct("<II")
_GRID_SIZE_AT = 4


@dataclass(frozen=True)
class Cell:
    cell_type: int
    arrow_type: int
    skill_no: int


@dataclass(frozen=True)
class SkillCell:
    column: int
    row: int
    arrow_type: int
    skill_no: int


@dataclass(frozen=True)
class SkillTree:
    width: int
    height: int
    # The skill cells only, in file order (column by column).
    skill_cells: tuple[SkillCell, ...]


def read_cells(reader: RecordReader, width: int, height: int, label: str) -> list[Cell]:
    """The `width * height` cells of one grid, in file order.

    Raises ValueError when the grid runs past the reader's end.
    """
    cell_count = width * height
    if cell_count * _CELL.size > reader.remaining():
        raise ValueError(f"{label} grid of {width} x {height} runs past the rows")
    return [Cell(*reader.unpack(_CELL)) for _ in range(cell_count)]


def parse_skill_tree(data: bytes, file_name: str) -> SkillTree:
    """The grid size and its skill cells.

    Raises ValueError on a bad magic, or when the grid runs past or ends
    before the string table.
    """
    rows_end = checked_string_table_start(data, file_name)
    width, height = _GRID_SIZE.unpack_from(data, _GRID_SIZE_AT)
    reader = RecordReader(data, _GRID_SIZE_AT + _GRID_SIZE.size, rows_end, file_name)
    cells = read_cells(reader, width, height, file_name)
    check_rows_end(data, reader.pos, f"{file_name} grid")
    skill_cells = tuple(
        SkillCell(column=index // height, row=index % height, arrow_type=cell.arrow_type, skill_no=cell.skill_no)
        for index, cell in enumerate(cells)
        if cell.cell_type == CELL_TYPE_SKILL
    )
    return SkillTree(width=width, height=height, skill_cells=skill_cells)

"""`ui_skillgroup_*.bss`: the skill window layout of every class.

    PABR | u32 class_count | class_count x grid
    | u32 tab_class_count | tab_class_count x tabs
    | u32 class_slots | class_slots x u16 | string table | trailer

    grid: u8 class_type | u32 width | u32 height | width*height x cell,
          column by column (cell index = column * height + row)
    cell: u32 type_count | type_count x u8 type | u16 group_no | u8 | u8 subgroup
    tabs: u8 class_type | u32 tab_count | u32 0 | tab_count x (u32 string_index | u8 subgroup)

Cell type 2 holds a `skillgroup.bss` group; the others draw the tree lines.
The grid is the developer sheet's cell grid: skill cards sit in sheet columns
0, 3 and 6, the three card columns of the skill window. Full layout in
docs/file-formats/ui_skillgroup_bss.md.
"""

from __future__ import annotations

import struct
from dataclasses import dataclass

from _common.pabr_strings import read_string_table, string_at, string_table_start

_MAGIC = b"PABR"
_U32 = struct.Struct("<I")
_GRID_HEADER = struct.Struct("<BII")
_CELL_TAIL = struct.Struct("<HBB")
_TABS_HEADER = struct.Struct("<BII")
_TAB = struct.Struct("<IB")
_CLASS_SLOT_SIZE = 2
_CELL_TYPE_SKILL_GROUP = 2
CARD_COLUMNS = 3


@dataclass(frozen=True)
class SkillCell:
    row: int
    column: int
    group_no: int
    subgroup: int


@dataclass(frozen=True)
class ClassGrid:
    class_type: int
    width: int
    height: int
    # Skill group cells only, column by column.
    cells: tuple[SkillCell, ...]


@dataclass(frozen=True)
class Tab:
    key: str
    subgroup: int


@dataclass(frozen=True)
class SkillWindow:
    grids: tuple[ClassGrid, ...]
    tabs: dict[int, tuple[Tab, ...]]


def card_column(column: int, width: int) -> int:
    """The card column (0 left, 1 middle, 2 right) a grid column is shown in."""
    return column * CARD_COLUMNS // width


def _check(end: int, limit: int, what: str) -> None:
    if end > limit:
        raise ValueError(f"{what} runs past 0x{limit:X}")


def _parse_grid(data: bytes, pos: int, limit: int) -> tuple[ClassGrid, int]:
    _check(pos + _GRID_HEADER.size, limit, f"class grid at 0x{pos:X}")
    class_type, width, height = _GRID_HEADER.unpack_from(data, pos)
    pos += _GRID_HEADER.size
    cells: list[SkillCell] = []
    for index in range(width * height):
        _check(pos + _U32.size, limit, f"class {class_type} cell {index}")
        (type_count,) = _U32.unpack_from(data, pos)
        types_end = pos + _U32.size + type_count
        _check(types_end + _CELL_TAIL.size, limit, f"class {class_type} cell {index}")
        group_no, _, subgroup = _CELL_TAIL.unpack_from(data, types_end)
        if _CELL_TYPE_SKILL_GROUP in data[pos + _U32.size:types_end]:
            column, row = divmod(index, height)
            cells.append(SkillCell(row=row, column=column, group_no=group_no, subgroup=subgroup))
        pos = types_end + _CELL_TAIL.size
    return ClassGrid(class_type=class_type, width=width, height=height, cells=tuple(cells)), pos


def _parse_tabs(data: bytes, pos: int, limit: int, strings: list[str]) -> tuple[int, tuple[Tab, ...], int]:
    _check(pos + _TABS_HEADER.size, limit, f"tab entry at 0x{pos:X}")
    class_type, tab_count, _ = _TABS_HEADER.unpack_from(data, pos)
    pos += _TABS_HEADER.size
    _check(pos + tab_count * _TAB.size, limit, f"class {class_type} tabs")
    tabs = tuple(
        Tab(key=string_at(strings, string_index), subgroup=subgroup)
        for string_index, subgroup in _TAB.iter_unpack(data[pos:pos + tab_count * _TAB.size])
    )
    return class_type, tabs, pos + tab_count * _TAB.size


def parse_ui_skillgroup(data: bytes) -> SkillWindow:
    """Every class grid and tab list.

    Raises ValueError when a field runs past the string table or the class
    table does not end exactly where the string table starts.
    """
    if data[:4] != _MAGIC:
        raise ValueError("ui_skillgroup file does not start with PABR")

    limit = string_table_start(data)
    strings = read_string_table(data)
    (class_count,) = _U32.unpack_from(data, 4)
    pos = 8
    grids: list[ClassGrid] = []
    for _ in range(class_count):
        grid, pos = _parse_grid(data, pos, limit)
        grids.append(grid)

    _check(pos + _U32.size, limit, "tab directory")
    (tab_class_count,) = _U32.unpack_from(data, pos)
    pos += _U32.size
    tabs: dict[int, tuple[Tab, ...]] = {}
    for _ in range(tab_class_count):
        class_type, class_tabs, pos = _parse_tabs(data, pos, limit, strings)
        tabs[class_type] = class_tabs

    _check(pos + _U32.size, limit, "class table")
    (class_slots,) = _U32.unpack_from(data, pos)
    pos += _U32.size + class_slots * _CLASS_SLOT_SIZE
    if pos != limit:
        raise ValueError(f"class table ends at 0x{pos:X}, the string table starts at 0x{limit:X}")
    return SkillWindow(grids=tuple(grids), tabs=tabs)

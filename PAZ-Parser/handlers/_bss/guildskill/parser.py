"""`guildskill.bss`: the guild skill keys, placed on the guild skill tree.

    PABR | u32 row_count | row_count x Row | string table | u32 table_start | u32 0
    Row (4 bytes): u16 skill_level | u16 skill_no

The rows are read as a PABR value table (`_bss.pabr_values`). The tree is
`uiguildskilltreelayout.bss`, read by `_bss.uiskilltreelayout.parser`; a
skill cell there gives the skill's column and row in the guild window. Full
layout in docs/file-formats/guildskill_bss.md.
"""

from __future__ import annotations

from dataclasses import dataclass

from _bss.pabr_values.layout import RowCount, ValueField, ValueTable
from _bss.pabr_values.parser import parse_value_table
from _bss.uiskilltreelayout.parser import parse_skill_tree


FILE_NAME = "guildskill.bss"
TREE_FILE_NAME = "uiguildskilltreelayout.bss"

_ROWS = ValueTable(
    FILE_NAME,
    (ValueField("skill_level", "H"), ValueField("skill_no", "H")),
    RowCount.COUNTED,
)


@dataclass(frozen=True)
class TreeCell:
    """Where a skill sits in the guild skill tree grid."""

    column: int
    row: int


def parse_guild_skills(data: bytes) -> list[dict]:
    """The rows as `{"skill_level", "skill_no"}` records, in file order.

    Raises ValueError on a bad magic or rows that do not end where the string
    table starts.
    """
    return parse_value_table(data, _ROWS)


def tree_cells(tree_data: bytes) -> dict[int, TreeCell]:
    """Skill number -> its cell in `uiguildskilltreelayout.bss`; the first cell when a skill has several.

    Raises ValueError when the grid does not parse.
    """
    cells: dict[int, TreeCell] = {}
    for cell in parse_skill_tree(tree_data, TREE_FILE_NAME).skill_cells:
        cells.setdefault(cell.skill_no, TreeCell(cell.column, cell.row))
    return cells

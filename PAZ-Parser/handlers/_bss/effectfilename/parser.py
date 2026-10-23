"""`effectfilename.bss`: the hit and footstep effect grids.

    PABR | Attack Table[10] | Special Table[10] | Ground Row[30]
         | String Table | u32 string_table_start | u32 0
    Attack Table: Weapon Row[100]     Special Table: Weapon Row[501]
    Weapon Row: u32[100] effect_refs (one per armor type)
    Ground Row: u32[5] effect_refs (one per movement column)

No row count follows the magic: the grids have a fixed size. Every ref
indexes the string table; a ref to the empty string is an empty cell.
Layout 2 in docs/file-formats/effectfilename_bss.md.
"""

from __future__ import annotations

import struct
from collections.abc import Iterator
from dataclasses import dataclass

from _common.pabr_strings import check_pabr, check_rows_end, read_string_table, string_at


FILE_NAME = "effectfilename.bss"

# Grid names, as the doc's File Layout fields.
ATTACK_TABLES = "attack_tables"
SPECIAL_ATTACK_TABLES = "special_attack_tables"
GROUND_ROWS = "ground_rows"

_MAGIC_SIZE = 4
_REF_SIZE = 4
_TABLE_COUNT = 10
_ATTACK_WEAPON_ROWS = 100
_SPECIAL_WEAPON_ROWS = 501
_ARMOR_CELLS = 100
_GROUND_ROW_COUNT = 30
_GROUND_COLUMNS = 5


@dataclass(frozen=True)
class _Grid:
    """One grid: `tables` x `rows` x `columns` refs (`tables` is 0 for no table level)."""

    name: str
    tables: int
    rows: int
    columns: int

    @property
    def ref_count(self) -> int:
        return max(self.tables, 1) * self.rows * self.columns


_GRIDS = (
    _Grid(ATTACK_TABLES, _TABLE_COUNT, _ATTACK_WEAPON_ROWS, _ARMOR_CELLS),
    _Grid(SPECIAL_ATTACK_TABLES, _TABLE_COUNT, _SPECIAL_WEAPON_ROWS, _ARMOR_CELLS),
    _Grid(GROUND_ROWS, 0, _GROUND_ROW_COUNT, _GROUND_COLUMNS),
)
REF_COUNT = sum(grid.ref_count for grid in _GRIDS)


def _grid_cells(grid: _Grid, refs: tuple[int, ...], strings: list[str]) -> Iterator[dict]:
    """The filled cells of one grid in file order."""
    for index, ref in enumerate(refs):
        effect = string_at(strings, ref)
        if not effect:
            continue
        table, rest = divmod(index, grid.rows * grid.columns)
        row, column = divmod(rest, grid.columns)
        yield {
            "grid": grid.name,
            "table_index": table if grid.tables else None,
            "row_index": row,
            "column_index": column,
            "effect_ref": ref,
            "effect": effect,
        }


def parse_effectfilename_cells(data: bytes) -> list[dict]:
    """Every cell that names an effect, grid by grid in file order.

    Raises ValueError on a bad magic, a ref past the string table, or grids
    that do not end where the string table starts.
    """
    check_pabr(data, FILE_NAME)
    check_rows_end(data, _MAGIC_SIZE + REF_COUNT * _REF_SIZE, f"{FILE_NAME} grids")
    strings = read_string_table(data)
    cells: list[dict] = []
    pos = _MAGIC_SIZE
    for grid in _GRIDS:
        refs = struct.unpack_from(f"<{grid.ref_count}I", data, pos)
        pos += grid.ref_count * _REF_SIZE
        bad = next((ref for ref in refs if ref >= len(strings)), None)
        if bad is not None:
            raise ValueError(f"{FILE_NAME} {grid.name} ref {bad} is past the {len(strings)} strings")
        cells.extend(_grid_cells(grid, refs, strings))
    return cells

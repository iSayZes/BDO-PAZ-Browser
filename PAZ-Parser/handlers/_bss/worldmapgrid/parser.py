"""Reads the world map grids (docs/file-formats/worldmapgrid_bss.md).

    PABR | u8 cells[1984][2176] | u32 string_count (0) | u32 table_start | u32 0

Seven files share the layout, one byte per world cell. The grid stores no
size and no row count: the cells start right after the magic and fill the
space up to the string table. A cell covers 1,600 x 1,600 world units (8 x 8
cells per 12,800-unit sector); row 0 is the south edge (smallest z), column 0
the west edge (smallest x).
"""

from __future__ import annotations

from collections.abc import Collection, Sequence
from dataclasses import dataclass

from _common.binary import u32
from _common.pabr_strings import TRAILER_SIZE, check_rows_end, checked_string_table_start

GRID_COLUMNS = 2176
GRID_ROWS = 1984
# The cells follow the 4-byte magic; there is no u32 row count.
CELLS_AT = 4
CELL_COUNT = GRID_COLUMNS * GRID_ROWS
CELL_UNITS = 1600
# World x of column 0's west edge and world z of row 0's south edge.
GRID_MIN_X = -2_048_000
GRID_MIN_Z = -1_126_400
_STRING_COUNT_SIZE = 4
_BYTE_VALUES = 256
_FULL_BYTE = 0xFF
_BYTE_ORDER = "little"


@dataclass(frozen=True)
class CellArea:
    """Where one cell value sits: its cell count and its bounding box in cells."""

    value: int
    cell_count: int
    column_min: int
    column_max: int
    row_min: int
    row_max: int


def read_cells(data: bytes, file_name: str) -> bytes:
    """The `GRID_ROWS` x `GRID_COLUMNS` cell bytes, row by row from the south.

    Raises ValueError on a bad magic or trailer, when the cells do not end
    where the string table starts, or when the string table holds strings.
    """
    table_start = checked_string_table_start(data, file_name)
    check_rows_end(data, CELLS_AT + CELL_COUNT, f"{file_name} cells")
    string_count = u32(data, table_start)
    if string_count or table_start + _STRING_COUNT_SIZE + TRAILER_SIZE != len(data):
        raise ValueError(f"{file_name} has {string_count} strings, but the grid layout has none")
    return data[CELLS_AT:table_start]


def cell_areas(cells: bytes) -> list[CellArea]:
    """One `CellArea` per distinct cell value, in value order."""
    counts: dict[int, int] = {}
    columns: dict[int, list[int]] = {}
    rows: dict[int, list[int]] = {}
    for row in range(GRID_ROWS):
        line = cells[row * GRID_COLUMNS : (row + 1) * GRID_COLUMNS]
        for value in _line_values(line):
            needle = bytes((value,))
            counts[value] = counts.get(value, 0) + line.count(needle)
            first, last = line.find(needle), line.rfind(needle)
            box = columns.get(value)
            if box is None:
                columns[value] = [first, last]
                rows[value] = [row, row]
                continue
            box[0], box[1] = min(box[0], first), max(box[1], last)
            rows[value][1] = row
    return [
        CellArea(value, counts[value], *columns[value], *rows[value])
        for value in sorted(counts)
    ]


def split_areas(cells: bytes, split_cells: bytes, values: Collection[int]) -> dict[tuple[int, int], CellArea]:
    """One `CellArea` per (cell value, split value) pair, for the cell values in `values`.

    `split_cells` is a second grid read with `read_cells` (the territory
    grid); a pair's area holds the cells where `cells` has the value and
    `split_cells` the split value.
    """
    if len(split_cells) != len(cells):
        raise ValueError(f"the split grid has {len(split_cells)} cells, the grid {len(cells)}")
    # Stands in for every cell outside the pair; a byte none of `values` uses.
    outside = next((byte for byte in range(_BYTE_VALUES) if byte not in values), None)
    if outside is None:
        raise ValueError("every byte value is split, so no byte is left to mask the other cells")
    grid = _as_int(cells)
    fill = _as_int(bytes((outside,)) * len(cells))
    wanted = _byte_mask(cells, values)
    areas: dict[tuple[int, int], CellArea] = {}
    for split_value in sorted(set(split_cells)):
        pair = wanted & _byte_mask(split_cells, (split_value,))
        masked = ((grid & pair) | (fill & ~pair)).to_bytes(len(cells), _BYTE_ORDER)
        for area in cell_areas(masked):
            if area.value != outside:
                areas[(area.value, split_value)] = area
    return areas


def _as_int(cells: bytes) -> int:
    """The cells as one int, so `&` and `|` work on all of them at once."""
    return int.from_bytes(cells, _BYTE_ORDER)


def _byte_mask(cells: bytes, selected: Collection[int]) -> int:
    """`_as_int` of a grid that is `0xFF` where `cells` holds a selected value, else `0`."""
    table = bytes(_FULL_BYTE if byte in selected else 0 for byte in range(_BYTE_VALUES))
    return _as_int(cells.translate(table))


def merge_areas(areas: Sequence[CellArea]) -> CellArea:
    """One area over the cells of `areas`, which share a cell value: summed counts, the box around their boxes."""
    return CellArea(
        areas[0].value,
        sum(area.cell_count for area in areas),
        min(area.column_min for area in areas),
        max(area.column_max for area in areas),
        min(area.row_min for area in areas),
        max(area.row_max for area in areas),
    )


def _line_values(line: bytes) -> set[int]:
    """The distinct values of one row; a row of one value skips the set."""
    first = line[0]
    if line.count(first) == len(line):
        return {first}
    return set(line)


def world_x(column: int) -> int:
    """World x of a column's west edge."""
    return GRID_MIN_X + column * CELL_UNITS


def world_z(row: int) -> int:
    """World z of a row's south edge."""
    return GRID_MIN_Z + row * CELL_UNITS

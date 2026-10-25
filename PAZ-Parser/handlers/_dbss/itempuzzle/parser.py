"""`itempuzzle.dbss`: the inventory puzzles, items laid out on a 5 x 5 grid.

    u32 count | count x Row (120 bytes)
    Row: u16 puzzle_key | u32[25] puzzle_item_keys | u32 start_puzzle_item_key
         | i32 start_puzzle_item_index | i16 width_max_index | i16 height_max_index
         | u32 make_item_key | i16 line_count

The 2016 `gc::ItemPuzzleStaticStatus` packed. `puzzle_item_keys` is the grid
row by row, `0` for an empty cell. `itempuzzleoffset.dbss` (u32 count, then
u16 puzzle key, u32 offset, u32 size per row) points at the row start.
Layout 1 in docs/file-formats/dbss/itempuzzle_dbss.md.
"""

from __future__ import annotations

import struct

from _common.counted_rows import counted_row_values


FILE_NAME = "itempuzzle.dbss"
OFFSET_FILE = "itempuzzleoffset.dbss"

GRID_SIDE = 5
_GRID_CELLS = GRID_SIDE * GRID_SIDE
_ROW = struct.Struct(f"<H{_GRID_CELLS}IIihhIh")
_TAIL_FIELDS = (
    "start_puzzle_item_key",
    "start_puzzle_item_index",
    "width_max_index",
    "height_max_index",
    "make_item_key",
    "line_count",
)


def parse_itempuzzle_records(data: bytes) -> list[dict]:
    """Every puzzle in file order. Raises ValueError when the rows do not fill the file."""
    return [
        {
            "puzzle_key": values[0],
            "puzzle_item_keys": list(values[1 : 1 + _GRID_CELLS]),
            **dict(zip(_TAIL_FIELDS, values[1 + _GRID_CELLS :], strict=True)),
        }
        for values in counted_row_values(data, _ROW, FILE_NAME)
    ]

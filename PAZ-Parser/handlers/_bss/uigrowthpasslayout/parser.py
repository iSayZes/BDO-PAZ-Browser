"""`uigrowthpasslayout.bss`: the quest grid of each Growth Pass category.

    "PABR" | u32 layout_count | layout_count x layout | 12-byte trailer

    layout: u32 category_key | u32 col_count | u32 row_count
            | row_count x col_count x 6-byte cell, row by row

    cell:   u16 quest_chain_id | u16 quest_id | u8 cell_type | u8 unknown_05

    trailer: u32 0 | u32 trailer offset | u32 0

Full layout and the cell type values in docs/file-formats/bss/uigrowthpasslayout_bss.md.
"""

from __future__ import annotations

import struct
from dataclasses import dataclass

from _common.binary import u32
from _common.pabr_offset import PABR_MAGIC


_HEADER_SIZE = 8
_LAYOUT_HEADER = struct.Struct("<III")
_CELL = struct.Struct("<HHBB")
_TRAILER_SIZE = 12
_TRAILER_OFFSET_AT = 4


@dataclass(frozen=True)
class LayoutCell:
    category_key: int
    row: int
    col: int
    quest_chain_id: int
    quest_id: int
    cell_type: int
    unknown_05: int


@dataclass(frozen=True)
class GrowthPassLayout:
    category_key: int
    col_count: int
    row_count: int
    cells: tuple[LayoutCell, ...]


def parse_uigrowthpasslayout(data: bytes) -> list[GrowthPassLayout]:
    """Every category's grid in file order.

    Raises ValueError on a missing magic, a grid that runs past the file, or
    grids that do not end where the trailer says they do.
    """
    if len(data) < _HEADER_SIZE + _TRAILER_SIZE or data[:4] != PABR_MAGIC:
        raise ValueError("uigrowthpasslayout.bss has invalid magic.")

    layouts: list[GrowthPassLayout] = []
    pos = _HEADER_SIZE
    for _ in range(u32(data, 4)):
        layout, pos = _read_layout(data, pos)
        layouts.append(layout)

    trailer_offset = u32(data, len(data) - _TRAILER_SIZE + _TRAILER_OFFSET_AT)
    if pos != trailer_offset:
        raise ValueError(f"grids end at 0x{pos:X}, the trailer says 0x{trailer_offset:X}")
    return layouts


def _read_layout(data: bytes, pos: int) -> tuple[GrowthPassLayout, int]:
    category_key, col_count, row_count = _LAYOUT_HEADER.unpack_from(data, pos)
    cells_start = pos + _LAYOUT_HEADER.size
    cells_end = cells_start + col_count * row_count * _CELL.size
    if cells_end > len(data) - _TRAILER_SIZE:
        raise ValueError(f"category {category_key}: {col_count} x {row_count} grid runs past the file")

    cells = tuple(
        LayoutCell(category_key, index // col_count, index % col_count, chain, quest, cell_type, unknown_05)
        for index, (chain, quest, cell_type, unknown_05) in enumerate(
            _CELL.iter_unpack(data[cells_start:cells_end])
        )
    )
    return GrowthPassLayout(category_key, col_count, row_count, cells), cells_end

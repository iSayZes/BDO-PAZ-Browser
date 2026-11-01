"""The world map grids: one row per distinct cell value, not one per cell.

A grid holds 4,317,184 cells, so the table lists each value with what it
joins to (`kinds.py`), its cell count and its bounding box, in cells and in
world units. The region group grid gives a value two groups share one row
per group (`region_groups.py`).
"""

from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from bdo_models import PazEntry
from table_sort import SORT_ASC, TableSort

from _common.html import Column, e, text_list_cell
from _common.lang import handler_text
from _common.row_table import RowTableHandler
from .cell_join import GridRow
from .kinds import GridKind
from .parser import read_cells, world_x, world_z

_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"
_MAX_KEYS = 4


def _record(row: GridRow) -> dict:
    area, join = row.area, row.join
    return {
        "value": area.value,
        "keys": list(join.keys),
        "name": ", ".join(join.names) or None,
        "cell_count": area.cell_count,
        "column_min": area.column_min,
        "column_max": area.column_max,
        "row_min": area.row_min,
        "row_max": area.row_max,
        # The box's outer edges: the east and north edge of the last cell.
        "x_min": world_x(area.column_min),
        "x_max": world_x(area.column_max + 1),
        "z_min": world_z(area.row_min),
        "z_max": world_z(area.row_max + 1),
    }


class WorldMapGridHandler(RowTableHandler):
    """One handler class for the seven grids; `kind` says what a cell value joins."""

    lang_dir = _LANG_DIR

    def __init__(self, kind: GridKind) -> None:
        self.kind = kind
        self.file_name = kind.file_name

    def companions(self, entry: PazEntry) -> list[str]:
        folder = entry.internal_path.rsplit("/", 1)[0]
        return [f"{folder}/{name}" for name in self.kind.companions]

    def default_sort(self) -> TableSort | None:
        return TableSort("value", SORT_ASC)

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        return [_record(row) for row in self.kind.rows(read_cells(data, self.file_name), companions)]

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["value"], "num", sort_key="value"),
            Column(labels[self.kind.key_kind.value]),
            Column(labels["name"], sort_key="name"),
            Column(labels["cellCount"], "num", sort_key="cell_count"),
            Column(labels["columns"], "num", sort_key="column_min"),
            Column(labels["rows"], "num", sort_key="row_min"),
            Column(labels["worldX"], "num", sort_key="x_min"),
            Column(labels["worldZ"], "num", sort_key="z_min"),
        ]

    def cells(self, record: dict) -> list[str]:
        return [
            e(record["value"]),
            text_list_cell(record["keys"], _MAX_KEYS) or _EMPTY,
            e(record["name"] or _EMPTY),
            e(f"{record['cell_count']:,}"),
            self._range(record["column_min"], record["column_max"]),
            self._range(record["row_min"], record["row_max"]),
            self._range(record["x_min"], record["x_max"]),
            self._range(record["z_min"], record["z_max"]),
        ]

    def _range(self, low: int, high: int) -> str:
        return e(handler_text(self.lang, _LANG_DIR, "cells.range", low=low, high=high))

"""effectfilename.bss preview handler: one row per grid cell that names an effect.

The grids are mostly empty refs (the empty string), so only filled cells
become records. The row is the weapon type (attack and special grids) or
the ground type; the column the armor type or the movement column.
"""

from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from table_sort import TableSort

from _common.html import Column, e
from _common.lang import load_handler_strings
from _common.row_table import RowTableHandler
from .parser import (
    ATTACK_TABLES,
    FILE_NAME,
    GROUND_ROWS,
    SPECIAL_ATTACK_TABLES,
    parse_effectfilename_cells,
)


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"
_GRID_LABEL_KEYS = {
    ATTACK_TABLES: "attack",
    SPECIAL_ATTACK_TABLES: "special",
    GROUND_ROWS: "ground",
}


def _effect_text(effect: str) -> str:
    """The comma-separated effect list with a space after each comma, so it wraps."""
    return effect.replace(",", ", ")


class EffectFileNameBssHandler(RowTableHandler):
    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["grid"], sort_key="grid"),
            Column(labels["table"], "num", sort_key="table_index"),
            Column(labels["row"], "num", sort_key="row_index"),
            Column(labels["column"], "num", sort_key="column_index"),
            Column(labels["effect"], sort_key="effect"),
        ]

    def default_sort(self) -> TableSort | None:
        # File order: grid, table, row and column together give it.
        return None

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        return parse_effectfilename_cells(data)

    def cells(self, record: dict) -> list[str]:
        grids = load_handler_strings(self.lang, self.lang_dir)["grids"]
        table_index = record["table_index"]
        return [
            e(grids[_GRID_LABEL_KEYS[record["grid"]]]),
            e(_EMPTY if table_index is None else table_index),
            e(record["row_index"]),
            e(record["column_index"]),
            e(_effect_text(record["effect"])),
        ]

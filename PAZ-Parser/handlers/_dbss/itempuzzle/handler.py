"""itempuzzle.dbss preview handler: each inventory puzzle's pieces and the shape they are laid out in.

Each piece gets a letter (`A` for the first in grid order); the Pattern
column draws the grid rows up to `height_max_index` and `width_max_index`
with those letters and `.` for an empty cell.
"""
from __future__ import annotations

from collections import Counter
from collections.abc import Mapping, Sequence
from pathlib import Path
from string import ascii_uppercase

from _common.html import Column, e, html_list_cell, icon_html_label_cell
from _common.item_key import item_key_icon_path, item_key_text, item_key_text_tagged
from _common.offset_table import OffsetTableHandler, keyed_offset_handler
from _common.pa_text import pa_html
from _common.pabr_offset import parse_bare_offset_rows
from _common.row_table import RowTableHandler
from .parser import FILE_NAME, GRID_SIDE, parse_itempuzzle_records


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY_CELL = "."
_ROW_SEPARATOR = " / "


def item_puzzle_offset_handler() -> OffsetTableHandler:
    return keyed_offset_handler(_LANG_DIR, parse_bare_offset_rows, "puzzle_key", "puzzleKey")


def _pieces(grid: Sequence[int]) -> list[tuple[int, int]]:
    """`(item_key, count)` of every piece, in the order it first shows in the grid."""
    return list(Counter(key for key in grid if key).items())


def _pattern(grid: Sequence[int], letters: Mapping[int, str], width_max: int, height_max: int) -> str:
    """`AB / A.`: the grid rows up to the last used row and column, a letter per piece."""
    return _ROW_SEPARATOR.join(
        "".join(letters.get(grid[row * GRID_SIDE + col], _EMPTY_CELL) for col in range(width_max + 1))
        for row in range(height_max + 1)
    )


def _piece_label(letter: str, item_key: int, count: int) -> str:
    return f"{letter}: {item_key_text(item_key)} x{count}"


class ItemPuzzleHandler(RowTableHandler):
    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["puzzleKey"], "num", sort_key="puzzle_key"),
            # List and shape columns: they would only sort by their string form.
            Column(labels["pieces"]),
            Column(labels["pattern"]),
            Column(labels["size"]),
        ]

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        records = []
        for record in parse_itempuzzle_records(data):
            grid = record["puzzle_item_keys"]
            pieces = _pieces(grid)
            letters = {key: ascii_uppercase[index] for index, (key, _count) in enumerate(pieces)}
            records.append({
                **record,
                "pieces": [[key, count] for key, count in pieces],
                "pieces_text": ", ".join(_piece_label(letters[key], key, count) for key, count in pieces),
                "pattern": _pattern(grid, letters, record["width_max_index"], record["height_max_index"]),
                "size_text": f"{record['width_max_index'] + 1} x {record['height_max_index'] + 1}",
            })
        return records

    def _pieces_cell(self, record: dict) -> str:
        entries = [
            icon_html_label_cell(
                item_key_icon_path(key),
                f"{e(ascii_uppercase[index])}: {pa_html(item_key_text_tagged(key))} x{count:,}",
            )
            for index, (key, count) in enumerate(record["pieces"])
        ]
        return html_list_cell(entries)

    def cells(self, record: dict) -> list[str]:
        return [
            e(record["puzzle_key"]),
            self._pieces_cell(record),
            e(record["pattern"]),
            e(record["size_text"]),
        ]

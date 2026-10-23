"""itemenchantpuzzle.dbss preview handler: one row per first piece with its puzzles.

Each puzzle key links to its `itempuzzle.dbss` row.
"""

from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from _common.html import Column, e, html_list_cell, record_link
from _common.item_key import item_key_list_cell, item_key_text
from _common.row_table import RowTableHandler
from _dbss.itempuzzle.parser import FILE_NAME as PUZZLE_FILE
from .parser import FILE_NAME, KEY_FIELD, parse_itemenchantpuzzle_records


_LANG_DIR = Path(__file__).parent / "lang"
_ONE_ITEM = 1
_PUZZLE_PATH = f"gamecommondata/binary/{PUZZLE_FILE}"
_PUZZLE_KEY_FIELD = "puzzle_key"
_LINK_CLASS = "record-link"


def _puzzle_links(puzzle_keys: list[int]) -> str:
    return html_list_cell(
        [record_link(str(key), _PUZZLE_PATH, _PUZZLE_KEY_FIELD, key, _LINK_CLASS) for key in puzzle_keys]
    )


class ItemEnchantPuzzleHandler(RowTableHandler):
    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["itemKey"], "num", sort_key=KEY_FIELD),
            Column(labels["item"], sort_key="item_name"),
            Column(labels["puzzleCount"], "num", sort_key="puzzle_key_count"),
            Column(labels["puzzleKeys"]),
        ]

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        return [
            {**record, "item_name": item_key_text(record[KEY_FIELD])}
            for record in parse_itemenchantpuzzle_records(data)
        ]

    def cells(self, record: dict) -> list[str]:
        return [
            e(record[KEY_FIELD]),
            item_key_list_cell([record[KEY_FIELD]], _ONE_ITEM),
            e(record["puzzle_key_count"]),
            _puzzle_links(record["puzzle_keys"]),
        ]

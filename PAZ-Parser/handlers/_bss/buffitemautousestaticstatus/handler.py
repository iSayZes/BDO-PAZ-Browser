"""buffitemautousestaticstatus.bss preview handler: one row per item the auto-use of buff items can use."""
from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from table_sort import TableSort

from _common.html import Column, e
from _common.item_key import item_key_list_cell, item_key_text
from _common.row_table import RowTableHandler
from .parser import FILE_NAME, KEY_FIELD, parse_buffitemautouse_records


_LANG_DIR = Path(__file__).parent / "lang"
_ONE_ITEM = 1


class BuffItemAutoUseBssHandler(RowTableHandler):
    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["itemKey"], "num", sort_key=KEY_FIELD),
            Column(labels["item"], sort_key="item_name"),
            Column(labels["categoryKey"], "num", sort_key="category_key"),
        ]

    def default_sort(self) -> TableSort | None:
        # File order: the client's own order inside each category.
        return None

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        return [
            {**record, "item_name": item_key_text(record[KEY_FIELD])}
            for record in parse_buffitemautouse_records(data)
        ]

    def cells(self, record: dict) -> list[str]:
        return [
            e(record[KEY_FIELD]),
            item_key_list_cell([record[KEY_FIELD]], _ONE_ITEM),
            e(record["category_key"]),
        ]

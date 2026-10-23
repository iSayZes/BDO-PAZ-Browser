"""itemchange.bss preview handler: one row per Change Item conversion."""

from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from _common.html import Column, e
from _common.item_key import item_key_list_cell, item_key_text
from _common.row_table import RowTableHandler
from .parser import FILE_NAME, KEY_FIELD, parse_itemchange_records


_LANG_DIR = Path(__file__).parent / "lang"
_ONE_ITEM = 1
# Each item key field and the record field that holds its name.
_ITEM_FIELDS = (
    ("from_item_key", "from_item_name"),
    ("to_item_key", "to_item_name"),
)


class ItemChangeBssHandler(RowTableHandler):
    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["key"], "num", sort_key=KEY_FIELD),
            Column(labels["fromItem"], sort_key="from_item_name"),
            Column(labels["toItem"], sort_key="to_item_name"),
            Column(labels["type"], "num", sort_key="type"),
        ]

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        return [
            {**row, **{name: item_key_text(row[key]) for key, name in _ITEM_FIELDS}}
            for row in parse_itemchange_records(data)
        ]

    def cells(self, record: dict) -> list[str]:
        return [
            e(record[KEY_FIELD]),
            *(item_key_list_cell([record[key]], _ONE_ITEM) for key, _ in _ITEM_FIELDS),
            e(record["type"]),
        ]

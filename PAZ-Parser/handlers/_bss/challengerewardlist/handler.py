"""challengerewardlist.bss preview handler: one row per challenge reward item key."""
from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from _common.html import Column, e
from _common.item_key import item_key_list_cell, item_key_text
from _common.row_table import RowTableHandler
from .parser import FILE_NAME, KEY_FIELD, parse_challengerewardlist_records


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"
_ONE_ITEM = 1


class ChallengeRewardListHandler(RowTableHandler):
    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["itemKey"], "num", sort_key=KEY_FIELD),
            Column(labels["itemId"], "num", sort_key="item_id"),
            Column(labels["enchantLevel"], "num", sort_key="enchant_level"),
            Column(labels["item"], sort_key="item_name"),
        ]

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        return [
            {**record, "item_name": item_key_text(record[KEY_FIELD]) if record["item_id"] else ""}
            for record in parse_challengerewardlist_records(data)
        ]

    def cells(self, record: dict) -> list[str]:
        return [
            e(record[KEY_FIELD]),
            e(record["item_id"]),
            e(record["enchant_level"]),
            item_key_list_cell([record[KEY_FIELD]], _ONE_ITEM) if record["item_id"] else _EMPTY,
        ]

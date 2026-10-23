"""itemgroupingstaticstatus.bss preview handler: one row per item group type with its items."""

from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from _common.html import Column, e
from _common.linked_items import item_list_cell, item_list_fields
from _common.row_table import RowTableHandler
from .parser import FILE_NAME, KEY_FIELD, parse_itemgrouping_groups


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"


class ItemGroupingBssHandler(RowTableHandler):
    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["itemGroupType"], "num", sort_key=KEY_FIELD),
            Column(labels["itemCount"], "num", sort_key="item_count"),
            Column(labels["items"]),
        ]

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        return [{**group, **item_list_fields(group["item_ids"])} for group in parse_itemgrouping_groups(data)]

    def cells(self, record: dict) -> list[str]:
        return [
            e(record[KEY_FIELD]),
            e(record["item_count"] or _EMPTY),
            item_list_cell(record["item_ids"]),
        ]

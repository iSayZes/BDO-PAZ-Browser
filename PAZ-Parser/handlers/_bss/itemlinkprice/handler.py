"""itemlinkprice.bss preview handler: each item next to the item its price follows."""
from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from _common.html import Column, e
from _common.item_key import item_key_list_cell, item_key_text
from _common.row_table import RowTableHandler
from .parser import FILE_NAME, parse_itemlinkprice_records


_LANG_DIR = Path(__file__).parent / "lang"


class ItemLinkPriceHandler(RowTableHandler):
    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["itemKey"], "num", sort_key="price_follow_item_key"),
            Column(labels["item"], sort_key="price_follow_item_name"),
            Column(labels["targetItemKey"], "num", sort_key="price_target_item_key"),
            Column(labels["targetItem"], sort_key="price_target_item_name"),
        ]

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        return [
            {
                **record,
                "price_follow_item_name": item_key_text(record["price_follow_item_key"]),
                "price_target_item_name": item_key_text(record["price_target_item_key"]),
            }
            for record in parse_itemlinkprice_records(data)
        ]

    def cells(self, record: dict) -> list[str]:
        return [
            e(record["price_follow_item_key"]),
            item_key_list_cell([record["price_follow_item_key"]], 1),
            e(record["price_target_item_key"]),
            item_key_list_cell([record["price_target_item_key"]], 1),
        ]

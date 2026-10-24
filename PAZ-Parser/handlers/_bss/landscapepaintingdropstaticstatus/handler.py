"""landscapepaintingdropstaticstatus.bss preview handler: one row per landscape painting with its drop item."""
from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from _common.html import Column, e
from _common.item_key import item_key_list_cell, item_key_text
from _common.loc import loc_text
from _common.row_table import RowTableHandler
from .parser import FILE_NAME, KEY_FIELD, parse_landscapepaintingdrop_records


_LANG_DIR = Path(__file__).parent / "lang"
_ONE_ITEM = 1
_EMPTY = "-"
# LOC type 126 names a landscape painting by its type (str_id1).
LOC_LANDSCAPE_PAINTING = 126


class LandscapePaintingDropBssHandler(RowTableHandler):
    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["type"], "num", sort_key=KEY_FIELD),
            Column(labels["name"], sort_key="name"),
            Column(labels["dropItem"], sort_key="drop_item_name"),
        ]

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        return [
            {
                **record,
                "name": loc_text(LOC_LANDSCAPE_PAINTING, record[KEY_FIELD]) or record["name_kr"],
                "drop_item_name": item_key_text(record["drop_item_key"]),
            }
            for record in parse_landscapepaintingdrop_records(data)
        ]

    def cells(self, record: dict) -> list[str]:
        return [
            e(record[KEY_FIELD]),
            e(record["name"]) if record["name"] else _EMPTY,
            item_key_list_cell([record["drop_item_key"]], _ONE_ITEM),
        ]

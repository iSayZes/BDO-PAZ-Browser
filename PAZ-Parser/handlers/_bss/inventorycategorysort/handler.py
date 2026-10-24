"""inventorycategorysort.bss preview handler: one row per inventory category."""
from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from _common.html import Column, e
from _common.loc import loc_lookup
from _common.pa_text import strip_pa_tags
from _common.row_table import RowTableHandler
from .parser import FILE_NAME, KEY_FIELD, parse_inventorycategorysort_records


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"
# LOC type 122 names a category by (str_id1 unknown_name_kr_00, str_id2 category_key).
LOC_INVENTORY_CATEGORY = 122


def category_name(record: dict) -> str:
    """The category's LOC type 122 name, else its Korean name."""
    text = loc_lookup(LOC_INVENTORY_CATEGORY, record["unknown_name_kr_00"], record[KEY_FIELD])
    return strip_pa_tags(text).strip() or record["name_kr"]


class InventoryCategorySortBssHandler(RowTableHandler):
    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["categoryKey"], "num", sort_key=KEY_FIELD),
            Column(labels["name"], sort_key="name"),
        ]

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        return [
            {**record, "name": category_name(record)}
            for record in parse_inventorycategorysort_records(data)
        ]

    def cells(self, record: dict) -> list[str]:
        return [
            e(record[KEY_FIELD]),
            e(record["name"]) if record["name"] else _EMPTY,
        ]

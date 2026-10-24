"""limiteditemsubgroup.bss preview handler: one row per limited shop item of an item subgroup."""
from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from table_sort import TableSort

from _common.html import Column, e
from _common.item_key import item_key_list_cell, item_key_text
from _common.lang import handler_text
from _common.row_table import RowTableHandler
from .parser import FILE_NAME, KEY_FIELD, parse_limiteditemsubgroup_records


_LANG_DIR = Path(__file__).parent / "lang"
_ONE_ITEM = 1
# The reset types the NPC shop Lua names (panel_dialog_npcshop_all_1, client
# 3482): LUA_LIMITEDITEMSHOP_*_DAY, _WEEK, _MONTH and _SIEGE.
RESET_TYPES = (1, 2, 3, 4)


class LimitedItemSubGroupBssHandler(RowTableHandler):
    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["subgroupKey"], "num", sort_key=KEY_FIELD),
            Column(labels["item"], sort_key="item_name"),
            Column(labels["purchaseSubject"], "num", sort_key="purchase_subject"),
            Column(labels["purchaseCountLimit"], "num", sort_key="purchase_count_limit"),
            Column(labels["resetType"], sort_key="reset_type"),
        ]

    def default_sort(self) -> TableSort | None:
        # File order keeps each subgroup's items together.
        return None

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        return [
            {**record, "item_name": item_key_text(record["item_key"])}
            for record in parse_limiteditemsubgroup_records(data)
        ]

    def _reset_type_text(self, reset_type: int) -> str:
        """`1 Day`: the reset type and its name, or the bare value outside the Lua's four."""
        if reset_type not in RESET_TYPES:
            return str(reset_type)
        return f"{reset_type} {handler_text(self.lang, _LANG_DIR, f'resetTypes.{reset_type}')}"

    def cells(self, record: dict) -> list[str]:
        return [
            e(record[KEY_FIELD]),
            item_key_list_cell([record["item_key"]], _ONE_ITEM),
            e(record["purchase_subject"]),
            e(f"{record['purchase_count_limit']:,}"),
            e(self._reset_type_text(record["reset_type"])),
        ]

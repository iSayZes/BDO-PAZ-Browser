from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from bdo_models import PazEntry

from _bss.jewelgroupstaticstatus.names import jewel_groups
from _bss.jewelgroupstaticstatus.parser import FILE_NAME as JEWEL_GROUP_FILE
from _common.html import Column, e, icon_cell
from _common.icon_index import IconKind, icon_path
from _common.item_key import item_name_tagged
from _common.lang import load_handler_strings
from _common.pa_text import pa_cell, pa_fields
from _common.row_table import RowTableHandler
from _dbss.itemenchant.handler import LANG_DIR as ITEM_ENCHANT_LANG_DIR, sibling_paths
from _dbss.itemenchant.labels import crystal_group_label
from .parser import FILE_NAME, OFFSET_FILE, parse_itemenchantbackend_records


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"


class ItemEnchantBackendHandler(RowTableHandler):
    """One row per item from its level-0 block: the access level and the crystal group."""

    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def companions(self, entry: PazEntry) -> list[str]:
        # The jewel group table is optional: without it crystal groups show as numbers.
        return sibling_paths(entry, [OFFSET_FILE, JEWEL_GROUP_FILE])

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        offset_raw = companions.get(OFFSET_FILE)
        if offset_raw is None:
            raise ValueError(f"{OFFSET_FILE} companion not found.")

        # The crystal group texts are the itemenchant.dbss ones.
        values = load_handler_strings(self.lang, ITEM_ENCHANT_LANG_DIR)["values"]
        groups = jewel_groups(companions.get(JEWEL_GROUP_FILE))
        return [
            {
                **record,
                **pa_fields("item_name", item_name_tagged(record["item_id"])),
                "icon_path": icon_path(IconKind.ITEM, record["item_id"]),
                "crystal_group_label": crystal_group_label(record["crystal_group"], groups, values),
            }
            for record in parse_itemenchantbackend_records(data, offset_raw)
        ]

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["itemId"], "num", sort_key="item_id"),
            Column(labels["icon"], sort_key="icon_path"),
            Column(labels["item"], sort_key="item_name"),
            Column(labels["maxLevel"], "num", sort_key="max_enchant_level"),
            Column(labels["accessLevel"], "num", sort_key="item_access_level"),
            Column(labels["crystalGroup"], sort_key="crystal_group_label"),
        ]

    def cells(self, record: dict) -> list[str]:
        return [
            e(record["item_id"]),
            icon_cell(record["icon_path"]) if record["icon_path"] else _EMPTY,
            pa_cell(record, "item_name") if record["item_name"] else e(record["item_id"]),
            e(record["max_enchant_level"]),
            e(record["item_access_level"]),
            e(record["crystal_group_label"] or _EMPTY),
        ]

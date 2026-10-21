"""instancefieldreward.dbss preview handler: the reward item groups of each instance dungeon."""
from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from _bss.itemmaingroup.parser import ITEMMAINGROUP_PATH
from _common.html import Column, e, html_list_cell, record_link, text_list_cell
from _common.offset_table import OffsetTableHandler, keyed_offset_handler
from _common.row_table import RowTableHandler
from _common.town import town_name
from .parser import FILE_NAME, KEY_FIELD, parse_instancefieldreward_records, parse_instancefieldrewardoffset_rows


_LANG_DIR = Path(__file__).parent / "lang"
_LINK_CLASS = "record-link"
_MAX_REGIONS = 10


def instance_field_reward_offset_handler() -> OffsetTableHandler:
    return keyed_offset_handler(_LANG_DIR, parse_instancefieldrewardoffset_rows, KEY_FIELD, "instanceDungeonNo")


def _region_text(region_key: int) -> str:
    name = town_name(region_key)
    return f"{name} ({region_key})" if name else str(region_key)


def _item_groups_cell(item_groups: list[int]) -> str:
    return html_list_cell([
        record_link(str(group), ITEMMAINGROUP_PATH, "group_id", group, _LINK_CLASS) if group else "-"
        for group in item_groups
    ])


class InstanceFieldRewardHandler(RowTableHandler):
    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["instanceDungeonNo"], "num", sort_key=KEY_FIELD),
            Column(labels["learnSkill"], "num", sort_key="learn_skill"),
            Column(labels["itemGroups"]),
            Column(labels["relatedRegions"]),
        ]

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        return [
            {**record, "related_region_names": [_region_text(key) for key in record["related_regions"]]}
            for record in parse_instancefieldreward_records(data)
        ]

    def cells(self, record: dict) -> list[str]:
        return [
            e(record[KEY_FIELD]),
            e(record["learn_skill"]),
            _item_groups_cell(record["item_groups"]),
            text_list_cell(record["related_region_names"], _MAX_REGIONS) or "-",
        ]

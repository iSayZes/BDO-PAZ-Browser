"""enchantactiveskillitem.bss preview handler: each gear level with the skill it grants."""
from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from _common.html import Column, e, icon_html_label_cell, record_link
from _common.icon_index import IconKind, icon_path
from _common.item_key import item_key_list_cell, item_key_text
from _common.lookup_builders import SKILL
from _common.pa_text import pa_cell, pa_fields
from _common.row_table import RowTableHandler
from _common.skill import skill_name_tagged, split_skill_key
from .parser import FILE_NAME, parse_enchantactiveskillitem_records


_LANG_DIR = Path(__file__).parent / "lang"
_LINK_CLASS = "record-link"


def _skill_fields(skill_key: int) -> dict:
    """The skill number, level and LOC name of a skill key."""
    skill_no, skill_level = split_skill_key(skill_key)
    return {"skill_no": skill_no, "skill_level": skill_level, **pa_fields("skill_name", skill_name_tagged(skill_no))}


class EnchantActiveSkillItemHandler(RowTableHandler):
    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["itemKey"], "num", sort_key="item_key"),
            Column(labels["item"], sort_key="item_name"),
            Column(labels["skillNo"], "num", sort_key="skill_no"),
            Column(labels["skill"], sort_key="skill_name"),
            Column(labels["skillLevel"], "num", sort_key="skill_level"),
        ]

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        return [
            {
                **record,
                "item_name": item_key_text(record["item_key"]),
                **_skill_fields(record["skill_key"]),
            }
            for record in parse_enchantactiveskillitem_records(data)
        ]

    def cells(self, record: dict) -> list[str]:
        skill_no = record["skill_no"]
        return [
            e(record["item_key"]),
            item_key_list_cell([record["item_key"]], 1),
            record_link(str(skill_no), SKILL, "skill_no", skill_no, _LINK_CLASS),
            icon_html_label_cell(icon_path(IconKind.SKILL, skill_no), pa_cell(record, "skill_name")),
            e(record["skill_level"]),
        ]

"""skillawakeningability2.bss preview handler: the Skill Add-on options of each skill."""
from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from bdo_models import PazEntry

from _common.html import Column, e, icon_html_label_cell
from _common.icon_index import IconKind, icon_path
from _common.pa_text import pa_cell, pa_fields, pa_key, pa_list_cell, pa_list_fields
from _common.row_table import RowTableHandler
from _common.skill import skill_name_tagged
from _common.skill_cells import skill_link
from _dbss.skillawakeningability.parser import FILE_NAME as ABILITY_FILE
from _dbss.skillawakeningability.text import ability_description_tagged, korean_descriptions
from .parser import FILE_NAME, KEY_FIELD, parse_skillawakeningability2_records


_LANG_DIR = Path(__file__).parent / "lang"
ADD_ONS_FIELD = "add_ons"
# Options shown in the cell before the rest collapse into a hoverable count.
_MAX_ADD_ONS = 3


def _add_on_texts(ability_indexes: list[int], korean: Mapping[int, str]) -> list[str]:
    """Each option's tagged effect text, else its ability index."""
    return [
        ability_description_tagged(index, korean.get(index, "")) or str(index)
        for index in ability_indexes
    ]


class SkillAwakeningAbility2Handler(RowTableHandler):
    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["skillNo"], "num", sort_key=KEY_FIELD),
            Column(labels["skill"], sort_key="skill"),
            Column(labels["abilityCount"], "num", sort_key="ability_count"),
            Column(labels["addOns"]),
        ]

    def companions(self, entry: PazEntry) -> list[str]:
        folder = entry.internal_path.rsplit("/", 1)[0]
        return [f"{folder}/{ABILITY_FILE}"]

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        # Optional: without it the options keep their LOC text only.
        ability_raw = companions.get(ABILITY_FILE)
        korean = korean_descriptions(ability_raw) if ability_raw else {}
        return [
            {
                **record,
                **pa_fields("skill", skill_name_tagged(record[KEY_FIELD])),
                **pa_list_fields(ADD_ONS_FIELD, _add_on_texts(record["ability_indexes"], korean)),
            }
            for record in parse_skillawakeningability2_records(data)
        ]

    def cells(self, record: dict) -> list[str]:
        skill_no = record[KEY_FIELD]
        return [
            skill_link(skill_no, str(skill_no)),
            icon_html_label_cell(icon_path(IconKind.SKILL, skill_no), pa_cell(record, "skill")),
            e(record["ability_count"]),
            pa_list_cell(record[pa_key(ADD_ONS_FIELD)], _MAX_ADD_ONS),
        ]

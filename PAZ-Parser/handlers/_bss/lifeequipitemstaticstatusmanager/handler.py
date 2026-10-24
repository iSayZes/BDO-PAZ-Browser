"""lifeequipitemstaticstatusmanager.bss preview handler: one row per effect type of a Life Skill tab.

Life stat types with an empty list get no row. The life skill name is the
client's GAME sheet text (`CppEnums.LifeExperienceString`), the effect type
name the 2016 `gc::BuffModule::Type` member the buff view uses.
"""

from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from _common.html import Column, e
from _common.row_table import RowTableHandler
from _dbss.buff.effect import EFFECT_TYPE_NAMES, effect_type_text
from _dbss.lifeexp.labels import life_skill_name
from .parser import FILE_NAME, parse_life_equip_records


_LANG_DIR = Path(__file__).parent / "lang"


class LifeEquipItemStaticStatusManagerBssHandler(RowTableHandler):
    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["lifeStatType"], "num", sort_key="life_stat_type"),
            Column(labels["lifeSkill"], sort_key="life_skill_name"),
            Column(labels["effectType"], sort_key="effect_type"),
        ]

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        return [
            {
                **record,
                "life_skill_name": life_skill_name(record["life_stat_type"]),
                "effect_type_name": EFFECT_TYPE_NAMES.get(record["effect_type"], ""),
            }
            for record in parse_life_equip_records(data)
        ]

    def cells(self, record: dict) -> list[str]:
        return [
            e(record["life_stat_type"]),
            e(record["life_skill_name"]),
            e(effect_type_text(record["effect_type"])),
        ]

"""skillawakeningability.dbss preview handler: each Skill Add-on effect with its buff and text."""
from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from _common.buff import buff_label, buff_list_cell
from _common.html import Column, e
from _common.offset_table import OffsetTableHandler, keyed_offset_handler
from _common.pa_text import pa_cell, pa_fields
from _common.row_table import RowTableHandler
from .parser import (
    FILE_NAME,
    KEY_FIELD,
    parse_skillawakeningability_records,
    parse_skillawakeningabilityoffset_rows,
)
from .text import ability_description_tagged


_LANG_DIR = Path(__file__).parent / "lang"
_ONE_BUFF = 1


def skill_awakening_ability_offset_handler() -> OffsetTableHandler:
    return keyed_offset_handler(_LANG_DIR, parse_skillawakeningabilityoffset_rows, KEY_FIELD, "abilityIndex")


class SkillAwakeningAbilityHandler(RowTableHandler):
    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["abilityIndex"], "num", sort_key=KEY_FIELD),
            Column(labels["buff"], sort_key="buff_id"),
            Column(labels["effect"], sort_key="description"),
        ]

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        return [
            {
                **record,
                "buff": buff_label(record["buff_id"]),
                **pa_fields("description", ability_description_tagged(record[KEY_FIELD], record["description_kr"])),
            }
            for record in parse_skillawakeningability_records(data)
        ]

    def cells(self, record: dict) -> list[str]:
        return [
            e(record[KEY_FIELD]),
            buff_list_cell([record["buff_id"]], _ONE_BUFF),
            pa_cell(record, "description"),
        ]

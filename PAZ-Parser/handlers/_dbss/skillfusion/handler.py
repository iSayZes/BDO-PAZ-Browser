"""skillfusion.dbss preview handler: each enhanced skill with its main and sub skill."""
from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from _common.html import Column, e, record_link
from _common.lookup_builders import SKILL
from _common.offset_table import OffsetTableHandler, keyed_offset_handler
from _common.row_table import RowTableHandler
from _common.skill import skill_name, split_skill_key
from .parser import FILE_NAME, KEY_FIELD, parse_skillfusion_records, parse_skillfusionoffset_rows


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"
_LINK_CLASS = "record-link"
# key field -> the prefix of its skill number and name fields.
_SKILL_FIELDS = {
    KEY_FIELD: "fusion_skill",
    "main_skill_key": "main_skill",
    "sub_skill_key": "sub_skill",
}


def skill_fusion_offset_handler() -> OffsetTableHandler:
    return keyed_offset_handler(_LANG_DIR, parse_skillfusionoffset_rows, KEY_FIELD, "skillKey")


def _skill_fields(record: dict) -> dict:
    """`<prefix>_no` and `<prefix>_name` for each skill key of a row."""
    fields: dict = {}
    for key_field, prefix in _SKILL_FIELDS.items():
        skill_no, _level = split_skill_key(record[key_field])
        fields[f"{prefix}_no"] = skill_no
        fields[f"{prefix}_name"] = skill_name(skill_no)
    return fields


def _skill_link(skill_no: int) -> str:
    return record_link(str(skill_no), SKILL, "skill_no", skill_no, _LINK_CLASS)


class SkillFusionHandler(RowTableHandler):
    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["skillNo"], "num", sort_key="fusion_skill_no"),
            Column(labels["skill"], sort_key="fusion_skill_name"),
            Column(labels["mainSkillNo"], "num", sort_key="main_skill_no"),
            Column(labels["mainSkill"], sort_key="main_skill_name"),
            Column(labels["subSkillNo"], "num", sort_key="sub_skill_no"),
            Column(labels["subSkill"], sort_key="sub_skill_name"),
            Column(labels["slot"], "num", sort_key="slot_no"),
            Column(labels["order"], "num", sort_key="order_no"),
        ]

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        return [{**record, **_skill_fields(record)} for record in parse_skillfusion_records(data)]

    def cells(self, record: dict) -> list[str]:
        return [
            _skill_link(record["fusion_skill_no"]),
            e(record["fusion_skill_name"] or _EMPTY),
            _skill_link(record["main_skill_no"]),
            e(record["main_skill_name"] or _EMPTY),
            _skill_link(record["sub_skill_no"]),
            e(record["sub_skill_name"] or _EMPTY),
            e(record["slot_no"]),
            e(record["order_no"]),
        ]

"""classcooltimeuilist.bss preview handler: one row per skill of a class type's list.

Class types with an empty list get no row. The class name is LOC type 21,
the skill name LOC type 10 (else the Korean `skilltype.dbss` name).
"""

from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from _common.class_type import class_name
from _common.html import Column, e
from _common.row_table import RowTableHandler
from _common.skill import skill_name
from .parser import FILE_NAME, parse_cooltime_records


_LANG_DIR = Path(__file__).parent / "lang"


class ClassCoolTimeUiListBssHandler(RowTableHandler):
    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["classType"], "num", sort_key="class_type"),
            Column(labels["className"], sort_key="class_name"),
            Column(labels["showType"], "num", sort_key="show_type"),
            Column(labels["skillNo"], "num", sort_key="skill_no"),
            Column(labels["skillName"], sort_key="skill_name"),
        ]

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        return [
            {
                **record,
                "class_name": class_name(record["class_type"]),
                "skill_name": skill_name(record["skill_no"]),
            }
            for record in parse_cooltime_records(data)
        ]

    def cells(self, record: dict) -> list[str]:
        return [
            e(record["class_type"]),
            e(record["class_name"]),
            e(record["show_type"]),
            e(record["skill_no"]),
            e(record["skill_name"]),
        ]

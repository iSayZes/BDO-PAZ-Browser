"""instancefieldcommon.bss preview handler: the entry limits of each instance type and mode."""
from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from _common.html import Column, e
from _common.quest.quest import quest_title
from _common.row_table import RowTableHandler
from .parser import FILE_NAME, parse_instancefieldcommon_records


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"


class InstanceFieldCommonHandler(RowTableHandler):
    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["instanceType"], "num", sort_key="instance_type"),
            Column(labels["instanceMode"], "num", sort_key="instance_mode"),
            Column(labels["level"], "num", sort_key="limited_character_level"),
            Column(labels["quest"], sort_key="quest"),
            Column(labels["questName"], sort_key="quest_name"),
            Column(labels["message"], sort_key="limited_quest_text_kr"),
        ]

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        return [
            {
                **record,
                "quest": f"{record['limited_quest_group']}, {record['limited_quest_id']}",
                "quest_name": quest_title(record["limited_quest_group"], record["limited_quest_id"]) or None,
            }
            for record in parse_instancefieldcommon_records(data)
        ]

    def cells(self, record: dict) -> list[str]:
        return [
            e(record["instance_type"]),
            e(record["instance_mode"]),
            e(record["limited_character_level"]),
            e(record["quest"]),
            e(record["quest_name"] or _EMPTY),
            e(record["limited_quest_text_kr"] or _EMPTY),
        ]

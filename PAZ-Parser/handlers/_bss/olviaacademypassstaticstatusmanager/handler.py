"""olviaacademypassstaticstatusmanager.bss preview handler: one row per pass step.

The step column shows `quest_index + 1`, the number the quest titles carry
("Gathering Time! 1." is `quest_index` 0). Both quests link to their rows in
`olviaacademypassquestlist.bss`, whose view links each quest back to its
step by `base_quest`.
"""

from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from _common.html import Column, e
from _common.row_table import RowTableHandler
from _bss.allquestlist.olvia_academy import PASS_LIST, pass_type_name, quest_link, quest_text
from .parser import FILE_NAME, parse_pass_records


_LANG_DIR = Path(__file__).parent / "lang"


class OlviaAcademyPassBssHandler(RowTableHandler):
    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["passType"], "num", sort_key="pass_type"),
            Column(labels["passTypeName"], sort_key="pass_type_name"),
            Column(labels["step"], "num", sort_key="quest_index"),
            Column(labels["baseQuest"], sort_key="base_quest_text"),
            Column(labels["passQuest"], sort_key="pass_quest_text"),
        ]

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        return [
            {
                **record,
                "pass_type_name": pass_type_name(record["pass_type"]),
                "base_quest_text": quest_text(record["base_quest"]),
                "pass_quest_text": quest_text(record["pass_quest"]),
            }
            for record in parse_pass_records(data)
        ]

    def cells(self, record: dict) -> list[str]:
        return [
            e(record["pass_type"]),
            e(record["pass_type_name"]),
            e(record["quest_index"] + 1),
            quest_link(record["base_quest"], PASS_LIST),
            quest_link(record["pass_quest"], PASS_LIST),
        ]

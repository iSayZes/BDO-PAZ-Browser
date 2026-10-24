"""olviaacademycurriculumss.bss preview handler: one row per subject, then one per reward group.

Each row names its curriculum or family reward, its subject or reward group
and the start quest, all from the RESOURCE sheet and LOC type 18 when LOC is
loaded, and lists its quests. Every quest links to its row in the curriculum
or reward quest list, whose views link back here by `row_ref`.
"""

from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from _common.html import Column, e, html_list_cell
from _common.lang import load_handler_strings
from _common.row_table import RowTableHandler
from _bss.allquestlist.olvia_academy import CURRICULUM_LIST, REWARD_LIST, quest_link, quest_text, resource_text
from .parser import CURRICULUM_SECTION, FILE_NAME, parse_curriculum_records


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"
_LINE_BREAK = "<br>"


def _shown_fields(record: dict) -> dict:
    """The columns both row kinds share: the curriculum or reward, then the subject or reward group."""
    if record["section"] == CURRICULUM_SECTION:
        return {
            "parent_index": record["curriculum_index"],
            "parent_text": resource_text(record["curriculum_title"]),
            "index": record["subject_index"],
            "title_text": resource_text(record["subject_title"]),
            "start_quest_text": quest_text(record["start_quest"]),
        }
    return {
        "parent_index": record["reward_index"],
        "parent_text": resource_text(record["reward_title"]),
        "index": record["reward_group_index"],
        "title_text": resource_text(record["reward_group_title"]),
        "start_quest_text": None,
    }


class OlviaAcademyCurriculumBssHandler(RowTableHandler):
    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["section"], sort_key="section"),
            Column(labels["parentIndex"], "num", sort_key="parent_index"),
            Column(labels["parent"], sort_key="parent_text"),
            Column(labels["index"], "num", sort_key="index"),
            Column(labels["title"], sort_key="title_text"),
            Column(labels["startQuest"], sort_key="start_quest_text"),
            Column(labels["questCount"], "num", sort_key="quest_count"),
            Column(labels["quests"]),
        ]

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        return [
            {**record, **_shown_fields(record), "quest_count": len(record["quests"])}
            for record in parse_curriculum_records(data)
        ]

    def cells(self, record: dict) -> list[str]:
        sections = load_handler_strings(self.lang, _LANG_DIR)["sections"]
        quest_list = CURRICULUM_LIST if record["section"] == CURRICULUM_SECTION else REWARD_LIST
        return [
            e(sections[record["section"]]),
            e(record["parent_index"]),
            e(record["parent_text"] or _EMPTY),
            e(record["index"]),
            e(record["title_text"] or _EMPTY),
            e(record["start_quest_text"] or _EMPTY),
            e(record["quest_count"]),
            html_list_cell([quest_link(quest, quest_list) for quest in record["quests"]], separator=_LINE_BREAK) or _EMPTY,
        ]

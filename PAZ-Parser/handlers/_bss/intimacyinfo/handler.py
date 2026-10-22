"""intimacyinfo.bss preview handler: per NPC the quests, shops, knowledge and talks its amity unlocks."""
from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from bdo_models import PazEntry

from _common.character import character_name
from _common.character_link import (
    character_key_cell,
    character_row_ids,
    characterstatic_offset_companion,
    has_character_row,
)
from _common.html import Column, e, html_list_cell
from _common.knowledge import knowledge_name
from _common.lang import load_handler_strings
from _common.quest.dialog import dialog_name
from _common.quest.quest import quest_title
from _common.row_table import RowTableHandler
from .parser import FILE_NAME, KEY_FIELD, QUEST_TYPE, parse_intimacyinfo_records


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"
_LINE_SEPARATOR = "; "
# CppEnums.IntimacyInformationTypeInfo values whose entry names a knowledge or a dialog.
_KNOWLEDGE_TYPE = 3
_TALK_TYPE = 4


def _quest_text(info: dict) -> str:
    """`Title (2023/4)`, or the quest number alone without a LOC title."""
    number = f"{info['quest_group']}/{info['quest_id']}"
    title = quest_title(info["quest_group"], info["quest_id"])
    return f"{title} ({number})" if title else number


def _knowledge_text(info: dict) -> str:
    key = info["knowledge_key"]
    name = knowledge_name(key)
    return f"{name} ({key})" if name else str(key)


def _dialog_text(character_key: int, info: dict) -> str:
    index = info["dialog_index"]
    name = dialog_name(character_key, index)
    return f"{name} ({index})" if name else str(index)


def _target_text(character_key: int, info: dict) -> str:
    """What the entry links: a quest, a knowledge, a dialog, or '' for a shop."""
    if info["type_index"] == QUEST_TYPE:
        return _quest_text(info)
    if info["type_index"] == _KNOWLEDGE_TYPE:
        return _knowledge_text(info)
    if info["type_index"] == _TALK_TYPE:
        return _dialog_text(character_key, info)
    return ""


class IntimacyInfoBssHandler(RowTableHandler):
    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def companions(self, entry: PazEntry) -> list[str]:
        return [characterstatic_offset_companion(entry.internal_path)]

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["npcKey"], "num", sort_key=KEY_FIELD),
            Column(labels["npc"], sort_key="name"),
            Column(labels["entryCount"], "num", sort_key="entry_count"),
            Column(labels["entries"], sort_key="entries_text"),
        ]

    def _entry_text(self, character_key: int, info: dict) -> str:
        """`Quest: Title (2023/4) ▲ 100`, in the UI language."""
        strings = load_handler_strings(self.lang, _LANG_DIR)
        kind = strings["types"].get(str(info["type_index"]), str(info["type_index"]))
        operator = strings["operators"].get(str(info["operator_type"]), str(info["operator_type"]))
        target = _target_text(character_key, info)
        head = f"{kind}: {target}" if target else kind
        return f"{head} {operator} {info['intimacy']}"

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        row_ids = character_row_ids(companions)
        records = []
        for record in parse_intimacyinfo_records(data):
            key = record[KEY_FIELD]
            entries = [self._entry_text(key, info) for info in record["infos"]]
            records.append(
                {
                    **record,
                    "name": character_name(key),
                    "has_character_row": has_character_row(row_ids, key),
                    "entry_count": len(entries),
                    "entries_text": _LINE_SEPARATOR.join(entries),
                    "_entries": entries,
                }
            )
        return records

    def cells(self, record: dict) -> list[str]:
        return [
            character_key_cell(record[KEY_FIELD], record["has_character_row"]),
            e(record["name"]) if record["name"] else _EMPTY,
            e(record["entry_count"]),
            html_list_cell([e(text) for text in record["_entries"]], separator="<br>") or _EMPTY,
        ]

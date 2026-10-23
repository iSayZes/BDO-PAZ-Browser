"""intimacyrelation.dbss preview handler: each NPC's first meeting lines, cutscene and knowledge."""
from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from _common.character import character_name
from _common.html import Column, e
from _common.knowledge import knowledge_name
from _common.offset_table import OffsetTableHandler, keyed_offset_handler
from _common.pa_text import pa_fields, pa_key, pa_line_cell, pa_list_cell, pa_list_fields
from _common.row_table import RowTableHandler
from .parser import (
    DIALOG_LINE_COUNT,
    FILE_NAME,
    KEY_FIELD,
    knowledge_key_of,
    parse_intimacyrelation_records,
    parse_intimacyrelationoffset_rows,
)
from .text import COVERED_SLOT, DISCOVER_SLOT, dialog_lines, dialog_text


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"


def intimacy_relation_offset_handler() -> OffsetTableHandler:
    return keyed_offset_handler(_LANG_DIR, parse_intimacyrelationoffset_rows, KEY_FIELD, "npcKey")


def _display_fields(record: dict) -> dict:
    """NPC and knowledge names, and the texts in the user's language with their tagged copies."""
    npc_key = record[KEY_FIELD]
    knowledge_key = knowledge_key_of(record["discover_function"])
    return {
        "npc_name": character_name(npc_key) or None,
        "knowledge_key": knowledge_key,
        "knowledge_name": (knowledge_name(knowledge_key) or None) if knowledge_key is not None else None,
        **pa_fields("covered_dialog", dialog_text(npc_key, COVERED_SLOT, record["covered_dialog_kr"])),
        **pa_fields("discover_dialog", dialog_text(npc_key, DISCOVER_SLOT, record["discover_dialog_kr"])),
        **pa_list_fields("discover_dialogs", dialog_lines(npc_key, record["discover_dialogs_kr"])),
    }


class IntimacyRelationHandler(RowTableHandler):
    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["npcKey"], "num", sort_key=KEY_FIELD),
            Column(labels["npc"], sort_key="npc_name"),
            Column(labels["knowledgeKey"], "num", sort_key="knowledge_key"),
            Column(labels["knowledge"], sort_key="knowledge_name"),
            Column(labels["cutscene"], sort_key="discover_cutscene"),
            Column(labels["coveredDialog"], sort_key="covered_dialog"),
            Column(labels["discoverDialog"], sort_key="discover_dialog"),
            Column(labels["dialogLines"]),
        ]

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        return [{**record, **_display_fields(record)} for record in parse_intimacyrelation_records(data)]

    def cells(self, record: dict) -> list[str]:
        knowledge_key = record["knowledge_key"]
        return [
            e(record[KEY_FIELD]),
            e(record["npc_name"] or _EMPTY),
            e(knowledge_key) if knowledge_key is not None else _EMPTY,
            e(record["knowledge_name"] or _EMPTY),
            e(record["discover_cutscene"] or _EMPTY),
            pa_line_cell(record, "covered_dialog"),
            pa_line_cell(record, "discover_dialog"),
            pa_list_cell(record[pa_key("discover_dialogs")], DIALOG_LINE_COUNT),
        ]

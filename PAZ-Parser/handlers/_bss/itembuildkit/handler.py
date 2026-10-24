"""itembuildkit.bss preview handler: one row per structure a siege build kit places."""

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
from _common.html import Column, e, icon_cell
from _common.inline_text import decode_inline_text
from _common.item_key import item_key_list_cell, item_key_text
from _common.pa_text import pa_fields, pa_line_cell
from _common.row_table import RowTableHandler
from _common.ui_texture import UI_TEXTURE_ICON_ROOT, ui_texture_path
from .parser import FILE_NAME, parse_itembuildkit_entries


_LANG_DIR = Path(__file__).parent / "lang"
_ONE_ITEM = 1
_EMPTY = "-"


def _entry_record(entry: dict, row_ids: frozenset[int] | None) -> dict:
    character_key = entry["character_key"]
    return {
        **entry,
        "name": character_name(character_key) or str(character_key),
        "has_character_row": has_character_row(row_ids, character_key),
        "item_name": item_key_text(entry["item_key"]),
        "icon_path": ui_texture_path(entry["icon_image_file_text"], UI_TEXTURE_ICON_ROOT),
        **pa_fields("description_kr", decode_inline_text(entry["description_kr"])),
    }


class ItemBuildKitBssHandler(RowTableHandler):
    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def companions(self, entry: PazEntry) -> list[str]:
        return [characterstatic_offset_companion(entry.internal_path)]

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["characterKey"], "num", sort_key="character_key"),
            Column(labels["name"], sort_key="name"),
            Column(labels["kitItem"], sort_key="item_name"),
            Column(labels["useCondition"], sort_key="use_condition_text"),
            Column(labels["contentsEventType"], "num", sort_key="contents_event_type"),
            Column(labels["contentsEventParam1"], "num", sort_key="contents_event_param1"),
            Column(labels["icon"], sort_key="icon_path"),
            Column(labels["description"], sort_key="description_kr"),
        ]

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        row_ids = character_row_ids(companions)
        return [_entry_record(entry, row_ids) for entry in parse_itembuildkit_entries(data)]

    def cells(self, record: dict) -> list[str]:
        return [
            character_key_cell(record["character_key"], record["has_character_row"]),
            e(record["name"]),
            item_key_list_cell([record["item_key"]], _ONE_ITEM),
            e(record["use_condition_text"] or _EMPTY),
            e(record["contents_event_type"]),
            e(record["contents_event_param1"]),
            icon_cell(record["icon_path"]),
            pa_line_cell(record, "description_kr"),
        ]

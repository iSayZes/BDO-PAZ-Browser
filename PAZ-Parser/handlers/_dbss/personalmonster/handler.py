"""personalmonster.dbss preview handler: each Dark Rift boss with its difficulty, image and drop items."""
from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from bdo_models import PazEntry

from _bss.stringtable.parser import GAME_SHEET
from _bss.stringtable.text import ui_hash_text
from _common.character import character_name
from _common.character_link import (
    character_key_cell,
    character_row_ids,
    characterstatic_offset_companion,
    has_character_row,
)
from _common.html import Column, e, icon_cell
from _common.item_key import item_key_list_cell, item_key_text
from _common.loc import loc_text
from _common.offset_table import OffsetTableHandler, keyed_offset_handler
from _common.row_table import RowTableHandler
from _common.string_hash import key_hash
from _common.ui_texture import ui_texture_path
from .parser import FILE_NAME, KEY_FIELD, parse_personalmonster_records, parse_personalmonsteroffset_rows


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"
# LOC type 61 holds each boss description under its character key.
LOC_DESCRIPTION = 61
# The Dark Rift window labels difficulty N with this GAME sheet key.
_DIFFICULTY_KEY_PREFIX = "LUA_PERSONALMONSTER_DIFFICULTY_"
# The Dark Rift window has 8 reward slots (`_pcRewardSlotCount`).
_MAX_DROP_ITEMS = 8


def personal_monster_offset_handler() -> OffsetTableHandler:
    return keyed_offset_handler(_LANG_DIR, parse_personalmonsteroffset_rows, KEY_FIELD, "characterKey")


def difficulty_name(difficulty: int) -> str:
    """`Normal (1)`: the Dark Rift window's label of a difficulty, else its number."""
    name = ui_hash_text(GAME_SHEET, key_hash(f"{_DIFFICULTY_KEY_PREFIX}{difficulty}"))
    return f"{name} ({difficulty})" if name else str(difficulty)


class PersonalMonsterHandler(RowTableHandler):
    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["characterKey"], "num", sort_key=KEY_FIELD),
            Column(labels["name"], sort_key="name"),
            Column(labels["difficulty"], sort_key="difficulty"),
            Column(labels["description"], sort_key="description"),
            Column(labels["image"], sort_key="monster_image"),
            Column(labels["dropItems"], sort_key="drop_item_count"),
        ]

    def companions(self, entry: PazEntry) -> list[str]:
        return [characterstatic_offset_companion(entry.internal_path)]

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        records = parse_personalmonster_records(data)
        row_ids = character_row_ids(companions)
        return [
            {
                **record,
                "name": character_name(record[KEY_FIELD]),
                "difficulty_name": difficulty_name(record["difficulty"]),
                "description": loc_text(LOC_DESCRIPTION, record[KEY_FIELD]) or record["description_kr"],
                "drop_item_names": [item_key_text(key) for key in record["drop_item_keys"]],
                "has_character_row": has_character_row(row_ids, record[KEY_FIELD]),
            }
            for record in records
        ]

    def cells(self, record: dict) -> list[str]:
        return [
            character_key_cell(record[KEY_FIELD], record["has_character_row"]),
            e(record["name"] or _EMPTY),
            e(record["difficulty_name"]),
            e(record["description"] or _EMPTY),
            icon_cell(ui_texture_path(record["monster_image"])),
            item_key_list_cell(record["drop_item_keys"], _MAX_DROP_ITEMS) or _EMPTY,
        ]

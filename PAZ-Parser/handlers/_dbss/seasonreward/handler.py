"""seasonreward.dbss preview handler: one row per Season server season and its reward items."""
from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from _bss.stringtable.parser import GAME_SHEET
from _bss.stringtable.text import ui_hash_tagged
from _common.html import Column, e
from _common.item_key import item_key_list_cell, item_key_text
from _common.pa_text import pa_cell, pa_fields
from _common.row_table import RowTableHandler
from _common.string_hash import key_hash
from .parser import FILE_NAME, KEY_FIELD, parse_seasonreward_records


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"
_LIST_SEPARATOR = ", "
_REWARD_PREVIEW_ITEMS = 4


def game_key_tagged(key: str) -> str:
    """LOC text of a `GAME` sheet key with its PA tags, or the key itself when LOC has none."""
    if not key:
        return ""
    return ui_hash_tagged(GAME_SHEET, key_hash(key)) or key


class SeasonRewardHandler(RowTableHandler):
    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["seasonNo"], "num", sort_key=KEY_FIELD),
            Column(labels["season"], sort_key="season_name"),
            Column(labels["description"], sort_key="description"),
            Column(labels["rewards"], sort_key="reward_names"),
        ]

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        return [
            {
                **record,
                **pa_fields("season_name", game_key_tagged(record["season_name_key"])),
                **pa_fields("description", game_key_tagged(record["description_key"])),
                "reward_names": _LIST_SEPARATOR.join(item_key_text(key) for key in record["reward_item_keys"]),
            }
            for record in parse_seasonreward_records(data)
        ]

    def cells(self, record: dict) -> list[str]:
        keys = record["reward_item_keys"]
        return [
            e(record[KEY_FIELD]),
            pa_cell(record, "season_name"),
            pa_cell(record, "description"),
            item_key_list_cell(keys, _REWARD_PREVIEW_ITEMS) if keys else _EMPTY,
        ]

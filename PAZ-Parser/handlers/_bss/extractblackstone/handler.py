"""extractblackstone.bss preview handler: the Black Stone item per difficulty, gear kind and enhancement level.

The difficulty names (Easy, Normal, Hard) follow the developer comment on the
1784 `ExtractBlackStone` sheet and the `__eEnchantDifficulty_*` names of the
client Lua. The two counts of an entry are not confirmed yet
(`unknown_05`, `unknown_0d`) and stay off the table.
"""
from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from _common.enchant_level import enchant_level_text
from _common.html import Column, e
from _common.item_key import item_key_list_cell, item_key_text
from _common.lang import load_handler_strings
from _common.row_table import RowTableHandler
from .parser import FILE_NAME, parse_extractblackstone_records


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"


class ExtractBlackStoneHandler(RowTableHandler):
    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["difficulty"], "num", sort_key="difficulty"),
            Column(labels["difficultyName"], sort_key="difficulty_name"),
            Column(labels["gear"], sort_key="gear"),
            Column(labels["enchantLevel"], "num", sort_key="enchant_level"),
            Column(labels["resultItem"], sort_key="result_item_name"),
        ]

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        strings = load_handler_strings(self.lang, _LANG_DIR)
        difficulties: Mapping[str, str] = strings["difficulties"]
        gear: Mapping[str, str] = strings["gear"]
        return [
            {
                **record,
                "difficulty_name": difficulties.get(str(record["difficulty"]), ""),
                "gear": gear["weapon" if record["is_weapon"] else "armor"],
                "enchant_level_text": enchant_level_text(record["enchant_level"]),
                "result_item_name": item_key_text(record["result_item_key"]),
            }
            for record in parse_extractblackstone_records(data)
        ]

    def cells(self, record: dict) -> list[str]:
        return [
            e(record["difficulty"]),
            e(record["difficulty_name"] or _EMPTY),
            e(record["gear"]),
            e(record["enchant_level_text"] or record["enchant_level"]),
            item_key_list_cell([record["result_item_key"]], 1),
        ]

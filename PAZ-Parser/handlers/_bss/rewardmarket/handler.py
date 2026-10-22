"""rewardmarket.bss preview handler: each pet exchange trade with the pet it takes and the items it gives."""
from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from _common.character import character_name
from _common.html import Column, e, icon_label_cell, record_link
from _common.icon_index import IconKind, icon_path
from _common.item_key import item_count_list_cell, item_count_text
from _common.row_table import RowTableHandler
from .parser import FILE_NAME, KEY_FIELD, parse_rewardmarket_records


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"
_LINK_CLASS = "record-link"
PET_PATH = "gamecommondata/binary/pet.dbss"
_PET_FIELD = "pet_id"


class RewardMarketHandler(RowTableHandler):
    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["tradeKey"], "num", sort_key=KEY_FIELD),
            Column(labels["petKey"], "num", sort_key="pet_key"),
            Column(labels["pet"], sort_key="pet_name"),
            Column(labels["rewards"], sort_key="rewards_text"),
        ]

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        return [
            {
                **record,
                "pet_name": character_name(record["pet_key"]),
                "rewards_text": ", ".join(
                    item_count_text(reward["item_key"], reward["item_count"]) for reward in record["rewards"]
                ),
            }
            for record in parse_rewardmarket_records(data)
        ]

    def cells(self, record: dict) -> list[str]:
        pet_key = record["pet_key"]
        rewards = [(reward["item_key"], reward["item_count"]) for reward in record["rewards"]]
        return [
            e(record[KEY_FIELD]),
            record_link(str(pet_key), PET_PATH, _PET_FIELD, pet_key, _LINK_CLASS),
            icon_label_cell(icon_path(IconKind.CHARACTER, pet_key), record["pet_name"]) if record["pet_name"] else _EMPTY,
            item_count_list_cell(rewards) or _EMPTY,
        ]

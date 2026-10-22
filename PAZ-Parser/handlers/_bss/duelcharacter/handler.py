"""duelcharacter.bss preview handler: the item copy quest and fuel items of Tag Characters."""
from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from _common.html import Column, e
from _common.item_key import item_key_text
from _common.quest.quest import quest_title, split_packed_quest_id
from _common.row_table import RowTableHandler
from .parser import FILE_NAME, parse_duelcharacter_records


_LANG_DIR = Path(__file__).parent / "lang"
_ITEM_FIELDS = ("need_item_for_copy", "need_item_for_individual_copy")


def _quest_text(packed_quest_id: int) -> str:
    """`Black Spirit's Gift (Marni's Suspicious Device) (21418, 5)`, or the IDs alone."""
    chain_id, quest_id = split_packed_quest_id(packed_quest_id)
    ids = f"({chain_id}, {quest_id})"
    title = quest_title(chain_id, quest_id)
    return f"{title} {ids}" if title else ids


class DuelCharacterBssHandler(RowTableHandler):
    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["itemCopyQuest"], sort_key="item_copy_quest_text"),
            Column(labels["copyItem"], sort_key="need_item_for_copy_text"),
            Column(labels["singleCopyItem"], sort_key="need_item_for_individual_copy_text"),
        ]

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        return [
            {
                **record,
                "item_copy_quest_text": _quest_text(record["item_copy_quest"]),
                **{f"{field}_text": item_key_text(record[field]) for field in _ITEM_FIELDS},
            }
            for record in parse_duelcharacter_records(data)
        ]

    def cells(self, record: dict) -> list[str]:
        return [
            e(record["item_copy_quest_text"]),
            *(e(record[f"{field}_text"]) for field in _ITEM_FIELDS),
        ]

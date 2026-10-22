"""marblegamediceitemgroup.dbss preview handler: the dice items of each Black Spirit's Adventure drop group.

Each group shows the game items that grant it (`group_items.py`) and its
dice item keys, each a link to its `marblegamediceitemkey.dbss` row.
"""
from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from _common.html import Column, e, html_list_cell, record_link
from _common.offset_table import OffsetTableHandler, keyed_offset_handler
from _common.row_table import RowTableHandler
from _dbss.marblegamediceitemkey.parser import FILE_NAME as DICE_ITEM_KEY_FILE, KEY_FIELD as DICE_ITEM_KEY_FIELD
from .group_items import group_item_ids, item_fields, items_cell
from .parser import FILE_NAME, KEY_FIELD, parse_marblegamediceitemgroup_records, parse_marblegamediceitemgroupoffset_rows


_LANG_DIR = Path(__file__).parent / "lang"
_LINK_CLASS = "record-link"
DICE_ITEM_KEY_PATH = f"gamecommondata/binary/{DICE_ITEM_KEY_FILE}"


def marble_dice_item_group_offset_handler() -> OffsetTableHandler:
    return keyed_offset_handler(_LANG_DIR, parse_marblegamediceitemgroupoffset_rows, KEY_FIELD, "groupKey")


def _group_record(record: dict) -> dict:
    dice_item_keys = [entry[DICE_ITEM_KEY_FIELD] for entry in record["entries"]]
    return {
        **record,
        "dice_item_keys": dice_item_keys,
        "dice_items_text": ", ".join(str(key) for key in dice_item_keys),
        **item_fields(group_item_ids([record[KEY_FIELD]])),
    }


class MarbleDiceItemGroupHandler(RowTableHandler):
    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["groupKey"], "num", sort_key=KEY_FIELD),
            Column(labels["items"], sort_key="item_count"),
            # A list column: it would only sort by its string form.
            Column(labels["diceItems"]),
        ]

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        return [_group_record(record) for record in parse_marblegamediceitemgroup_records(data)]

    def cells(self, record: dict) -> list[str]:
        links = [
            record_link(str(key), DICE_ITEM_KEY_PATH, DICE_ITEM_KEY_FIELD, key, _LINK_CLASS)
            for key in record["dice_item_keys"]
        ]
        return [
            e(record[KEY_FIELD]),
            items_cell(record["item_ids"]),
            html_list_cell(links),
        ]

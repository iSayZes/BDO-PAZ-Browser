"""marblegamediceitemkey.dbss preview handler: each Black Spirit's Adventure dice item key.

The file holds the keys only. The view lists the `marblegamediceitemgroup.dbss`
groups that drop each key, each a link to its row, and the game items that
grant those groups.
"""
from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from bdo_models import PazEntry

from _common.html import Column, e, html_list_cell, record_link
from _common.offset_table import OffsetTableHandler, keyed_offset_handler
from _common.row_table import RowTableHandler
from _dbss.marblegamediceitemgroup.group_items import group_item_ids, item_fields, items_cell
from _dbss.marblegamediceitemgroup.parser import (
    FILE_NAME as GROUP_FILE,
    KEY_FIELD as GROUP_KEY_FIELD,
    groups_by_dice_item,
)
from .parser import FILE_NAME, KEY_FIELD, parse_marblegamediceitemkey_records, parse_marblegamediceitemkeyoffset_rows


_LANG_DIR = Path(__file__).parent / "lang"
_LINK_CLASS = "record-link"
_EMPTY = "-"
GROUP_PATH = f"gamecommondata/binary/{GROUP_FILE}"


def marble_dice_item_key_offset_handler() -> OffsetTableHandler:
    return keyed_offset_handler(_LANG_DIR, parse_marblegamediceitemkeyoffset_rows, KEY_FIELD, "diceItemKey")


def _key_record(dice_item_key: int, group_keys: list[int]) -> dict:
    return {
        KEY_FIELD: dice_item_key,
        "group_keys": group_keys,
        "groups_text": ", ".join(str(key) for key in group_keys),
        **item_fields(group_item_ids(group_keys)),
    }


class MarbleDiceItemKeyHandler(RowTableHandler):
    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def companions(self, entry: PazEntry) -> list[str]:
        folder = entry.internal_path.rsplit("/", 1)[0]
        return [f"{folder}/{GROUP_FILE}"]

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["diceItemKey"], "num", sort_key=KEY_FIELD),
            Column(labels["items"], sort_key="item_count"),
            # A list column: it would only sort by its string form.
            Column(labels["groups"]),
        ]

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        try:
            groups = groups_by_dice_item(companions.get(GROUP_FILE))
        except ValueError as ex:
            raise ValueError(f"{GROUP_FILE}: {ex}") from ex
        return [
            _key_record(record[KEY_FIELD], groups.get(record[KEY_FIELD], []))
            for record in parse_marblegamediceitemkey_records(data)
        ]

    def cells(self, record: dict) -> list[str]:
        links = [
            record_link(str(key), GROUP_PATH, GROUP_KEY_FIELD, key, _LINK_CLASS)
            for key in record["group_keys"]
        ]
        return [
            e(record[KEY_FIELD]),
            items_cell(record["item_ids"]),
            html_list_cell(links) or _EMPTY,
        ]

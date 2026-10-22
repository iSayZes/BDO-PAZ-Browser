"""customizeditem.dbss preview handler: the item each condition gives out of a per-character box.

Each record shows its key (the `contents_event_param1` of the box items that
open it), the number of choices and each choice as `Condition: Item`, the
condition named by `condition.py` and the item with its icon and level.
"""
from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from _common.html import Column, e, hidden_slice, html_list_cell, icon_html_label_cell
from _common.item_key import item_key_icon_path, item_key_text, item_key_text_tagged
from _common.offset_table import OffsetTableHandler, keyed_offset_handler
from _common.pa_text import pa_html
from _common.row_table import RowTableHandler
from .condition import condition_text
from .parser import FILE_NAME, KEY_FIELD, parse_customizeditem_records, parse_customizeditemoffset_rows


_LANG_DIR = Path(__file__).parent / "lang"
# Choices shown in a cell; hovering the count lists the rest.
_SHOWN_CHOICES = 6
# Display-only: the condition text of each item, for the cell labels.
_CONDITION_TEXTS = "_condition_texts"
_CHOICE_SEPARATOR = "<br>"


def customized_item_offset_handler() -> OffsetTableHandler:
    return keyed_offset_handler(_LANG_DIR, parse_customizeditemoffset_rows, KEY_FIELD, "boxKey")


def _choice_text(condition: str, item_key: int) -> str:
    return f"{condition}: {item_key_text(item_key)}"


def _with_choices(record: dict) -> dict:
    conditions = [condition_text(item["condition"]) for item in record["items"]]
    return {
        **record,
        "choices": [
            _choice_text(condition, item["item_key"])
            for condition, item in zip(conditions, record["items"], strict=True)
        ],
        _CONDITION_TEXTS: conditions,
    }


def _choices_cell(record: dict) -> str:
    items = record["items"][:_SHOWN_CHOICES]
    conditions = record[_CONDITION_TEXTS]
    labels = [
        icon_html_label_cell(
            item_key_icon_path(item["item_key"]),
            f"{e(condition)}: {pa_html(item_key_text_tagged(item['item_key']))}",
        )
        for condition, item in zip(conditions, items)
    ]
    hidden_names = hidden_slice(record["choices"], _SHOWN_CHOICES)
    return html_list_cell(labels, record["item_count"] - len(labels), hidden_names, _CHOICE_SEPARATOR)


class CustomizedItemHandler(RowTableHandler):
    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["boxKey"], "num", sort_key=KEY_FIELD),
            Column(labels["choices"], "num", sort_key="item_count"),
            # A list column: it would only sort by its string form.
            Column(labels["items"]),
        ]

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        return [_with_choices(record) for record in parse_customizeditem_records(data)]

    def cells(self, record: dict) -> list[str]:
        return [
            e(record[KEY_FIELD]),
            e(record["item_count"]),
            _choices_cell(record),
        ]

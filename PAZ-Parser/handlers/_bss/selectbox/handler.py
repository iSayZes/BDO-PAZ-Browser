"""selectbox.bss preview handler: one row per choose-your-item box.

Each type gets a column with its items and counts; the Tabs column names the
tab texture of every type the box uses.
"""

from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from _common.html import Column, e, text_list_cell
from _common.item_key import item_count_list_cell, item_count_text
from _common.row_table import RowTableHandler
from .parser import FILE_NAME, KEY_FIELD, TYPE_COUNT, parse_selectbox_boxes


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"
_TAB_PREVIEW = TYPE_COUNT


def _items_field(type_index: int) -> str:
    return f"type{type_index}_items"


def _count_field(type_index: int) -> str:
    return f"type{type_index}_count"


def _type_fields(type_index: int, entries: list[dict]) -> dict:
    """The item texts of one type for search and export, and its entry count (None sorts last)."""
    return {
        _items_field(type_index): [item_count_text(entry["item_key"], entry["item_count"]) for entry in entries],
        _count_field(type_index): len(entries) or None,
    }


def _box_record(box: dict) -> dict:
    type_lists = box["type_lists"]
    type_fields = [_type_fields(type_index, entries) for type_index, entries in enumerate(type_lists)]
    return {
        **box,
        # The tab texture of each used type, from its first entry.
        "tabs": [entries[0]["texture_name_text"] for entries in type_lists if entries],
        **{name: value for fields in type_fields for name, value in fields.items()},
    }


class SelectBoxBssHandler(RowTableHandler):
    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["key"], "num", sort_key=KEY_FIELD),
            Column(labels["tabs"]),
            *(
                Column(labels[f"type{type_index}"], sort_key=_count_field(type_index))
                for type_index in range(TYPE_COUNT)
            ),
        ]

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        return [_box_record(box) for box in parse_selectbox_boxes(data)]

    def cells(self, record: dict) -> list[str]:
        return [
            e(record[KEY_FIELD] if record[KEY_FIELD] is not None else _EMPTY),
            text_list_cell(record["tabs"], _TAB_PREVIEW) or _EMPTY,
            *(
                item_count_list_cell((entry["item_key"], entry["item_count"]) for entry in entries) or _EMPTY
                for entries in record["type_lists"]
            ),
        ]

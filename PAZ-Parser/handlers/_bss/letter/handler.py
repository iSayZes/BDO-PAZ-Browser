"""letter.bss preview handler: the letter window of each letter item, with its text and background."""
from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from _bss.stringtable.parser import RESOURCE_SHEET
from _bss.stringtable.text import ui_hash_tagged
from _common.html import Column, e, flag_cell, icon_cell
from _common.inline_text import decode_inline_text
from _common.item_key import item_name
from _common.pa_text import pa_fields, pa_line_cell
from _common.row_table import RowTableHandler
from _common.string_hash import key_hash
from _common.ui_texture import ui_texture_path
from .parser import FILE_NAME, KEY_FIELD, parse_letter_records


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"


def letter_text_tagged(string_key: str) -> str:
    """The LOC text of a `RESOURCE` sheet key with its PA tags, or ''.

    UI strings store a line break as the two characters `\\n`, which
    `PAGetString()` turns into one; the text here gets real newlines too.
    """
    return decode_inline_text(ui_hash_tagged(RESOURCE_SHEET, key_hash(string_key))) if string_key else ""


class LetterBssHandler(RowTableHandler):
    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["itemKey"], "num", sort_key=KEY_FIELD),
            Column(labels["item"], sort_key="item_name"),
            Column(labels["textKey"], sort_key="main_desc_string_key"),
            Column(labels["text"], sort_key="text"),
            Column(labels["background"], sort_key="texture_path"),
            Column(labels["centered"], sort_key="is_center_alignment"),
        ]

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        return [
            {
                **record,
                "item_name": item_name(record[KEY_FIELD]),
                **pa_fields("text", letter_text_tagged(record["main_desc_string_key"])),
                "_texture_file": ui_texture_path(record["texture_path"]),
            }
            for record in parse_letter_records(data)
        ]

    def cells(self, record: dict) -> list[str]:
        return [
            e(record[KEY_FIELD]),
            e(record["item_name"]) if record["item_name"] else _EMPTY,
            e(record["main_desc_string_key"]) if record["main_desc_string_key"] else _EMPTY,
            pa_line_cell(record, "text"),
            icon_cell(record["_texture_file"]),
            flag_cell(bool(record["is_center_alignment"])),
        ]

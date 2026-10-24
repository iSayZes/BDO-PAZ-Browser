"""form.dbss preview handler: each mount form with its type, action, tier, icons and characters."""
from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from bdo_models import PazEntry

from _common.character import character_name
from _common.character_link import (
    character_key_cell,
    character_row_ids,
    characterstatic_offset_companion,
    has_character_row,
)
from _common.html import Column, e, html_list_cell, icon_cell
from _common.icon_index import clean_stored_icon_path
from _common.lang import load_handler_strings
from _common.offset_table import OffsetTableHandler, keyed_offset_handler
from _common.row_table import RowTableHandler
from _common.ui_texture import ui_texture_path
from .parser import FILE_NAME, KEY_FIELD, parse_form_records, parse_formoffset_rows


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"
_LIST_SEPARATOR = "; "


def form_offset_handler() -> OffsetTableHandler:
    return keyed_offset_handler(_LANG_DIR, parse_formoffset_rows, KEY_FIELD, "index")


def _icon(stored: str) -> str:
    return icon_cell(ui_texture_path(clean_stored_icon_path(stored)))


def _character_cell(character: dict) -> str:
    """The key linked to its `characterstatic.dbss` row, then its name."""
    key_html = character_key_cell(character["character_key"], character["has_character_row"])
    return f'{key_html} {e(character["name"])}' if character["name"] else key_html


class FormHandler(RowTableHandler):
    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def companions(self, entry: PazEntry) -> list[str]:
        return [characterstatic_offset_companion(entry.internal_path)]

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["index"], "num", sort_key=KEY_FIELD),
            Column(labels["type"], sort_key="type_name"),
            Column(labels["actionIndex"], "num", sort_key="action_index"),
            Column(labels["tier"], "num", sort_key="tier"),
            Column(labels["icon1"], sort_key="icon_1"),
            Column(labels["icon2"], sort_key="icon_2"),
            Column(labels["characters"], sort_key="characters_text"),
        ]

    def _type_name(self, form_type: int) -> str | None:
        """`Horse` for type 0 (eFormType_Horse); None for type 1, the sheet's blank."""
        return load_handler_strings(self.lang, _LANG_DIR)["types"].get(str(form_type))

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        row_ids = character_row_ids(companions)
        records = []
        for record in parse_form_records(data):
            characters = [
                {
                    "character_key": key,
                    "name": character_name(key),
                    "has_character_row": has_character_row(row_ids, key),
                }
                for key in record["character_keys"]
            ]
            records.append(
                {
                    **record,
                    "type_name": self._type_name(record["type"]),
                    "characters": characters,
                    "characters_text": _LIST_SEPARATOR.join(
                        f'{c["character_key"]} {c["name"]}'.strip() for c in characters
                    ) or None,
                }
            )
        return records

    def cells(self, record: dict) -> list[str]:
        characters = [_character_cell(character) for character in record["characters"]]
        return [
            e(record[KEY_FIELD]),
            e(record["type_name"] or _EMPTY),
            e(record["action_index"]),
            e(record["tier"]),
            _icon(record["icon_1"]),
            _icon(record["icon_2"]),
            html_list_cell(characters, separator="<br>") or _EMPTY,
        ]

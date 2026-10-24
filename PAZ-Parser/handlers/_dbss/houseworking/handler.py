"""houseworking.dbss preview handler: the exchanges a worker can run at each crafting tool."""
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
from _common.html import Column, e, html_list_cell
from _common.item_exchange import exchange_cell, exchange_text
from _common.lang import load_handler_strings
from _common.offset_table import OffsetTableHandler, keyed_offset_handler
from _common.row_table import RowTableHandler
from .parser import FILE_NAME, KEY_FIELD, parse_houseworking_records, parse_houseworkingoffset_rows


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"
_LIST_SEPARATOR = "; "
# Between an exchange and its unit production.
_WORK_SEPARATOR = ", "


def house_working_offset_handler() -> OffsetTableHandler:
    return keyed_offset_handler(_LANG_DIR, parse_houseworkingoffset_rows, KEY_FIELD, "toolKey")


class HouseWorkingHandler(RowTableHandler):
    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def companions(self, entry: PazEntry) -> list[str]:
        return [characterstatic_offset_companion(entry.internal_path)]

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["toolKey"], "num", sort_key=KEY_FIELD),
            Column(labels["tool"], sort_key="name"),
            Column(labels["works"], sort_key="works_text"),
        ]

    def _units_text(self, work: dict) -> str:
        """`unit production 3`, in the UI language."""
        return load_handler_strings(self.lang, _LANG_DIR)["cells"]["units"].format(units=work["unit_production"])

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        row_ids = character_row_ids(companions)
        return [
            {
                **record,
                "name": character_name(record[KEY_FIELD]),
                "has_character_row": has_character_row(row_ids, record[KEY_FIELD]),
                "works_text": _LIST_SEPARATOR.join(
                    f'{exchange_text(work["exchange_key"])}{_WORK_SEPARATOR}{self._units_text(work)}'
                    for work in record["works"]
                ) or None,
            }
            for record in parse_houseworking_records(data)
        ]

    def _works_cell(self, works: list[dict]) -> str:
        """One line per work: the exchange linked to its `itemexchangesource.bss` row and its unit production."""
        if not works:
            return _EMPTY
        lines = [f'{exchange_cell(work["exchange_key"])}{_WORK_SEPARATOR}{e(self._units_text(work))}' for work in works]
        return html_list_cell(lines, separator="<br>")

    def cells(self, record: dict) -> list[str]:
        return [
            character_key_cell(record[KEY_FIELD], record["has_character_row"]),
            e(record["name"] or _EMPTY),
            self._works_cell(record["works"]),
        ]

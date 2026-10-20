"""maid.dbss preview handler: duties, cooldown, PC room and head maid flags and icons of each maid."""
from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.character import character_name
from _common.character_link import (
    character_key_cell,
    character_row_ids,
    characterstatic_offset_companion,
    has_character_row,
)
from _common.duration import format_duration
from _common.html import Column, e, error, flag_cell, html_list_cell, icon_cell, sort_keys, table
from _common.icon_index import clean_stored_icon_path
from _common.lang import handler_text, load_handler_strings
from _common.offset_table import OffsetColumn, OffsetTableHandler, offset_column, offset_records, size_column
from _common.pabr_offset import parse_bare_offset_rows
from _common.ui_texture import ui_texture_path
from .parser import CHIEF_FIELDS, FILE_NAME, FLAG_FIELDS, parse_maid_records


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"
# Lang column key of each flag in FLAG_FIELDS, then CHIEF_FIELDS.
_FLAG_LABELS = ("warehouseIn", "warehouseOut", "marketSubmit", "marketBuy", "repair", "pcRoom")
_CHIEF_LABELS = ("headMaid", "headMaidMarket")
_SKILL_FIELDS = (("skill_0", "skill1"), ("skill_1", "skill2"))


def maid_offset_handler() -> OffsetTableHandler:
    return OffsetTableHandler(
        _LANG_DIR,
        [
            OffsetColumn("character_key", "characterKey"),
            offset_column("offset", "dataOffset"),
            size_column("size", "size"),
        ],
        offset_records(parse_bare_offset_rows, "character_key"),
    )


def _form_icons(forms: list[dict]) -> str:
    """One icon cell per form, or a dash for a row without forms."""
    icons = [icon_cell(ui_texture_path(clean_stored_icon_path(form["icon_path"]))) for form in forms]
    return html_list_cell(icons) if icons else _EMPTY


def _form_action_indexes(forms: list[dict]) -> str:
    return ", ".join(e(form["action_index"]) for form in forms) or _EMPTY


class MaidHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["characterKey"], "num", sort_key="character_key"),
            Column(cols["name"], sort_key="name"),
            Column(cols["maxActionIndex"], "num", sort_key="max_action_index"),
            Column(cols["coolTime"], "num", sort_key="cool_time"),
            *(Column(cols[label], sort_key=field) for field, label in zip(FLAG_FIELDS, _FLAG_LABELS)),
            *(Column(cols[label], "num", sort_key=field) for field, label in _SKILL_FIELDS),
            Column(cols["actionIndex"], "num"),
            Column(cols["icon"]),
            *(Column(cols[label], sort_key=field) for field, label in zip(CHIEF_FIELDS, _CHIEF_LABELS)),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def companions(self, entry: PazEntry) -> list[str]:
        return [characterstatic_offset_companion(entry.internal_path)]

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        try:
            records = parse_maid_records(data)
            row_ids = character_row_ids(companions)
        except ValueError as ex:
            return [{"_error": f"{FILE_NAME} could not be parsed: {ex}"}]

        return [
            {
                **record,
                "name": character_name(record["character_key"]),
                "has_character_row": has_character_row(row_ids, record["character_key"]),
            }
            for record in records
        ]

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        if records and "_error" in records[0]:
            return error(records[0]["_error"])

        start = page * page_size
        rows = [
            [
                character_key_cell(r["character_key"], r["has_character_row"]),
                e(r["name"] or _EMPTY),
                e(r["max_action_index"]),
                e(format_duration(r["cool_time"]) or _EMPTY),
                *(flag_cell(r[field] != 0) for field in FLAG_FIELDS),
                *(e(r[field]) for field, _ in _SKILL_FIELDS),
                _form_action_indexes(r["forms"]),
                _form_icons(r["forms"]),
                *(flag_cell(r[field] != 0) for field in CHIEF_FIELDS),
            ]
            for r in records[start : start + page_size]
        ]
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records))
        return table(meta, self._columns(), rows)

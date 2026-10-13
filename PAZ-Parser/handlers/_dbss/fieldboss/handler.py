"""fieldboss.dbss preview handler: the field boss character list in file order."""
from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.character import character_name, character_title
from _common.html import Column, e, error, sort_keys, table
from _common.lang import handler_text, load_handler_strings
from _common.offset_table import OffsetColumn, OffsetTableHandler, offset_column, offset_records, size_column
from _common.pa_text import pa_cell, pa_fields
from _common.pabr_offset import parse_bare_offset_rows
from .parser import FILE_NAME, parse_fieldboss_records


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"


def field_boss_offset_handler() -> OffsetTableHandler:
    return OffsetTableHandler(
        _LANG_DIR,
        [
            OffsetColumn("character_id", "characterId"),
            offset_column("offset", "byteOffset"),
            size_column("size", "size"),
        ],
        offset_records(parse_bare_offset_rows, "character_id"),
    )


class FieldBossHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["characterId"], "num", sort_key="character_id"),
            Column(cols["name"], sort_key="name"),
            Column(cols["title"], sort_key="title"),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        try:
            records = parse_fieldboss_records(data)
        except ValueError as ex:
            return [{"_error": f"{FILE_NAME} could not be parsed: {ex}"}]

        return [
            {
                **record,
                "name": character_name(record["character_id"]),
                **pa_fields("title", character_title(record["character_id"])),
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
                e(r["character_id"]),
                e(r["name"] or _EMPTY),
                pa_cell(r, "title"),
            ]
            for r in records[start : start + page_size]
        ]
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records))
        return table(meta, self._columns(), rows)

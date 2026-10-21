"""servanttransformdata.dbss preview handler: the ship appearance changes, in file order."""
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
from _common.html import Column, e, error, sort_keys, table
from _common.lang import handler_text, load_handler_strings
from _common.offset_table import OffsetColumn, OffsetTableHandler, offset_column, offset_records, size_column
from _common.pabr_offset import parse_bare_offset_rows
from .parser import FILE_NAME, parse_servanttransformdata_records


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"


def servant_transform_data_offset_handler() -> OffsetTableHandler:
    return OffsetTableHandler(
        _LANG_DIR,
        [
            OffsetColumn("form_key", "formKey"),
            offset_column("offset", "dataOffset"),
            size_column("size", "size"),
        ],
        offset_records(parse_bare_offset_rows, "form_key"),
    )


def _with_character(record: dict, side: str, row_ids: frozenset[int] | None) -> dict:
    """The name and row flag of the `from` or `to` character, keyed by side."""
    character_key = record[f"{side}_character_key"]
    return {
        f"{side}_name": character_name(character_key),
        f"{side}_has_character_row": has_character_row(row_ids, character_key),
    }


class ServantTransformDataHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["formKey"], "num", sort_key="form_key"),
            Column(cols["fromCharacterKey"], "num", sort_key="from_character_key"),
            Column(cols["fromName"], sort_key="from_name"),
            Column(cols["toCharacterKey"], "num", sort_key="to_character_key"),
            Column(cols["toName"], sort_key="to_name"),
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
            records = parse_servanttransformdata_records(data)
            row_ids = character_row_ids(companions)
        except ValueError as ex:
            return [{"_error": f"{FILE_NAME} could not be parsed: {ex}"}]

        return [
            {
                **record,
                **_with_character(record, "from", row_ids),
                **_with_character(record, "to", row_ids),
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
                e(r["form_key"]),
                character_key_cell(r["from_character_key"], r["from_has_character_row"]),
                e(r["from_name"] or _EMPTY),
                character_key_cell(r["to_character_key"], r["to_has_character_row"]),
                e(r["to_name"] or _EMPTY),
            ]
            for r in records[start : start + page_size]
        ]
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records))
        return table(meta, self._columns(), rows)

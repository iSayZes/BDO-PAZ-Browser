"""collectresourcename.dbss preview handler: gathering models in file order."""
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
from _common.offset_table import OffsetColumn, OffsetTableHandler, offset_column, offset_records, offset_text, size_column
from _common.pabr_offset import parse_bare_u32_offset_rows
from .parser import FILE_NAME, parse_collectresourcename_records


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"


def collect_resource_name_offset_handler() -> OffsetTableHandler:
    return OffsetTableHandler(
        _LANG_DIR,
        [
            OffsetColumn("name_hash", "nameHash", offset_text),
            offset_column("data_offset", "dataOffset"),
            size_column("data_size", "size"),
        ],
        offset_records(parse_bare_u32_offset_rows, "name_hash", "data_offset", "data_size"),
    )


class CollectResourceNameHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["nameHash"], "num", sort_key="name_hash"),
            Column(cols["model"], sort_key="resource_file_name"),
            Column(cols["characterId"], "num", sort_key="character_key"),
            Column(cols["name"], sort_key="character_name"),
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
            records = parse_collectresourcename_records(data)
            row_ids = character_row_ids(companions)
        except ValueError as ex:
            return [{"_error": f"{FILE_NAME} could not be parsed: {ex}"}]

        return [
            {
                **record,
                "character_name": character_name(record["character_key"]),
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
                e(offset_text(r["name_hash"])),
                e(r["resource_file_name"]),
                character_key_cell(r["character_key"], r["has_character_row"]),
                e(r["character_name"] or _EMPTY),
            ]
            for r in records[start : start + page_size]
        ]
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records))
        return table(meta, self._columns(), rows)

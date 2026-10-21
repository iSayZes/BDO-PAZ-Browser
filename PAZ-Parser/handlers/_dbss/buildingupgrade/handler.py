"""buildingupgrade.dbss preview handler: siege building upgrades and their source items."""
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
from _common.item_key import item_count_list_cell, item_count_text
from _common.lang import handler_text, load_handler_strings
from _common.offset_table import OffsetColumn, OffsetTableHandler, offset_column, offset_records, size_column
from _common.pabr_offset import parse_bare_offset_rows
from .parser import FILE_NAME, parse_buildingupgrade_records


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"


def building_upgrade_offset_handler() -> OffsetTableHandler:
    return OffsetTableHandler(
        _LANG_DIR,
        [
            OffsetColumn("character_key", "characterKey"),
            offset_column("offset", "dataOffset"),
            size_column("size", "size"),
        ],
        offset_records(parse_bare_offset_rows, "character_key"),
    )


def _with_display_fields(record: dict, row_ids: frozenset[int] | None) -> dict:
    """The record with both character names, their link flags and the
    source items as plain text for tab search and CSV export."""
    character_key = record["character_key"]
    target_key = record["target_character_key"]
    return {
        **record,
        "name": character_name(character_key),
        "has_character_row": has_character_row(row_ids, character_key),
        "target_name": character_name(target_key),
        "has_target_row": has_character_row(row_ids, target_key),
        "source_items": [item_count_text(item["item_key"], item["count"]) for item in record["items"]],
    }


class BuildingUpgradeHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["characterKey"], "num", sort_key="character_key"),
            Column(cols["name"], sort_key="name"),
            Column(cols["upgradeTime"], "num", sort_key="upgrade_time"),
            Column(cols["upgradeLevel"], "num", sort_key="upgrade_level"),
            Column(cols["targetCharacterKey"], "num", sort_key="target_character_key"),
            Column(cols["targetName"], sort_key="target_name"),
            Column(cols["sourceItems"]),
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
            records = parse_buildingupgrade_records(data)
            row_ids = character_row_ids(companions)
        except ValueError as ex:
            return [{"_error": f"{FILE_NAME} could not be parsed: {ex}"}]
        return [_with_display_fields(record, row_ids) for record in records]

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
                e(f"{r['upgrade_time']:,}"),
                e(r["upgrade_level"]),
                character_key_cell(r["target_character_key"], r["has_target_row"]),
                e(r["target_name"] or _EMPTY),
                item_count_list_cell((item["item_key"], item["count"]) for item in r["items"]) or _EMPTY,
            ]
            for r in records[start : start + page_size]
        ]
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records))
        return table(meta, self._columns(), rows)

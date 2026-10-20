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
from _common.html import Column, e, sort_keys, table
from _common.item_key import item_count_list_cell, item_count_text, item_key_list_cell, item_key_text
from _common.lang import handler_text, load_handler_strings
from _common.offset_table import OffsetColumn, OffsetTableHandler, offset_column, size_column
from .parser import parse_servantupgrade_offset_records, parse_servantupgrade_records


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"
_MAIN_ITEMS_SHOWN = 4


def servant_upgrade_offset_handler() -> OffsetTableHandler:
    return OffsetTableHandler(
        _LANG_DIR,
        [
            OffsetColumn("character_id", "characterId"),
            OffsetColumn("upgrade_character_id", "upgradeCharacterId"),
            offset_column("offset", "dataOffset"),
            size_column("size", "size"),
        ],
        parse_servantupgrade_offset_records,
    )


def _ship_name(character_id: int) -> str:
    """The ship's name in the user's language, else its character ID."""
    return character_name(character_id) or str(character_id)


def _used(items: list[dict]) -> list[tuple[int, int]]:
    """`(item_key, count)` of the filled slots; unused slots are all zero."""
    return [(item["item_key"], item["count"]) for item in items if item["item_key"]]


class ServantUpgradeHandler(PreviewHandler):
    """One table row per upgrade, from the ship before it to the ship after it."""

    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["characterId"], "num", sort_key="character_id"),
            Column(cols["ship"], sort_key="name"),
            Column(cols["upgradeCharacterId"], "num", sort_key="upgrade_character_id"),
            Column(cols["upgradeShip"], sort_key="upgrade_name"),
            Column(cols["mainItems"]),
            Column(cols["subItems"]),
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
        row_ids = character_row_ids(companions)
        records = []
        for record in parse_servantupgrade_records(data):
            ship, upgrade = record["character_id"], record["upgrade_character_id"]
            records.append(
                {
                    **record,
                    "name": _ship_name(ship),
                    "upgrade_name": _ship_name(upgrade),
                    # Plain text for tab search and CSV export.
                    "main_item_names": [item_key_text(key) for key, _ in _used(record["main_items"])],
                    "sub_item_names": [item_count_text(key, count) for key, count in _used(record["sub_items"])],
                    "has_character_row": has_character_row(row_ids, ship),
                    "upgrade_has_character_row": has_character_row(row_ids, upgrade),
                }
            )
        return records

    def _row(self, r: dict) -> list[str]:
        main_keys = [key for key, _ in _used(r["main_items"])]
        return [
            character_key_cell(r["character_id"], r["has_character_row"]),
            e(r["name"]),
            character_key_cell(r["upgrade_character_id"], r["upgrade_has_character_row"]),
            e(r["upgrade_name"]),
            item_key_list_cell(main_keys, _MAIN_ITEMS_SHOWN) or _EMPTY,
            item_count_list_cell(_used(r["sub_items"])) or _EMPTY,
        ]

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        start = page * page_size
        ships = len({r["character_id"] for r in records})
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records), ships=ships)
        rows = [self._row(r) for r in records[start : start + page_size]]
        return table(meta, self._columns(), rows)

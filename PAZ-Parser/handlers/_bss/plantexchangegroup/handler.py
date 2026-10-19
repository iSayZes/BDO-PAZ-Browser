from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.html import Column, e, sort_keys, table
from _common.item_exchange import exchange_cell, exchange_text
from _common.item_key import item_key_list_cell
from _common.lang import handler_text, load_handler_strings
from _common.loc import is_loc_loaded
from _common.production_items import production_item_fields, production_luck_item_fields
from _dbss.plantzone.parser import parse_plantzone_records
from .node_names import english_group_names
from .parser import parse_plantexchangegroup_records


_LANG_DIR = Path(__file__).parent / "lang"
_ZONE_FILE = "plantzone.dbss"
_ZONE_OFFSET_FILE = "plantzoneoffset.dbss"
_EMPTY = "-"
_LIST_PREVIEW_ITEMS = 8


def _english_names(companions: dict[str, bytes]) -> dict[int, str]:
    """English group names by production key; empty without LOC or the zone tables."""
    zones = companions.get(_ZONE_FILE)
    zone_offsets = companions.get(_ZONE_OFFSET_FILE)
    if not is_loc_loaded() or zones is None or zone_offsets is None:
        return {}
    # Without the NODE_PARENT index no zone has a parent, so no key gets a name.
    return english_group_names(parse_plantzone_records(zones, zone_offsets))


class PlantExchangeGroupBssHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["productionKey"], "num", sort_key="production_key"),
            Column(cols["name"], sort_key="name"),
            Column(cols["exchange"], "num", sort_key="exchange_key"),
            # List columns: they would only sort by their string form.
            Column(cols["items"]),
            Column(cols["luckItems"]),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def companions(self, entry: PazEntry) -> list[str]:
        folder = entry.internal_path.rsplit("/", 1)[0]
        return [
            f"{folder}/{_ZONE_FILE}",
            f"{folder}/{_ZONE_OFFSET_FILE}",
        ]

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        english = _english_names(companions)
        records: list[dict] = []
        for record in parse_plantexchangegroup_records(data):
            name_en = english.get(record["production_key"], "")
            records.append({
                **record,
                **production_item_fields(record["production_key"]),
                **production_luck_item_fields(record["production_key"]),
                # The exchange name and key as text, so tab search and CSV export see them.
                "exchange": exchange_text(record["exchange_key"]),
                "name_en": name_en,
                # The Korean label stands in where no English name is unique.
                "name": name_en or record["name_kr"],
            })
        return records

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        start = page * page_size
        slice_ = records[start : start + page_size]
        resolved = sum(1 for record in records if record["item_keys"] is not None)
        luck = sum(1 for record in records if record["luck_item_keys"] is not None)
        meta = handler_text(
            self.lang, _LANG_DIR, "meta.count", count=len(records), resolved=resolved, luck=luck,
        )
        rows = [
            [
                e(record["production_key"]),
                e(record["name"] or _EMPTY),
                exchange_cell(record["exchange_key"]),
                item_key_list_cell(record["item_keys"] or [], _LIST_PREVIEW_ITEMS) or _EMPTY,
                item_key_list_cell(record["luck_item_keys"] or [], _LIST_PREVIEW_ITEMS) or _EMPTY,
            ]
            for record in slice_
        ]
        return table(meta, self._columns(), rows)

"""World territories BSS handler."""
from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.html import Column, e, flag_cell, icon_cell, sort_keys, table
from _common.item_key import item_key_list_cell, item_name
from _common.lang import handler_text, load_handler_strings
from _common.territory import nation_name, territory_name
from .parser import POSITION_FIELDS, parse_territoryinfo_records


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"
# Column label key per position field, in file order.
_POSITION_LABELS = dict(zip(POSITION_FIELDS, ("occupyingTent", "militiaAttack", "militiaDefense")))
_BOOTY_PREVIEW_ITEMS = 2


def _position_text(position: list[float]) -> str:
    """Whole-number `x, y, z`, or "" for the all-zero "no position" value."""
    if not any(position):
        return ""
    return ", ".join(str(round(axis)) for axis in position)


def _items_text(item_ids: list[int]) -> str:
    """The item names joined, for sorting; an ID stands in for a missing name."""
    return ", ".join(item_name(item_id) or str(item_id) for item_id in item_ids)


class TerritoryInfoBssHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["key"], "num", sort_key="territory_key"),
            Column(cols["icon"], sort_key="icon_small_path"),
            Column(cols["territory"], sort_key="name"),
            Column(cols["nation"], sort_key="nation"),
            Column(cols["lordTerritory"], sort_key="is_lord_territory_only"),
            Column(cols["kingTerritory"], sort_key="is_king_territory_only"),
            Column(cols["booty"], sort_key="booty"),
            # Position columns: an x, y, z list would only sort by its string form.
            *(Column(cols[_POSITION_LABELS[field]]) for field in POSITION_FIELDS),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        records: list[dict] = []
        for record in parse_territoryinfo_records(data):
            key = record["territory_key"]
            records.append({
                **record,
                "name": territory_name(key) or record["name_kr"],
                "nation": nation_name(key) or record["nation_kr"],
                "booty": _items_text(record["booty_item_ids"]),
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
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records))
        rows = [
            [
                e(r["territory_key"]),
                icon_cell(r["icon_small_path"]) if r["icon_small_path"] else _EMPTY,
                e(r["name"] or _EMPTY),
                e(r["nation"] or _EMPTY),
                flag_cell(r["is_lord_territory_only"]),
                flag_cell(r["is_king_territory_only"]),
                item_key_list_cell(r["booty_item_ids"], _BOOTY_PREVIEW_ITEMS) or _EMPTY,
                *(e(_position_text(r[field]) or _EMPTY) for field in POSITION_FIELDS),
            ]
            for r in slice_
        ]
        return table(meta, self._columns(), rows)

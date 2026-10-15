"""World territories BSS handler."""
from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.html import Column, e, flag_cell, icon_cell, sort_keys, table, text_list_cell
from _common.item_key import item_key_list_cell, item_name
from _common.lang import handler_text, load_handler_strings
from _common.territory import nation_name, territory_name
from .parser import parse_territoryinfo_records


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"
_POSITION_PREVIEW_ITEMS = 3


def _position_text(position: list[float]) -> str:
    """Whole-number `x, y, z`, or "" for the all-zero "no position" value."""
    if not any(position):
        return ""
    return ", ".join(str(round(axis)) for axis in position)


def _item_text(item_id: int) -> str:
    return item_name(item_id) or str(item_id)


def _item_cell(item_id: int) -> str:
    """The item with its icon and grade colour, or a dash for item 0."""
    return item_key_list_cell([item_id], 1) if item_id else _EMPTY


class TerritoryInfoBssHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["key"], "num", sort_key="territory_key"),
            Column(cols["icon"], sort_key="icon_small_path"),
            Column(cols["territory"], sort_key="name"),
            Column(cols["nation"], sort_key="nation"),
            Column(cols["autonomous"], sort_key="is_autonomous"),
            Column(cols["crown"], sort_key="crown"),
            Column(cols["armor"], sort_key="armor"),
            # A list column: it would only sort by its string form.
            Column(cols["positions"]),
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
                "crown": _item_text(record["crown_item_id"]),
                "armor": _item_text(record["armor_item_id"]),
                "position_texts": [
                    text for text in map(_position_text, record["positions"]) if text
                ],
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
                flag_cell(r["is_autonomous"]),
                _item_cell(r["crown_item_id"]),
                _item_cell(r["armor_item_id"]),
                text_list_cell(r["position_texts"], _POSITION_PREVIEW_ITEMS, separator="; ") or _EMPTY,
            ]
            for r in slice_
        ]
        return table(meta, self._columns(), rows)

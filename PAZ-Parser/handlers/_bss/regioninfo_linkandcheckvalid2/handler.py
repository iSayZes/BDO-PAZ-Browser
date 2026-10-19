from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.html import Column, e, sort_keys, table, text_list_cell
from _common.lang import handler_text, load_handler_strings
from _common.town import town_name
from .parser import parse_region_link_records


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"
_LIST_PREVIEW_ITEMS = 6


def _region_label(region_key: int) -> str:
    """LOC type 17 region name, or the bare key when LOC has none."""
    return town_name(region_key) or str(region_key)


def _display_fields(record: dict) -> dict:
    keys = record["pc_delivery_region_keys"]
    return {
        "region_name": town_name(record["region_key"]) or None,
        "link_count": len(keys),
        "linked_regions": [_region_label(key) for key in keys],
    }


class RegionLinkBssHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["regionKey"], "num", sort_key="region_key"),
            Column(cols["regionName"], sort_key="region_name"),
            Column(cols["linkCount"], "num", sort_key="link_count"),
            Column(cols["linkedRegions"]),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        return [
            {**record, **_display_fields(record)}
            for record in parse_region_link_records(data)
        ]

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
                e(record["region_key"]),
                e(record["region_name"] or _EMPTY),
                e(record["link_count"]),
                text_list_cell(record["linked_regions"], _LIST_PREVIEW_ITEMS) or _EMPTY,
            ]
            for record in slice_
        ]

        return table(meta, self._columns(), rows)

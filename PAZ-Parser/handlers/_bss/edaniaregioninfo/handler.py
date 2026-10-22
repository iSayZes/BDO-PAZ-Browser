from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.html import Column, e, sort_keys, table
from _common.lang import handler_text, load_handler_strings
from .castle import castle_name
from .parser import parse_edaniaregioninfo_records


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"


class EdaniaRegionInfoBssHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["edaniaRegion"], "num", sort_key="edania_region"),
            Column(cols["castle"], sort_key="castle_name"),
            Column(cols["mapColor"], "num", sort_key="map_color"),
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
            {**record, "castle_name": castle_name(record["edania_region"])}
            for record in parse_edaniaregioninfo_records(data)
        ]

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        start = page * page_size
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records))
        rows = [
            [
                e(r["edania_region"]),
                e(r["castle_name"] or _EMPTY),
                e(r["map_color"]),
            ]
            for r in records[start : start + page_size]
        ]
        return table(meta, self._columns(), rows)

from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.html import Column, e, sort_keys, table
from _common.lang import handler_text, load_handler_strings
from .names import NO_LIMIT, jewel_group_name
from .parser import parse_jewel_group_records


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"


class JewelGroupStaticStatusBssHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["group"], "num", sort_key="group"),
            Column(cols["name"], sort_key="name"),
            Column(cols["maxCount"], "num", sort_key="max_count"),
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
            {**group, "name": jewel_group_name(group["group"], group["max_count"], group["name_kr"])}
            for group in parse_jewel_group_records(data)
        ]

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        start = page * page_size
        no_limit = handler_text(self.lang, _LANG_DIR, "values.noLimit")
        rows = [
            [
                e(r["group"]),
                e(r["name"] or _EMPTY),
                e(no_limit if r["max_count"] == NO_LIMIT else r["max_count"]),
            ]
            for r in records[start : start + page_size]
        ]
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records))
        return table(meta, self._columns(), rows)

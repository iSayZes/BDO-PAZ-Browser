from __future__ import annotations

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from ..common.html import e, table
from .parser import parse_worldquest_records


_HEADERS: list[tuple[str, str, str]] = [
    ("Count", "num", ""),
    ("Status", "", ""),
]


class WorldQuestDbssHandler(PreviewHandler):
    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        return parse_worldquest_records(data)

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        start = page * page_size
        slice_ = records[start : start + page_size]
        count = records[0]["count"] if records else 0
        meta = f"Header count: {count:,}"
        rows = [
            [
                e(r["count"]),
                e(r["status"]),
            ]
            for r in slice_
        ]
        return table(meta, _HEADERS, rows)

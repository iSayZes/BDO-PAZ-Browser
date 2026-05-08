from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.html import e, table
from _common.lang import load_handler_strings
from .parser import parse_worldquest_records


_LANG_DIR = Path(__file__).parent / "lang"


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
        cols = load_handler_strings(self.lang, _LANG_DIR).get("columns", {})
        headers: list[tuple[str, str, str]] = [
            (cols.get("count", "Count"), "num", ""),
            (cols.get("status", "Status"), "", ""),
        ]
        rows = [
            [
                e(r["count"]),
                e(r["status"]),
            ]
            for r in slice_
        ]
        return table(meta, headers, rows)

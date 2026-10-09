from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.html import Column, e, flag_cell, sort_keys, table
from _common.lang import handler_text, load_handler_strings
from _dbss.pcgrowth.text import class_display_name
from .parser import parse_pcgrowthsimply_records


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"


class PcGrowthSimplyBssHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["classType"], "num", sort_key="class_type"),
            Column(cols["className"], sort_key="class_name"),
            Column(cols["playable"], sort_key="is_playable"),
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
            {**record, "class_name": class_display_name(record["class_type"], record["name_kr"])}
            for record in parse_pcgrowthsimply_records(data)
        ]

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        start = page * page_size
        playable = sum(r["is_playable"] for r in records)
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records), playable=playable)
        rows = [
            [
                e(r["class_type"]),
                e(r["class_name"] or _EMPTY),
                flag_cell(r["is_playable"]),
            ]
            for r in records[start : start + page_size]
        ]
        return table(meta, self._columns(), rows)

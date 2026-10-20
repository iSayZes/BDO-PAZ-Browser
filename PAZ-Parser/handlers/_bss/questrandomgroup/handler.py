"""questrandomgroup.bss preview handler: one row per random quest group."""
from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.html import Column, e, error, sort_keys, table
from _common.lang import handler_text, load_handler_strings
from .parser import FILE_NAME, parse_questrandomgroup_records


_LANG_DIR = Path(__file__).parent / "lang"


class QuestRandomGroupBssHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        # unknown_* fields stay on the record for search and export, not shown.
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["groupKey"], "num", sort_key="group_key"),
            Column(cols["questCount"], "num", sort_key="quest_count"),
            Column(cols["drawCount"], "num", sort_key="draw_count"),
            Column(cols["mainId"], "num", sort_key="quest_chain_id"),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        try:
            return parse_questrandomgroup_records(data)
        except ValueError as ex:
            return [{"_error": f"{FILE_NAME} could not be parsed: {ex}"}]

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        if records and "_error" in records[0]:
            return error(records[0]["_error"])

        start = page * page_size
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records))
        rows = [
            [
                e(record["group_key"]),
                e(record["quest_count"]),
                e(record["draw_count"]),
                e(record["quest_chain_id"]),
            ]
            for record in records[start : start + page_size]
        ]
        return table(meta, self._columns(), rows)

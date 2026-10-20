"""multiplequest.bss preview handler: one row per quest chain with its quest ID range."""
from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.html import Column, e, error, sort_keys, table
from _common.lang import handler_text, load_handler_strings
from _common.loc import is_loc_loaded
from _common.pa_text import pa_cell, pa_fields
from _common.quest.quest import quest_title_tagged
from .parser import FILE_NAME, parse_multiplequest_records


_LANG_DIR = Path(__file__).parent / "lang"


class MultipleQuestBssHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["mainId"], "num", sort_key="quest_chain_id"),
            Column(cols["minSubId"], "num", sort_key="min_quest_id"),
            Column(cols["minTitle"], sort_key="min_title"),
            Column(cols["maxSubId"], "num", sort_key="max_quest_id"),
            Column(cols["maxTitle"], sort_key="max_title"),
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
            records = parse_multiplequest_records(data)
        except ValueError as ex:
            return [{"_error": f"{FILE_NAME} could not be parsed: {ex}"}]

        has_loc = is_loc_loaded()

        def title(chain: int, quest: int) -> str:
            return quest_title_tagged(chain, quest) if has_loc else ""

        # Titles as text, so tab search and CSV export see them.
        return [
            {
                **record,
                **pa_fields("min_title", title(record["quest_chain_id"], record["min_quest_id"])),
                **pa_fields("max_title", title(record["quest_chain_id"], record["max_quest_id"])),
            }
            for record in records
        ]

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
                e(record["quest_chain_id"]),
                e(record["min_quest_id"]),
                pa_cell(record, "min_title"),
                e(record["max_quest_id"]),
                pa_cell(record, "max_title"),
            ]
            for record in records[start : start + page_size]
        ]
        return table(meta, self._columns(), rows)

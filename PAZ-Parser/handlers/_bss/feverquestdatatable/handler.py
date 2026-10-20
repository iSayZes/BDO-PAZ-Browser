"""feverquestdatatable.bss preview handler: each Agris Fever quest and its point cost."""
from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.html import Column, e, error, sort_keys, table
from _common.lang import handler_text, load_handler_strings
from _common.quest.quest import quest_title
from .parser import FILE_NAME, parse_feverquestdatatable_records


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"


class FeverQuestDataTableBssHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["mainId"], "num", sort_key="quest_chain_id"),
            Column(cols["subId"], "num", sort_key="quest_id"),
            Column(cols["title"], sort_key="title"),
            Column(cols["feverPoint"], "num", sort_key="consumption_fever_point"),
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
            rows = parse_feverquestdatatable_records(data)
        except ValueError as ex:
            return [{"_error": f"{FILE_NAME} could not be parsed: {ex}"}]

        # The file holds no text, so without LOC the title is empty.
        return [
            {**row, "title": quest_title(row["quest_chain_id"], row["quest_id"])}
            for row in rows
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
                e(record["quest_id"]),
                e(record["title"] or _EMPTY),
                e(f"{record['consumption_fever_point']:,}"),
            ]
            for record in records[start : start + page_size]
        ]
        return table(meta, self._columns(), rows)

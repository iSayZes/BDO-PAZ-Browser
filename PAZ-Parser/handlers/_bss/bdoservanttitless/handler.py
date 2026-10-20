from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.character import character_name
from _common.character_link import (
    character_key_cell,
    character_row_ids,
    characterstatic_offset_companion,
    has_character_row,
)
from _common.html import Column, e, sort_keys, table
from _common.lang import handler_text, load_handler_strings
from _common.loc import loc_text
from .parser import parse_bdoservanttitless_records


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"
# The breed title the horse windows show as Base Coat, keyed by character ID.
_LOC_SERVANT_TITLE = 111


class BdoServantTitlesBssHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["characterId"], "num", sort_key="character_id"),
            Column(cols["name"], sort_key="name"),
            Column(cols["titleName"], "num", sort_key="title_name"),
            Column(cols["title"], sort_key="title"),
            Column(cols["contentsOption"], "num", sort_key="contents_option"),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def companions(self, entry: PazEntry) -> list[str]:
        return [characterstatic_offset_companion(entry.internal_path)]

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        row_ids = character_row_ids(companions)
        return [
            {
                **record,
                # The shown name: LOC in the user's language, else the character ID.
                "name": character_name(record["character_id"]) or str(record["character_id"]),
                "title": loc_text(_LOC_SERVANT_TITLE, record["character_id"]) or record["title_kr"],
                # 0 is "no contents group"; None keeps those rows last in a sort.
                "contents_option": record["contents_option"] or None,
                "has_character_row": has_character_row(row_ids, record["character_id"]),
            }
            for record in parse_bdoservanttitless_records(data)
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
                character_key_cell(r["character_id"], r["has_character_row"]),
                e(r["name"]),
                e(r["title_name"]),
                e(r["title"]),
                e(r["contents_option"] or _EMPTY),
            ]
            for r in records[start : start + page_size]
        ]
        return table(meta, self._columns(), rows)

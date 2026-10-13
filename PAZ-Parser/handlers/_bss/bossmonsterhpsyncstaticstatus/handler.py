"""bossmonsterhpsyncstaticstatus.bss preview handler: boss sector boxes in file order."""
from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.character import character_name
from _common.html import Column, e, error, sort_keys, table
from _common.lang import handler_text, load_handler_strings
from .parser import FILE_NAME, parse_bossmonsterhpsync_records


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"


class BossMonsterHpSyncStaticStatusBssHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["key"], "num", sort_key="key"),
            Column(cols["characterId"], "num", sort_key="character_id"),
            Column(cols["name"], sort_key="name"),
            Column(cols["sectorX"], "num", sort_key="min_x"),
            Column(cols["sectorZ"], "num", sort_key="min_z"),
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
            records = parse_bossmonsterhpsync_records(data)
        except ValueError as ex:
            return [{"_error": f"{FILE_NAME} could not be parsed: {ex}"}]

        return [{**record, "name": character_name(record["character_id"])} for record in records]

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        if records and "_error" in records[0]:
            return error(records[0]["_error"])

        start = page * page_size
        rows = [
            [
                e(r["key"]),
                e(r["character_id"]),
                e(r["name"] or _EMPTY),
                e(f"{r['min_x']}..{r['max_x']}"),
                e(f"{r['min_z']}..{r['max_z']}"),
            ]
            for r in records[start : start + page_size]
        ]
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records))
        return table(meta, self._columns(), rows)

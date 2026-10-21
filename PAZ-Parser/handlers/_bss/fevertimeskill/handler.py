"""fevertimeskill.bss preview handler: each Agris Fever drop skill and its drop bonus."""
from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.html import Column, e, error, sort_keys, table
from _common.lang import handler_text, load_handler_strings
from _common.rate import rate_percent
from _common.skill import skill_name
from .parser import FILE_NAME, parse_fevertimeskill_records


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"


class FeverTimeSkillBssHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["index"], "num", sort_key="index"),
            Column(cols["skillNo"], "num", sort_key="skill_no"),
            Column(cols["skill"], sort_key="skill_name"),
            Column(cols["dropAmount"], "num", sort_key="description"),
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
            rows = parse_fevertimeskill_records(data)
        except ValueError as ex:
            return [{"_error": f"{FILE_NAME} could not be parsed: {ex}"}]

        # LOC type 10, then the Korean skilltype.dbss name; empty without either.
        return [{**row, "skill_name": skill_name(row["skill_no"])} for row in rows]

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
                e(record["index"]),
                e(record["skill_no"]),
                e(record["skill_name"] or _EMPTY),
                e(rate_percent(record["description"])),
            ]
            for record in records[start : start + page_size]
        ]
        return table(meta, self._columns(), rows)

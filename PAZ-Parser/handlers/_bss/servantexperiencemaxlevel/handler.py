from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.character import character_name
from _common.html import Column, e, sort_keys, table
from _common.lang import handler_text, load_handler_strings
from .parser import parse_servantexperiencemaxlevel_records


_LANG_DIR = Path(__file__).parent / "lang"


class ServantExperienceMaxLevelBssHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["characterId"], "num", sort_key="character_id"),
            Column(cols["name"], sort_key="name"),
            Column(cols["maxLevel"], "num", sort_key="max_level"),
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
            # The shown name: LOC in the user's language, else the character ID.
            {**record, "name": character_name(record["character_id"]) or str(record["character_id"])}
            for record in parse_servantexperiencemaxlevel_records(data)
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
            [e(r["character_id"]), e(r["name"]), e(r["max_level"])]
            for r in records[start : start + page_size]
        ]
        return table(meta, self._columns(), rows)

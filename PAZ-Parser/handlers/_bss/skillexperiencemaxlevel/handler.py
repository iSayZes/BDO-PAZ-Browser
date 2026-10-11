from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.html import Column, e, sort_keys, table
from _common.lang import handler_text, load_handler_strings
from .parser import parse_skillexperiencemaxlevel_records


_LANG_DIR = Path(__file__).parent / "lang"


class SkillExperienceMaxLevelBssHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [Column(cols["maxLevel"], "num", sort_key="max_level")]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        return parse_skillexperiencemaxlevel_records(data, entry.internal_path.rsplit("/", 1)[-1])

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        start = page * page_size
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records))
        rows = [[e(r["max_level"])] for r in records[start : start + page_size]]
        return table(meta, self._columns(), rows)

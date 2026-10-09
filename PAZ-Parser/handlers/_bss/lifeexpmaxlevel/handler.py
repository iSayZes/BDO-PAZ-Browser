from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.html import Column, e, sort_keys, table
from _common.lang import handler_text, load_handler_strings
from _dbss.lifeexp.labels import life_skill_name, rank_text
from .parser import parse_lifeexpmaxlevel_records


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"


class LifeExpMaxLevelBssHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["lifeSkillId"], "num", sort_key="life_skill"),
            Column(cols["lifeSkill"], sort_key="life_skill_name"),
            Column(cols["maxLevel"], "num", sort_key="max_level"),
            # Sorting by Max Level gives the rank order.
            Column(cols["maxRank"]),
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
            {
                **record,
                "life_skill_name": life_skill_name(record["life_skill"]),
                "max_rank": rank_text(record["max_level"]),
            }
            for record in parse_lifeexpmaxlevel_records(data)
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
                e(r["life_skill"]),
                e(r["life_skill_name"]),
                e(r["max_level"]),
                e(r["max_rank"] or _EMPTY),
            ]
            for r in records[start : start + page_size]
        ]
        return table(meta, self._columns(), rows)

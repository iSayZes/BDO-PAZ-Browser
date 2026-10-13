from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.html import Column, e, sort_keys, table
from _common.lang import handler_text, load_handler_strings
from _dbss.lifeexp.labels import rank_text
from .parser import parse_traininglevelskillstat_records


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"
# 1,000,000 = 100%.
_RATE_PER_PERCENT = 10_000


def rate_text(rate: int) -> str:
    """A rate as the Character Info Training tooltip shows it: one decimal."""
    return f"{rate / _RATE_PER_PERCENT:.1f}%"


class TrainingLevelSkillStatBssHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["level"], "num", sort_key="level"),
            # Sorting by Level gives the rank order.
            Column(cols["rank"]),
            Column(cols["skillRate"], "num", sort_key="add_vehicle_skill_owner_rate"),
            Column(cols["speedRate"], "num", sort_key="add_servant_stat_rate"),
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
            {**record, "rank": rank_text(record["level"])}
            for record in parse_traininglevelskillstat_records(data)
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
                e(r["level"]),
                e(r["rank"] or _EMPTY),
                e(rate_text(r["add_vehicle_skill_owner_rate"])),
                e(rate_text(r["add_servant_stat_rate"])),
            ]
            for r in records[start : start + page_size]
        ]
        return table(meta, self._columns(), rows)

from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler
from table_sort import TableSort

from _common.html import Column, e, sort_keys, table
from _common.lang import handler_text, load_handler_strings
from _bss.pabr_values.oceansiege_names import siege_day_name
from .parser import parse_pvp_day_records


_LANG_DIR = Path(__file__).parent / "lang"


def _time_text(time: list[int]) -> str:
    """A (day_of_week, hour, minute) time as `Monday 07:00`; `0` is Sunday (the doc's Notes)."""
    day, hour, minute = time
    return f"{siege_day_name(day)} {hour:02d}:{minute:02d}"


class EdaniaPvpDayOptionBssHandler(PreviewHandler):
    """One row per schedule entry: its row number and its two times."""

    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["row"], "num", sort_key="row"),
            Column(cols["time1"]),
            Column(cols["time2"]),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def default_sort(self) -> TableSort | None:
        # File order keeps each row's entries together.
        return None

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        return parse_pvp_day_records(data)

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        start = page * page_size
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records))
        rows = [
            [e(r["row"]), *(e(_time_text(time)) for time in r["times"])]
            for r in records[start : start + page_size]
        ]
        return table(meta, self._columns(), rows)

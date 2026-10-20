"""barterlifelevelinfo.bss preview handler: the parley discount per Barter level."""
from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.html import Column, e, error, sort_keys, table
from _common.lang import handler_text, load_handler_strings
from _dbss.lifeexp.labels import rank_text
from .parser import DISCOUNT_POINTS_PER_PERCENT, FILE_NAME, parse_barterlifelevelinfo_records


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"


class BarterLifeLevelInfoBssHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["level"], "num", sort_key="level"),
            # Sorting by Level gives the rank order.
            Column(cols["rank"]),
            Column(cols["discountPoint"], "num", sort_key="discount_point"),
            Column(cols["discount"], "num", sort_key="discount_percent"),
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
            records = parse_barterlifelevelinfo_records(data)
        except ValueError as ex:
            return [{"_error": f"{FILE_NAME} could not be parsed: {ex}"}]

        return [
            {
                **record,
                "rank": rank_text(record["level"]),
                # As the Barter window shows it: the points over e1Percent.
                "discount_percent": record["discount_point"] / DISCOUNT_POINTS_PER_PERCENT,
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
                e(r["level"]),
                e(r["rank"] or _EMPTY),
                e(f"{r['discount_point']:,}"),
                e(f"{r['discount_percent']:.2f}%"),
            ]
            for r in records[start : start + page_size]
        ]
        return table(meta, self._columns(), rows)

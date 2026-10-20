from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.html import Column, e, sort_keys, table
from _common.lang import handler_text, load_handler_strings
from _common.rate import rate_percent
from _common.town import town_name
from .parser import parse_blizzardregioninfo_records


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"
def _wind(record: dict) -> str:
    return ", ".join(f"{record[axis]:g}" for axis in ("wind_x", "wind_y", "wind_z"))


class BlizzardRegionInfoBssHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["key"], "num", sort_key="key"),
            Column(cols["regionKey"], "num", sort_key="region_key"),
            Column(cols["regionName"], sort_key="region_name"),
            Column(cols["effectChanceMin"], "num", sort_key="effect_spawn_percent_min"),
            Column(cols["effectChanceMax"], "num", sort_key="effect_spawn_percent_max"),
            Column(cols["wind"], "num", sort_key="wind_x"),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        # LOC type 17 names every regioninfo.bss region, as in that table.
        return [
            {**record, "region_name": town_name(record["region_key"])}
            for record in parse_blizzardregioninfo_records(data)
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
                e(r["key"]),
                e(r["region_key"]),
                e(r["region_name"] or _EMPTY),
                e(rate_percent(r["effect_spawn_percent_min"])),
                e(rate_percent(r["effect_spawn_percent_max"])),
                e(_wind(r)),
            ]
            for r in records[start : start + page_size]
        ]
        return table(meta, self._columns(), rows)

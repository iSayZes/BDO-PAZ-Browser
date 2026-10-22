from __future__ import annotations

from collections.abc import Callable
from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler
from table_sort import TableSort

from _common.html import Column, e, sort_keys, table
from _common.lang import handler_text, load_handler_strings
from _common.territory import territory_name
from .parser import parse_revive_position_records


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"


def _coordinate_cell(value: float) -> str:
    """A world coordinate to the nearest unit."""
    return e(f"{value:,.0f}")


class OceanSiegeRevivePositionBssHandler(PreviewHandler):
    """One row per revive position: its territory and its world position.

    `parse` reads the file into records with `territory_key`, `x`, `y` and
    `z`: the ocean siege reader by default, or the one of
    `siege2024revivepositionstaticstatus.bss`, which shows the same columns.
    """

    def __init__(self, parse: Callable[[bytes], list[dict]] = parse_revive_position_records) -> None:
        self._parse = parse

    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["territoryKey"], "num", sort_key="territory_key"),
            Column(cols["territory"], sort_key="territory_name"),
            Column(cols["x"], "num", sort_key="x"),
            Column(cols["y"], "num", sort_key="y"),
            Column(cols["z"], "num", sort_key="z"),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def default_sort(self) -> TableSort | None:
        # File order keeps each territory's groups together, in group order.
        return None

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        return [
            {**record, "territory_name": territory_name(record["territory_key"])}
            for record in self._parse(data)
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
                e(r["territory_key"]),
                e(r["territory_name"]) if r["territory_name"] else _EMPTY,
                _coordinate_cell(r["x"]),
                _coordinate_cell(r["y"]),
                _coordinate_cell(r["z"]),
            ]
            for r in records[start : start + page_size]
        ]
        return table(meta, self._columns(), rows)

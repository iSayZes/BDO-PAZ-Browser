from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler
from table_sort import TableSort

from _common.html import Column, e, sort_keys, table
from _common.lang import handler_text, load_handler_strings
from .parser import parse_revive_position_records


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"
# Between the positions of one revive point in its cell.
_POSITION_SEPARATOR = " | "


def _position_text(position: list[float]) -> str:
    """`x, y, z` to the nearest unit."""
    return ", ".join(f"{value:.0f}" for value in position)


def _number_cell(value: int | None) -> str:
    return _EMPTY if value is None else e(value)


class RoseWarRevivePositionStaticStatusBssHandler(PreviewHandler):
    """One row per revive point: a team point by its type, or a sanctum point by its key."""

    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["respawnPositionType"], "num", sort_key="respawn_position_type"),
            Column(cols["sanctumId"], "num", sort_key="fierce_battle_key"),
            Column(cols["positions"], "num"),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def default_sort(self) -> TableSort | None:
        # Team points and sanctum points each have their own key field, so the
        # table opens in file order: the team points, then the sanctums.
        return None

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        return parse_revive_position_records(data)

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
                _number_cell(r["respawn_position_type"]),
                _number_cell(r["fierce_battle_key"]),
                e(_POSITION_SEPARATOR.join(_position_text(position) for position in r["positions"])),
            ]
            for r in records[start : start + page_size]
        ]
        return table(meta, self._columns(), rows)

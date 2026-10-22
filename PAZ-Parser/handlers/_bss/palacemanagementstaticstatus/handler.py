from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler
from table_sort import TableSort

from _common.character import character_name
from _common.html import Column, e, sort_keys, table
from _common.item_exchange import exchange_cell
from _common.lang import handler_text, load_handler_strings
from _common.rate import rate_percent
from .parser import MANUFACTURE, PRODUCTION, parse_palace_records


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"
# The board group type labels in lang `types`, by `board_group_type`.
_TYPE_KEYS = {PRODUCTION: "production", MANUFACTURE: "manufacture"}


class PalaceManagementBssHandler(PreviewHandler):
    """One row per board item: its board group, board, chance and exchange."""

    def _strings(self) -> dict[str, dict[str, str]]:
        return load_handler_strings(self.lang, _LANG_DIR)

    def _columns(self) -> list[Column]:
        cols = self._strings()["columns"]
        return [
            Column(cols["boardGroupKey"], "num", sort_key="board_group_key"),
            Column(cols["boardGroup"], sort_key="board_group_name_kr"),
            Column(cols["type"], sort_key="board_group_type"),
            Column(cols["npc"], sort_key="npc_name"),
            Column(cols["boardKey"], "num", sort_key="board_key"),
            Column(cols["board"], sort_key="board_name_kr"),
            Column(cols["itemIndex"], "num", sort_key="item_index"),
            Column(cols["probability"], "num", sort_key="probability"),
            Column(cols["exchange"], sort_key="exchange_key"),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def default_sort(self) -> TableSort | None:
        # File order keeps each group's boards and each board's items together.
        return None

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        return [
            {**record, "npc_name": character_name(record["npc_character_key"])}
            for record in parse_palace_records(data)
        ]

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        start = page * page_size
        strings = self._strings()
        types = strings["types"]
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records))
        rows = [
            [
                e(r["board_group_key"]),
                e(r["board_group_name_kr"] or _EMPTY),
                e(types[_TYPE_KEYS[r["board_group_type"]]] if r["board_group_type"] in _TYPE_KEYS else r["board_group_type"]),
                e(r["npc_name"] or r["npc_character_key"]),
                e(r["board_key"]),
                e(r["board_name_kr"] or _EMPTY),
                e(r["item_index"]),
                e(_EMPTY if r["probability"] is None else rate_percent(r["probability"])),
                exchange_cell(r["exchange_key"]),
            ]
            for r in records[start : start + page_size]
        ]
        return table(meta, self._columns(), rows)

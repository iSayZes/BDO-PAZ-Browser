"""Preview handlers for itemtradegrouptonpc.dbss and itemtradegroupfromnpc.dbss: trade goods per NPC."""
from __future__ import annotations

from collections.abc import Callable
from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.character import character_name
from _common.html import Column, e, icon_cell, sort_keys, table
from _common.icon_index import IconKind, icon_path
from _common.item_key import item_name_tagged
from _common.lang import handler_text, load_handler_strings
from _common.offset_table import OffsetColumn, OffsetTableHandler, offset_column, offset_records, size_column
from _common.pa_text import pa_cell, pa_fields
from _common.pabr_offset import parse_bare_offset_rows
from _common.trade_group import trade_group_text, trade_group_tooltip
from .commerce_types import commerce_type_name
from .parser import parse_itemtradegrouptonpc_records


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"


def item_trade_group_offset_handler() -> OffsetTableHandler:
    return OffsetTableHandler(
        _LANG_DIR,
        [
            OffsetColumn("character_id", "characterId"),
            offset_column("offset", "dataOffset"),
            size_column("size", "size"),
        ],
        offset_records(parse_bare_offset_rows, "character_id"),
    )


class ItemTradeGroupHandler(PreviewHandler):
    """One table row per item entry; `parse_records` reads the file's layout into those entries."""

    def __init__(self, parse_records: Callable[[bytes], list[dict]] = parse_itemtradegrouptonpc_records) -> None:
        self._parse_records = parse_records

    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["characterId"], "num", sort_key="character_id"),
            Column(cols["npc"], sort_key="name"),
            Column(cols["itemId"], "num", sort_key="item_id"),
            Column(cols["icon"], sort_key="icon_path"),
            Column(cols["item"], sort_key="item_name"),
            Column(cols["category"], sort_key="commerce_type_name"),
            Column(
                cols["tradeGroup"],
                extra_attrs=f'title="{e(trade_group_tooltip(self.lang))}"',
                sort_key="trade_group_type",
            ),
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
                "name": character_name(record["character_id"]),
                **pa_fields("item_name", item_name_tagged(record["item_id"])),
                "icon_path": icon_path(IconKind.ITEM, record["item_id"]),
                "commerce_type_name": commerce_type_name(record["commerce_type"]),
                "trade_group_text": trade_group_text(self.lang, record["trade_group_type"]),
            }
            for record in self._parse_records(data)
        ]

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        start = page * page_size
        meta = handler_text(
            self.lang,
            _LANG_DIR,
            "meta.count",
            count=len(records),
            npcs=len({record["character_id"] for record in records}),
        )
        rows = [
            [
                e(r["character_id"]),
                e(r["name"] or _EMPTY),
                e(r["item_id"]),
                icon_cell(r["icon_path"]),
                pa_cell(r, "item_name") if r["item_name"] else e(r["item_id"]),
                e(r["commerce_type_name"]),
                e(r["trade_group_text"]),
            ]
            for r in records[start : start + page_size]
        ]
        return table(meta, self._columns(), rows)

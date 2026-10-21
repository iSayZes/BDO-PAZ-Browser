"""auction.dbss preview handler: one row per auction with the goods it starts with."""
from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.character import character_name
from _common.enum_name import enum_name
from _common.html import Column, e, error, sort_keys, table, text_list_cell
from _common.item_key import item_name
from _common.lang import handler_text, load_handler_strings
from _common.offset_table import OffsetColumn, OffsetTableHandler, offset_column, offset_records, size_column
from _common.pabr_offset import parse_pabr_offset_rows
from .names import AUCTION_TYPE_NAMES
from .parser import FILE_NAME, parse_auction_records


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"
_MAX_GOODS = 6


def auction_offset_handler() -> OffsetTableHandler:
    return OffsetTableHandler(
        _LANG_DIR,
        [
            OffsetColumn("auction_no", "auctionNo"),
            offset_column("offset", "dataOffset"),
            size_column("size", "size"),
        ],
        offset_records(parse_pabr_offset_rows, "auction_no"),
    )


def _named_houses(houses: list[dict]) -> list[dict]:
    return [{**house, "name": character_name(house["character_key"])} for house in houses]


def _named_items(items: list[dict]) -> list[dict]:
    return [{**item, "name": item_name(item["item_key"])} for item in items]


class AuctionHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["auctionNo"], "num", sort_key="auction_no"),
            Column(cols["auctionType"], sort_key="auction_type_name"),
            Column(cols["description"], sort_key="desc_kr"),
            Column(cols["startTickCount"], "num", sort_key="start_tick_count"),
            Column(cols["intervalTickCount"], "num", sort_key="interval_tick_count"),
            Column(cols["houses"]),
            Column(cols["items"]),
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
            records = parse_auction_records(data)
        except ValueError as ex:
            return [{"_error": f"{FILE_NAME} could not be parsed: {ex}"}]

        return [
            {
                **record,
                "auction_type_name": enum_name(AUCTION_TYPE_NAMES, record["auction_type"]),
                "houses": _named_houses(record["houses"]),
                "items": _named_items(record["items"]),
            }
            for record in records
        ]

    def _goods_cell(self, goods: list[dict], key_field: str, price_field: str) -> str:
        labels = [
            handler_text(
                self.lang,
                _LANG_DIR,
                "goods.entry",
                name=good["name"] or str(good[key_field]),
                price=good[price_field],
            )
            for good in goods
        ]
        return text_list_cell(labels, _MAX_GOODS) or _EMPTY

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        if records and "_error" in records[0]:
            return error(records[0]["_error"])

        start = page * page_size
        rows = [
            [
                e(r["auction_no"]),
                e(r["auction_type_name"]),
                e(r["desc_kr"] or _EMPTY),
                e(f"{r['start_tick_count']:,}"),
                e(f"{r['interval_tick_count']:,}"),
                self._goods_cell(r["houses"], "character_key", "lower_price"),
                self._goods_cell(r["items"], "item_key", "price"),
            ]
            for r in records[start : start + page_size]
        ]
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records))
        return table(meta, self._columns(), rows)

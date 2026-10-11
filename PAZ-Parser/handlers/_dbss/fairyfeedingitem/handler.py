"""fairyfeedingitem.dbss parsed preview handlers."""
from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.html import Column, e, icon_cell, sort_keys, table
from _common.icon_index import IconKind, icon_path
from _common.item_key import item_name_tagged
from _common.lang import handler_text, load_handler_strings
from _common.offset_table import OffsetColumn, OffsetTableHandler, offset_column, size_column
from _common.pa_text import pa_cell, pa_fields
from .parser import (
    parse_fairyfeedingitem_records,
    parse_fairyfeedingitemoffset_records,
)


_LANG_DIR = Path(__file__).parent / "lang"


class FairyFeedingItemHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["itemId"], "num", sort_key="item_id"),
            Column(cols["icon"], sort_key="icon_path"),
            Column(cols["item"], sort_key="item_name"),
            Column(cols["exp"], "num", sort_key="exp"),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        records: list[dict] = []

        for record in parse_fairyfeedingitem_records(data):
            item_id = record["item_id"]
            records.append({
                **record,
                **pa_fields("item_name", item_name_tagged(item_id)),
                "icon_path": icon_path(IconKind.ITEM, item_id),
            })

        return records

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        start = page * page_size
        slice_ = records[start : start + page_size]

        rows = [
            [
                e(record["item_id"]),
                icon_cell(record["icon_path"]),
                pa_cell(record, "item_name") if record["item_name"] else e(record["item_id"]),
                e(f"{record['exp']:,}"),
            ]
            for record in slice_
        ]

        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records))
        return table(meta, self._columns(), rows)


def fairy_feeding_item_offset_handler() -> OffsetTableHandler:
    return OffsetTableHandler(
        _LANG_DIR,
        [
            OffsetColumn("item_id", "itemId"),
            offset_column("data_offset", "dataOffset"),
            size_column("data_size", "dataSize"),
            offset_column("record_start", "recordStart"),
        ],
        parse_fairyfeedingitemoffset_records,
    )

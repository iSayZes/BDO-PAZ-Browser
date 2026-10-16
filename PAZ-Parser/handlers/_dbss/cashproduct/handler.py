from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.html import Column, e, icon_cell, sort_keys, table
from _common.icon_index import IconKind, icon_path
from _common.lang import handler_text, load_handler_strings
from _common.loc import resolve_text_binds
from _common.item_key import item_name_tagged
from _common.pa_text import pa_cell, pa_fields, pa_line_cell
from _common.offset_table import OffsetColumn, OffsetTableHandler, offset_column, size_column
from .parser import (
    parse_cashproduct_records,
    parse_cashproductoffset_records,
)
from .text import product_texts


_LANG_DIR = Path(__file__).parent / "lang"
_OFFSET_FILE = "cashproductoffset.dbss"

_EMPTY = "-"


def cash_product_offset_handler() -> OffsetTableHandler:
    return OffsetTableHandler(
        _LANG_DIR,
        [
            OffsetColumn("product_id", "productId"),
            offset_column("data_offset", "dataOffset"),
            size_column("data_size", "dataSize"),
        ],
        parse_cashproductoffset_records,
    )


class CashProductHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["productId"], "num", sort_key="product_id"),
            Column(cols["icon"], sort_key="icon_path"),
            Column(cols["product"], sort_key="product"),
            Column(cols["itemId"], "num", sort_key="item_id"),
            Column(cols["item"], sort_key="item_name"),
            Column(cols["description"], sort_key="description"),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def companions(self, entry: PazEntry) -> list[str]:
        folder = entry.internal_path.rsplit("/", 1)[0]
        if folder == entry.internal_path:
            return [_OFFSET_FILE]
        return [f"{folder}/{_OFFSET_FILE}"]

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        offset_raw = companions.get(_OFFSET_FILE)
        if offset_raw is None:
            raise ValueError(f"{_OFFSET_FILE} companion not found.")

        records = parse_cashproduct_records(data, offset_raw)
        texts = product_texts()
        for record in records:
            # 0 means no linked item. None renders a dash and sorts last.
            item_id = record["item_id"] = record["item_id"] or None
            # The item's own icon, not the shop tile the product stores.
            record["icon_path"] = icon_path(IconKind.ITEM, item_id) if item_id else ""
            record.update(pa_fields("item_name", item_name_tagged(item_id) if item_id else ""))
            # User language first; the block's Korean name stands in without LOC.
            text = texts.get(record["product_id"])
            record.update(pa_fields("product", (text.name if text else "") or resolve_text_binds(record["product_name"])))
            record.update(pa_fields("description", text.description if text else ""))

        return records

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        start = page * page_size
        slice_ = records[start : start + page_size]
        linked = sum(1 for record in records if record["item_id"])
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records), linked=linked)
        rows = [
            [
                e(record["product_id"]),
                icon_cell(record["icon_path"]) if record["icon_path"] else _EMPTY,
                pa_cell(record, "product"),
                e(record["item_id"] or _EMPTY),
                pa_cell(record, "item_name"),
                pa_line_cell(record, "description"),
            ]
            for record in slice_
        ]
        return table(meta, self._columns(), rows)

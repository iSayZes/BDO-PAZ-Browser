"""waititem.dbss preview handler: Registration Queue item keys in file order."""
from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.html import Column, e, icon_cell, sort_keys, table
from _common.item_key import item_key_icon_path, item_key_text_tagged
from _common.lang import handler_text, load_handler_strings
from _common.offset_table import OffsetColumn, OffsetTableHandler, offset_column, offset_records, size_column
from _common.pa_text import pa_cell, pa_fields
from _common.pabr_offset import parse_bare_u32_offset_rows
from .parser import parse_waititem_records


_LANG_DIR = Path(__file__).parent / "lang"


def wait_item_offset_handler() -> OffsetTableHandler:
    return OffsetTableHandler(
        _LANG_DIR,
        [
            OffsetColumn("item_key", "itemKey"),
            offset_column("offset", "dataOffset"),
            size_column("size", "size"),
        ],
        offset_records(parse_bare_u32_offset_rows, "item_key"),
    )


class WaitItemHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["itemId"], "num", sort_key="item_id"),
            Column(cols["enchantLevel"], "num", sort_key="enchant_level"),
            Column(cols["icon"], sort_key="icon_path"),
            Column(cols["item"], sort_key="item_name"),
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
                **pa_fields("item_name", item_key_text_tagged(record["item_key"])),
                "icon_path": item_key_icon_path(record["item_key"]),
            }
            for record in parse_waititem_records(data)
        ]

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        start = page * page_size
        rows = [
            [
                e(r["item_id"]),
                e(r["enchant_level"]),
                icon_cell(r["icon_path"]),
                pa_cell(r, "item_name"),
            ]
            for r in records[start : start + page_size]
        ]
        meta = handler_text(
            self.lang,
            _LANG_DIR,
            "meta.count",
            count=len(records),
            items=len({r["item_id"] for r in records}),
        )
        return table(meta, self._columns(), rows)

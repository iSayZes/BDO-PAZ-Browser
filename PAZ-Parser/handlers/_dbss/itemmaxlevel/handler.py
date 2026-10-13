from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.html import Column, e, icon_cell, sort_keys, table
from _common.icon_index import IconKind, icon_path
from _common.item_key import item_name_tagged
from _common.lang import handler_text, load_handler_strings
from _common.offset_table import OffsetColumn, OffsetTableHandler, offset_column, offset_records, size_column
from _common.pa_text import pa_cell, pa_fields
from _common.pabr_offset import parse_pabr_u32_offset_rows
from .parser import parse_itemmaxlevel_records


_LANG_DIR = Path(__file__).parent / "lang"


def item_max_level_offset_handler() -> OffsetTableHandler:
    return OffsetTableHandler(
        _LANG_DIR,
        [
            OffsetColumn("item_id", "itemId"),
            offset_column("offset", "dataOffset"),
            size_column("size", "size"),
        ],
        offset_records(parse_pabr_u32_offset_rows, "item_id"),
    )


class ItemMaxLevelHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["itemId"], "num", sort_key="item_id"),
            Column(cols["icon"], sort_key="icon_path"),
            Column(cols["item"], sort_key="item_name"),
            Column(cols["maxLevel"], "num", sort_key="max_enchant_level"),
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
                **pa_fields("item_name", item_name_tagged(record["item_id"])),
                "icon_path": icon_path(IconKind.ITEM, record["item_id"]),
            }
            for record in parse_itemmaxlevel_records(data)
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
            enhanceable=sum(1 for record in records if record["max_enchant_level"]),
        )
        rows = [
            [
                e(r["item_id"]),
                icon_cell(r["icon_path"]),
                pa_cell(r, "item_name") if r["item_name"] else e(r["item_id"]),
                e(r["max_enchant_level"]),
            ]
            for r in records[start : start + page_size]
        ]
        return table(meta, self._columns(), rows)

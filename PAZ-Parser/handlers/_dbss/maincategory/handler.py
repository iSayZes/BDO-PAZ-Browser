"""maincategory.dbss preview handler: the Pearl Shop main categories."""
from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.html import Column, e, flag_cell, icon_cell, sort_keys, table
from _common.lang import handler_text, load_handler_strings
from _common.offset_table import OffsetColumn, OffsetTableHandler, offset_column, size_column
from _common.ui_texture import ui_texture_path
from .parser import OFFSET_FILE, parse_maincategory_records, parse_maincategoryoffset_records


_LANG_DIR = Path(__file__).parent / "lang"


def main_category_offset_handler() -> OffsetTableHandler:
    return OffsetTableHandler(
        _LANG_DIR,
        [
            OffsetColumn("category_id", "categoryId"),
            offset_column("record_offset", "dataOffset"),
            size_column("record_size", "size"),
        ],
        parse_maincategoryoffset_records,
    )


class MainCategoryHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["categoryId"], "num", sort_key="category_id"),
            Column(cols["displayOrder"], "num", sort_key="display_order"),
            Column(cols["tabImageNo"], "num", sort_key="tab_image_no"),
            Column(cols["categoryType"], "num", sort_key="category_type"),
            Column(cols["eventCategory"], "num", sort_key="event_category"),
            Column(cols["isDisplay"], sort_key="is_display"),
            Column(cols["icon"], sort_key="icon_path"),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def companions(self, entry: PazEntry) -> list[str]:
        folder = entry.internal_path.rsplit("/", 1)[0]
        return [f"{folder}/{OFFSET_FILE}"]

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        offset_raw = companions.get(OFFSET_FILE)
        if offset_raw is None:
            raise ValueError(f"{OFFSET_FILE} companion not found.")
        return [
            # The stored path hangs off ui_texture/; the cell loads the image from there.
            {**record, "_icon_file": ui_texture_path(record["icon_path"])}
            for record in parse_maincategory_records(data, offset_raw)
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
                e(r["category_id"]),
                e(r["display_order"]),
                e(r["tab_image_no"]),
                e(r["category_type"]),
                e(r["event_category"]),
                flag_cell(r["is_display"]),
                icon_cell(r["_icon_file"]),
            ]
            for r in records[start : start + page_size]
        ]
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records))
        return table(meta, self._columns(), rows)

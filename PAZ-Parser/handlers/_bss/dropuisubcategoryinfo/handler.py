from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.html import Column, e, sort_keys, sprite_icon_cell, table
from _common.lang import handler_text, load_handler_strings
from _common.loc import loc_text
from _common.texture_string import TEXTURE_STRING_COMBINE, TEXTURE_STRING_COMBINE_PATH, icon_fields, parse_texture_regions
from .parser import parse_sub_category_records


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"

# Category names, keyed (key, 0, 0, 0); the drop window's filter buttons.
_LOC_CATEGORY = 115


class DropUiSubCategoryInfoBssHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["key"], "num", sort_key="key"),
            Column(cols["name"], sort_key="name"),
            Column(cols["icon"], sort_key="icon_texture"),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def companions(self, entry: PazEntry) -> list[str]:
        return [TEXTURE_STRING_COMBINE_PATH]

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        categories = parse_sub_category_records(data)
        textures = parse_texture_regions(
            companions.get(TEXTURE_STRING_COMBINE),
            (category["icon_texture"] for category in categories),
        )
        return [
            {
                **category,
                "name": loc_text(_LOC_CATEGORY, category["key"]) or category["name_kr"],
                **icon_fields(textures, category["icon_texture"]),
            }
            for category in categories
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
                e(r["key"]),
                e(r["name"] or _EMPTY),
                sprite_icon_cell(r["icon_path"], r["icon_region"]),
            ]
            for r in records[start : start + page_size]
        ]
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records))
        return table(meta, self._columns(), rows)

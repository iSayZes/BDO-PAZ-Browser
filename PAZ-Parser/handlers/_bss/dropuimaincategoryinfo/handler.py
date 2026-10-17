from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.html import Column, e, sort_keys, sprite_icon_cell, table
from _common.lang import handler_text, load_handler_strings
from _common.territory import territory_name
from _common.texture_string import TEXTURE_STRING_COMBINE, TEXTURE_STRING_COMBINE_PATH, icon_fields, parse_texture_regions
from .parser import parse_main_category_records


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"
# The tab button adds a state to the stored key: `_Normal`, `_Over` or `_Click`
# (panel_window_renewdropitem_all_1.luac); the table shows the idle state.
_NORMAL_STATE = "_Normal"


class DropUiMainCategoryInfoBssHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["key"], "num", sort_key="key"),
            Column(cols["territoryKey"], "num", sort_key="territory_key"),
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
        tabs = parse_main_category_records(data)
        textures = parse_texture_regions(
            companions.get(TEXTURE_STRING_COMBINE),
            (tab["icon_texture"] + _NORMAL_STATE for tab in tabs),
        )
        return [
            {
                **tab,
                # LOC type 12 `str_id4` 1 is the tab name, `Inner Edania` where 0 says `Alyaelli`.
                "name": territory_name(tab["territory_key"]),
                **icon_fields(textures, tab["icon_texture"] + _NORMAL_STATE),
            }
            for tab in tabs
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
                e(r["territory_key"]),
                e(r["name"] or _EMPTY),
                sprite_icon_cell(r["icon_path"], r["icon_region"]),
            ]
            for r in records[start : start + page_size]
        ]
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records))
        return table(meta, self._columns(), rows)

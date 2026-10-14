"""growthpasscategory.dbss preview handler: the Growth Pass window's tabs."""
from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.html import Column, e, sort_keys, sprite_icon_cell, table
from _common.lang import handler_text, load_handler_strings
from _common.loc import loc_tagged
from _common.offset_table import OffsetColumn, OffsetTableHandler, offset_column, offset_records, size_column
from _common.pa_text import pa_cell, pa_fields
from _common.pabr_offset import parse_bare_u32_offset_rows
from _common.texture_string import TEXTURE_STRING_COMBINE, TEXTURE_STRING_COMBINE_PATH, parse_texture_regions
from .parser import parse_growthpasscategory_records


_LANG_DIR = Path(__file__).parent / "lang"
_OFFSET_FILE = "growthpasscategoryoffset.dbss"
# Category names, keyed (category_key, 0, 0, 0).
_NAME_LOC_TYPE = 107


def growth_pass_category_offset_handler() -> OffsetTableHandler:
    return OffsetTableHandler(
        _LANG_DIR,
        [
            OffsetColumn("category_key", "categoryKey"),
            offset_column("offset", "dataOffset"),
            size_column("size", "size"),
        ],
        offset_records(parse_bare_u32_offset_rows, "category_key"),
    )


class GrowthPassCategoryHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["categoryKey"], "num", sort_key="category_key"),
            Column(cols["icon"], sort_key="icon_texture"),
            Column(cols["name"], sort_key="name"),
            Column(cols["questChain"], "num", sort_key="quest_chain_id"),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def companions(self, entry: PazEntry) -> list[str]:
        folder = entry.internal_path.rsplit("/", 1)[0]
        return [f"{folder}/{_OFFSET_FILE}", TEXTURE_STRING_COMBINE_PATH]

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        offset_raw = companions.get(_OFFSET_FILE)
        if offset_raw is None:
            raise ValueError(f"{_OFFSET_FILE} companion not found.")

        categories = parse_growthpasscategory_records(data, offset_raw)
        textures = parse_texture_regions(
            companions.get(TEXTURE_STRING_COMBINE),
            (category.icon_texture for category in categories),
        )
        records: list[dict] = []
        for category in categories:
            icon = textures.get(category.icon_texture)
            name = loc_tagged(_NAME_LOC_TYPE, category.category_key) or category.name_kr
            records.append({
                "category_key": category.category_key,
                "name_kr": category.name_kr,
                **pa_fields("name", name),
                "icon_texture": category.icon_texture,
                "icon_path": icon.path if icon else "",
                "icon_region": list(icon.region) if icon else None,
                "quest_chain_id": category.quest_chain_id,
            })
        return records

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        start = page * page_size
        rows = [
            [
                e(r["category_key"]),
                sprite_icon_cell(r["icon_path"], r["icon_region"]),
                pa_cell(r, "name"),
                e(r["quest_chain_id"]),
            ]
            for r in records[start : start + page_size]
        ]
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records))
        return table(meta, self._columns(), rows)

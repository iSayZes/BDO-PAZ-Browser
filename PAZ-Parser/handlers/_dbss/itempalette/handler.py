"""itempalette.dbss preview handler: each dye item with the palette colour it applies."""
from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from bdo_models import PazEntry

from _common.html import Column, e
from _common.item_key import item_key_list_cell, item_key_text
from _common.offset_table import OffsetTableHandler, keyed_offset_handler
from _common.row_table import RowTableHandler
from _dbss.dyeingpalette.display import color_cell, palette_color_hexes, palette_name
from _dbss.dyeingpalette.parser import FILE_NAME as PALETTE_FILE
from .parser import FILE_NAME, KEY_FIELD, parse_itempalette_records, parse_itempaletteoffset_rows


_LANG_DIR = Path(__file__).parent / "lang"


def item_palette_offset_handler() -> OffsetTableHandler:
    return keyed_offset_handler(_LANG_DIR, parse_itempaletteoffset_rows, KEY_FIELD, "itemKey")


class ItemPaletteHandler(RowTableHandler):
    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["itemKey"], "num", sort_key="item_key"),
            Column(labels["item"], sort_key="item_name"),
            Column(labels["paletteType"], "num", sort_key="palette_type"),
            Column(labels["palette"], sort_key="palette_name"),
            Column(labels["paletteIndex"], "num", sort_key="palette_index"),
            Column(labels["color"], sort_key="color_hex"),
        ]

    def companions(self, entry: PazEntry) -> list[str]:
        folder = entry.internal_path.rsplit("/", 1)[0]
        return [f"{folder}/{PALETTE_FILE}"]

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        colors = palette_color_hexes(companions.get(PALETTE_FILE))
        return [
            {
                **record,
                "item_name": item_key_text(record["item_key"]),
                "palette_name": palette_name(record["palette_type"]),
                "color_hex": colors.get((record["palette_type"], record["palette_index"])),
            }
            for record in parse_itempalette_records(data)
        ]

    def cells(self, record: dict) -> list[str]:
        return [
            e(record["item_key"]),
            item_key_list_cell([record["item_key"]], 1),
            e(record["palette_type"]),
            e(record["palette_name"] or "-"),
            e(record["palette_index"]),
            color_cell(record["color_hex"]),
        ]

"""dyeingpalette.dbss preview handler: one row per palette colour, with the dye items that apply it.

The file stores one row per palette; the table lists its colours, each with
the palette's fields and its `palette_index`, the position `itempalette.dbss`
points at.
"""
from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from bdo_models import PazEntry
from table_sort import TableSort

from _common.binary import whole_float
from _common.html import Column, e
from _common.item_key import item_key_list_cell, item_key_text
from _common.offset_table import OffsetTableHandler, keyed_offset_handler
from _common.pabr_offset import parse_bare_u8_offset_rows
from _common.row_table import RowTableHandler
from _dbss.itempalette.parser import FILE_NAME as ITEM_PALETTE_FILE, parse_itempalette_records
from .display import color_cell, color_hex, palette_name
from .parser import FILE_NAME, parse_dyeingpalette_rows


_LANG_DIR = Path(__file__).parent / "lang"
_MAX_ITEMS = 3


def dyeing_palette_offset_handler() -> OffsetTableHandler:
    return keyed_offset_handler(_LANG_DIR, parse_bare_u8_offset_rows, "palette_type", "paletteType")


def _dye_items(item_palette: bytes | None) -> dict[tuple[int, int], list[int]]:
    """`(palette_type, palette_index) -> item keys` of `itempalette.dbss`, empty without it.

    Raises ValueError when it does not parse.
    """
    if item_palette is None:
        return {}
    items: dict[tuple[int, int], list[int]] = {}
    for row in parse_itempalette_records(item_palette):
        items.setdefault((row["palette_type"], row["palette_index"]), []).append(row["item_key"])
    return items


class DyeingPaletteHandler(RowTableHandler):
    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["paletteType"], "num", sort_key="palette_type"),
            Column(labels["palette"], sort_key="palette_name"),
            Column(labels["paletteIndex"], "num", sort_key="palette_index"),
            Column(labels["color"], sort_key="color_hex"),
            Column(labels["environment"], "num", sort_key="environment"),
            Column(labels["specular"], "num", sort_key="specular"),
            # A list column: it would only sort by its string form.
            Column(labels["items"]),
        ]

    def default_sort(self) -> TableSort | None:
        # The file order, palette type then palette index, spans two fields.
        return None

    def companions(self, entry: PazEntry) -> list[str]:
        folder = entry.internal_path.rsplit("/", 1)[0]
        return [f"{folder}/{ITEM_PALETTE_FILE}"]

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        items = _dye_items(companions.get(ITEM_PALETTE_FILE))
        records = []
        for row in parse_dyeingpalette_rows(data):
            palette = {
                "palette_type": row["palette_type"],
                "unknown_01": row["unknown_01"],
                "palette_name": palette_name(row["palette_type"]),
            }
            for index, color in enumerate(row["colors"]):
                item_keys = items.get((row["palette_type"], index), [])
                records.append({
                    **palette,
                    "palette_index": index,
                    **color,
                    "environment": whole_float(round(color["environment"], 4)),
                    "specular": whole_float(round(color["specular"], 4)),
                    "color_hex": color_hex(color),
                    "item_keys": item_keys,
                    "item_names": ", ".join(item_key_text(key) for key in item_keys),
                })
        return records

    def cells(self, record: dict) -> list[str]:
        return [
            e(record["palette_type"]),
            e(record["palette_name"] or "-"),
            e(record["palette_index"]),
            color_cell(record["color_hex"]),
            e(record["environment"]),
            e(record["specular"]),
            item_key_list_cell(record["item_keys"], _MAX_ITEMS) if record["item_keys"] else e("-"),
        ]

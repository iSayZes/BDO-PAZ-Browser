from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.html import e, icon_cell, table
from _common.icon_index import IconKind, icon_path
from _common.lang import load_handler_strings
from _common.loc import is_loc_loaded, loc_lookup, strip_pa_tags
from .parser import (
    parse_cashproduct_records,
    parse_cashproductoffset_records,
)


_LANG_DIR = Path(__file__).parent / "lang"
_OFFSET_FILE = "cashproductoffset.dbss"

# Item display names live in LOC type 0, keyed by item ID.
_LOC_TYPE_ITEM = 0

_EMPTY = "-"


def _item_name(item_id: int) -> str:
    if not item_id or not is_loc_loaded():
        return ""

    return strip_pa_tags(loc_lookup(_LOC_TYPE_ITEM, item_id, 0, 0, 0)).strip()


class CashProductOffsetHandler(PreviewHandler):
    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        return parse_cashproductoffset_records(data)

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        start = page * page_size
        slice_ = records[start : start + page_size]
        meta = f"{len(records):,} offset records"

        cols = load_handler_strings(self.lang, _LANG_DIR).get("offsetColumns", {})
        headers: list[tuple[str, str, str]] = [
            (cols.get("productId", "Product ID"), "num", ""),
            (cols.get("dataOffset", "Data Offset"), "num", ""),
            (cols.get("dataSize", "Data Size"), "num", ""),
        ]
        rows = [
            [
                e(record["product_id"]),
                e(f"0x{record['data_offset']:08X}"),
                e(f"{record['data_size']:,}"),
            ]
            for record in slice_
        ]
        return table(meta, headers, rows)


class CashProductHandler(PreviewHandler):
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
        for record in records:
            item_id = record["item_id"]
            # The item's own icon, not the shop tile the product stores.
            record["icon_path"] = icon_path(IconKind.ITEM, item_id) if item_id else ""
            # LOC already answers in the user's language; the block's Korean
            # name is only a fallback for products with no linked item.
            record["item_name"] = _item_name(item_id) or record["product_name"]

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
        meta = f"{len(records):,} cash products · {linked:,} linked items"

        cols = load_handler_strings(self.lang, _LANG_DIR).get("columns", {})
        headers: list[tuple[str, str, str]] = [
            (cols.get("itemId", "Item ID"), "num", ""),
            (cols.get("icon", "Icon"), "", ""),
            (cols.get("item", "Item"), "", ""),
        ]
        rows = [
            [
                e(record["item_id"] or _EMPTY),
                icon_cell(record["icon_path"]) if record["icon_path"] else _EMPTY,
                e(record.get("item_name") or _EMPTY),
            ]
            for record in slice_
        ]
        return table(meta, headers, rows)

"""encyclopedia.bss preview handler: Fishing Encyclopedia entries in file order."""
from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.html import Column, e, error, icon_cell, sort_keys, table
from _common.item_key import item_key_list_cell, item_key_text
from _common.lang import handler_text, load_handler_strings
from _common.pa_text import pa_fields, pa_line_cell
from .parser import FILE_NAME, parse_encyclopedia_records
from .text import entry_description


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"
_ONE_ITEM = 1


def _size_text(size: float) -> str:
    """`7` for a whole size, `7.5` otherwise."""
    return f"{size:g}"


def _average_size(record: dict) -> float:
    """The window's Average Size (`getAverageValue()`), matched on four fish."""
    return (record["base_size"] + record["unknown_10"]) / 2


class EncyclopediaBssHandler(PreviewHandler):
    def _strings(self) -> dict:
        return load_handler_strings(self.lang, _LANG_DIR)

    def _columns(self) -> list[Column]:
        cols = self._strings()["columns"]
        return [
            Column(cols["key"], "num", sort_key="key"),
            Column(cols["itemId"], "num", sort_key="item_id"),
            Column(cols["item"], sort_key="item_name"),
            Column(cols["image"], sort_key="image_path"),
            Column(cols["category"], sort_key="category_name"),
            Column(cols["rareness"], "num", sort_key="rareness"),
            Column(cols["baseSize"], "num", sort_key="base_size"),
            Column(cols["averageSize"], "num", sort_key="average_size"),
            Column(cols["description"], sort_key="description"),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        try:
            records = parse_encyclopedia_records(data)
        except ValueError as ex:
            return [{"_error": f"{FILE_NAME} could not be parsed: {ex}"}]

        categories = self._strings()["categories"]
        return [
            {
                **record,
                "item_name": item_key_text(record["item_id"]),
                "category_name": categories.get(str(record["category"]), str(record["category"])),
                "average_size": _average_size(record),
                **pa_fields("description", entry_description(record["key"]) or record["description_kr"]),
            }
            for record in records
        ]

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        if records and "_error" in records[0]:
            return error(records[0]["_error"])

        start = page * page_size
        rows = [
            [
                e(r["key"]),
                e(r["item_id"]),
                item_key_list_cell([r["item_id"]], _ONE_ITEM),
                icon_cell(r["image_path"]) if r["image_path"] else _EMPTY,
                e(r["category_name"]),
                e(r["rareness"]),
                e(_size_text(r["base_size"])),
                e(_size_text(r["average_size"])),
                pa_line_cell(r, "description"),
            ]
            for r in records[start : start + page_size]
        ]
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records))
        return table(meta, self._columns(), rows)

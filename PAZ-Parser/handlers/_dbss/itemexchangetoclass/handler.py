"""itemexchangetoclass.dbss preview handler: the item each class gets for one weapon exchange group."""
from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.class_type import class_name
from _common.html import Column, e, error, hidden_slice, icon_html_list_cell, sort_keys, table
from _common.item_key import item_key_icon_path, item_key_text, item_key_text_tagged
from _common.lang import handler_text, load_handler_strings
from _common.offset_table import OffsetColumn, OffsetTableHandler, offset_column, offset_records, size_column
from _common.pa_text import pa_html
from _common.pabr_offset import parse_bare_u32_offset_rows
from .parser import FILE_NAME, parse_itemexchangetoclass_records


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"
_ITEMS_SHOWN = 6


def item_exchange_to_class_offset_handler() -> OffsetTableHandler:
    return OffsetTableHandler(
        _LANG_DIR,
        [
            OffsetColumn("key", "key"),
            offset_column("data_offset", "dataOffset"),
            size_column("data_size", "size"),
        ],
        offset_records(parse_bare_u32_offset_rows, "key", "data_offset", "data_size"),
    )


def _class_slots(item_keys: list[int]) -> list[tuple[int, int]]:
    """`(class_type, item_key)` of every filled slot, lowest class type first."""
    return [(class_type, item_key) for class_type, item_key in enumerate(item_keys) if item_key]


def _class_item_text(class_type: int, item_key: int) -> str:
    return f"{class_name(class_type)}: {item_key_text(item_key)}"


def _items_cell(record: dict) -> str:
    """The first filled slots as class and item, each with its icon, and a count of the rest."""
    slots = _class_slots(record["item_keys"])
    entries = [
        (item_key_icon_path(item_key), f"{e(class_name(class_type))}: {pa_html(item_key_text_tagged(item_key))}")
        for class_type, item_key in slots[:_ITEMS_SHOWN]
    ]
    hidden = hidden_slice(record["class_items"], _ITEMS_SHOWN)
    return icon_html_list_cell(entries, len(slots) - len(entries), hidden_names=hidden)


class ItemExchangeToClassHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["key"], "num", sort_key="key"),
            Column(cols["exchangeType"], sort_key="exchange_type"),
            Column(cols["classCount"], "num", sort_key="class_count"),
            # A list column: it would only sort by its string form.
            Column(cols["items"]),
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
            records = parse_itemexchangetoclass_records(data)
        except ValueError as ex:
            return [{"_error": f"{FILE_NAME} could not be parsed: {ex}"}]

        type_names = load_handler_strings(self.lang, _LANG_DIR)["exchangeTypes"]
        return [
            {
                **record,
                "exchange_type_name": type_names.get(str(record["exchange_type"]), str(record["exchange_type"])),
                "class_count": len(_class_slots(record["item_keys"])),
                # Class and item as text, so tab search and CSV export see them.
                "class_items": [_class_item_text(*slot) for slot in _class_slots(record["item_keys"])],
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
                e(r["exchange_type_name"]),
                e(r["class_count"]),
                _items_cell(r) or _EMPTY,
            ]
            for r in records[start : start + page_size]
        ]
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records))
        return table(meta, self._columns(), rows)

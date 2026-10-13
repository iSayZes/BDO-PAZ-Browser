"""alchemystonechange.dbss preview handler: Growth recipes in file order."""
from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.html import Column, e, icon_cell, icon_html_label_cell, sort_keys, table
from _common.icon_index import IconKind, icon_path
from _common.item_key import item_name_tagged
from _common.lang import handler_text, load_handler_strings
from _common.offset_table import OffsetColumn, OffsetTableHandler, offset_column, offset_records, size_column
from _common.pa_text import pa_fields, pa_html, pa_key
from _common.pabr_offset import parse_bare_u32_offset_rows
from .parser import parse_alchemystonechange_records


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"
# A row with no result item (every Totem of the Sea row) holds 0; the record
# holds None, so the empty cell sorts last.
_NO_RESULT = 0


def alchemy_stone_change_offset_handler() -> OffsetTableHandler:
    return OffsetTableHandler(
        _LANG_DIR,
        [
            OffsetColumn("item_id", "itemId"),
            offset_column("offset", "dataOffset"),
            size_column("size", "size"),
        ],
        offset_records(parse_bare_u32_offset_rows, "item_id"),
    )


def _item_fields(field: str, item_id: int | None) -> dict:
    """The item's LOC name (`pa_fields`) and icon path under `<field>_name` and
    `<field>_icon_path`; both empty without an item."""
    if item_id is None:
        return {**pa_fields(f"{field}_name", ""), f"{field}_icon_path": ""}
    return {
        **pa_fields(f"{field}_name", item_name_tagged(item_id)),
        f"{field}_icon_path": icon_path(IconKind.ITEM, item_id),
    }


def _name_html(record: dict, field: str, item_id: int) -> str:
    """The item name in its grade colour, else its ID."""
    name_field = f"{field}_name"
    return pa_html(record[pa_key(name_field)]) if record[name_field] else e(item_id)


def _material_cell(record: dict) -> str:
    """The material icon and name, then ` x<count>`."""
    count = e(f"x{record['material_count']:,}")
    label = f"{_name_html(record, 'material', record['material_item_id'])} {count}"
    return icon_html_label_cell(record["material_icon_path"], label)


def _result_cell(record: dict) -> str:
    if record["result_item_id"] is None:
        return _EMPTY
    return icon_html_label_cell(
        record["result_icon_path"],
        _name_html(record, "result", record["result_item_id"]),
    )


class AlchemyStoneChangeHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["itemId"], "num", sort_key="item_id"),
            Column(cols["icon"], sort_key="item_icon_path"),
            Column(cols["item"], sort_key="item_name"),
            Column(cols["material"], sort_key="material_name"),
            Column(cols["condition"], sort_key="condition"),
            Column(cols["resultId"], "num", sort_key="result_item_id"),
            Column(cols["result"], sort_key="result_name"),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        records: list[dict] = []
        for record in parse_alchemystonechange_records(data):
            result_item_id = record["result_item_id"] if record["result_item_id"] != _NO_RESULT else None
            records.append({
                **record,
                "result_item_id": result_item_id,
                **_item_fields("item", record["item_id"]),
                **_item_fields("material", record["material_item_id"]),
                **_item_fields("result", result_item_id),
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
                e(r["item_id"]),
                icon_cell(r["item_icon_path"]),
                _name_html(r, "item", r["item_id"]),
                _material_cell(r),
                e(r["condition"]),
                e(r["result_item_id"]) if r["result_item_id"] is not None else _EMPTY,
                _result_cell(r),
            ]
            for r in records[start : start + page_size]
        ]
        meta = handler_text(
            self.lang,
            _LANG_DIR,
            "meta.count",
            count=len(records),
            materials=len({r["material_item_id"] for r in records}),
        )
        return table(meta, self._columns(), rows)

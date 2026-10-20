from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.html import Column, e, icon_cell, sort_keys, table
from _common.icon_index import IconKind, icon_path
from _common.item_key import item_name_tagged
from _common.lang import handler_text, load_handler_strings
from _common.offset_table import OffsetColumn, OffsetTableHandler, offset_column, size_column
from _common.pa_text import pa_cell, pa_fields
from _common.rate import rate_percent
from .parser import (
    LoyalismType,
    parse_employeeloyalismitem_records,
    parse_employeeloyalismitemoffset_records,
)


_LANG_DIR = Path(__file__).parent / "lang"
_OFFSET_FILE = "employeeloyalismitemoffset.dbss"


def _recovery_text(loyalism_type: int, recovery_value: int) -> str:
    """`+100` condition points, or `100%` for the condition rate a cure sets."""
    if loyalism_type == LoyalismType.RESURRECTION:
        return rate_percent(recovery_value)
    return f"+{recovery_value:,}"


def employee_loyalism_item_offset_handler() -> OffsetTableHandler:
    return OffsetTableHandler(
        _LANG_DIR,
        [
            OffsetColumn("item_id", "itemId"),
            offset_column("data_offset", "dataOffset"),
            size_column("data_size", "dataSize"),
        ],
        parse_employeeloyalismitemoffset_records,
    )


class EmployeeLoyalismItemHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["itemId"], "num", sort_key="item_id"),
            Column(cols["icon"], sort_key="icon_path"),
            Column(cols["item"], sort_key="item_name"),
            Column(cols["loyalismType"], sort_key="loyalism_type_name"),
            Column(cols["recovery"], "num", sort_key="recovery_value"),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def companions(self, entry: PazEntry) -> list[str]:
        folder = entry.internal_path.rsplit("/", 1)[0]
        return [f"{folder}/{_OFFSET_FILE}"]

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        offset_data = companions.get(_OFFSET_FILE)
        if offset_data is None:
            raise ValueError(f"{_OFFSET_FILE} companion not found.")

        type_names: dict[str, str] = load_handler_strings(self.lang, _LANG_DIR)["loyalismTypes"]
        records: list[dict] = []
        for record in parse_employeeloyalismitem_records(data, offset_data):
            loyalism_type = record["loyalism_type"]
            item_id = record["item_id"]
            records.append({
                **record,
                **pa_fields("item_name", item_name_tagged(item_id)),
                "icon_path": icon_path(IconKind.ITEM, item_id),
                "loyalism_type_name": type_names.get(str(loyalism_type), str(loyalism_type)),
                "recovery": _recovery_text(loyalism_type, record["recovery_value"]),
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
                e(record["item_id"]),
                icon_cell(record["icon_path"]),
                pa_cell(record, "item_name") if record["item_name"] else e(record["item_id"]),
                e(record["loyalism_type_name"]),
                e(record["recovery"]),
            ]
            for record in records[start : start + page_size]
        ]
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records))
        return table(meta, self._columns(), rows)

"""repairmaxendurance.dbss preview handler: the materials that restore each item's max durability."""
from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.html import Column, e, error, hidden_slice, html_list_cell, icon_html_label_cell, sort_keys, table
from _common.item_key import item_key_icon_path, item_key_text, item_key_text_tagged
from _common.lang import handler_text, load_handler_strings
from _common.offset_table import OffsetColumn, OffsetTableHandler, offset_column, offset_records, size_column
from _common.pa_text import pa_html
from _common.pabr_offset import parse_bare_u32_offset_rows
from .parser import FILE_NAME, parse_repairmaxendurance_records


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"
_LIST_PREVIEW_MATERIALS = 6


def repair_max_endurance_offset_handler() -> OffsetTableHandler:
    return OffsetTableHandler(
        _LANG_DIR,
        [
            OffsetColumn("item_key", "itemKey"),
            offset_column("data_offset", "dataOffset"),
            size_column("data_size", "size"),
        ],
        offset_records(parse_bare_u32_offset_rows, "item_key", "data_offset", "data_size"),
    )


def _repair_suffix(lang: str, repair_count: int, need_money: int) -> str:
    """` +10`, or ` +10, 5,000 silver` for a material that also costs silver."""
    if not need_money:
        return f" +{repair_count:,}"
    return " " + handler_text(lang, _LANG_DIR, "material.withMoney", count=repair_count, money=need_money)


def _materials(record: dict) -> list[tuple[int, int, int]]:
    """Each material as `(item_key, repair_count, need_money)`."""
    return list(
        zip(record["material_item_keys"], record["material_repair_counts"], record["material_need_money"])
    )


class RepairMaxEnduranceHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["itemKey"], "num", sort_key="item_key"),
            Column(cols["item"], sort_key="item_name"),
            # A list column: it would only sort by its string form.
            Column(cols["materials"]),
            Column(cols["onlyNeedMoney"], "num", sort_key="only_need_money"),
            Column(cols["onlyMoneyRepairCount"], "num", sort_key="only_money_repair_count"),
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
            records = parse_repairmaxendurance_records(data)
        except ValueError as ex:
            return [{"_error": f"{FILE_NAME} could not be parsed: {ex}"}]
        return [self._record_fields(record) for record in records]

    def _record_fields(self, record: dict) -> dict:
        return {
            **record,
            "item_name": item_key_text(record["item_key"]),
            # The text form of the list, so tab search and CSV export see it.
            "materials": [
                item_key_text(key) + _repair_suffix(self.lang, count, money)
                for key, count, money in _materials(record)
            ],
        }

    def _materials_cell(self, record: dict) -> str:
        """The first materials with icon, grade colour and repair count, and a count of the rest."""
        materials = _materials(record)
        shown = [
            icon_html_label_cell(
                item_key_icon_path(key),
                pa_html(item_key_text_tagged(key)) + e(_repair_suffix(self.lang, count, money)),
            )
            for key, count, money in materials[:_LIST_PREVIEW_MATERIALS]
        ]
        hidden_names = hidden_slice(record["materials"], _LIST_PREVIEW_MATERIALS)
        return html_list_cell(shown, len(materials) - len(shown), hidden_names) or _EMPTY

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
                e(r["item_key"]),
                icon_html_label_cell(item_key_icon_path(r["item_key"]), pa_html(item_key_text_tagged(r["item_key"]))),
                self._materials_cell(r),
                e(f"{r['only_need_money']:,}"),
                e(r["only_money_repair_count"]),
            ]
            for r in records[start : start + page_size]
        ]
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records))
        return table(meta, self._columns(), rows)

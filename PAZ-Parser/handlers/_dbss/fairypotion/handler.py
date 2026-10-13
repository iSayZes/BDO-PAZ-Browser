from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler
from table_sort import SORT_ASC, TableSort

from _common.html import Column, e, icon_cell, sort_keys, table
from _common.icon_index import IconKind, icon_path
from _common.item_key import item_name_tagged
from _common.lang import handler_text, load_handler_strings
from _common.offset_table import OffsetColumn, OffsetTableHandler, offset_column, size_column
from _common.pa_text import pa_cell, pa_fields
from .parser import parse_fairypotion_records, parse_fairypotionoffset_records


_LANG_DIR = Path(__file__).parent / "lang"


class FairyPotionHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["potionType"], "num", sort_key="potion_type"),
            Column(cols["resource"], sort_key="resource"),
            Column(cols["itemId"], "num", sort_key="item_id"),
            Column(cols["icon"], sort_key="icon_path"),
            Column(cols["item"], sort_key="item_name"),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def default_sort(self) -> TableSort | None:
        # HP first, as the fairy window lists the HP slot before the MP slot.
        return TableSort("potion_type", SORT_ASC)

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        resources: dict[str, str] = load_handler_strings(self.lang, _LANG_DIR)["resources"]
        records: list[dict] = []

        for record in parse_fairypotion_records(data):
            potion_type = record["potion_type"]
            item_id = record["item_id"]
            records.append({
                **record,
                "resource": resources.get(str(potion_type), str(potion_type)),
                **pa_fields("item_name", item_name_tagged(item_id)),
                "icon_path": icon_path(IconKind.ITEM, item_id),
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
                e(record["potion_type"]),
                e(record["resource"]),
                e(record["item_id"]),
                icon_cell(record["icon_path"]),
                pa_cell(record, "item_name") if record["item_name"] else e(record["item_id"]),
            ]
            for record in records[start : start + page_size]
        ]

        list_count = len({record["potion_type"] for record in records})
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records), lists=list_count)
        return table(meta, self._columns(), rows)


def fairy_potion_offset_handler() -> OffsetTableHandler:
    return OffsetTableHandler(
        _LANG_DIR,
        [
            OffsetColumn("potion_type", "potionType"),
            offset_column("data_offset", "dataOffset"),
            size_column("data_size", "dataSize"),
        ],
        parse_fairypotionoffset_records,
    )

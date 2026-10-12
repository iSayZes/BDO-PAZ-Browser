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
from .parser import parse_alchemycharge_records, parse_alchemychargeoffset_records


_LANG_DIR = Path(__file__).parent / "lang"


def alchemy_charge_offset_handler() -> OffsetTableHandler:
    return OffsetTableHandler(
        _LANG_DIR,
        [
            OffsetColumn("stone_type", "stoneType"),
            OffsetColumn("item_id", "itemId"),
            offset_column("offset", "dataOffset"),
            size_column("size", "size"),
        ],
        parse_alchemychargeoffset_records,
    )


class AlchemyChargeHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["stoneType"], sort_key="stone_type"),
            Column(cols["itemId"], "num", sort_key="item_id"),
            Column(cols["icon"], sort_key="icon_path"),
            Column(cols["item"], sort_key="item_name"),
            Column(cols["chargePoint"], "num", sort_key="charge_point"),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def default_sort(self) -> TableSort | None:
        # Destruction first; each stone type keeps the file's material order.
        return TableSort("stone_type", SORT_ASC)

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        stone_names = load_handler_strings(self.lang, _LANG_DIR)["stoneTypes"]
        return [
            {
                **record,
                "stone_type_name": stone_names.get(str(record["stone_type"]), str(record["stone_type"])),
                **pa_fields("item_name", item_name_tagged(record["item_id"])),
                "icon_path": icon_path(IconKind.ITEM, record["item_id"]),
            }
            for record in parse_alchemycharge_records(data)
        ]

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        start = page * page_size
        meta = handler_text(
            self.lang,
            _LANG_DIR,
            "meta.count",
            count=len(records),
            types=len({record["stone_type"] for record in records}),
        )
        rows = [
            [
                e(r["stone_type_name"]),
                e(r["item_id"]),
                icon_cell(r["icon_path"]),
                pa_cell(r, "item_name") if r["item_name"] else e(r["item_id"]),
                e(r["charge_point"]),
            ]
            for r in records[start : start + page_size]
        ]
        return table(meta, self._columns(), rows)

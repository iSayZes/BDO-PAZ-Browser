"""purchaselimitgroup.dbss preview handler: Pearl Shop purchase limits shared by a product group."""
from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.html import Column, e, error, sort_keys, table
from _common.lang import handler_text, load_handler_strings
from _common.offset_table import OffsetColumn, OffsetTableHandler, offset_column, offset_records, size_column
from _common.pabr_offset import parse_bare_u32_offset_rows
from .parser import FILE_NAME, parse_purchaselimitgroup_records


_LANG_DIR = Path(__file__).parent / "lang"
# Label keys of CppEnums.CashPurchaseLimitType, in value order from 0.
_LIMIT_TYPE_KEYS = ("none", "atCharacter", "atAccount")


def purchase_limit_group_offset_handler() -> OffsetTableHandler:
    return OffsetTableHandler(
        _LANG_DIR,
        [
            OffsetColumn("group_no", "groupNo"),
            offset_column("data_offset", "dataOffset"),
            size_column("data_size", "size"),
        ],
        offset_records(parse_bare_u32_offset_rows, "group_no", "data_offset", "data_size"),
    )


class PurchaseLimitGroupHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["groupNo"], "num", sort_key="group_no"),
            Column(cols["purchaseType"], sort_key="purchase_type"),
            Column(cols["purchaseCount"], "num", sort_key="purchase_count"),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def _limit_type_name(self, purchase_type: int) -> str:
        """The limit type label, or the bare value outside the enum."""
        if not 0 <= purchase_type < len(_LIMIT_TYPE_KEYS):
            return str(purchase_type)
        return load_handler_strings(self.lang, _LANG_DIR)["limitTypes"][_LIMIT_TYPE_KEYS[purchase_type]]

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        try:
            records = parse_purchaselimitgroup_records(data)
        except ValueError as ex:
            return [{"_error": f"{FILE_NAME} could not be parsed: {ex}"}]
        return [
            {**record, "purchase_type_name": self._limit_type_name(record["purchase_type"])}
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
                e(r["group_no"]),
                e(r["purchase_type_name"]),
                e(f"{r['purchase_count']:,}"),
            ]
            for r in records[start : start + page_size]
        ]
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records))
        return table(meta, self._columns(), rows)

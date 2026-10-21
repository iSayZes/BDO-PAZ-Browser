"""carriagespec.dbss preview handler: weight limits, fees and trade goods flags per transport carriage type."""
from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.html import Column, e, error, flag_cell, sort_keys, table
from _common.lang import handler_text, load_handler_strings
from _common.offset_table import OffsetColumn, OffsetTableHandler, offset_column, offset_records, size_column
from _common.pabr_offset import parse_bare_u8_offset_rows
from .parser import FILE_NAME, parse_carriagespec_records


_LANG_DIR = Path(__file__).parent / "lang"

# (record field, lang column key); every one is a whole number shown with thousands separators.
_NUMBER_FIELDS = (
    ("distance_per_minute", "distancePerMinute"),
    ("loadage", "loadage"),
    ("transport_max_weight", "transportMaxWeight"),
    ("camasilb_add_transport_max_weight", "camasilbAddTransportMaxWeight"),
    ("base_fee", "baseFee"),
    ("overload_weight", "overloadWeight"),
    ("fee_per_weight", "feePerWeight"),
)
_FLAG_FIELDS = (
    ("non_stack_trade", "nonStackTrade"),
    ("stack_trade", "stackTrade"),
    ("expiration_period_trade", "expirationPeriodTrade"),
)


def carriage_spec_offset_handler() -> OffsetTableHandler:
    return OffsetTableHandler(
        _LANG_DIR,
        [
            OffsetColumn("carriage_key", "carriageKey"),
            offset_column("offset", "dataOffset"),
            size_column("size", "size"),
        ],
        offset_records(parse_bare_u8_offset_rows, "carriage_key"),
    )


class CarriageSpecHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["carriageKey"], "num", sort_key="carriage_key"),
            *(Column(cols[label], "num", sort_key=field) for field, label in _NUMBER_FIELDS),
            *(Column(cols[label], sort_key=field) for field, label in _FLAG_FIELDS),
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
            return parse_carriagespec_records(data)
        except ValueError as ex:
            return [{"_error": f"{FILE_NAME} could not be parsed: {ex}"}]

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
                e(r["carriage_key"]),
                *(e(f"{r[field]:,}") for field, _ in _NUMBER_FIELDS),
                *(flag_cell(r[field] != 0) for field, _ in _FLAG_FIELDS),
            ]
            for r in records[start : start + page_size]
        ]
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records))
        return table(meta, self._columns(), rows)

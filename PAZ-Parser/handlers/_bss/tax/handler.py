from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler
from table_sort import TableSort

from _common.html import Column, e, sort_keys, table
from _common.lang import handler_text, load_handler_strings
from _common.territory import territory_name
from .parser import parse_tax_records


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"
# CppEnums.TaxType 0 to 5 (global_define_cpp_enum.luac, client 3482), without
# the eTaxType prefix; 6 and 7 from the 2016 gc::TaxType (tax_bss.md, Tax Types).
TAX_TYPE_NAMES: tuple[str, ...] = (
    "BuyItemFromSystem",
    "ReserveTemp",
    "BuyHorseFromServantMarket",
    "BuyHorseFromServantMating",
    "DeliverItemByPublicWagon",
    "SellItemToItemMarket",
    "SellWorkerToMarket",
    "SellPetInAuction",
)


def tax_type_text(tax_type: int) -> str:
    """`4 DeliverItemByPublicWagon`: a tax type and its enum name, or the bare value outside the enum."""
    if 0 <= tax_type < len(TAX_TYPE_NAMES):
        return f"{tax_type} {TAX_TYPE_NAMES[tax_type]}"
    return str(tax_type)


class TaxBssHandler(PreviewHandler):
    """One row per territory and tax type: the bounds and the system rate."""

    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["territoryKey"], "num", sort_key="territory_key"),
            Column(cols["territory"], sort_key="territory_name"),
            Column(cols["taxType"], sort_key="tax_type"),
            Column(cols["minPercentOrPrice"], "num", sort_key="min_percent_or_price"),
            Column(cols["maxPercentOrPrice"], "num", sort_key="max_percent_or_price"),
            Column(cols["systemPercent"], "num", sort_key="system_percent"),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def default_sort(self) -> TableSort | None:
        # File order keeps each territory's eight tax types together.
        return None

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        return [
            {**record, "territory_name": territory_name(record["territory_key"])}
            for record in parse_tax_records(data)
        ]

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        start = page * page_size
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records))
        rows = [
            [
                e(r["territory_key"]),
                e(r["territory_name"]) if r["territory_name"] else _EMPTY,
                e(tax_type_text(r["tax_type"])),
                e(f"{r['min_percent_or_price']:,}"),
                e(f"{r['max_percent_or_price']:,}"),
                e(f"{r['system_percent']:,}"),
            ]
            for r in records[start : start + page_size]
        ]
        return table(meta, self._columns(), rows)

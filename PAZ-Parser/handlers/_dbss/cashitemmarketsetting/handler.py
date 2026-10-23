"""cashitemmarketsetting.dbss preview handler: the Central Market price settings of each Pearl Shop item."""
from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from _common.html import Column, e, icon_cell
from _common.icon_index import IconKind, icon_path
from _common.item_key import item_name_tagged
from _common.offset_table import OffsetTableHandler, keyed_offset_handler
from _common.pa_text import pa_cell, pa_fields
from _common.row_table import RowTableHandler
from .parser import (
    FILE_NAME,
    KEY_FIELD,
    parse_cashitemmarketsetting_records,
    parse_cashitemmarketsettingoffset_rows,
)


_LANG_DIR = Path(__file__).parent / "lang"


def cash_item_market_setting_offset_handler() -> OffsetTableHandler:
    return keyed_offset_handler(_LANG_DIR, parse_cashitemmarketsettingoffset_rows, KEY_FIELD, "itemId")


def _number(value: int) -> str:
    return e(f"{value:,}")


class CashItemMarketSettingHandler(RowTableHandler):
    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["itemId"], "num", sort_key=KEY_FIELD),
            Column(labels["icon"], sort_key="icon_path"),
            Column(labels["item"], sort_key="item_name"),
            Column(labels["basePrice"], "num", sort_key="base_price_for_item_market"),
            Column(labels["maxestPercent"], "num", sort_key="maxest_percent_for_item_market"),
            Column(labels["minestPercent"], "num", sort_key="minest_percent_for_item_market"),
            Column(labels["maxRegisterCount"], "num", sort_key="max_register_count_for_item_market"),
        ]

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        return [
            {
                **record,
                **pa_fields("item_name", item_name_tagged(record[KEY_FIELD])),
                "icon_path": icon_path(IconKind.ITEM, record[KEY_FIELD]),
            }
            for record in parse_cashitemmarketsetting_records(data)
        ]

    def cells(self, record: dict) -> list[str]:
        return [
            e(record[KEY_FIELD]),
            icon_cell(record["icon_path"]),
            pa_cell(record, "item_name") if record["item_name"] else e(record[KEY_FIELD]),
            _number(record["base_price_for_item_market"]),
            _number(record["maxest_percent_for_item_market"]),
            _number(record["minest_percent_for_item_market"]),
            e(record["max_register_count_for_item_market"]),
        ]

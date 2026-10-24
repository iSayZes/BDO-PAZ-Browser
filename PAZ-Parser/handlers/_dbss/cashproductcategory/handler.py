"""cashproductcategory.dbss preview handler: the Pearl Shop category tree, one row per category."""
from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from table_sort import TableSort

from _common.enum_name import enum_name
from _common.html import Column, e, flag_cell
from _common.offset_table import OffsetTableHandler, keyed_offset_handler
from _common.pa_text import pa_fields, pa_line_cell
from _common.row_table import RowTableHandler
from .parser import FILE_NAME, KEY_FIELD, parse_cashproductcategory_records, parse_cashproductcategoryoffset_rows
from .text import PRICE_TYPE_NAMES, category_label_tagged


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"


def cash_product_category_offset_handler() -> OffsetTableHandler:
    return keyed_offset_handler(_LANG_DIR, parse_cashproductcategoryoffset_rows, KEY_FIELD, "mainKey")


def _key_cell(value: int | None) -> str:
    return _EMPTY if value is None else e(value)


class CashProductCategoryHandler(RowTableHandler):
    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["mainKey"], "num", sort_key=KEY_FIELD),
            Column(labels["middleKey"], "num", sort_key="middle_key"),
            Column(labels["smallKey"], "num", sort_key="small_key"),
            Column(labels["name"], sort_key="name"),
            Column(labels["uniqueNo"], "num", sort_key="unique_no"),
            Column(labels["priceType"], sort_key="price_type_name"),
            Column(labels["useable"], sort_key="is_useable"),
            Column(labels["specialCategoryType"], "num", sort_key="special_category_type"),
            Column(labels["tagType"], "num", sort_key="tag_type"),
            Column(labels["tagOrder"], "num", sort_key="tag_order"),
        ]

    def default_sort(self) -> TableSort | None:
        # The file order is the shop's tree: each main category, then its
        # middle and small ones; no single field gives that order.
        return None

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        return [
            {
                **record,
                **pa_fields("name", category_label_tagged(record)),
                "price_type_name": enum_name(PRICE_TYPE_NAMES, record["price_type"]),
            }
            for record in parse_cashproductcategory_records(data)
        ]

    def cells(self, record: dict) -> list[str]:
        return [
            e(record[KEY_FIELD]),
            _key_cell(record["middle_key"]),
            _key_cell(record["small_key"]),
            pa_line_cell(record, "name"),
            e(record["unique_no"]),
            e(record["price_type_name"]),
            flag_cell(bool(record["is_useable"])),
            e(record["special_category_type"]),
            e(record["tag_type"]),
            e(record["tag_order"]),
        ]

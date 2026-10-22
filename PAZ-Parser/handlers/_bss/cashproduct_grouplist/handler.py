"""cashproduct_grouplist.bss preview handler: each Pearl Shop offer group with its products."""
from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from _common.html import Column, e, hidden_slice, html_list_cell, record_link
from _common.pa_text import strip_pa_tags
from _common.row_table import RowTableHandler
from _dbss.cashproduct.text import product_texts
from .parser import FILE_NAME, KEY_FIELD, parse_cashproduct_grouplist_records


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"
_LINK_CLASS = "record-link"
CASH_PRODUCT_PATH = "gamecommondata/binary/cashproduct.dbss"
_PRODUCT_FIELD = "product_id"
# Products shown in the list cell before the rest collapse into a count.
_MAX_PRODUCTS = 6


def _product_label(product_no: int, names: Mapping[int, str]) -> str:
    """`Name (product number)`, or the number alone when LOC has no name."""
    name = names.get(product_no, "")
    return f"{name} ({product_no})" if name else str(product_no)


class CashProductGroupListHandler(RowTableHandler):
    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["offerGroup"], "num", sort_key=KEY_FIELD),
            Column(labels["productCount"], "num", sort_key="product_count"),
            Column(labels["products"], sort_key="products_text"),
        ]

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        names = {
            product_no: " ".join(strip_pa_tags(text.name).split())
            for product_no, text in product_texts().items()
        }
        records = []
        for record in parse_cashproduct_grouplist_records(data):
            labels = [_product_label(product_no, names) for product_no in record["product_nos"]]
            records.append({**record, "products_text": ", ".join(labels), "_product_labels": labels})
        return records

    def cells(self, record: dict) -> list[str]:
        product_nos = record["product_nos"]
        labels = record["_product_labels"]
        shown = [
            record_link(label, CASH_PRODUCT_PATH, _PRODUCT_FIELD, product_no, _LINK_CLASS)
            for product_no, label in zip(product_nos[:_MAX_PRODUCTS], labels)
        ]
        products = html_list_cell(shown, len(product_nos) - _MAX_PRODUCTS, hidden_slice(labels, _MAX_PRODUCTS))
        return [
            e(record[KEY_FIELD]),
            e(record["product_count"]),
            products or _EMPTY,
        ]

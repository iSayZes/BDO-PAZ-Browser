"""cashchoose.dbss preview handler: each Pearl Shop choice pack with the products a buyer picks from."""
from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from _common.html import Column, e, flag_cell, hidden_slice, html_list_cell, icon_cell, record_link
from _common.icon_index import clean_stored_icon_path
from _common.offset_table import OffsetTableHandler, keyed_offset_handler
from _common.pa_text import strip_pa_tags
from _common.row_table import RowTableHandler
from _common.ui_texture import UI_TEXTURE_ICON_ROOT, ui_texture_path
from _dbss.cashproduct.text import product_texts
from .parser import FILE_NAME, KEY_FIELD, parse_cashchoose_records, parse_cashchooseoffset_rows


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"
_LINK_CLASS = "record-link"
CASH_PRODUCT_PATH = "gamecommondata/binary/cashproduct.dbss"
_PRODUCT_FIELD = "product_id"
# Products shown in the list cell before the rest collapse into a count.
_MAX_PRODUCTS = 6


def cash_choose_offset_handler() -> OffsetTableHandler:
    return keyed_offset_handler(_LANG_DIR, parse_cashchooseoffset_rows, KEY_FIELD, "chooseKey")


def _products(record: dict) -> list[tuple[int, int]]:
    """The (product number, stack count) of every filled slot, in slot order."""
    return [
        (product_no, stack)
        for product_no, stack in zip(record["include_product_no"], record["stack_count"], strict=True)
        if product_no
    ]


def _product_label(product_no: int, stack: int, names: Mapping[int, str]) -> str:
    """`Name (product number)`, or the number alone when LOC has no name; `xN` for a stack above 1."""
    name = names.get(product_no, "")
    label = f"{name} ({product_no})" if name else str(product_no)
    return f"{label} x{stack:,}" if stack > 1 else label


def _icon_path(stored: str) -> str:
    """PAZ path of the stored pack icon, relative to `ui_texture/icon/`; '' for none."""
    return ui_texture_path(clean_stored_icon_path(stored), UI_TEXTURE_ICON_ROOT)


class CashChooseHandler(RowTableHandler):
    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["chooseKey"], "num", sort_key=KEY_FIELD),
            Column(labels["icon"], sort_key="icon_path"),
            Column(labels["chooseCount"], "num", sort_key="choose_count"),
            Column(labels["isChooseDuplicate"], sort_key="is_choose_duplicate"),
            Column(labels["productCount"], "num", sort_key="choose_cash_count"),
            Column(labels["products"], sort_key="products_text"),
        ]

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        names = {
            product_no: " ".join(strip_pa_tags(text.name).split())
            for product_no, text in product_texts().items()
        }
        records = []
        for record in parse_cashchoose_records(data):
            products = _products(record)
            labels = [_product_label(product_no, stack, names) for product_no, stack in products]
            records.append(
                {
                    **record,
                    "icon_path": _icon_path(record["display_icon_path"]),
                    "products_text": ", ".join(labels),
                    "_product_nos": [product_no for product_no, _ in products],
                    "_product_labels": labels,
                }
            )
        return records

    def cells(self, record: dict) -> list[str]:
        product_nos = record["_product_nos"]
        labels = record["_product_labels"]
        shown = [
            record_link(label, CASH_PRODUCT_PATH, _PRODUCT_FIELD, product_no, _LINK_CLASS)
            for product_no, label in zip(product_nos[:_MAX_PRODUCTS], labels)
        ]
        products = html_list_cell(shown, len(product_nos) - _MAX_PRODUCTS, hidden_slice(labels, _MAX_PRODUCTS))
        return [
            e(record[KEY_FIELD]),
            icon_cell(record["icon_path"]),
            e(record["choose_count"]),
            flag_cell(bool(record["is_choose_duplicate"])),
            e(record["choose_cash_count"]),
            products or _EMPTY,
        ]

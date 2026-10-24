"""coupon.dbss preview handler: each Pearl Shop discount coupon with its discount and category."""
from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from _common.html import Column, e, icon_html_label_cell
from _common.loc import loc_tagged
from _common.offset_table import OffsetTableHandler, keyed_offset_handler
from _common.pa_text import pa_fields, pa_html, pa_key, strip_pa_tags
from _common.rate import rate_percent
from _common.row_table import RowTableHandler
from _common.ui_texture import UI_TEXTURE_ICON_ROOT, ui_texture_path
from _dbss.cashproductcategory.text import ALL_CATEGORIES_KEY, category_name_tagged, category_path_text
from .parser import FILE_NAME, KEY_FIELD, NO_CATEGORY, parse_coupon_records, parse_couponoffset_rows


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"
LOC_COUPON_NAME = 47


def coupon_offset_handler() -> OffsetTableHandler:
    return keyed_offset_handler(_LANG_DIR, parse_couponoffset_rows, KEY_FIELD, "couponKey")


def _category_key(value: int) -> int | None:
    return None if value == NO_CATEGORY else value


def _category_text(record: dict) -> str:
    """The category path in the loaded language, else the Korean expression the row stores.

    A coupon without a main category applies to all of them, the name LOC
    keeps under the all-categories key.
    """
    main = _category_key(record["category_main"])
    if main is None:
        text = " ".join(strip_pa_tags(category_name_tagged(ALL_CATEGORIES_KEY)).split())
    else:
        text = category_path_text(main, _category_key(record["category_middle"]), _category_key(record["category_small"]))
    return text or " ".join(record["category_expression_kr"].split())


def _num_cell(value: int | None) -> str:
    return _EMPTY if value is None else e(f"{value:,}")


class CouponHandler(RowTableHandler):
    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["couponKey"], "num", sort_key=KEY_FIELD),
            Column(labels["name"], sort_key="name"),
            Column(labels["discountRate"], "num", sort_key="discount_rate_shown"),
            Column(labels["discountPearl"], "num", sort_key="discount_pearl_shown"),
            Column(labels["maxDiscountPearl"], "num", sort_key="max_discount_pearl_shown"),
            Column(labels["minProductPearl"], "num", sort_key="min_product_pearl_shown"),
            Column(labels["expirationDays"], "num", sort_key="expiration_days"),
            Column(labels["category"], sort_key="category"),
        ]

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        return [
            {
                **record,
                **pa_fields("name", loc_tagged(LOC_COUPON_NAME, record[KEY_FIELD]) or record["name_kr"].strip()),
                "discount_rate_shown": record["discount_rate"] or None,
                "discount_pearl_shown": record["discount_pearl"] or None,
                "max_discount_pearl_shown": record["max_discount_pearl"] or None,
                "min_product_pearl_shown": record["min_product_pearl"] or None,
                "category": _category_text(record),
                "_icon_file": ui_texture_path(record["icon_path"], UI_TEXTURE_ICON_ROOT),
            }
            for record in parse_coupon_records(data)
        ]

    def cells(self, record: dict) -> list[str]:
        rate = record["discount_rate_shown"]
        return [
            e(record[KEY_FIELD]),
            icon_html_label_cell(record["_icon_file"], pa_html(record[pa_key("name")])),
            _EMPTY if rate is None else e(rate_percent(rate)),
            _num_cell(record["discount_pearl_shown"]),
            _num_cell(record["max_discount_pearl_shown"]),
            _num_cell(record["min_product_pearl_shown"]),
            e(record["expiration_days"]),
            e(record["category"]) if record["category"] else _EMPTY,
        ]

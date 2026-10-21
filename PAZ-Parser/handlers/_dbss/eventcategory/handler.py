"""eventcategory.dbss preview handler: the event cart's discount periods and steps."""
from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from _common.html import Column, e, text_list_cell
from _common.offset_table import OffsetTableHandler, keyed_offset_handler
from _common.row_table import RowTableHandler
from .parser import DISCOUNT_STEP_COUNT, FILE_NAME, KEY_FIELD, parse_eventcategory_records, parse_eventcategoryoffset_rows


_LANG_DIR = Path(__file__).parent / "lang"


def event_category_offset_handler() -> OffsetTableHandler:
    return keyed_offset_handler(_LANG_DIR, parse_eventcategoryoffset_rows, KEY_FIELD, "index")


def _used_steps(steps: list[dict]) -> list[dict]:
    """The discount steps up to the first empty one; the rest of the ten are zero."""
    used = []
    for step in steps:
        if not step["discount_ceiling"] and not step["discount_price"]:
            break
        used.append(step)
    return used


class EventCategoryHandler(RowTableHandler):
    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["index"], "num", sort_key=KEY_FIELD),
            Column(labels["categoryMain"], "num", sort_key="cash_coupon_category_main"),
            Column(labels["categoryMiddle"], "num", sort_key="cash_coupon_category_middle"),
            Column(labels["categorySmall"], "num", sort_key="cash_coupon_category_small"),
            Column(labels["discountStart"], sort_key="discount_start_period"),
            Column(labels["discountEnd"], sort_key="discount_end_period"),
            Column(labels["eventType"], "num", sort_key="event_type"),
            Column(labels["maxDiscountPearl"], "num", sort_key="max_discount_pearl"),
            Column(labels["discountSteps"]),
        ]

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        return [
            {**record, "discount_step_texts": [
                f"{step['discount_ceiling']:,}: {step['discount_price']:,}" for step in _used_steps(record["discount_steps"])
            ]}
            for record in parse_eventcategory_records(data)
        ]

    def cells(self, record: dict) -> list[str]:
        return [
            e(record[KEY_FIELD]),
            e(record["cash_coupon_category_main"]),
            e(record["cash_coupon_category_middle"]),
            e(record["cash_coupon_category_small"]),
            e(record["discount_start_period"]),
            e(record["discount_end_period"]),
            e(record["event_type"]),
            e(f"{record['max_discount_pearl']:,}"),
            text_list_cell(record["discount_step_texts"], DISCOUNT_STEP_COUNT) or "-",
        ]

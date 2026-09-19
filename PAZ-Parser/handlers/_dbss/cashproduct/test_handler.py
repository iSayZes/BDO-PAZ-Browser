from __future__ import annotations

from dataclasses import replace
from typing import Any

import pytest

from tests.framework import (
    CountTest,
    HandlerCase,
    HandlerResult,
    PosTest,
    RangeTest,
    SchemaTest,
    TargetTest,
    case_id,
    run_case,
)


_ICON_DIR = "ui_texture/icon/new_icon/09_cash/03_product"

CASE = HandlerCase(
    handler_name="cashproduct.dbss",
    data_file="cashproduct.dbss",
    companion_files={"cashproductoffset.dbss": "cashproductoffset.dbss"},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["Item"],
    internal_path="gamecommondata/binary/cashproduct.dbss",
    tests=[
        SchemaTest(
            required_keys=[
                "product_id",
                "product_name",
                "icon_path",
                "item_id",
                "block_size",
                "item_name",
            ],
        ),
        CountTest(expected=28_689),
        RangeTest(col="item_id", min_val=0, max_val=0xFFFFFF),
        PosTest(
            pos=0,
            expected={
                "product_id": 114415,
                "icon_path": f"{_ICON_DIR}/00103985.dds",
                "item_id": 613110,
                "block_size": 764,
            },
        ),
        # Product ID, icon ID and item ID are three unrelated numbers; only this
        # file ties them together.
        TargetTest(
            col="product_id",
            value=117722,
            expected={
                "icon_path": f"{_ICON_DIR}/00105099.dds",
                "item_id": 340916,
                "item_name": "[Guardian] Shell Belle Outfit Set",
                "block_size": 1294,
            },
        ),
    ],
)


@pytest.fixture(scope="module")
def cashproduct_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_cashproduct_dbss(
    spec: Any,
    cashproduct_result: HandlerResult,
) -> None:
    spec.check(cashproduct_result.records)

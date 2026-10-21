from __future__ import annotations

from dataclasses import replace
from typing import Any

import pytest

from tests.framework import (
    DeclaredCountTest,
    HandlerCase,
    HandlerResult,
    RangeTest,
    SchemaTest,
    TargetTest,
    case_id,
    fixed_rows,
    header_count,
    run_case,
)

from _dbss.employeeloyalismitem.parser import LoyalismType


_OFFSET_FILE = "employeeloyalismitemoffset.dbss"
_HEADER_SIZE = 4
_ROW_SIZE = 9
_OFFSET_ROW_SIZE = 12

_CHOWDER = 6394
_ELIXIR_OF_REGENERATION = 6395

CASE = HandlerCase(
    handler_name="employeeloyalismitem.dbss",
    data_file="employeeloyalismitem.dbss",
    companion_files={_OFFSET_FILE: _OFFSET_FILE},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["item_name"],
    internal_path="gamecommondata/binary/employeeloyalismitem.dbss",
    tests=[
        SchemaTest(required_keys=[
            "loyalism_type", "item_id", "recovery_value",
            "item_name", "icon_path", "loyalism_type_name", "recovery",
        ]),
        DeclaredCountTest(declared=header_count()),
        DeclaredCountTest(declared=header_count(companion=_OFFSET_FILE)),
        # The header count fills the file exactly.
        DeclaredCountTest(declared=fixed_rows(_ROW_SIZE, header_size=_HEADER_SIZE)),
        RangeTest(col="loyalism_type", min_val=min(LoyalismType), max_val=max(LoyalismType)),
        # Item IDs carry no enhancement level in the top byte.
        RangeTest(col="item_id", min_val=1, max_val=0x00FFFFFF),
        # Chowder adds condition points; the Elixir of Regeneration cures a sick sailor.
        TargetTest(
            col="item_id",
            value=_CHOWDER,
            expected={
                "loyalism_type": LoyalismType.LOYALTY,
                "item_name": "Chowder",
                "loyalism_type_name": "Condition",
            },
        ),
        TargetTest(
            col="item_id",
            value=_ELIXIR_OF_REGENERATION,
            expected={
                "loyalism_type": LoyalismType.RESURRECTION,
                "item_name": "Elixir of Regeneration",
                "loyalism_type_name": "Sick Sailor",
            },
        ),
    ],
)

OFFSET_CASE = HandlerCase(
    handler_name=_OFFSET_FILE,
    data_file=_OFFSET_FILE,
    companion_files={},
    loc_file=None,
    uses_loc=False,
    loc_fields=[],
    internal_path=f"gamecommondata/binary/{_OFFSET_FILE}",
    tests=[
        SchemaTest(required_keys=["item_id", "data_offset", "data_size"]),
        DeclaredCountTest(declared=header_count()),
        DeclaredCountTest(declared=fixed_rows(_OFFSET_ROW_SIZE, header_size=_HEADER_SIZE)),
        RangeTest(col="data_size", min_val=_ROW_SIZE, max_val=_ROW_SIZE),
    ],
)


@pytest.fixture(scope="module")
def employeeloyalismitem_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.fixture(scope="module")
def employeeloyalismitemoffset_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_OFFSET_RESULT", None)
    if result is None:
        result = run_case(replace(OFFSET_CASE, tests=[]))
        request.module._OFFSET_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_employeeloyalismitem_dbss(
    spec: Any,
    employeeloyalismitem_result: HandlerResult,
) -> None:
    employeeloyalismitem_result.check(spec)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_employeeloyalismitemoffset_dbss(
    spec: Any,
    employeeloyalismitemoffset_result: HandlerResult,
) -> None:
    employeeloyalismitemoffset_result.check(spec)

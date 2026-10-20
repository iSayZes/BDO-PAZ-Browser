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


_HEADER_SIZE = 4
_RECORD_SIZE = 28
_OFFSET_ROW_SIZE = 12
_PAYLOAD_SIZE = 24

_ICON_DIR = "ui_texture/icon/new_icon/product_icon_png"
_SWEET_HONEY_WINE = 54030
_ORNETTES_DARK_HONEY_WINE = 18448

CASE = HandlerCase(
    handler_name="fairyfeedingitem.dbss",
    data_file="fairyfeedingitem.dbss",
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["item_name"],
    internal_path="gamecommondata/binary/fairyfeedingitem.dbss",
    tests=[
        SchemaTest(
            required_keys=[
                "key",
                "item_id",
                "padding_08",
                "exp",
                "unknown_14",
                "item_name",
                "icon_path",
            ],
        ),
        DeclaredCountTest(declared=header_count()),
        # The header count fills the file exactly.
        DeclaredCountTest(declared=fixed_rows(_RECORD_SIZE, header_size=_HEADER_SIZE)),
        # Item IDs carry no enhancement level in the top byte.
        RangeTest(col="item_id", min_val=1, max_val=0x00FFFFFF),
        # Every listed item grants some EXP.
        RangeTest(col="exp", min_val=1, max_val=float("inf")),
        # The record key is the item ID.
        TargetTest(
            col="item_id",
            value=_SWEET_HONEY_WINE,
            expected={
                "key": _SWEET_HONEY_WINE,
                "item_name": "Sweet Honey Wine",
                "icon_path": f"{_ICON_DIR}/00054030.png",
            },
        ),
        TargetTest(
            col="item_id",
            value=_ORNETTES_DARK_HONEY_WINE,
            expected={
                "key": _ORNETTES_DARK_HONEY_WINE,
                "item_name": "Ornette's Dark Honey Wine",
            },
        ),
    ],
)

OFFSET_CASE = HandlerCase(
    handler_name="fairyfeedingitemoffset.dbss",
    data_file="fairyfeedingitemoffset.dbss",
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=False,
    loc_fields=[],
    internal_path="gamecommondata/binary/fairyfeedingitemoffset.dbss",
    tests=[
        SchemaTest(required_keys=["item_id", "data_offset", "data_size", "record_start"]),
        DeclaredCountTest(declared=header_count()),
        DeclaredCountTest(declared=fixed_rows(_OFFSET_ROW_SIZE, header_size=_HEADER_SIZE)),
        # Every payload is the 24 bytes trailing the 4-byte key prefix.
        RangeTest(col="data_size", min_val=_PAYLOAD_SIZE, max_val=_PAYLOAD_SIZE),
        # The first record follows the main file's u32 count.
        TargetTest(col="data_offset", value=8, expected={"record_start": 4}),
        TargetTest(col="item_id", value=_SWEET_HONEY_WINE, expected={"data_size": _PAYLOAD_SIZE}),
    ],
)


@pytest.fixture(scope="module")
def fairyfeedingitem_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.fixture(scope="module")
def fairyfeedingitemoffset_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_OFFSET_RESULT", None)
    if result is None:
        result = run_case(replace(OFFSET_CASE, tests=[]))
        request.module._OFFSET_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_fairyfeedingitem_dbss(
    spec: Any,
    fairyfeedingitem_result: HandlerResult,
) -> None:
    fairyfeedingitem_result.check(spec)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_fairyfeedingitemoffset_dbss(
    spec: Any,
    fairyfeedingitemoffset_result: HandlerResult,
) -> None:
    fairyfeedingitemoffset_result.check(spec)

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


_ICON_DIR = "ui_texture/icon/new_icon/product_icon_png"
_SWEET_HONEY_WINE = 54030
_ORNETTES_DARK_HONEY_WINE = 18448

CASE = HandlerCase(
    handler_name="fairyupgraderate.bss",
    data_file="fairyupgraderate.bss",
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["Item"],
    internal_path="gamecommondata/binary/fairyupgraderate.bss",
    tests=[
        SchemaTest(
            required_keys=[
                "step",
                "unknown_lead",
                "success_cap_ppm",
                "item_id",
                "rate_ppm",
                "items_for_max",
                "reserved",
                "chance_pct",
                "upgrade",
                "item_name",
                "icon_path",
            ],
        ),
        # 3 upgrade steps x 2 usable items.
        CountTest(expected=6),
        RangeTest(col="step", min_val=0, max_val=2),
        RangeTest(col="success_cap_ppm", min_val=1_000_000, max_val=1_000_000),
        RangeTest(col="unknown_lead", min_val=0, max_val=0),
        RangeTest(col="reserved", min_val=0, max_val=0),
        PosTest(
            pos=0,
            expected={
                "step": 0,
                "item_id": _SWEET_HONEY_WINE,
                "item_name": "Sweet Honey Wine",
                "rate_ppm": 22222,
                "items_for_max": 45,
                "icon_path": f"{_ICON_DIR}/00054030.png",
                "upgrade": "Faint → Glimmering",
            },
        ),
        PosTest(
            pos=1,
            expected={
                "step": 0,
                "item_id": _ORNETTES_DARK_HONEY_WINE,
                "item_name": "Ornette's Dark Honey Wine",
                "rate_ppm": 333333,
                "items_for_max": 3,
                "icon_path": f"{_ICON_DIR}/00018448.png",
            },
        ),
        # Published Tier 3 -> Tier 4 cost: 400 Sweet Honey Wine or 25 Ornette's.
        PosTest(
            pos=-1,
            expected={
                "step": 2,
                "item_id": _ORNETTES_DARK_HONEY_WINE,
                "rate_ppm": 40000,
                "items_for_max": 25,
                "upgrade": "Brilliant → Radiant",
            },
        ),
        TargetTest(
            col="rate_ppm",
            value=2500,
            expected={
                "step": 2,
                "item_id": _SWEET_HONEY_WINE,
                "items_for_max": 400,
            },
        ),
        # Middle step: Glimmering -> Brilliant is a flat 10% per Ornette's.
        TargetTest(
            col="rate_ppm",
            value=100000,
            expected={
                "step": 1,
                "item_id": _ORNETTES_DARK_HONEY_WINE,
                "items_for_max": 10,
                "chance_pct": 10.0,
                "upgrade": "Glimmering → Brilliant",
            },
        ),
    ],
)


@pytest.fixture(scope="module")
def fairyupgraderate_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_fairyupgraderate_bss(
    spec: Any,
    fairyupgraderate_result: HandlerResult,
) -> None:
    spec.check(fairyupgraderate_result.records)

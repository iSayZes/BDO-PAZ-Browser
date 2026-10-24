from __future__ import annotations

import struct
from dataclasses import replace
from typing import Any

import pytest

from tests.fixtures import load_binary_fixture
from tests.framework import (
    DeclaredCountTest,
    HandlerCase,
    HandlerResult,
    SchemaTest,
    TargetTest,
    case_id,
    fixed_rows,
    header_count,
    run_case,
)

from _bss.lifeexpmaxlevel.parser import parse_lifeexpmaxlevel_records
from .parser import FILE_NAME, parse_tradeexperiencess_records
from .sale_exp import RATE_0_1, RATE_SCALE, sale_exp_at_1000


_COUNT_SIZE = 4
_ROW_SIZE = 8
# LifeExperienceType trade in the lifeexp.dbss labels.
_TRADING = 7

CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["rank"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=["trading_level", "rank", "trade_exp", "sale_exp_rate_0_1"]),
        DeclaredCountTest(declared=header_count(offset=0)),
        DeclaredCountTest(declared=fixed_rows(_ROW_SIZE, header_size=_COUNT_SIZE)),
        # Row 0 is Trading level 1; level 0 has no row.
        TargetTest(col="trading_level", value=1, expected={"rank": "Beginner 1"}),
        TargetTest(col="trading_level", value=41, expected={"rank": "Artisan 1"}),
    ],
)


@pytest.fixture(scope="module")
def tradeexperiencess_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_tradeexperiencess_bss(spec: Any, tradeexperiencess_result: HandlerResult) -> None:
    tradeexperiencess_result.check(spec)


def test_rows_run_up_to_the_trading_max_level(tradeexperiencess_result: HandlerResult) -> None:
    max_levels = parse_lifeexpmaxlevel_records(load_binary_fixture("lifeexpmaxlevel.bss"))
    trading_max = max_levels[_TRADING]["max_level"]
    levels = [record["trading_level"] for record in tradeexperiencess_result.records]
    assert levels == list(range(1, trading_max + 1))


def test_sale_exp_cuts_off_the_fraction() -> None:
    assert sale_exp_at_1000(133_806, RATE_0_1) == 13_380
    assert sale_exp_at_1000(133_806, RATE_SCALE) == 133_806


def test_sale_exp_keeps_at_least_one() -> None:
    assert sale_exp_at_1000(3, RATE_0_1) == 1
    assert sale_exp_at_1000(0, RATE_0_1) == 1


def test_a_partial_row_raises() -> None:
    with pytest.raises(ValueError, match="rows of 8"):
        parse_tradeexperiencess_records(struct.pack("<I", 2) + bytes(_ROW_SIZE + 3))


def test_a_file_without_its_count_raises() -> None:
    with pytest.raises(ValueError, match="row count"):
        parse_tradeexperiencess_records(bytes(2))

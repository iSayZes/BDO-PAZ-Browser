from __future__ import annotations

import struct
from dataclasses import replace
from typing import Any

import pytest

from tests.framework import (
    DeclaredCountTest,
    HandlerCase,
    HandlerResult,
    SchemaTest,
    case_id,
    header_count,
    run_case,
)

from .parser import DISCOUNT_POINTS_PER_PERCENT, FILE_NAME, parse_barterlifelevelinfo_records


_COUNT_OFFSET = 4
_FIRST_LEVEL = 1


CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["rank"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=["level", "discount_point", "rank", "discount_percent"]),
        DeclaredCountTest(declared=header_count(offset=_COUNT_OFFSET)),
    ],
)


@pytest.fixture(scope="module")
def barter_level_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_barterlifelevelinfo_bss(spec: Any, barter_level_result: HandlerResult) -> None:
    barter_level_result.check(spec)


def test_levels_count_up_from_one(barter_level_result: HandlerResult) -> None:
    levels = [r["level"] for r in barter_level_result.records]
    assert levels == list(range(_FIRST_LEVEL, len(levels) + _FIRST_LEVEL))


def test_the_discount_never_falls_with_the_level(barter_level_result: HandlerResult) -> None:
    points = [r["discount_point"] for r in barter_level_result.records]
    assert points == sorted(points)


def test_the_discount_stays_below_one_hundred_percent(barter_level_result: HandlerResult) -> None:
    assert all(0 <= r["discount_percent"] < 100 for r in barter_level_result.records)


def test_discount_percent_is_the_points_over_e1_percent(barter_level_result: HandlerResult) -> None:
    for r in barter_level_result.records:
        assert r["discount_percent"] == r["discount_point"] / DISCOUNT_POINTS_PER_PERCENT


def test_parser_rejects_rows_that_miss_the_string_table() -> None:
    rows = struct.pack("<II", 1, 0) + struct.pack("<II", 2, 27329)
    data = b"PABR" + struct.pack("<I", 2) + rows + struct.pack("<III", 0, 8 + len(rows), 0)
    assert [r["level"] for r in parse_barterlifelevelinfo_records(data)] == [1, 2]
    with pytest.raises(ValueError):
        parse_barterlifelevelinfo_records(b"PABR" + struct.pack("<I", 3) + data[8:])

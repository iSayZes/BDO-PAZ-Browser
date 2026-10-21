from __future__ import annotations

import struct
from dataclasses import replace
from typing import Any

import pytest

from tests.fixtures import load_binary_fixture
from tests.framework import (
    HandlerCase,
    HandlerResult,
    RangeTest,
    SchemaTest,
    TargetTest,
    case_id,
    run_case,
)

from .parser import DAY_COUNT, FILE_NAME, GAME_SERVICE_TYPES


# eGameServiceType_KOR_REAL of CppEnums.GameServiceType.
_KOR_REAL = 3
_HOURS_IN_DAY = 24

CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=False,
    loc_fields=[],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=[
            "service_type", "unknown_group_key", "unknown_00", "unknown_02", "unknown_04", "unknown_05",
            "unknown_06", "service_name",
        ]),
        TargetTest(col="service_type", value=_KOR_REAL, expected={"service_name": "KOR_REAL"}),
        RangeTest(col="service_type", min_val=min(GAME_SERVICE_TYPES), max_val=max(GAME_SERVICE_TYPES)),
    ],
)


@pytest.fixture(scope="module")
def limit_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_instancefieldcommonlimitentertime_bss(spec: Any, limit_result: HandlerResult) -> None:
    limit_result.check(spec)


def test_one_row_per_service_type(limit_result: HandlerResult) -> None:
    """The rows the file declares each hold a different service type."""
    (declared,) = struct.unpack_from("<I", load_binary_fixture(FILE_NAME))
    assert len({r["service_type"] for r in limit_result.records}) == declared


def test_entries_repeat_their_keys(limit_result: HandlerResult) -> None:
    """An entry repeats its group's key and its row's service type."""
    for record in limit_result.records:
        assert record["unknown_00"] == record["unknown_group_key"]
        assert record["unknown_04"] == record["service_type"]


def test_day_values_are_hours(limit_result: HandlerResult) -> None:
    for record in limit_result.records:
        assert len(record["unknown_06"]) == DAY_COUNT
        assert all(0 <= value < _HOURS_IN_DAY for pair in record["unknown_06"] for value in pair)

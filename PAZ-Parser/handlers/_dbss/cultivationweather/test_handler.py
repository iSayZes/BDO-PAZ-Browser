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
from tests.offset_rows import offset_row_problems

from .handler import WEATHER_KIND_FIELDS
from .parser import FILE_NAME, OFFSET_FILE, parse_cultivationweatheroffset_rows


_COUNT_SIZE = 4
_KEY_PREFIX_SIZE = 4
_OFFSET_ROW_SIZE = 12
# Pepper: the `#Nodename` of key 57001 in the CultivationWeather_Table sheet of client 1784.
_PEPPER = 57001

CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file=None,
    uses_loc=False,
    loc_fields=[],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=["exchange_key", "weathers", "exchange", *WEATHER_KIND_FIELDS.values()]),
        DeclaredCountTest(declared=header_count(offset=0)),
        TargetTest(col="exchange_key", value=_PEPPER, expected={"exchange_key": _PEPPER}),
    ],
)

OFFSET_CASE = HandlerCase(
    handler_name=OFFSET_FILE,
    data_file=OFFSET_FILE,
    companion_files={},
    loc_file=None,
    uses_loc=False,
    loc_fields=[],
    internal_path=f"gamecommondata/binary/{OFFSET_FILE}",
    tests=[
        SchemaTest(required_keys=["exchange_key", "data_offset", "data_size"]),
        DeclaredCountTest(declared=header_count(offset=0)),
        DeclaredCountTest(declared=fixed_rows(_OFFSET_ROW_SIZE, header_size=_COUNT_SIZE)),
    ],
)


@pytest.fixture(scope="module")
def weather_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.fixture(scope="module")
def offset_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_OFFSET_RESULT", None)
    if result is None:
        result = run_case(replace(OFFSET_CASE, tests=[]))
        request.module._OFFSET_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_cultivationweather_dbss(spec: Any, weather_result: HandlerResult) -> None:
    weather_result.check(spec)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_cultivationweatheroffset_dbss(spec: Any, offset_result: HandlerResult) -> None:
    offset_result.check(spec)


def test_every_weather_kind_has_a_column(weather_result: HandlerResult) -> None:
    """The view shows each kind in its own column, so an unknown kind would be hidden."""
    unknown = {
        weather["weather_kind"]
        for record in weather_result.records
        for weather in record["weathers"]
        if weather["weather_kind"] not in WEATHER_KIND_FIELDS
    }
    assert not unknown, unknown


def test_offset_rows_point_past_the_key_prefix() -> None:
    rows = parse_cultivationweatheroffset_rows(load_binary_fixture(OFFSET_FILE))
    problems = offset_row_problems(
        load_binary_fixture(FILE_NAME), rows, struct.Struct("<I"), lead=_KEY_PREFIX_SIZE
    )
    assert not problems, problems

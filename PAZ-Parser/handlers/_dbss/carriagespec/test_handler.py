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
    RangeTest,
    SchemaTest,
    TargetTest,
    case_id,
    fixed_rows,
    header_count,
    run_case,
)

from _common.pabr_offset import parse_bare_u8_offset_rows
from .parser import FILE_NAME, OFFSET_FILE, ROW_SIZE, parse_carriagespec_records


_COUNT_SIZE = 4
_FLAG_FIELDS = ("non_stack_trade", "stack_trade", "expiration_period_trade")


CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file=None,
    uses_loc=False,
    loc_fields=[],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(
            required_keys=[
                "carriage_key",
                "distance_per_minute",
                "loadage",
                "transport_max_weight",
                "camasilb_add_transport_max_weight",
                "base_fee",
                "overload_weight",
                "fee_per_weight",
                *_FLAG_FIELDS,
            ]
        ),
        DeclaredCountTest(declared=header_count(offset=0)),
        DeclaredCountTest(declared=fixed_rows(ROW_SIZE, header_size=_COUNT_SIZE)),
        *(RangeTest(col=field, min_val=0, max_val=1) for field in _FLAG_FIELDS),
        # Key 1 is the first sheet row since client 1485; only its key is stable.
        TargetTest(col="carriage_key", value=1, expected={"carriage_key": 1}),
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
        SchemaTest(required_keys=["carriage_key", "offset", "size"]),
        DeclaredCountTest(declared=header_count(offset=0)),
        RangeTest(col="size", min_val=ROW_SIZE, max_val=ROW_SIZE),
    ],
)


@pytest.fixture(scope="module")
def carriage_spec_result(request: Any) -> HandlerResult:
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
def test_carriagespec_dbss(spec: Any, carriage_spec_result: HandlerResult) -> None:
    carriage_spec_result.check(spec)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_carriagespecoffset_dbss(spec: Any, offset_result: HandlerResult) -> None:
    offset_result.check(spec)


def test_carriage_keys_are_unique(carriage_spec_result: HandlerResult) -> None:
    keys = [r["carriage_key"] for r in carriage_spec_result.records]
    assert len(keys) == len(set(keys))


def test_offset_rows_point_at_each_row() -> None:
    """Each index row starts at its row's carriage_key and covers the whole row."""
    records = parse_carriagespec_records(load_binary_fixture(FILE_NAME))
    expected = {r["carriage_key"]: (_COUNT_SIZE + index * ROW_SIZE, ROW_SIZE) for index, r in enumerate(records)}
    rows = parse_bare_u8_offset_rows(load_binary_fixture(OFFSET_FILE))
    assert {row.entry_id: (row.offset, row.size) for row in rows} == expected


def test_parser_reads_a_row_and_rejects_extra_or_missing_bytes() -> None:
    data = struct.pack("<IBiiiiqiqBBB", 1, 2, 6500, 20, 600_000_000, 15_000_000, 2**40, 7, 3, 1, 1, 0)
    assert parse_carriagespec_records(data) == [
        {
            "carriage_key": 2,
            "distance_per_minute": 6500,
            "loadage": 20,
            "transport_max_weight": 600_000_000,
            "camasilb_add_transport_max_weight": 15_000_000,
            "base_fee": 2**40,
            "overload_weight": 7,
            "fee_per_weight": 3,
            "non_stack_trade": 1,
            "stack_trade": 1,
            "expiration_period_trade": 0,
        }
    ]
    with pytest.raises(ValueError):
        parse_carriagespec_records(data + b"\x00")
    with pytest.raises(ValueError):
        parse_carriagespec_records(data[:-1])

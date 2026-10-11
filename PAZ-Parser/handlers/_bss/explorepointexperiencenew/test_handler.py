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

from .parser import FILE_NAME, parse_explorepointexperience_records


_COUNT = struct.Struct("<I")
_ROW = struct.Struct("<HQ")

CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file=None,
    uses_loc=False,
    loc_fields=[],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=["contribution_points", "exp"]),
        DeclaredCountTest(declared=header_count(offset=0)),
    ],
)


@pytest.fixture(scope="module")
def explorepointexperience_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_explorepointexperiencenew_bss(spec: Any, explorepointexperience_result: HandlerResult) -> None:
    explorepointexperience_result.check(spec)


def test_the_curve_starts_at_zero_points_and_rises(explorepointexperience_result: HandlerResult) -> None:
    points = [r["contribution_points"] for r in explorepointexperience_result.records]
    assert points[0] == 0
    assert points == sorted(set(points))
    assert all(r["exp"] > 0 for r in explorepointexperience_result.records)


def _file(*rows: tuple[int, int]) -> bytes:
    return _COUNT.pack(len(rows)) + b"".join(_ROW.pack(*row) for row in rows)


def test_rows_are_read_in_file_order() -> None:
    records = parse_explorepointexperience_records(_file((0, 95), (50, 2**40)))
    assert records == [
        {"contribution_points": 0, "exp": 95},
        {"contribution_points": 50, "exp": 2**40},
    ]


def test_a_file_that_misses_its_declared_rows_raises() -> None:
    with pytest.raises(ValueError, match="declares 2 rows"):
        parse_explorepointexperience_records(_file((0, 95), (50, 123))[:-1])


def test_a_file_without_a_row_count_raises() -> None:
    with pytest.raises(ValueError, match="too short"):
        parse_explorepointexperience_records(b"\x01")

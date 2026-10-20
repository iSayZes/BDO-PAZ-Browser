from __future__ import annotations

import math
from dataclasses import replace
from typing import Any

import pytest

from tests.framework import (
    DeclaredCountTest,
    HandlerCase,
    HandlerResult,
    SchemaTest,
    case_id,
    fixed_rows,
    run_case,
)

from ..pabr_values.handler import VALUE_BYTES_FIELD
from .parser import FIELDS, FILE_NAME, FILE_SIZE, parse_solare_etc_option


CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=False,
    loc_fields=[],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=[*FIELDS, VALUE_BYTES_FIELD]),
        # The whole file is one set of five f32 values.
        DeclaredCountTest(declared=fixed_rows(row_size=FILE_SIZE)),
    ],
)


@pytest.fixture(scope="module")
def solare_etc_option_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_solareetcoptionstaticstatus_bss(spec: Any, solare_etc_option_result: HandlerResult) -> None:
    solare_etc_option_result.check(spec)


def test_values_are_finite_floats(solare_etc_option_result: HandlerResult) -> None:
    (record,) = solare_etc_option_result.records
    assert all(isinstance(record[name], float) and math.isfinite(record[name]) for name in FIELDS)


def test_value_bytes_hold_the_whole_file(solare_etc_option_result: HandlerResult) -> None:
    (record,) = solare_etc_option_result.records
    assert len(bytes.fromhex(record[VALUE_BYTES_FIELD])) == FILE_SIZE


def test_a_file_of_another_size_raises() -> None:
    # Client 3002 had three f32 values (Layout 1); the parser reads Layout 2 only.
    with pytest.raises(ValueError, match="not the 20"):
        parse_solare_etc_option(bytes(12))

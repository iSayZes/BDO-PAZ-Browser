from __future__ import annotations

from dataclasses import replace
from typing import Any

import pytest

from tests.framework import CountTest, HandlerCase, HandlerResult, PosTest, RangeTest, SchemaTest, TargetTest, case_id, run_case


PETEXP_CASE = HandlerCase(
    handler_name="petexp.dbss",
    data_file="petexp.dbss",
    companion_files={"petexpoffset.dbss": "petexpoffset.dbss"},
    loc_file=None,
    uses_loc=False,
    loc_fields=[],
    internal_path="gamecommondata/binary/petexp.dbss",
    tests=[
        SchemaTest(
            required_keys=[
                "exp_table_id",
                "prefix_exp_table_id",
                "offset_exp_table_id",
                "key_match",
                "max_level",
                "level",
                "required_exp",
                "data_offset",
                "data_size",
            ]
        ),
        CountTest(expected=160),
        RangeTest(col="level", min_val=1, max_val=50),
        PosTest(pos=0, expected={"exp_table_id": 9, "max_level": 50, "level": 1, "required_exp": 2055}),
        PosTest(pos=49, expected={"exp_table_id": 9, "max_level": 50, "level": 50, "required_exp": 13861}),
        PosTest(pos=-1, expected={"exp_table_id": 1, "max_level": 10, "level": 10, "required_exp": 1200}),
        TargetTest(
            col="exp_table_id",
            value=8,
            expected={"max_level": 30, "level": 1, "required_exp": 1746, "key_match": True},
        ),
    ],
)

OFFSET_CASE = HandlerCase(
    handler_name="petexpoffset.dbss",
    data_file="petexpoffset.dbss",
    companion_files={},
    loc_file=None,
    uses_loc=False,
    loc_fields=[],
    internal_path="gamecommondata/binary/petexpoffset.dbss",
    tests=[
        SchemaTest(required_keys=["exp_table_id", "data_offset", "data_size", "record_start"]),
        CountTest(expected=9),
        PosTest(pos=0, expected={"exp_table_id": 9, "data_offset": 6, "data_size": 406, "record_start": 4}),
        PosTest(pos=-1, expected={"exp_table_id": 1, "data_offset": 3270, "data_size": 406, "record_start": 3268}),
    ],
)


@pytest.fixture(scope="module")
def petexp_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_PETEXP_RESULT", None)
    if result is None:
        result = run_case(replace(PETEXP_CASE, tests=[]))
        request.module._PETEXP_RESULT = result
    return result


@pytest.fixture(scope="module")
def offset_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_OFFSET_RESULT", None)
    if result is None:
        result = run_case(replace(OFFSET_CASE, tests=[]))
        request.module._OFFSET_RESULT = result
    return result


@pytest.mark.parametrize("spec", PETEXP_CASE.tests, ids=case_id)
def test_petexp_dbss(spec: Any, petexp_result: HandlerResult) -> None:
    spec.check(petexp_result.records)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_petexpoffset_dbss(spec: Any, offset_result: HandlerResult) -> None:
    spec.check(offset_result.records)

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


CASE = HandlerCase(
    handler_name="fairyfeedenchantfailcount.bss",
    data_file="fairyfeedenchantfailcount.bss",
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=False,
    loc_fields=[],
    internal_path="gamecommondata/binary/fairyfeedenchantfailcount.bss",
    tests=[
        SchemaTest(
            required_keys=[
                "record",
                "group_id",
                "sub_key",
                "value_a",
                "value_b",
            ],
        ),
        # 7 records: groups 1-2 hold two entries each, groups 3-7 hold one.
        CountTest(expected=9),
        RangeTest(col="group_id", min_val=1, max_val=7),
        RangeTest(col="record", min_val=0, max_val=6),
        RangeTest(col="value_b", min_val=200, max_val=350),
        PosTest(
            pos=0,
            expected={
                "record": 0,
                "group_id": 1,
                "sub_key": 19,
                "value_a": 0,
                "value_b": 200,
            },
        ),
        PosTest(
            pos=1,
            expected={
                "record": 0,
                "group_id": 1,
                "sub_key": 20,
                "value_a": 0,
                "value_b": 300,
            },
        ),
        # Group 7 is the only one with a value_a above 100.
        PosTest(
            pos=-1,
            expected={
                "record": 6,
                "group_id": 7,
                "sub_key": 0,
                "value_a": 300,
                "value_b": 350,
            },
        ),
        # Groups 3-6 are identical apart from their ID.
        TargetTest(
            col="group_id",
            value=4,
            expected={
                "record": 3,
                "sub_key": 0,
                "value_a": 100,
                "value_b": 300,
            },
        ),
        # The second two-entry record mirrors the first.
        TargetTest(
            col="record",
            value=1,
            expected={
                "group_id": 2,
                "sub_key": 19,
                "value_a": 0,
                "value_b": 200,
            },
        ),
    ],
)


@pytest.fixture(scope="module")
def fairyfeedenchantfailcount_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_fairyfeedenchantfailcount_bss(
    spec: Any,
    fairyfeedenchantfailcount_result: HandlerResult,
) -> None:
    spec.check(fairyfeedenchantfailcount_result.records)

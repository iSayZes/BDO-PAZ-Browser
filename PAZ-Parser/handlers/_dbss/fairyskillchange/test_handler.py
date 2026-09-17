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
    handler_name="fairyskillchange.dbss",
    data_file="fairyskillchange.dbss",
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=False,
    loc_fields=[],
    internal_path="gamecommondata/binary/fairyskillchange.dbss",
    tests=[
        SchemaTest(required_keys=["key", "level", "orb_cost"]),
        CountTest(expected=50),
        RangeTest(col="level", min_val=1, max_val=50),
        RangeTest(col="orb_cost", min_val=1, max_val=5),
        # Records are stored out of level order; position 0 is level 47.
        PosTest(pos=0, expected={"key": 47, "level": 47, "orb_cost": 4}),
        PosTest(pos=-1, expected={"level": 16, "orb_cost": 1}),
        # Orb-cost band boundaries (Theiah's Orbs needed to reroll skills).
        TargetTest(col="level", value=1, expected={"orb_cost": 1}),
        TargetTest(col="level", value=19, expected={"orb_cost": 1}),
        TargetTest(col="level", value=20, expected={"orb_cost": 2}),
        TargetTest(col="level", value=29, expected={"orb_cost": 2}),
        TargetTest(col="level", value=30, expected={"orb_cost": 3}),
        TargetTest(col="level", value=40, expected={"orb_cost": 4}),
        TargetTest(col="level", value=50, expected={"orb_cost": 5}),
    ],
)

OFFSET_CASE = HandlerCase(
    handler_name="fairyskillchangeoffset.dbss",
    data_file="fairyskillchangeoffset.dbss",
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=False,
    loc_fields=[],
    internal_path="gamecommondata/binary/fairyskillchangeoffset.dbss",
    tests=[
        SchemaTest(required_keys=["level", "data_offset", "data_size", "record_start"]),
        CountTest(expected=50),
        RangeTest(col="level", min_val=1, max_val=50),
        # Every payload is the 8 bytes trailing the 4-byte key prefix.
        RangeTest(col="data_size", min_val=8, max_val=8),
        PosTest(pos=0, expected={"level": 47, "data_offset": 8, "record_start": 4}),
        PosTest(pos=1, expected={"level": 46, "data_offset": 20, "record_start": 16}),
        TargetTest(col="level", value=50, expected={"data_size": 8}),
    ],
)


@pytest.fixture(scope="module")
def fairyskillchange_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.fixture(scope="module")
def fairyskillchangeoffset_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_OFFSET_RESULT", None)
    if result is None:
        result = run_case(replace(OFFSET_CASE, tests=[]))
        request.module._OFFSET_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_fairyskillchange_dbss(
    spec: Any,
    fairyskillchange_result: HandlerResult,
) -> None:
    spec.check(fairyskillchange_result.records)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_fairyskillchangeoffset_dbss(
    spec: Any,
    fairyskillchangeoffset_result: HandlerResult,
) -> None:
    spec.check(fairyskillchangeoffset_result.records)

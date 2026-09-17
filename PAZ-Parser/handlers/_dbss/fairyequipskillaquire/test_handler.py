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


# 6 + 13 + 18 + 30 rollable skills across the four fairy grades.
_EXPECTED_ROWS = 67

FAIRY_EQUIP_SKILL_ACQUIRE_CASE = HandlerCase(
    handler_name="fairyequipskillaquire.dbss",
    data_file="fairyequipskillaquire.dbss",
    companion_files={
        "fairyequipskillaquireoffset.dbss": "fairyequipskillaquireoffset.dbss",
        "fairyequipskill.bss": "fairyequipskill.bss",
    },
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["Skill Name"],
    internal_path="gamecommondata/binary/fairyequipskillaquire.dbss",
    tests=[
        SchemaTest(
            required_keys=[
                "acquire_type_id",
                "fairy_grade",
                "grade_name",
                "equip_skill_id",
                "loc_id",
                "skill_name",
                "weight",
                "chance_pct",
                "total_weight",
            ]
        ),
        CountTest(expected=_EXPECTED_ROWS),
        RangeTest(col="acquire_type_id", min_val=501, max_val=504),
        RangeTest(col="fairy_grade", min_val=1, max_val=4),
        # Every grade's weights are parts-per-million summing to 1,000,000.
        RangeTest(col="total_weight", min_val=1_000_000, max_val=1_000_000),
        PosTest(
            pos=0,
            expected={
                "acquire_type_id": 504,
                "grade_name": "Radiant",
                "equip_skill_id": 0,
                "skill_name": "Tingling Breath I",
                "weight": 10000,
                "chance_pct": 1.0,
            },
        ),
        # Faint can only roll rank I skills plus Morning Star.
        TargetTest(
            col="acquire_type_id",
            value=501,
            expected={"grade_name": "Faint", "fairy_grade": 1},
        ),
        # Morning Star is the single most likely roll for a Faint fairy.
        TargetTest(
            col="weight",
            value=250000,
            expected={
                "acquire_type_id": 501,
                "equip_skill_id": 19,
                "skill_name": "Morning Star",
                "chance_pct": 25.0,
            },
        ),
        # Miraculous Cheer V is Radiant-only at 10%.
        TargetTest(
            col="loc_id",
            value=49129,
            expected={
                "acquire_type_id": 504,
                "equip_skill_id": 28,
                "skill_name": "Miraculous Cheer V",
                "weight": 100000,
                "chance_pct": 10.0,
            },
        ),
    ],
)

FAIRY_EQUIP_SKILL_ACQUIRE_OFFSET_CASE = HandlerCase(
    handler_name="fairyequipskillaquireoffset.dbss",
    data_file="fairyequipskillaquireoffset.dbss",
    companion_files={},
    loc_file=None,
    uses_loc=False,
    loc_fields=[],
    internal_path="gamecommondata/binary/fairyequipskillaquireoffset.dbss",
    tests=[
        SchemaTest(
            required_keys=[
                "acquire_type_id",
                "data_offset",
                "data_size",
                "record_start",
            ]
        ),
        CountTest(expected=4),
        RangeTest(col="data_size", min_val=174, max_val=174),
        PosTest(
            pos=0,
            expected={"acquire_type_id": 504, "data_offset": 6, "record_start": 4},
        ),
    ],
)


@pytest.fixture(scope="module")
def fairyequipskillaquire_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(FAIRY_EQUIP_SKILL_ACQUIRE_CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.fixture(scope="module")
def fairyequipskillaquireoffset_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_OFFSET_RESULT", None)
    if result is None:
        result = run_case(replace(FAIRY_EQUIP_SKILL_ACQUIRE_OFFSET_CASE, tests=[]))
        request.module._OFFSET_RESULT = result
    return result


@pytest.mark.parametrize("spec", FAIRY_EQUIP_SKILL_ACQUIRE_CASE.tests, ids=case_id)
def test_fairyequipskillaquire_dbss(
    spec: Any,
    fairyequipskillaquire_result: HandlerResult,
) -> None:
    spec.check(fairyequipskillaquire_result.records)


@pytest.mark.parametrize(
    "spec", FAIRY_EQUIP_SKILL_ACQUIRE_OFFSET_CASE.tests, ids=case_id
)
def test_fairyequipskillaquireoffset_dbss(
    spec: Any,
    fairyequipskillaquireoffset_result: HandlerResult,
) -> None:
    spec.check(fairyequipskillaquireoffset_result.records)

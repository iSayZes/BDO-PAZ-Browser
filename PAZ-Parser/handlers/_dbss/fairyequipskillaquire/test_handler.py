from __future__ import annotations

import math
from dataclasses import replace
from typing import Any

import pytest

from tests.framework import (
    DeclaredCountTest,
    HandlerCase,
    HandlerResult,
    RangeTest,
    SchemaTest,
    TargetTest,
    case_id,
    header_count,
    run_case,
)


_PPM_SCALE = 1_000_000
# Offset rows point 2 bytes into each 176-byte record, past its key prefix.
_RECORD_DATA_SIZE = 174

# One row per non-zero weight, so the header's record count does not give the
# row count; the offset case checks the declared record count.
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
                "skill_no",
                "skill_name",
                "weight",
                "chance_pct",
                "total_weight",
            ]
        ),
        RangeTest(col="acquire_type_id", min_val=501, max_val=504),
        RangeTest(col="fairy_grade", min_val=1, max_val=4),
        # Weights index the 43 catalog slots; zero weights are not rows.
        RangeTest(col="equip_skill_id", min_val=0, max_val=math.inf),
        RangeTest(col="weight", min_val=1, max_val=_PPM_SCALE),
        RangeTest(col="chance_pct", min_val=0.0, max_val=100.0),
        # Every grade's weights are parts-per-million summing to 1,000,000.
        RangeTest(col="total_weight", min_val=_PPM_SCALE, max_val=_PPM_SCALE),
        TargetTest(col="acquire_type_id", value=501, expected={"grade_name": "Faint", "fairy_grade": 1}),
        TargetTest(col="acquire_type_id", value=504, expected={"grade_name": "Radiant", "fairy_grade": 4}),
        TargetTest(
            col="skill_no",
            value=49096,
            expected={"equip_skill_id": 0, "skill_name": "Tingling Breath I"},
        ),
        TargetTest(
            col="skill_no",
            value=49120,
            expected={"equip_skill_id": 19, "skill_name": "Morning Star"},
        ),
        TargetTest(
            col="skill_no",
            value=49129,
            expected={"equip_skill_id": 28, "skill_name": "Miraculous Cheer V"},
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
        DeclaredCountTest(declared=header_count()),
        RangeTest(col="data_size", min_val=_RECORD_DATA_SIZE, max_val=_RECORD_DATA_SIZE),
        # The first record follows the main file's u32 count.
        TargetTest(col="data_offset", value=6, expected={"record_start": 4}),
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
    fairyequipskillaquire_result.check(spec)


@pytest.mark.parametrize(
    "spec", FAIRY_EQUIP_SKILL_ACQUIRE_OFFSET_CASE.tests, ids=case_id
)
def test_fairyequipskillaquireoffset_dbss(
    spec: Any,
    fairyequipskillaquireoffset_result: HandlerResult,
) -> None:
    fairyequipskillaquireoffset_result.check(spec)

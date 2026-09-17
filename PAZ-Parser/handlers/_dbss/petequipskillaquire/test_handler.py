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


# 20 populated acquire types x 14 rollable skills; key 0 has no weights.
_EXPECTED_ROWS = 280

PET_EQUIP_SKILL_ACQUIRE_CASE = HandlerCase(
    handler_name="petequipskillaquire.dbss",
    data_file="petequipskillaquire.dbss",
    companion_files={
        "petequipskillaquireoffset.dbss": "petequipskillaquireoffset.dbss",
        "petequipskill.bss": "petequipskill.bss",
    },
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["Skill Name"],
    internal_path="gamecommondata/binary/petequipskillaquire.dbss",
    tests=[
        SchemaTest(
            required_keys=[
                "acquire_type_id",
                "group",
                "tier",
                "equip_skill_id",
                "loc_id",
                "skill_name",
                "weight",
                "chance_pct",
                "total_weight",
            ]
        ),
        CountTest(expected=_EXPECTED_ROWS),
        # Only the mid-tier entry of each of 14 skill categories is rollable.
        RangeTest(col="equip_skill_id", min_val=1, max_val=36),
        # Pet weights are relative, not normalised to 1,000,000 like the fairy table.
        RangeTest(col="total_weight", min_val=700_000, max_val=1_010_000),
        PosTest(
            pos=0,
            expected={
                "acquire_type_id": 204,
                "group": 2,
                "tier": 4,
                "equip_skill_id": 1,
                "skill_name": "Karma Recovery +5%",
                "weight": 160000,
            },
        ),
        TargetTest(
            col="acquire_type_id",
            value=401,
            expected={"group": 4, "tier": 1, "total_weight": 700000},
        ),
        TargetTest(
            col="loc_id",
            value=49001,
            expected={"equip_skill_id": 9, "skill_name": "Luck +1"},
        ),
    ],
)

PET_EQUIP_SKILL_ACQUIRE_OFFSET_CASE = HandlerCase(
    handler_name="petequipskillaquireoffset.dbss",
    data_file="petequipskillaquireoffset.dbss",
    companion_files={},
    loc_file=None,
    uses_loc=False,
    loc_fields=[],
    internal_path="gamecommondata/binary/petequipskillaquireoffset.dbss",
    tests=[
        SchemaTest(
            required_keys=[
                "acquire_type_id",
                "data_offset",
                "data_size",
                "record_start",
            ]
        ),
        CountTest(expected=21),
        RangeTest(col="data_size", min_val=174, max_val=174),
        PosTest(
            pos=0,
            expected={"acquire_type_id": 204, "data_offset": 6, "record_start": 4},
        ),
    ],
)


@pytest.fixture(scope="module")
def petequipskillaquire_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(PET_EQUIP_SKILL_ACQUIRE_CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.fixture(scope="module")
def petequipskillaquireoffset_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_OFFSET_RESULT", None)
    if result is None:
        result = run_case(replace(PET_EQUIP_SKILL_ACQUIRE_OFFSET_CASE, tests=[]))
        request.module._OFFSET_RESULT = result
    return result


@pytest.mark.parametrize("spec", PET_EQUIP_SKILL_ACQUIRE_CASE.tests, ids=case_id)
def test_petequipskillaquire_dbss(
    spec: Any,
    petequipskillaquire_result: HandlerResult,
) -> None:
    spec.check(petequipskillaquire_result.records)


@pytest.mark.parametrize("spec", PET_EQUIP_SKILL_ACQUIRE_OFFSET_CASE.tests, ids=case_id)
def test_petequipskillaquireoffset_dbss(
    spec: Any,
    petequipskillaquireoffset_result: HandlerResult,
) -> None:
    spec.check(petequipskillaquireoffset_result.records)

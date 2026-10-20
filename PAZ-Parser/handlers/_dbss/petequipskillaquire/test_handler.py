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


# Offset rows point 2 bytes into each 176-byte record, past its key prefix.
_RECORD_DATA_SIZE = 174

# One row per non-zero weight, so the header's record count does not give the
# row count; the offset case checks the declared record count.
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
                "skill_no",
                "skill_name",
                "weight",
                "chance_pct",
                "total_weight",
            ]
        ),
        # Weights index the 43 Section 1 catalog slots; zero weights are not rows.
        RangeTest(col="equip_skill_id", min_val=0, max_val=math.inf),
        RangeTest(col="weight", min_val=1, max_val=float("inf")),
        RangeTest(col="chance_pct", min_val=0.0, max_val=100.0),
        # The key splits as group * 100 + tier.
        TargetTest(col="acquire_type_id", value=204, expected={"group": 2, "tier": 4}),
        TargetTest(col="acquire_type_id", value=401, expected={"group": 4, "tier": 1}),
        TargetTest(
            col="skill_no",
            value=49001,
            expected={"equip_skill_id": 9, "skill_name": "Luck +1"},
        ),
        TargetTest(
            col="equip_skill_id",
            value=1,
            expected={"skill_name": "Karma Recovery +5%"},
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
        DeclaredCountTest(declared=header_count()),
        RangeTest(col="data_size", min_val=_RECORD_DATA_SIZE, max_val=_RECORD_DATA_SIZE),
        # The first record follows the main file's u32 count.
        TargetTest(col="data_offset", value=6, expected={"record_start": 4}),
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
    petequipskillaquire_result.check(spec)


@pytest.mark.parametrize("spec", PET_EQUIP_SKILL_ACQUIRE_OFFSET_CASE.tests, ids=case_id)
def test_petequipskillaquireoffset_dbss(
    spec: Any,
    petequipskillaquireoffset_result: HandlerResult,
) -> None:
    petequipskillaquireoffset_result.check(spec)

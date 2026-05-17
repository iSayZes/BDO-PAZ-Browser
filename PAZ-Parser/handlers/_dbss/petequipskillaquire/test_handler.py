from __future__ import annotations

from dataclasses import replace
from typing import Any

import pytest

from tests.framework import (
    CountTest,
    HandlerCase,
    HandlerResult,
    PosTest,
    SchemaTest,
    TargetTest,
    case_id,
    run_case,
)


PET_EQUIP_SKILL_ACQUIRE_CASE = HandlerCase(
    handler_name="petequipskillaquire.dbss",
    data_file="petequipskillaquire.dbss",
    companion_files={
        "petequipskillaquireoffset.dbss": "petequipskillaquireoffset.dbss",
    },
    loc_file=None,
    uses_loc=False,
    loc_fields=[],
    internal_path="gamecommondata/binary/petequipskillaquire.dbss",
    tests=[
        SchemaTest(
            required_keys=[
                "acquire_type_id",
                "group",
                "tier",
                "active_entry_count",
                "max_cost",
                "sub0_cost_a",
                "sub0_cost_c",
                "cost_entries",
                "key_match",
            ]
        ),
        CountTest(expected=21),
        TargetTest(
            col="acquire_type_id",
            value=0,
            expected={
                "group": 0,
                "tier": 0,
                "active_entry_count": 0,
                "max_cost": 0,
                "key_match": True,
            },
        ),
        TargetTest(
            col="acquire_type_id",
            value=304,
            expected={
                "group": 3,
                "tier": 4,
                "sub0_cost_a": 160000,
                "key_match": True,
            },
        ),
        TargetTest(
            col="acquire_type_id",
            value=404,
            expected={
                "group": 4,
                "tier": 4,
                "sub0_cost_a": 10000,
                "max_cost": 120000,
                "key_match": True,
            },
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
        TargetTest(
            col="acquire_type_id",
            value=304,
            expected={
                "data_size": 174,
                "padding": 0,
            },
        ),
    ],
)


@pytest.fixture(scope="module")
def petequipskillaquire_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_PET_EQUIP_SKILL_ACQUIRE_RESULT", None)
    if result is None:
        result = run_case(replace(PET_EQUIP_SKILL_ACQUIRE_CASE, tests=[]))
        request.module._PET_EQUIP_SKILL_ACQUIRE_RESULT = result
    return result


@pytest.fixture(scope="module")
def petequipskillaquire_offset_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_PET_EQUIP_SKILL_ACQUIRE_OFFSET_RESULT", None)
    if result is None:
        result = run_case(replace(PET_EQUIP_SKILL_ACQUIRE_OFFSET_CASE, tests=[]))
        request.module._PET_EQUIP_SKILL_ACQUIRE_OFFSET_RESULT = result
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
    petequipskillaquire_offset_result: HandlerResult,
) -> None:
    spec.check(petequipskillaquire_offset_result.records)

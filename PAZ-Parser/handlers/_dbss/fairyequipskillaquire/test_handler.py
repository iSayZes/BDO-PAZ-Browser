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


FAIRY_EQUIP_SKILL_ACQUIRE_CASE = HandlerCase(
    handler_name="fairyequipskillaquire.dbss",
    data_file="fairyequipskillaquire.dbss",
    companion_files={
        "fairyequipskillaquireoffset.dbss": "fairyequipskillaquireoffset.dbss",
    },
    loc_file=None,
    uses_loc=False,
    loc_fields=[],
    internal_path="gamecommondata/binary/fairyequipskillaquire.dbss",
    tests=[
        SchemaTest(
            required_keys=[
                "acquire_type_id",
                "active_entry_count",
                "max_cost",
                "cost_entries",
                "key_match",
            ]
        ),
        CountTest(expected=4),
        PosTest(
            pos=0,
            expected={
                "acquire_type_id": 504,
                "active_entry_count": 12,
                "max_cost": 100000,
                "key_match": True,
            },
        ),
        TargetTest(
            col="acquire_type_id",
            value=501,
            expected={
                "active_entry_count": 5,
                "max_cost": 250000,
                "key_match": True,
                "data_offset": 534,
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
        PosTest(
            pos=0,
            expected={
                "acquire_type_id": 504,
                "data_offset": 6,
                "data_size": 174,
                "record_start": 4,
            },
        ),
        PosTest(
            pos=-1,
            expected={
                "acquire_type_id": 501,
                "data_offset": 534,
                "data_size": 174,
                "record_start": 532,
            },
        ),
    ],
)


@pytest.fixture(scope="module")
def fairyequipskillaquire_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_FAIRY_EQUIP_SKILL_ACQUIRE_RESULT", None)
    if result is None:
        result = run_case(replace(FAIRY_EQUIP_SKILL_ACQUIRE_CASE, tests=[]))
        request.module._FAIRY_EQUIP_SKILL_ACQUIRE_RESULT = result
    return result


@pytest.fixture(scope="module")
def fairyequipskillaquire_offset_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_FAIRY_EQUIP_SKILL_ACQUIRE_OFFSET_RESULT", None)
    if result is None:
        result = run_case(replace(FAIRY_EQUIP_SKILL_ACQUIRE_OFFSET_CASE, tests=[]))
        request.module._FAIRY_EQUIP_SKILL_ACQUIRE_OFFSET_RESULT = result
    return result


@pytest.mark.parametrize("spec", FAIRY_EQUIP_SKILL_ACQUIRE_CASE.tests, ids=case_id)
def test_fairyequipskillaquire_dbss(
    spec: Any,
    fairyequipskillaquire_result: HandlerResult,
) -> None:
    spec.check(fairyequipskillaquire_result.records)


@pytest.mark.parametrize("spec", FAIRY_EQUIP_SKILL_ACQUIRE_OFFSET_CASE.tests, ids=case_id)
def test_fairyequipskillaquireoffset_dbss(
    spec: Any,
    fairyequipskillaquire_offset_result: HandlerResult,
) -> None:
    spec.check(fairyequipskillaquire_offset_result.records)

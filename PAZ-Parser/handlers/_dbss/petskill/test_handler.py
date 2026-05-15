from __future__ import annotations

from dataclasses import replace
from typing import Any

import pytest

from tests.framework import CountTest, HandlerCase, HandlerResult, PosTest, SchemaTest, TargetTest, case_id, run_case


PETSKILL_CASE = HandlerCase(
    handler_name="petskill.dbss",
    data_file="petskill.dbss",
    companion_files={"petskilloffset.dbss": "petskilloffset.dbss"},
    loc_file=None,
    uses_loc=False,
    loc_fields=[],
    internal_path="gamecommondata/binary/petskill.dbss",
    tests=[
        SchemaTest(
            required_keys=[
                "pet_skill_id",
                "skill_group",
                "level",
                "raw_value_a",
                "raw_value_b",
                "row_marker",
                "pet_skill_id_match",
            ]
        ),
        CountTest(expected=490),
        PosTest(
            pos=0,
            expected={
                "pet_skill_id": 1,
                "skill_group": 1,
                "level": 1,
                "raw_value_a": 1280000,
                "raw_value_b": 0,
                "row_marker": 512,
                "pet_skill_id_match": True,
            },
        ),
        TargetTest(
            col="pet_skill_id",
            value=47,
            expected={
                "skill_group": 11,
                "level": 1,
                "raw_value_a": 3584000,
                "raw_value_b": 0,
                "extra_marker": 9,
            },
        ),
    ],
)

PETSKILL_OFFSET_CASE = HandlerCase(
    handler_name="petskilloffset.dbss",
    data_file="petskilloffset.dbss",
    companion_files={},
    loc_file=None,
    uses_loc=False,
    loc_fields=[],
    internal_path="gamecommondata/binary/petskilloffset.dbss",
    tests=[
        SchemaTest(required_keys=["pet_skill_id", "data_offset", "data_size", "record_start"]),
        CountTest(expected=49),
        PosTest(pos=0, expected={"pet_skill_id": 47, "data_offset": 6, "data_size": 190}),
        PosTest(pos=-1, expected={"pet_skill_id": 16, "data_offset": 9191, "data_size": 189}),
    ],
)


@pytest.fixture(scope="module")
def petskill_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_PETSKILL_RESULT", None)
    if result is None:
        result = run_case(replace(PETSKILL_CASE, tests=[]))
        request.module._PETSKILL_RESULT = result
    return result


@pytest.fixture(scope="module")
def petskill_offset_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_PETSKILL_OFFSET_RESULT", None)
    if result is None:
        result = run_case(replace(PETSKILL_OFFSET_CASE, tests=[]))
        request.module._PETSKILL_OFFSET_RESULT = result
    return result


@pytest.mark.parametrize("spec", PETSKILL_CASE.tests, ids=case_id)
def test_petskill_dbss(spec: Any, petskill_result: HandlerResult) -> None:
    spec.check(petskill_result.records)


@pytest.mark.parametrize("spec", PETSKILL_OFFSET_CASE.tests, ids=case_id)
def test_petskilloffset_dbss(spec: Any, petskill_offset_result: HandlerResult) -> None:
    spec.check(petskill_offset_result.records)

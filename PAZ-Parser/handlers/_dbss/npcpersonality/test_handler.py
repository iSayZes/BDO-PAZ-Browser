from __future__ import annotations

from dataclasses import replace
from typing import Any

import pytest

from tests.framework import CountTest, HandlerCase, HandlerResult, PosTest, SchemaTest, TargetTest, case_id, run_case


PERSONALITY_CASE = HandlerCase(
    handler_name="npcpersonality.dbss",
    data_file="npcpersonality.dbss",
    companion_files={"npcpersonalityoffset.dbss": "npcpersonalityoffset.dbss"},
    loc_file=None,
    uses_loc=False,
    loc_fields=[],
    internal_path="gamecommondata/binary/npcpersonality.dbss",
    tests=[
        SchemaTest(required_keys=["row", "personality_id", "group_a_id", "interest_min", "favor_max_excl", "personality_type"]),
        CountTest(expected=1182),
        PosTest(
            pos=0,
            expected={
                "row": 0,
                "personality_id": 47727,
                "group_a_id": 30949,
                "group_a_count": 6,
                "interest_min": 22.0,
                "interest_max_excl": 23.0,
                "favor_min": 26.0,
                "favor_max_excl": 28.0,
                "personality_type": 301,
            },
        ),
        TargetTest(
            col="personality_id",
            value=49518,
            expected={"group_a_id": 10218, "group_b_id": 10211, "group_c_id": 10217, "personality_type": 201},
        ),
    ],
)

OFFSET_CASE = HandlerCase(
    handler_name="npcpersonalityoffset.dbss",
    data_file="npcpersonalityoffset.dbss",
    companion_files={},
    loc_file=None,
    uses_loc=False,
    loc_fields=[],
    internal_path="gamecommondata/binary/npcpersonalityoffset.dbss",
    tests=[
        SchemaTest(required_keys=["personality_id", "data_offset"]),
        CountTest(expected=1182),
        PosTest(pos=0, expected={"personality_id": 47727, "data_offset": 6}),
        PosTest(pos=-1, expected={"personality_id": 49518, "data_offset": 40160}),
    ],
)


@pytest.fixture(scope="module")
def personality_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_PERSONALITY_RESULT", None)
    if result is None:
        result = run_case(replace(PERSONALITY_CASE, tests=[]))
        request.module._PERSONALITY_RESULT = result
    return result


@pytest.fixture(scope="module")
def offset_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_OFFSET_RESULT", None)
    if result is None:
        result = run_case(replace(OFFSET_CASE, tests=[]))
        request.module._OFFSET_RESULT = result
    return result


@pytest.mark.parametrize("spec", PERSONALITY_CASE.tests, ids=case_id)
def test_npcpersonality_dbss(spec: Any, personality_result: HandlerResult) -> None:
    spec.check(personality_result.records)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_npcpersonalityoffset_dbss(spec: Any, offset_result: HandlerResult) -> None:
    spec.check(offset_result.records)

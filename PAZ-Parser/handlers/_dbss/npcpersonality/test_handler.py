from __future__ import annotations

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


# Each offset row points 2 bytes into its 34-byte record, past the personality ID.
_HEADER_SIZE = 4
_RECORD_SIZE = 34
_ID_SIZE = 2

# personality_type is (major * 100) + variant, majors 1-12, variants 1-2.
_FIRST_PERSONALITY_TYPE = 101
_LAST_PERSONALITY_TYPE = 1202

PERSONALITY_CASE = HandlerCase(
    handler_name="npcpersonality.dbss",
    data_file="npcpersonality.dbss",
    companion_files={"npcpersonalityoffset.dbss": "npcpersonalityoffset.dbss"},
    loc_file=None,
    uses_loc=False,
    loc_fields=[],
    internal_path="gamecommondata/binary/npcpersonality.dbss",
    tests=[
        SchemaTest(
            required_keys=[
                "row",
                "personality_id",
                "group_a_id",
                "group_a_need_count",
                "group_b_id",
                "group_b_need_count",
                "group_c_id",
                "group_c_need_count",
                "interest_min",
                "interest_max",
                "favor_min",
                "favor_max",
                "personality_type",
            ]
        ),
        DeclaredCountTest(declared=header_count()),
        RangeTest(col="personality_type", min_val=_FIRST_PERSONALITY_TYPE, max_val=_LAST_PERSONALITY_TYPE),
        TargetTest(
            col="personality_id",
            value=47727,
            expected={"group_a_id": 30949, "group_b_id": 24202, "group_c_id": 25012, "personality_type": 301},
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
        DeclaredCountTest(declared=header_count()),
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
    personality_result.check(spec)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_npcpersonalityoffset_dbss(spec: Any, offset_result: HandlerResult) -> None:
    offset_result.check(spec)


def test_npcpersonalityoffset_indexes_every_record_once(
    personality_result: HandlerResult,
    offset_result: HandlerResult,
) -> None:
    id_by_offset = {
        _HEADER_SIZE + record["row"] * _RECORD_SIZE + _ID_SIZE: record["personality_id"]
        for record in personality_result.records
    }
    indexed = {row["data_offset"]: row["personality_id"] for row in offset_result.records}
    assert len(indexed) == len(offset_result.records), "two offset rows point at one record"
    assert indexed == id_by_offset

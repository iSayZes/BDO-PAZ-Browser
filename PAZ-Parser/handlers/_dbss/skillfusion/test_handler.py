from __future__ import annotations

import struct
from dataclasses import replace
from typing import Any

import pytest

from tests.fixtures import load_binary_fixture
from tests.framework import (
    DeclaredCountTest,
    HandlerCase,
    HandlerResult,
    SchemaTest,
    TargetTest,
    UserLanguageTest,
    case_id,
    fixed_rows,
    header_count,
    run_case,
)
from tests.offset_rows import offset_row_problems

from _common.skill import skill_key
from .parser import FILE_NAME, OFFSET_FILE, parse_skillfusionoffset_rows


_COUNT_SIZE = 4
_ROW_SIZE = 24
_OFFSET_ROW_SIZE = 12
# The index points past the row's u32 skill key, at `skill_fusion_key_dup`.
_KEY = struct.Struct("<I")
# A Warrior row of the SkillFusion sheet of client 1784: skill 2733 from main skill 1135 and sub skill 219.
_FUSION_SKILL_NO = 2733
_MAIN_SKILL_NO = 1135
_SUB_SKILL_NO = 219
_LEVEL = 1

CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["fusion_skill_name", "main_skill_name", "sub_skill_name"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=[
            "skill_fusion_key", "skill_fusion_key_dup", "main_skill_key", "sub_skill_key", "slot_no", "order_no",
            "fusion_skill_no", "fusion_skill_name", "main_skill_no", "sub_skill_no",
        ]),
        DeclaredCountTest(declared=header_count(offset=0)),
        DeclaredCountTest(declared=fixed_rows(_ROW_SIZE, header_size=_COUNT_SIZE)),
        TargetTest(
            col="fusion_skill_no",
            value=_FUSION_SKILL_NO,
            expected={"main_skill_no": _MAIN_SKILL_NO, "sub_skill_no": _SUB_SKILL_NO},
        ),
        UserLanguageTest(fields=["fusion_skill_name", "main_skill_name", "sub_skill_name"]),
    ],
)

OFFSET_CASE = HandlerCase(
    handler_name=OFFSET_FILE,
    data_file=OFFSET_FILE,
    companion_files={},
    loc_file=None,
    uses_loc=False,
    loc_fields=[],
    internal_path=f"gamecommondata/binary/{OFFSET_FILE}",
    tests=[
        SchemaTest(required_keys=["skill_fusion_key", "data_offset", "data_size"]),
        DeclaredCountTest(declared=header_count(offset=0)),
        DeclaredCountTest(declared=fixed_rows(_OFFSET_ROW_SIZE, header_size=_COUNT_SIZE)),
        TargetTest(
            col="skill_fusion_key",
            value=skill_key(_FUSION_SKILL_NO, _LEVEL),
            expected={"data_size": _ROW_SIZE - _KEY.size},
        ),
    ],
)


@pytest.fixture(scope="module")
def fusion_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.fixture(scope="module")
def offset_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_OFFSET_RESULT", None)
    if result is None:
        result = run_case(replace(OFFSET_CASE, tests=[]))
        request.module._OFFSET_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_skillfusion_dbss(spec: Any, fusion_result: HandlerResult) -> None:
    fusion_result.check(spec)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_skillfusionoffset_dbss(spec: Any, offset_result: HandlerResult) -> None:
    offset_result.check(spec)


def test_key_dup_repeats_the_key(fusion_result: HandlerResult) -> None:
    mismatched = [
        r["fusion_skill_no"] for r in fusion_result.records if r["skill_fusion_key_dup"] != r["skill_fusion_key"]
    ]
    assert not mismatched, mismatched


def test_offset_rows_point_at_their_rows() -> None:
    rows = parse_skillfusionoffset_rows(load_binary_fixture(OFFSET_FILE))
    problems = offset_row_problems(load_binary_fixture(FILE_NAME), rows, _KEY, lead=_KEY.size)
    assert not problems, problems

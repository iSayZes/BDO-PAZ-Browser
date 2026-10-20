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
    UserLanguageTest,
    case_id,
    header_count,
    run_case,
)

from .parser import FILE_NAME


# PABR magic, then the u32 count.
_COUNT_OFFSET = 4
# Index 1 is the base Agris Fever skill, Item Drop Quantity Effect (On).
_BASE_INDEX = 1
_BASE_SKILL_NO = 58988

CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["skill_name"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(
            required_keys=[
                "index",
                "skill_level",
                "skill_no",
                "skill_key",
                "description",
                "skill_name",
            ],
        ),
        DeclaredCountTest(declared=header_count(offset=_COUNT_OFFSET)),
        # The low half of the gc::SkillKey; skill levels start at 1.
        RangeTest(col="skill_level", min_val=1, max_val=0xFFFF),
        UserLanguageTest(fields=["skill_name"]),
        TargetTest(
            col="index",
            value=_BASE_INDEX,
            expected={
                "skill_no": _BASE_SKILL_NO,
                "skill_key": _BASE_SKILL_NO << 16 | 1,
            },
        ),
    ],
)


@pytest.fixture(scope="module")
def fevertimeskill_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_fevertimeskill_bss(spec: Any, fevertimeskill_result: HandlerResult) -> None:
    fevertimeskill_result.check(spec)


def test_each_index_has_one_row(fevertimeskill_result: HandlerResult) -> None:
    indexes = [r["index"] for r in fevertimeskill_result.records]
    assert indexes, f"{FILE_NAME} has no row"
    assert len(indexes) == len(set(indexes)), "an index has two rows"


def test_every_skill_has_a_name(fevertimeskill_result: HandlerResult) -> None:
    """Every row names a skill that LOC type 10 or skilltype.dbss knows."""
    unnamed = [r["skill_no"] for r in fevertimeskill_result.records if not r["skill_name"]]
    assert not unnamed, f"skills without a name: {unnamed}"

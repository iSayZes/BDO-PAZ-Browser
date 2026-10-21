from __future__ import annotations

from dataclasses import replace
from typing import Any

import pytest

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

from .parser import FILE_NAME


_COUNT_SIZE = 4
_ROW_SIZE = 13
# Taebaek's Belt at base level grants skill 10189, Blessing of Taebaek.
_TAEBAEKS_BELT = 12282
_BLESSING_OF_TAEBAEK = 10189

CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["item_name", "skill_name"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(
            required_keys=[
                "item_key", "skill_key", "item_key_dup", "unknown_0c", "item_name", "skill_no", "skill_level",
                "skill_name",
            ]
        ),
        DeclaredCountTest(declared=header_count(offset=0)),
        DeclaredCountTest(declared=fixed_rows(_ROW_SIZE, header_size=_COUNT_SIZE)),
        TargetTest(
            col="item_key",
            value=_TAEBAEKS_BELT,
            expected={"skill_no": _BLESSING_OF_TAEBAEK, "item_name": "Taebaek's Belt"},
        ),
        UserLanguageTest(fields=["item_name", "skill_name"]),
    ],
)


@pytest.fixture(scope="module")
def skill_item_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_enchantactiveskillitem_bss(spec: Any, skill_item_result: HandlerResult) -> None:
    skill_item_result.check(spec)


def test_item_keys_are_unique(skill_item_result: HandlerResult) -> None:
    keys = [r["item_key"] for r in skill_item_result.records]
    assert len(keys) == len(set(keys))


def test_second_item_key_is_a_copy(skill_item_result: HandlerResult) -> None:
    bad = [r["item_key"] for r in skill_item_result.records if r["item_key_dup"] != r["item_key"]]
    assert not bad, bad


def test_every_skill_has_a_name(skill_item_result: HandlerResult) -> None:
    unnamed = [r["skill_no"] for r in skill_item_result.records if not r["skill_name"]]
    assert not unnamed, unnamed

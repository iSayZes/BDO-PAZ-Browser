from __future__ import annotations

from dataclasses import replace
from typing import Any

import pytest

from tests.framework import HandlerCase, HandlerResult, RangeTest, SchemaTest, TargetTest, UserLanguageTest, case_id, run_case

from .parser import FILE_NAME, SLOT_COUNT


_WARRIOR = 0

CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["class", "skill"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=["class_type", "class", "slot", "skill_no", "unknown_02", "skill"]),
        RangeTest(col="slot", min_val=0, max_val=SLOT_COUNT - 1),
        TargetTest(col="class_type", value=_WARRIOR, expected={"class": "Warrior"}),
        UserLanguageTest(fields=["skill"]),
    ],
)


@pytest.fixture(scope="module")
def quick_slot_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_skillquickslotinfo_bss(spec: Any, quick_slot_result: HandlerResult) -> None:
    quick_slot_result.check(spec)


def test_filled_slots_name_a_skill(quick_slot_result: HandlerResult) -> None:
    unnamed = [(r["class_type"], r["slot"]) for r in quick_slot_result.records if not r["skill"]]
    assert not unnamed, unnamed


def test_slots_are_unique_per_class(quick_slot_result: HandlerResult) -> None:
    keys = [(r["class_type"], r["slot"]) for r in quick_slot_result.records]
    assert len(keys) == len(set(keys))

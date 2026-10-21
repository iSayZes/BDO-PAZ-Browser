from __future__ import annotations

from dataclasses import replace
from typing import Any

import pytest

from tests.case_input import CaseInput
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

from .parser import FILE_NAME, MATERIAL_COUNT, STEP_COUNT


_COUNT_SIZE = 4
_ROW_SIZE = 306
# Tungrad Earring, accessory choice 3 of group 1 in the step-up window.
_TUNGRAD_EARRING = 550803


def _declared_steps(source: CaseInput) -> int:
    """The table shows one row per step: five per file row."""
    return header_count(offset=0)(source) * STEP_COUNT


def _fixed_row_steps(source: CaseInput) -> int:
    """Five table rows per 306-byte file row."""
    return fixed_rows(_ROW_SIZE, header_size=_COUNT_SIZE)(source) * STEP_COUNT


CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["goal_item_name"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(
            required_keys=[
                "item_key", "group_no", "accessory_index", "enchant_level", "goal_item_key", "goal_item_name",
                "materials", "materials_text",
            ]
        ),
        DeclaredCountTest(declared=_declared_steps),
        DeclaredCountTest(declared=_fixed_row_steps),
        TargetTest(col="accessory_index", value=3, expected={"item_key": _TUNGRAD_EARRING, "group_no": 1}),
        UserLanguageTest(fields=["goal_item_name"]),
    ],
)


@pytest.fixture(scope="module")
def stepup_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_accessorystepup_dbss(spec: Any, stepup_result: HandlerResult) -> None:
    stepup_result.check(spec)


def test_every_step_has_all_materials(stepup_result: HandlerResult) -> None:
    short = [
        (r["accessory_index"], r["enchant_level"])
        for r in stepup_result.records
        if len(r["materials"]) != MATERIAL_COUNT
    ]
    assert not short, short


def test_last_material_is_the_accessory_one_level_below(stepup_result: HandlerResult) -> None:
    """The fifth material of a step is the row's accessory at the level the step starts from, count 1."""
    bad = [
        (r["accessory_index"], r["enchant_level"])
        for r in stepup_result.records
        if r["materials"][-1] != {"item_key": (r["enchant_level"] - 1) << 24 | r["item_key"], "need_count": 1}
    ]
    assert not bad, bad


def test_accessory_indexes_are_unique(stepup_result: HandlerResult) -> None:
    first_steps = [r["accessory_index"] for r in stepup_result.records if r["enchant_level"] == 1]
    assert len(first_steps) == len(set(first_steps)), first_steps

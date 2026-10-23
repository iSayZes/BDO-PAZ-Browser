from __future__ import annotations

from dataclasses import replace
from typing import Any

import pytest

from tests.framework import (
    DeclaredCountTest,
    HandlerCase,
    HandlerResult,
    PaFieldTest,
    RangeTest,
    SchemaTest,
    TargetTest,
    case_id,
    header_count,
    run_case,
)


_FILE_NAME = "tutorial.bss"
# Step 1.1 of the first pet tutorial: right-click the pet item in the
# inventory, its text box placed against the inventory window. The same row
# on clients 1784 and 3482 and in the client 1784 Tutorial_Table sheet.
_USE_PET_ITEM = "1.1"

CASE = HandlerCase(
    handler_name=_FILE_NAME,
    data_file=_FILE_NAME,
    companion_files={},
    loc_file=None,
    uses_loc=False,
    loc_fields=[],
    internal_path=f"gamecommondata/binary/{_FILE_NAME}",
    tests=[
        SchemaTest(
            required_keys=[
                "tutorial_type", "tutorial_index", "start_condition", "complete_condition", "start_event_keys",
                "title_kr", "desc_kr", "image_path", "base_pos_panel_hash", "pos", "pan", "attr",
                "unknown_start_event_keys_24", "accept_tutorial_type", "unknown_start_event_keys_26", "use_popup",
                "step", "title", "desc", "start_events_text", "base_pos_panel", "image_texture",
            ],
        ),
        DeclaredCountTest(declared=header_count(offset=4)),
        RangeTest(col="use_popup", min_val=0, max_val=1),
        PaFieldTest(field="desc"),
        TargetTest(
            col="step",
            value=_USE_PET_ITEM,
            expected={"complete_condition": "useitem(331059)", "base_pos_panel": "Panel_Window_Inventory_All"},
        ),
    ],
)


@pytest.fixture(scope="module")
def tutorial_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_tutorial_bss(spec: Any, tutorial_result: HandlerResult) -> None:
    tutorial_result.check(spec)


def test_steps_are_unique(tutorial_result: HandlerResult) -> None:
    keys = [(r["tutorial_type"], r["tutorial_index"]) for r in tutorial_result.records]
    assert len(keys) == len(set(keys))


def test_each_tutorial_runs_from_step_zero_without_gaps(tutorial_result: HandlerResult) -> None:
    """The Lua moves to index + 1 and ends the tutorial at the first missing step."""
    steps: dict[int, list[int]] = {}
    for record in tutorial_result.records:
        steps.setdefault(record["tutorial_type"], []).append(record["tutorial_index"])
    for tutorial_type, indexes in steps.items():
        assert sorted(indexes) == list(range(len(indexes))), tutorial_type


def test_every_step_has_a_title_and_a_complete_condition(tutorial_result: HandlerResult) -> None:
    for record in tutorial_result.records:
        assert record["title"], record["tutorial_type"]
        assert record["complete_condition"], record["tutorial_type"]


def test_every_panel_hash_names_a_panel(tutorial_result: HandlerResult) -> None:
    """A panel hash resolves through the `Panel_*` names of the step scripts."""
    unnamed = [
        r["base_pos_panel"] for r in tutorial_result.records
        if r["base_pos_panel"] and not r["base_pos_panel"].startswith("Panel_")
    ]
    assert not unnamed, unnamed

from __future__ import annotations

from dataclasses import replace
from typing import Any

import pytest

from tests.framework import HandlerCase, HandlerResult, RangeTest, SchemaTest, TargetTest, case_id, run_case
from .handler import ComboListHandler

_FILE = "valkyrie_auto.cl"

CASE = HandlerCase(
    handler_name=".cl",
    data_file=_FILE,
    companion_files={},
    loc_file=None,
    uses_loc=False,
    loc_fields=[],
    internal_path=f"character/pcaiscript/{_FILE}",
    tests=[
        SchemaTest(required_keys=[
            "combo", "section", "note", "weapon", "weapon_text", "console_only",
            "learn_check", "cool_check", "attributes", "steps",
        ]),
        # 0 common, 1 main weapon, 2 awakening, 3 mount (the file's own comment).
        RangeTest(col="weapon", min_val=0, max_val=3),
        # The stance swap works with either weapon and checks the awakening skill 1712.
        TargetTest(col="combo", value="BT_ACTION_CHANGE", expected={"weapon": 0, "learn_check": "1712"}),
    ],
)


@pytest.fixture(scope="module")
def cl_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_combolist(spec: Any, cl_result: HandlerResult) -> None:
    cl_result.check(spec)


def test_every_combo_has_a_name_and_a_step(cl_result: HandlerResult) -> None:
    for record in cl_result.records:
        assert record["combo"] and record["_steps"], record["combo"]


def test_most_steps_find_their_skill_command(cl_result: HandlerResult) -> None:
    steps = [step for record in cl_result.records for step in record["_steps"]]
    assert sum(1 for step in steps if step["commands"]) > len(steps) // 2


def test_the_parsed_tab_is_named_combo_list() -> None:
    assert ComboListHandler().parsed_label() == "Combo List"

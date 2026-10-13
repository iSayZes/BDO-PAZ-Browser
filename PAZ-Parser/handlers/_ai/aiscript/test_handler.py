from __future__ import annotations

from dataclasses import replace
from typing import Any

import pytest

from tests.framework import HandlerCase, HandlerResult, SchemaTest, TargetTest, case_id, run_case
from .handler import AiScriptHandler

_FILE = "mutanttreedummer_boss.ai"

CASE = HandlerCase(
    handler_name=".ai",
    data_file=_FILE,
    companion_files={},
    loc_file=None,
    uses_loc=False,
    loc_fields=[],
    internal_path=f"character/aiscript/boss/{_FILE}",
    tests=[
        SchemaTest(required_keys=[
            "state", "kind", "section", "note", "behavior", "action", "cycle_ms",
            "attributes", "runs", "transitions", "reached_from",
        ]),
        TargetTest(col="state", value="InitialState", expected={"kind": "state"}),
        TargetTest(col="state", value="HandleTakeDamage", expected={"kind": "handler"}),
    ],
)


@pytest.fixture(scope="module")
def ai_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_aiscript(spec: Any, ai_result: HandlerResult) -> None:
    ai_result.check(spec)


def test_every_state_has_a_name_and_an_exit(ai_result: HandlerResult) -> None:
    for record in ai_result.records:
        assert record["state"]
        if record["kind"] == "state":
            assert any(key.lower() == "exit" for key, _ in record["_edges"]), record["state"]


def test_reached_from_names_only_rows_of_the_file(ai_result: HandlerResult) -> None:
    names = {record["state"] for record in ai_result.records}
    for record in ai_result.records:
        assert set(record["_reached_from"]) <= names


def test_the_parsed_tab_is_named_ai_script() -> None:
    assert AiScriptHandler().parsed_label() == "AI Script"

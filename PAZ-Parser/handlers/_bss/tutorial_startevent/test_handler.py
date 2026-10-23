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

from _bss.tutorial.links import TUTORIAL_FILE
from _bss.tutorial.parser import parse_tutorial_records
from .parser import FILE_NAME, SELECTED_CONTROL_COUNT


_PABR_COUNT_OFFSET = 4
# Start event 1 searches the inventory for the pet item the pet tutorial hands out.
_PET_ITEM_EVENT = 1
_PET_ITEM = 331059
_HASH_TEXT_PREFIX = "0x"

CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={TUTORIAL_FILE: TUTORIAL_FILE},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["item_name"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=[
            "key", "item_where_type", "item_key", "black_bg", "white_bg", "white_ignore",
            "selected_panel_hash", "selected_controls", "snapping_effect_on", "do_lua",
            "item_name", "black_bg_text", "white_bg_text", "selected_text", "steps",
        ]),
        DeclaredCountTest(declared=header_count(offset=_PABR_COUNT_OFFSET)),
        TargetTest(col="key", value=_PET_ITEM_EVENT, expected={"item_key": _PET_ITEM}),
        RangeTest(col="white_ignore", min_val=0, max_val=1),
        RangeTest(col="snapping_effect_on", min_val=0, max_val=1),
    ],
)


@pytest.fixture(scope="module")
def start_event_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_tutorial_startevent_bss(spec: Any, start_event_result: HandlerResult) -> None:
    start_event_result.check(spec)


def test_keys_are_unique(start_event_result: HandlerResult) -> None:
    keys = [r["key"] for r in start_event_result.records]
    assert len(keys) == len(set(keys))


def test_every_row_has_five_selected_controls(start_event_result: HandlerResult) -> None:
    for r in start_event_result.records:
        assert len(r["selected_controls"]) == SELECTED_CONTROL_COUNT, r["key"]


def test_every_panel_and_control_has_a_name(start_event_result: HandlerResult) -> None:
    """No hash is left in hex: the tutorial scripts and the extra names cover every one."""
    for r in start_event_result.records:
        for field in ("black_bg_text", "white_bg_text", "selected_text"):
            assert _HASH_TEXT_PREFIX not in r[field], (r["key"], field, r[field])


def test_every_step_start_event_is_a_row(start_event_result: HandlerResult) -> None:
    """Both link directions hold: each key a `tutorial.bss` step lists is a row, and lists that step."""
    steps, _ = parse_tutorial_records(start_event_result.source.file(TUTORIAL_FILE))
    rows = {r["key"]: r for r in start_event_result.records}
    for step in steps:
        step_name = f"{step['tutorial_type']}.{step['tutorial_index']}"
        for key in step["start_event_keys"]:
            assert key in rows, (step_name, key)
            assert step_name in rows[key]["steps"], (step_name, key)

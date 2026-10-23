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
    case_id,
    header_count,
    run_case,
)

from _common.texture_string import TEXTURE_STRING_COMBINE


_FILE_NAME = "beginnerroadmapdata.bss"
_UNUSED_PARAMETER = -1
# Slot 1 is the main quest slot whose button opens the quest window
# (`processRoadMapEvent`: category 1, target UI 1).
_MAIN_QUEST = 1

CASE = HandlerCase(
    handler_name=_FILE_NAME,
    data_file=_FILE_NAME,
    companion_files={TEXTURE_STRING_COMBINE: TEXTURE_STRING_COMBINE},
    loc_file=None,
    uses_loc=False,
    loc_fields=[],
    internal_path=f"gamecommondata/binary/{_FILE_NAME}",
    tests=[
        SchemaTest(
            required_keys=[
                "roadmap_key", "title_kr", "desc_kr", "event_name_kr", "icon_texture_id", "background_texture_id",
                "character_texture_id", "event_parameters", "title", "desc", "event_text", "icon_path", "icon_region",
            ],
        ),
        DeclaredCountTest(declared=header_count(offset=4)),
        TargetTest(col="roadmap_key", value=_MAIN_QUEST, expected={"event_parameters": [1, 1, _UNUSED_PARAMETER]}),
    ],
)


@pytest.fixture(scope="module")
def roadmap_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_beginnerroadmapdata_bss(spec: Any, roadmap_result: HandlerResult) -> None:
    roadmap_result.check(spec)


def test_slot_keys_are_unique(roadmap_result: HandlerResult) -> None:
    keys = [r["roadmap_key"] for r in roadmap_result.records]
    assert len(keys) == len(set(keys))


def test_an_event_button_has_an_event(roadmap_result: HandlerResult) -> None:
    """`isHaveEvent()` shows the button; a named button needs a category, an unnamed one none."""
    for record in roadmap_result.records:
        has_event = record["event_parameters"][0] != _UNUSED_PARAMETER
        assert has_event == bool(record["event_name_kr"]), record["roadmap_key"]


def test_every_icon_resolves_to_a_sprite(roadmap_result: HandlerResult) -> None:
    unresolved = [r["icon_texture_id"] for r in roadmap_result.records if not r["icon_path"]]
    assert not unresolved, unresolved

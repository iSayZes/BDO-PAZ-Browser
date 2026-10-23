from __future__ import annotations

from dataclasses import replace
from typing import Any

import pytest

from tests.framework import (
    DeclaredCountTest,
    HandlerCase,
    HandlerResult,
    SchemaTest,
    case_id,
    header_count,
    run_case,
)

from _common.texture_string import TEXTURE_STRING_COMBINE


_FILE_NAME = "eventguidess.bss"
# The Lua names three values: none, __eEventGuideTag_Hot and __eEventGuideTag_New.
_TAG_VALUES = {0, 1, 2}

CASE = HandlerCase(
    handler_name=_FILE_NAME,
    data_file=_FILE_NAME,
    companion_files={TEXTURE_STRING_COMBINE: TEXTURE_STRING_COMBINE},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["reward_names"],
    internal_path=f"gamecommondata/binary/{_FILE_NAME}",
    tests=[
        SchemaTest(
            required_keys=[
                "event_key", "main_title_kr", "main_desc_kr", "sub_desc_kr", "period_desc_kr", "icon", "texture_bg",
                "start_time", "end_time", "web_keyword", "web_hash_id", "function", "function_desc_kr", "tag",
                "rewards", "title", "sub_desc", "start_text", "end_text", "reward_names", "icon_path",
            ],
        ),
        DeclaredCountTest(declared=header_count(offset=0)),
    ],
)


@pytest.fixture(scope="module")
def eventguide_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_eventguidess_bss(spec: Any, eventguide_result: HandlerResult) -> None:
    eventguide_result.check(spec)


def test_event_keys_are_unique(eventguide_result: HandlerResult) -> None:
    keys = [r["event_key"] for r in eventguide_result.records]
    assert len(keys) == len(set(keys))


def test_every_event_ends_after_it_starts(eventguide_result: HandlerResult) -> None:
    wrong = [r["event_key"] for r in eventguide_result.records if r["end_time"] <= r["start_time"]]
    assert not wrong, wrong


def test_tags_are_a_lua_tag_value(eventguide_result: HandlerResult) -> None:
    wrong = {r["tag"] for r in eventguide_result.records} - _TAG_VALUES
    assert not wrong, wrong


def test_every_event_has_a_title_and_a_period(eventguide_result: HandlerResult) -> None:
    for record in eventguide_result.records:
        assert record["main_title_kr"], record["event_key"]
        assert record["period_desc_kr"], record["event_key"]


def test_every_reward_names_an_item(eventguide_result: HandlerResult) -> None:
    """With English LOC each reward item key resolves to a name, not its bare number."""
    unnamed = [
        key for r in eventguide_result.records
        for key, name in zip(r["rewards"], r["reward_names"], strict=True)
        if name == str(key)
    ]
    assert not unnamed, unnamed

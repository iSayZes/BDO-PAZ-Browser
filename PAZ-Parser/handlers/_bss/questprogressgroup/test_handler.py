from __future__ import annotations

import struct
from dataclasses import replace
from typing import Any

import pytest

from tests.case_input import CaseInput
from tests.fixtures import load_binary_fixture
from tests.framework import (
    DeclaredCountTest,
    HandlerCase,
    HandlerResult,
    SchemaTest,
    TargetTest,
    UserLanguageTest,
    case_id,
    run_case,
)

from .parser import ENTRY, FILE_NAME, GROUP_HEAD


# PABR magic, then the u32 group count; the first group follows.
_GROUP_COUNT_OFFSET = 4
_FIRST_GROUP = 8
# [Bulgasal] Chilling Rumor, a chain of the second Land of the Morning Light quest board.
_BULGASAL_CHAIN = 8529
_MORNING_BOARD_2_GROUP = 2


def _head_key_per_entry(data: bytes) -> list[int]:
    """The `group_key` of each entry's group head, in entry order."""
    pos = _FIRST_GROUP
    keys: list[int] = []
    for _ in range(struct.unpack_from("<I", data, _GROUP_COUNT_OFFSET)[0]):
        group_key, quest_count = GROUP_HEAD.unpack_from(data, pos)
        keys.extend([group_key] * quest_count)
        pos += GROUP_HEAD.size + quest_count * ENTRY.size
    return keys


def _declared_entries(source: CaseInput) -> int:
    """The sum of the quest counts the group heads declare."""
    return len(_head_key_per_entry(source.file(None)))


CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["title", "final_title"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=[
            "group_key", "quest_chain_id", "quest_id", "final_quest_id", "title", "final_title",
        ]),
        DeclaredCountTest(declared=_declared_entries),
        TargetTest(
            col="quest_chain_id",
            value=_BULGASAL_CHAIN,
            expected={"group_key": _MORNING_BOARD_2_GROUP, "quest_id": 1},
        ),
        UserLanguageTest(fields=["title", "final_title"]),
    ],
)


@pytest.fixture(scope="module")
def questprogressgroup_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_questprogressgroup_bss(spec: Any, questprogressgroup_result: HandlerResult) -> None:
    questprogressgroup_result.check(spec)


def test_every_entry_repeats_its_group_key(questprogressgroup_result: HandlerResult) -> None:
    head_keys = _head_key_per_entry(load_binary_fixture(FILE_NAME))
    entry_keys = [r["group_key"] for r in questprogressgroup_result.records]
    assert entry_keys == head_keys, "an entry's group key differs from its group head"


def test_a_chain_sits_in_one_entry(questprogressgroup_result: HandlerResult) -> None:
    chains = [r["quest_chain_id"] for r in questprogressgroup_result.records]
    assert len(chains) == len(set(chains)), "a quest chain is listed twice"


def test_final_quest_follows_the_first(questprogressgroup_result: HandlerResult) -> None:
    for r in questprogressgroup_result.records:
        assert r["final_quest_id"] >= r["quest_id"], r["quest_chain_id"]


def test_both_quests_have_titles(questprogressgroup_result: HandlerResult) -> None:
    untitled = [
        (r["quest_chain_id"], quest)
        for r in questprogressgroup_result.records
        for quest, title in ((r["quest_id"], r["title"]), (r["final_quest_id"], r["final_title"]))
        if not title
    ]
    assert not untitled, f"quests without a LOC title: {untitled}"

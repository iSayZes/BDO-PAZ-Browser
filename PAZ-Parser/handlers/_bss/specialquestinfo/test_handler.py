from __future__ import annotations

import re
from dataclasses import replace
from typing import Any

import pytest

from tests.fixtures import load_binary_fixture
from tests.framework import (
    DeclaredCountTest,
    HandlerCase,
    HandlerResult,
    SchemaTest,
    UserLanguageTest,
    case_id,
    header_count,
    run_case,
)

from .parser import FILE_NAME


# PABR magic, then the u32 count.
_COUNT_OFFSET = 4
_QUEST_FILE = "quest.dbss"
_GROUP_CALL = re.compile(r"alreadyclearspecialquest\((\d+)\)", re.IGNORECASE)

CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["quests"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=["group_key", "quest_count", "packed_quest_ids", "quests"]),
        DeclaredCountTest(declared=header_count(offset=_COUNT_OFFSET)),
        UserLanguageTest(fields=["quests"]),
    ],
)

QUEST_CASE = HandlerCase(
    handler_name=_QUEST_FILE,
    data_file=_QUEST_FILE,
    companion_files={"allquestlist.bss": "allquestlist.bss"},
    loc_file=None,
    uses_loc=False,
    loc_fields=[],
    internal_path=f"gamecommondata/binary/{_QUEST_FILE}",
    tests=[],
)


@pytest.fixture(scope="module")
def specialquestinfo_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_specialquestinfo_bss(spec: Any, specialquestinfo_result: HandlerResult) -> None:
    specialquestinfo_result.check(spec)


def test_group_keys_are_unique(specialquestinfo_result: HandlerResult) -> None:
    keys = [r["group_key"] for r in specialquestinfo_result.records]
    assert len(keys) == len(set(keys)), "a group key has two groups"


def test_quest_names_follow_the_quest_ids(specialquestinfo_result: HandlerResult) -> None:
    for r in specialquestinfo_result.records:
        assert len(r["packed_quest_ids"]) == r["quest_count"] == len(r["quests"]), r["group_key"]


def test_every_called_group_is_in_the_file(specialquestinfo_result: HandlerResult) -> None:
    keys = {r["group_key"] for r in specialquestinfo_result.records}
    text = load_binary_fixture(_QUEST_FILE).decode("utf-16-le", errors="replace")
    called = {int(key) for key in _GROUP_CALL.findall(text)}
    assert called, "no quest calls alreadyclearspecialquest"
    assert called <= keys, f"called groups missing from {FILE_NAME}: {sorted(called - keys)}"


def test_every_quest_is_a_quest_record(specialquestinfo_result: HandlerResult) -> None:
    quests = {r["packed_quest_id"] for r in run_case(QUEST_CASE).records}
    listed = {packed for r in specialquestinfo_result.records for packed in r["packed_quest_ids"]}
    assert listed, f"{FILE_NAME} lists no quest"
    assert listed <= quests, f"quests missing from {_QUEST_FILE}: {sorted(listed - quests)}"

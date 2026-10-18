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


_NAME = "regionmonsterkillquestlist.bss"
# The quest.dbss category whose records are exactly this list.
_KILL_QUEST_CATEGORY = 12

CASE = HandlerCase(
    handler_name=_NAME,
    data_file=_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["Title"],
    internal_path=f"gamecommondata/binary/{_NAME}",
    tests=[
        SchemaTest(required_keys=["slot", "packed_quest_id", "quest_chain_id", "quest_id", "title"]),
        # The u32 count after the PABR magic.
        DeclaredCountTest(declared=header_count(offset=4)),
        # Magaia Subjugation I: (1 << 16) | 9324.
        TargetTest(col="packed_quest_id", value=74860, expected={"quest_chain_id": 9324, "quest_id": 1}),
    ],
)

QUEST_CASE = HandlerCase(
    handler_name="quest.dbss",
    data_file="quest.dbss",
    companion_files={"allquestlist.bss": "allquestlist.bss"},
    loc_file=None,
    uses_loc=False,
    loc_fields=[],
    internal_path="gamecommondata/binary/quest.dbss",
    tests=[],
)


@pytest.fixture(scope="module")
def kill_list(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_region_monster_kill_list(spec: Any, kill_list: HandlerResult) -> None:
    kill_list.check(spec)


def test_list_is_quest_category_12_in_record_order(kill_list: HandlerResult) -> None:
    quests = run_case(QUEST_CASE).records
    category = [
        record["packed_quest_id"]
        for record in quests
        if record["quest_category"] == _KILL_QUEST_CATEGORY
    ]
    assert [record["packed_quest_id"] for record in kill_list.records] == category

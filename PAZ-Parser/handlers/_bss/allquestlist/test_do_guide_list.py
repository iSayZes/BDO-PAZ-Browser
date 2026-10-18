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


_NAME = "doguildquestlist.bss"

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
        # A Very Minute Flaw: (76 << 16) | 1001.
        TargetTest(col="packed_quest_id", value=4981737, expected={"quest_chain_id": 1001, "quest_id": 76}),
    ],
)

ALL_QUESTS_CASE = replace(
    CASE,
    handler_name="allquestlist.bss",
    data_file="allquestlist.bss",
    uses_loc=False,
    loc_fields=[],
    internal_path="gamecommondata/binary/allquestlist.bss",
    tests=[],
)


@pytest.fixture(scope="module")
def guide_list(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_do_guide_list(spec: Any, guide_list: HandlerResult) -> None:
    guide_list.check(spec)


def test_entries_are_distinct_quests(guide_list: HandlerResult) -> None:
    listed = [record["packed_quest_id"] for record in guide_list.records]
    all_quests = {record["packed_quest_id"] for record in run_case(ALL_QUESTS_CASE).records}
    assert len(set(listed)) == len(listed)
    assert set(listed) <= all_quests

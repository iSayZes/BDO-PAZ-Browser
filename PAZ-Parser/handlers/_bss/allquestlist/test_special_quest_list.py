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


_NAME = "specialquestlist.bss"
# The quest.dbss category whose records are exactly this list.
_JOURNAL_PAGE_CATEGORY = 11

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
        # Page 1 of Igor Bartali's Adventures Vol. 1: (1 << 16) | 748.
        TargetTest(col="packed_quest_id", value=66284, expected={"quest_chain_id": 748, "quest_id": 1}),
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

JOURNAL_CASE = HandlerCase(
    handler_name="journalquest.dbss",
    data_file="journalquest.dbss",
    companion_files={"journalquestoffset.dbss": "journalquestoffset.dbss"},
    loc_file=None,
    uses_loc=False,
    loc_fields=[],
    internal_path="gamecommondata/binary/journalquest.dbss",
    tests=[],
)


@pytest.fixture(scope="module")
def special_list(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_special_quest_list(spec: Any, special_list: HandlerResult) -> None:
    special_list.check(spec)


def _packed_ids(result: HandlerResult) -> list[int]:
    return [record["packed_quest_id"] for record in result.records]


def test_list_is_quest_category_11_in_record_order(special_list: HandlerResult) -> None:
    quests = run_case(QUEST_CASE).records
    category = [
        record["packed_quest_id"]
        for record in quests
        if record["quest_category"] == _JOURNAL_PAGE_CATEGORY
    ]
    assert _packed_ids(special_list) == category


def test_list_holds_every_adventure_log_page(special_list: HandlerResult) -> None:
    books = run_case(JOURNAL_CASE).records
    pages = [page["raw_ref"] for book in books for page in book["page_refs"]]
    ids = _packed_ids(special_list)
    assert len(ids) == len(set(ids))
    assert sorted(ids) == sorted(pages)

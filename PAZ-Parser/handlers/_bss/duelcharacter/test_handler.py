from __future__ import annotations

from dataclasses import replace
from typing import Any

import pytest

from tests.framework import DeclaredCountTest, HandlerCase, HandlerResult, SchemaTest, case_id, run_case

from _bss.duelcharacter.parser import FILE_NAME, parse_duelcharacter_records


# The file is one fixed record.
_ONE_RECORD = 1
_RECORD_SIZE = 58

CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["item_copy_quest_text", "need_item_for_copy_text", "need_item_for_individual_copy_text"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(
            required_keys=[
                "item_copy_quest",
                "need_item_for_copy",
                "need_item_for_individual_copy",
                "unknown_0c",
                "unknown_38",
                "item_copy_quest_text",
                "need_item_for_copy_text",
                "need_item_for_individual_copy_text",
            ]
        ),
        DeclaredCountTest(declared=lambda _source: _ONE_RECORD),
    ],
)


@pytest.fixture(scope="module")
def duel_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_duelcharacter_bss(spec: Any, duel_result: HandlerResult) -> None:
    duel_result.check(spec)


def test_quest_and_items_resolve_to_names(duel_result: HandlerResult) -> None:
    # Checks the three named fields: a quest title and two item names, not bare IDs.
    record = duel_result.records[0]
    assert not record["item_copy_quest_text"].startswith("(")
    assert record["need_item_for_copy_text"] != str(record["need_item_for_copy"])
    assert record["need_item_for_individual_copy_text"] != str(record["need_item_for_individual_copy"])


def test_parse_rejects_another_size() -> None:
    with pytest.raises(ValueError):
        parse_duelcharacter_records(bytes(_RECORD_SIZE + 2))

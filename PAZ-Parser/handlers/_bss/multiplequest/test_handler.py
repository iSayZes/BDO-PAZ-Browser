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
    UserLanguageTest,
    case_id,
    header_count,
    run_case,
)

from .parser import FILE_NAME


# PABR magic, then the u32 row count.
_COUNT_OFFSET = 4
# [Crossroad] Adonna's Fortune Telling, one quest per card from quest 1 on.
_ADONNA_CHAIN = 9022


CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["min_title", "max_title"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=[
            "quest_chain_id", "min_quest_id", "max_quest_id", "min_title", "max_title",
        ]),
        DeclaredCountTest(declared=header_count(offset=_COUNT_OFFSET)),
        TargetTest(col="quest_chain_id", value=_ADONNA_CHAIN, expected={"min_quest_id": 1}),
        UserLanguageTest(fields=["min_title", "max_title"]),
    ],
)


@pytest.fixture(scope="module")
def multiplequest_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_multiplequest_bss(spec: Any, multiplequest_result: HandlerResult) -> None:
    multiplequest_result.check(spec)


def test_a_chain_sits_in_one_row(multiplequest_result: HandlerResult) -> None:
    chains = [r["quest_chain_id"] for r in multiplequest_result.records]
    assert len(chains) == len(set(chains)), "a quest chain is listed twice"


def test_the_range_is_not_reversed(multiplequest_result: HandlerResult) -> None:
    reversed_rows = [
        r["quest_chain_id"]
        for r in multiplequest_result.records
        if not 1 <= r["min_quest_id"] <= r["max_quest_id"]
    ]
    assert not reversed_rows, f"rows with min_quest_id 0 or above max_quest_id: {reversed_rows}"

from __future__ import annotations

from dataclasses import replace
from typing import Any

import pytest

from tests.fixtures import load_binary_fixture
from tests.framework import (
    DeclaredCountTest,
    HandlerCase,
    HandlerResult,
    SchemaTest,
    case_id,
    header_count,
    run_case,
)

from _dbss.itemimprovement.parser import SOURCE_FILE, parse_itemimprovementsource_records
from .parser import FILE_NAME


# PABR magic, then the u32 count.
_COUNT_OFFSET = 4

CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["item_name"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=["order", "item_id", "item_name", "icon_path"]),
        DeclaredCountTest(declared=header_count(offset=_COUNT_OFFSET)),
    ],
)


@pytest.fixture(scope="module")
def display_list_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_itemimprovementdefaultdisplaylist_bss(spec: Any, display_list_result: HandlerResult) -> None:
    display_list_result.check(spec)


def test_the_list_holds_the_stones_flagged_for_default_display(display_list_result: HandlerResult) -> None:
    stones = parse_itemimprovementsource_records(load_binary_fixture(SOURCE_FILE))
    flagged = {stone["item_id"] for stone in stones if stone["is_default_display"]}
    assert {r["item_id"] for r in display_list_result.records} == flagged

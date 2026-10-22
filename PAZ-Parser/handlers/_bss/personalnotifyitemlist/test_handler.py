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

from .parser import FILE_NAME, KEY_FIELD


# Gold Bar 1G, the first item of the list.
_GOLD_BAR_1G = 2

CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["item_name"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=[KEY_FIELD, "item_name"]),
        DeclaredCountTest(declared=header_count(offset=4)),
        TargetTest(col=KEY_FIELD, value=_GOLD_BAR_1G, expected={"item_name": "Gold Bar 1G"}),
        UserLanguageTest(fields=["item_name"]),
    ],
)


@pytest.fixture(scope="module")
def notify_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_personalnotifyitemlist_bss(spec: Any, notify_result: HandlerResult) -> None:
    notify_result.check(spec)


def test_the_item_ids_ascend_without_repeats(notify_result: HandlerResult) -> None:
    items = [record[KEY_FIELD] for record in notify_result.records]
    assert items == sorted(set(items))

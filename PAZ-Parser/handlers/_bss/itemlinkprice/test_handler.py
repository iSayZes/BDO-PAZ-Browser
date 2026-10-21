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


# The PABR magic before the count.
_COUNT_OFFSET = 4
# Fiery Kutum Shield follows the price of Kutum Shield (LinkPrice sheet of client 1784).
_FIERY_KUTUM_SHIELD = 694290
_KUTUM_SHIELD = 10140

CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["price_follow_item_name", "price_target_item_name"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=[
            "price_follow_item_key", "price_target_item_key", "price_follow_item_name", "price_target_item_name",
        ]),
        DeclaredCountTest(declared=header_count(offset=_COUNT_OFFSET)),
        TargetTest(
            col="price_follow_item_key",
            value=_FIERY_KUTUM_SHIELD,
            expected={"price_target_item_key": _KUTUM_SHIELD},
        ),
        UserLanguageTest(fields=["price_follow_item_name", "price_target_item_name"]),
    ],
)


@pytest.fixture(scope="module")
def link_price_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_itemlinkprice_bss(spec: Any, link_price_result: HandlerResult) -> None:
    link_price_result.check(spec)


def test_each_item_follows_one_price(link_price_result: HandlerResult) -> None:
    follow_keys = [r["price_follow_item_key"] for r in link_price_result.records]
    assert len(follow_keys) == len(set(follow_keys))

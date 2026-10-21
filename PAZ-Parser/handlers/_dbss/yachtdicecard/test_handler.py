from __future__ import annotations

from dataclasses import replace
from typing import Any

import pytest

from tests.framework import (
    DeclaredCountTest,
    HandlerCase,
    HandlerResult,
    RangeTest,
    SchemaTest,
    TargetTest,
    case_id,
    header_count,
    run_case,
)

from .parser import FILE_NAME


# Card 31 is the first symbol with eye 1 (the DiceCardList sheet of client 1784).
_CARD_31 = 31
_SYMBOLS = (1, 4)

CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file=None,
    uses_loc=False,
    loc_fields=[],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=["card_key", "card_key_dup", "symbol", "eye"]),
        DeclaredCountTest(declared=header_count(offset=0)),
        RangeTest(col="symbol", min_val=_SYMBOLS[0], max_val=_SYMBOLS[1]),
        TargetTest(col="card_key", value=_CARD_31, expected={"card_key_dup": _CARD_31, "symbol": 1, "eye": 1}),
    ],
)


@pytest.fixture(scope="module")
def yachtdicecard_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_yachtdicecard_dbss(spec: Any, yachtdicecard_result: HandlerResult) -> None:
    yachtdicecard_result.check(spec)


def test_keys_repeat_inside_each_row(yachtdicecard_result: HandlerResult) -> None:
    for r in yachtdicecard_result.records:
        assert r["card_key_dup"] == r["card_key"], r["card_key"]

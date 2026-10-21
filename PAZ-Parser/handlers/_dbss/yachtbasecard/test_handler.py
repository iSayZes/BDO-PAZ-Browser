from __future__ import annotations

from dataclasses import replace
from typing import Any

import pytest

from _common.ui_texture import UI_TEXTURE_ROOT
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


# Card 1 is the first symbol with eye 1 (the BaseCardList sheet of client 1784).
_CARD_1 = 1
_SYMBOLS = (1, 4)
_EYES = (1, 6)
_ARTWORK_FOLDER = f"{UI_TEXTURE_ROOT}ui_artwork/"

CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file=None,
    uses_loc=False,
    loc_fields=[],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=["card_key", "card_key_dup", "symbol", "eye", "image_path", "image_paz_path"]),
        DeclaredCountTest(declared=header_count(offset=0)),
        RangeTest(col="symbol", min_val=_SYMBOLS[0], max_val=_SYMBOLS[1]),
        RangeTest(col="eye", min_val=_EYES[0], max_val=_EYES[1]),
        TargetTest(col="card_key", value=_CARD_1, expected={"card_key_dup": _CARD_1, "symbol": 1, "eye": 1}),
    ],
)


@pytest.fixture(scope="module")
def yachtbasecard_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_yachtbasecard_dbss(spec: Any, yachtbasecard_result: HandlerResult) -> None:
    yachtbasecard_result.check(spec)


def test_keys_repeat_inside_each_row(yachtbasecard_result: HandlerResult) -> None:
    for r in yachtbasecard_result.records:
        assert r["card_key_dup"] == r["card_key"], r["card_key"]


def test_every_picture_is_a_ui_artwork_dds(yachtbasecard_result: HandlerResult) -> None:
    for r in yachtbasecard_result.records:
        assert r["image_paz_path"].startswith(_ARTWORK_FOLDER), r["image_path"]
        assert r["image_paz_path"].endswith(".dds"), r["image_path"]

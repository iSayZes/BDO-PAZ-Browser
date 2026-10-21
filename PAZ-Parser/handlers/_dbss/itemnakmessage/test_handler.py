from __future__ import annotations

import struct
from dataclasses import replace
from typing import Any

import pytest

from tests.fixtures import load_binary_fixture
from tests.framework import (
    DeclaredCountTest,
    HandlerCase,
    HandlerResult,
    PaFieldTest,
    SchemaTest,
    TargetTest,
    UserLanguageTest,
    case_id,
    header_count,
    run_case,
)
from tests.offset_rows import offset_row_problems

from _common.pabr_offset import parse_pabr_u32_offset_rows
from .parser import FILE_NAME, OFFSET_FILE


# The PABR magic before the index's count.
_OFFSET_COUNT_AT = 4
# Rich Merchant's Ring, the first row of the BigNakMessage sheet of client 1784.
_RICH_MERCHANTS_RING = 12034

CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["item_name", "main_message", "sub_message"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=[
            "item_key", "main_message_key", "sub_message_key", "item_name", "main_message", "sub_message",
        ]),
        DeclaredCountTest(declared=header_count(offset=0)),
        TargetTest(col="item_key", value=_RICH_MERCHANTS_RING, expected={"item_key": _RICH_MERCHANTS_RING}),
        PaFieldTest(field="main_message"),
        UserLanguageTest(fields=["item_name", "main_message", "sub_message"]),
    ],
)

OFFSET_CASE = HandlerCase(
    handler_name=OFFSET_FILE,
    data_file=OFFSET_FILE,
    companion_files={},
    loc_file=None,
    uses_loc=False,
    loc_fields=[],
    internal_path=f"gamecommondata/binary/{OFFSET_FILE}",
    tests=[
        SchemaTest(required_keys=["item_key", "data_offset", "data_size"]),
        DeclaredCountTest(declared=header_count(offset=_OFFSET_COUNT_AT)),
        TargetTest(col="item_key", value=_RICH_MERCHANTS_RING, expected={"item_key": _RICH_MERCHANTS_RING}),
    ],
)


@pytest.fixture(scope="module")
def message_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.fixture(scope="module")
def offset_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_OFFSET_RESULT", None)
    if result is None:
        result = run_case(replace(OFFSET_CASE, tests=[]))
        request.module._OFFSET_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_itemnakmessage_dbss(spec: Any, message_result: HandlerResult) -> None:
    message_result.check(spec)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_itemnakmessageoffset_dbss(spec: Any, offset_result: HandlerResult) -> None:
    offset_result.check(spec)


def test_every_message_key_has_text(message_result: HandlerResult) -> None:
    """Both keys name a `GAME` sheet string, so neither column falls back to the key."""
    for r in message_result.records:
        assert r["main_message"] != r["main_message_key"], r["item_key"]
        assert r["sub_message"] != r["sub_message_key"], r["item_key"]


def test_offset_rows_point_at_their_rows() -> None:
    rows = parse_pabr_u32_offset_rows(load_binary_fixture(OFFSET_FILE))
    problems = offset_row_problems(load_binary_fixture(FILE_NAME), rows, struct.Struct("<I"))
    assert not problems, problems

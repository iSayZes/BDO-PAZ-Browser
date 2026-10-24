from __future__ import annotations

import struct
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

from .parser import FILE_NAME, parse_autoseasonclose_file


_ROW_COUNT_AT = 4
_U32 = struct.Struct("<I")
# Row 1 of clients 1784 and 3482: [Season] Tuvala Helmet Conversion Stone,
# Tuvala Helmet (Season) to Tuvala Helmet.
_HELMET_ROW = {"change_item_key": 8046, "before_item_key": 694105, "after_item_key": 695105}

CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["change_item_name", "before_item_name", "after_item_name"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(
            required_keys=[
                "index",
                "change_item_key",
                "before_item_key",
                "after_item_key",
                "change_item_name",
                "before_item_name",
                "after_item_name",
            ],
        ),
        DeclaredCountTest(declared=header_count(offset=_ROW_COUNT_AT)),
        TargetTest(col="index", value=1, expected=_HELMET_ROW),
    ],
)


@pytest.fixture(scope="module")
def autoseason_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_autoseasonclosechangeitemstaticstatus_bss(spec: Any, autoseason_result: HandlerResult) -> None:
    autoseason_result.check(spec)


def test_each_season_item_has_one_row(autoseason_result: HandlerResult) -> None:
    # `index` repeats (54 and 85 twice on client 3482); the item before the change does not.
    items = [record["before_item_key"] for record in autoseason_result.records]
    assert len(items) == len(set(items))


def test_every_item_has_a_name(autoseason_result: HandlerResult) -> None:
    for record in autoseason_result.records:
        assert record["change_item_name"] and record["before_item_name"] and record["after_item_name"], record


def test_the_graduation_lists_are_filled(autoseason_result: HandlerResult) -> None:
    parsed = parse_autoseasonclose_file(autoseason_result.source.data)
    assert parsed.season_challenges and parsed.auto_graduation_quests and parsed.auto_graduation_items


def _pabr(body: bytes) -> bytes:
    table_start = 4 + len(body)
    return b"PABR" + body + _U32.pack(0) + _U32.pack(table_start) + _U32.pack(0)


def test_the_lists_follow_the_rows() -> None:
    body = (
        _U32.pack(1) + struct.pack("<IIII", 1, 8046, 694105, 695105)
        + _U32.pack(1) + struct.pack("<HIBB", 2964, 694111, 5, 1)
        + _U32.pack(1) + struct.pack("<BB", 1, 0)
        + _U32.pack(1) + _U32.pack(2 << 16 | 40071)
        + _U32.pack(2) + struct.pack("<II", 890081, 8445)
        + _U32.pack(0)
    )
    parsed = parse_autoseasonclose_file(_pabr(body))
    assert parsed.rows == [{"index": 1, **_HELMET_ROW}]
    assert parsed.season_challenges == [{"challenge_key": 2964, "item_id": 694111, "unknown_06": 5, "unknown_07": 1}]
    assert parsed.auto_graduation_character_types == [{"unknown_00": 1, "unknown_01": 0}]
    assert parsed.auto_graduation_quests == [2 << 16 | 40071]
    assert parsed.auto_graduation_items == [890081, 8445]


def test_lists_that_stop_short_of_the_string_table_raise() -> None:
    body = _U32.pack(0) * 7
    with pytest.raises(ValueError, match="string table starts"):
        parse_autoseasonclose_file(_pabr(body))

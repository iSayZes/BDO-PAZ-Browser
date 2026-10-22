from __future__ import annotations

import struct
from dataclasses import replace
from typing import Any

import pytest

from _common.lookup_index import IndexKind
from tests.fixtures import load_binary_fixture
from tests.framework import (
    DeclaredCountTest,
    HandlerCase,
    HandlerResult,
    SchemaTest,
    TargetTest,
    case_id,
    fixed_rows,
    header_count,
    run_case,
)
from tests.offset_rows import offset_row_problems

from _dbss.marblegamediceitemgroup.parser import FILE_NAME as GROUP_FILE
from .parser import FILE_NAME, OFFSET_FILE, ROW, parse_marblegamediceitemkey_records, parse_marblegamediceitemkeyoffset_rows


_COUNT_SIZE = 4
_OFFSET_ROW_SIZE = 12
# Dice item 101 (Pace of Delight - 1 Square) drops from group 1001 only,
# which item 756440 grants; dice item 201 (move back one square) is in no
# group (DiceItem_Table and DiceItemGroup_Table of client 1784).
_PACE_OF_DELIGHT_DICE_ITEM = 101
_PACE_OF_DELIGHT_GROUP = 1001
_PACE_OF_DELIGHT_ITEM = 756440
_MOVE_BACK_DICE_ITEM = 201


CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={GROUP_FILE: GROUP_FILE},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=[],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    lookup_indexes={IndexKind.MARBLE_DICE_GROUP_ITEMS: {_PACE_OF_DELIGHT_GROUP: (_PACE_OF_DELIGHT_ITEM,)}},
    tests=[
        SchemaTest(required_keys=["dice_item_key", "group_keys", "groups_text", "item_ids", "item_names", "item_count"]),
        DeclaredCountTest(declared=header_count(offset=0)),
        DeclaredCountTest(declared=fixed_rows(ROW.size, header_size=_COUNT_SIZE)),
        TargetTest(
            col="dice_item_key",
            value=_PACE_OF_DELIGHT_DICE_ITEM,
            expected={
                "group_keys": [_PACE_OF_DELIGHT_GROUP],
                "item_ids": [_PACE_OF_DELIGHT_ITEM],
                "item_names": ["Pace of Delight - 1 Square"],
            },
        ),
        TargetTest(
            col="dice_item_key",
            value=_MOVE_BACK_DICE_ITEM,
            expected={"group_keys": [], "item_ids": [], "item_count": None},
        ),
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
        SchemaTest(required_keys=["dice_item_key", "data_offset", "data_size"]),
        DeclaredCountTest(declared=header_count(offset=0)),
        DeclaredCountTest(declared=fixed_rows(_OFFSET_ROW_SIZE, header_size=_COUNT_SIZE)),
    ],
)


@pytest.fixture(scope="module")
def key_result(request: Any) -> HandlerResult:
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
def test_marblegamediceitemkey_dbss(spec: Any, key_result: HandlerResult) -> None:
    key_result.check(spec)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_marblegamediceitemkeyoffset_dbss(spec: Any, offset_result: HandlerResult) -> None:
    offset_result.check(spec)


def test_offset_rows_point_at_their_rows() -> None:
    rows = parse_marblegamediceitemkeyoffset_rows(load_binary_fixture(OFFSET_FILE))
    problems = offset_row_problems(load_binary_fixture(FILE_NAME), rows, ROW)
    assert not problems, problems


def test_keys_are_unique() -> None:
    keys = [r["dice_item_key"] for r in parse_marblegamediceitemkey_records(load_binary_fixture(FILE_NAME))]
    assert len(keys) == len(set(keys))


def test_parse_rejects_a_short_file() -> None:
    with pytest.raises(ValueError, match="2 rows of 4"):
        parse_marblegamediceitemkey_records(struct.pack("<3I", 2, 101, 102)[:-1])

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
    SchemaTest,
    case_id,
    header_count,
    run_case,
)

from _dbss.itempuzzle.parser import FILE_NAME as PUZZLE_FILE, parse_itempuzzle_records
from .parser import FILE_NAME, parse_itemenchantpuzzle_records


_HEAD = struct.Struct("<IQ")
_U32 = struct.Struct("<I")
# Ancient Pottery Fragment, the first piece of puzzle 1 on clients 1784 and 3482.
_POTTERY_FRAGMENT = 40001
_POTTERY_PUZZLE = 1

CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["item_name"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=["start_puzzle_item_key", "puzzle_key_count", "puzzle_keys", "item_name"]),
        DeclaredCountTest(declared=header_count(offset=0)),
    ],
)


@pytest.fixture(scope="module")
def puzzle_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_itemenchantpuzzle_dbss(spec: Any, puzzle_result: HandlerResult) -> None:
    puzzle_result.check(spec)


def test_the_pottery_fragment_starts_the_pottery_puzzle(puzzle_result: HandlerResult) -> None:
    record = next(r for r in puzzle_result.records if r["start_puzzle_item_key"] == _POTTERY_FRAGMENT)
    assert _POTTERY_PUZZLE in record["puzzle_keys"]


def test_items_are_unique(puzzle_result: HandlerResult) -> None:
    items = [record["start_puzzle_item_key"] for record in puzzle_result.records]
    assert len(items) == len(set(items))


def test_every_puzzle_is_listed_once_under_its_first_piece(puzzle_result: HandlerResult) -> None:
    start_items = {
        row["puzzle_key"]: row["start_puzzle_item_key"]
        for row in parse_itempuzzle_records(load_binary_fixture(PUZZLE_FILE))
    }
    listed = [
        (key, record["start_puzzle_item_key"]) for record in puzzle_result.records for key in record["puzzle_keys"]
    ]
    assert sorted(key for key, _ in listed) == sorted(start_items)
    assert all(start_items[key] == item for key, item in listed)


def test_records_read_item_and_puzzle_keys() -> None:
    data = _U32.pack(2) + _HEAD.pack(40001, 1) + struct.pack("<H", 1) + _HEAD.pack(4459, 2) + struct.pack("<HH", 95, 96)
    assert parse_itemenchantpuzzle_records(data) == [
        {"start_puzzle_item_key": 40001, "puzzle_key_count": 1, "puzzle_keys": [1]},
        {"start_puzzle_item_key": 4459, "puzzle_key_count": 2, "puzzle_keys": [95, 96]},
    ]


def test_a_count_past_the_end_raises() -> None:
    data = _U32.pack(1) + _HEAD.pack(40001, 3) + struct.pack("<H", 1)
    with pytest.raises(ValueError, match="runs past the end"):
        parse_itemenchantpuzzle_records(data)

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
    RangeTest,
    SchemaTest,
    TargetTest,
    case_id,
    fixed_rows,
    header_count,
    run_case,
)
from tests.offset_rows import offset_row_problems

from _common.pabr_offset import parse_bare_offset_rows
from .parser import FILE_NAME, GRID_SIDE, OFFSET_FILE


_COUNT_SIZE = 4
_ROW_SIZE = 120
_OFFSET_ROW_SIZE = 10
_LAST_INDEX = GRID_SIDE - 1
# Puzzle 1 lays three Ancient Pottery Fragments in a row (ItemPuzzle_Table of client 1784).
_POTTERY_PUZZLE = 1
_POTTERY_PIECES = [40001, 40002, 40003] + [0] * (GRID_SIDE * GRID_SIDE - 3)

CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["pieces_text"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=[
            "puzzle_key", "puzzle_item_keys", "start_puzzle_item_key", "start_puzzle_item_index",
            "width_max_index", "height_max_index", "make_item_key", "line_count",
            "pieces", "pieces_text", "pattern", "size_text",
        ]),
        DeclaredCountTest(declared=header_count(offset=0)),
        DeclaredCountTest(declared=fixed_rows(_ROW_SIZE, header_size=_COUNT_SIZE)),
        RangeTest(col="line_count", min_val=GRID_SIDE, max_val=GRID_SIDE),
        RangeTest(col="width_max_index", min_val=0, max_val=_LAST_INDEX),
        RangeTest(col="height_max_index", min_val=0, max_val=_LAST_INDEX),
        TargetTest(
            col="puzzle_key",
            value=_POTTERY_PUZZLE,
            expected={"puzzle_item_keys": _POTTERY_PIECES, "pattern": "ABC", "size_text": "3 x 1"},
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
        SchemaTest(required_keys=["puzzle_key", "data_offset", "data_size"]),
        DeclaredCountTest(declared=header_count(offset=0)),
        DeclaredCountTest(declared=fixed_rows(_OFFSET_ROW_SIZE, header_size=_COUNT_SIZE)),
        TargetTest(col="puzzle_key", value=_POTTERY_PUZZLE, expected={"data_size": _ROW_SIZE}),
    ],
)


@pytest.fixture(scope="module")
def puzzle_result(request: Any) -> HandlerResult:
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
def test_itempuzzle_dbss(spec: Any, puzzle_result: HandlerResult) -> None:
    puzzle_result.check(spec)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_itempuzzleoffset_dbss(spec: Any, offset_result: HandlerResult) -> None:
    offset_result.check(spec)


def test_start_and_bounds_follow_from_the_grid(puzzle_result: HandlerResult) -> None:
    """The fields after the grid are what the loader works out from it (docs: Notes)."""
    for r in puzzle_result.records:
        used = [index for index, key in enumerate(r["puzzle_item_keys"]) if key]
        assert used, r["puzzle_key"]
        assert r["start_puzzle_item_index"] == used[0], r["puzzle_key"]
        assert r["start_puzzle_item_key"] == r["puzzle_item_keys"][used[0]], r["puzzle_key"]
        assert r["width_max_index"] == max(index % GRID_SIDE for index in used), r["puzzle_key"]
        assert r["height_max_index"] == max(index // GRID_SIDE for index in used), r["puzzle_key"]


def test_offset_rows_point_at_their_rows() -> None:
    rows = parse_bare_offset_rows(load_binary_fixture(OFFSET_FILE))
    problems = offset_row_problems(load_binary_fixture(FILE_NAME), rows, struct.Struct("<H"))
    assert not problems, problems

from __future__ import annotations

from dataclasses import replace
from typing import Any

import pytest

from _common.item_grade import ITEM_GRADE_COLORS
from tests.case_input import CaseInput
from tests.fixtures import load_binary_fixture
from tests.framework import (
    DeclaredCountTest,
    HandlerCase,
    HandlerResult,
    RangeTest,
    SchemaTest,
    TargetTest,
    case_id,
    run_case,
)

from .parser import FILE_NAME, GRADE_BLOCK_SIZE, LEVEL_COUNT, LEVEL_ROW, OFFSET_FILE, parse_minigamefindtooloffset


_PEN = 20
# The u8 that opens each grade block (Layout 2).
_BLOCK_HEAD_SIZE = 1


def _index_rows(source: CaseInput) -> int:
    """The rows `minigamefindtooloffset.dbss` lists, over all its groups."""
    return len(parse_minigamefindtooloffset(source.file(OFFSET_FILE)))


CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={OFFSET_FILE: OFFSET_FILE},
    loc_file=None,
    uses_loc=False,
    loc_fields=[],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(
            required_keys=[
                "item_grade",
                "enchant_level",
                "unknown_00",
                "r_click_count",
                "open_slot_count",
                "decrease_damage_rate",
                "enchant_level_text",
            ],
        ),
        DeclaredCountTest(declared=_index_rows),
        RangeTest(col="item_grade", min_val=0, max_val=len(ITEM_GRADE_COLORS) - 1),
        RangeTest(col="enchant_level", min_val=0, max_val=LEVEL_COUNT - 1),
        TargetTest(col="enchant_level", value=_PEN, expected={"enchant_level_text": "PEN"}),
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
        SchemaTest(required_keys=["item_grade", "enchant_level", "data_offset", "data_size"]),
        RangeTest(col="enchant_level", min_val=0, max_val=LEVEL_COUNT - 1),
        TargetTest(col="enchant_level", value=0, expected={"item_grade": 0, "data_size": LEVEL_ROW.size}),
    ],
)


@pytest.fixture(scope="module")
def tool_result(request: Any) -> HandlerResult:
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
def test_minigamefindtool_dbss(spec: Any, tool_result: HandlerResult) -> None:
    tool_result.check(spec)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_minigamefindtooloffset_dbss(spec: Any, offset_result: HandlerResult) -> None:
    offset_result.check(spec)


def test_offset_rows_point_at_their_rows(tool_result: HandlerResult) -> None:
    """Each index row names the grade and level of the main row at its offset, in file order."""
    data = load_binary_fixture(FILE_NAME)
    index = parse_minigamefindtooloffset(load_binary_fixture(OFFSET_FILE))
    keys = [(r["item_grade"], r["enchant_level"]) for r in tool_result.records]
    assert [(row.item_grade, row.enchant_level) for row in index] == keys
    for row, record in zip(index, tool_result.records, strict=True):
        assert row.data_size == LEVEL_ROW.size, row
        expected_offset = row.item_grade * GRADE_BLOCK_SIZE + _BLOCK_HEAD_SIZE + row.enchant_level * LEVEL_ROW.size
        assert row.data_offset == expected_offset, row
        assert LEVEL_ROW.unpack_from(data, row.data_offset) == (
            record["r_click_count"],
            record["open_slot_count"],
            record["decrease_damage_rate"],
        ), row

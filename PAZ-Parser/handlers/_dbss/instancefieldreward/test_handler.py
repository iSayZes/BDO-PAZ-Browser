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
    TargetTest,
    case_id,
    fixed_rows,
    header_count,
    run_case,
)
from tests.offset_rows import offset_row_problems

from .parser import FILE_NAME, ITEM_GROUP_COUNT, OFFSET_FILE, parse_instancefieldrewardoffset_rows


_COUNT_SIZE = 4
_OFFSET_ROW_SIZE = 10
# The index points past the leading u16 key.
_KEY_SIZE = 2
# InstanceDundeonNo 199 of the Instance_Reward sheet of client 1784.
_DUNGEON_199 = 199

CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=False,
    loc_fields=[],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=[
            "instance_dungeon_no", "instance_dungeon_no_dup", "learn_skill", "item_groups",
            "push_item_count", "push_items", "related_region_count", "related_regions", "related_region_names",
        ]),
        DeclaredCountTest(declared=header_count(offset=0)),
        TargetTest(col="instance_dungeon_no", value=_DUNGEON_199, expected={"instance_dungeon_no_dup": _DUNGEON_199}),
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
        SchemaTest(required_keys=["instance_dungeon_no", "data_offset", "data_size"]),
        DeclaredCountTest(declared=header_count(offset=0)),
        DeclaredCountTest(declared=fixed_rows(_OFFSET_ROW_SIZE, header_size=_COUNT_SIZE)),
    ],
)


@pytest.fixture(scope="module")
def reward_result(request: Any) -> HandlerResult:
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
def test_instancefieldreward_dbss(spec: Any, reward_result: HandlerResult) -> None:
    reward_result.check(spec)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_instancefieldrewardoffset_dbss(spec: Any, offset_result: HandlerResult) -> None:
    offset_result.check(spec)


def test_rows_hold_their_lists(reward_result: HandlerResult) -> None:
    """Five item groups per row; each count matches its list."""
    for record in reward_result.records:
        assert len(record["item_groups"]) == ITEM_GROUP_COUNT
        assert len(record["push_items"]) == record["push_item_count"]
        assert len(record["related_regions"]) == record["related_region_count"]
        assert record["instance_dungeon_no"] == record["instance_dungeon_no_dup"]


def test_offset_rows_point_at_their_rows() -> None:
    rows = parse_instancefieldrewardoffset_rows(load_binary_fixture(OFFSET_FILE))
    problems = offset_row_problems(load_binary_fixture(FILE_NAME), rows, struct.Struct("<H"), lead=_KEY_SIZE)
    assert not problems, problems

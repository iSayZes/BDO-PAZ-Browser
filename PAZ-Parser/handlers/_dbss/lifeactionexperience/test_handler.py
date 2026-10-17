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

from _common.pabr_offset import parse_bare_u32_offset_rows
from .parser import (
    EMPTY_LIFE_ACTION_TYPE,
    FILE_NAME,
    OFFSET_FILE,
    SLOT_COUNT,
    parse_lifeactionexperience_records,
)


_COUNT_OFFSET = 0
_COUNT_SIZE = 4
_ROW_SIZE = 26
_ITEM_KEY_SIZE = 4
_OFFSET_ROW_SIZE = 12
# Iron Ore, a gathered material with a row since client 1784.
_IRON_ORE = 4001


CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["item_name"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=[
            "item_key", "item_key_dup", "life_action_types", "experiences", "icon_path", "item_name",
            "life_skill_1", "exp_1", "life_skill_2", "exp_2",
        ]),
        DeclaredCountTest(declared=header_count(offset=_COUNT_OFFSET)),
        DeclaredCountTest(declared=fixed_rows(_ROW_SIZE, header_size=_COUNT_SIZE)),
        TargetTest(col="item_key", value=_IRON_ORE, expected={"item_key_dup": _IRON_ORE}),
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
        DeclaredCountTest(declared=header_count(offset=_COUNT_OFFSET)),
        DeclaredCountTest(declared=fixed_rows(_OFFSET_ROW_SIZE, header_size=_COUNT_SIZE)),
    ],
)


@pytest.fixture(scope="module")
def life_action_result(request: Any) -> HandlerResult:
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
def test_lifeactionexperience_dbss(spec: Any, life_action_result: HandlerResult) -> None:
    life_action_result.check(spec)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_lifeactionexperienceoffset_dbss(spec: Any, offset_result: HandlerResult) -> None:
    offset_result.check(spec)


def test_item_key_is_stored_twice(life_action_result: HandlerResult) -> None:
    assert all(r["item_key_dup"] == r["item_key"] for r in life_action_result.records)


def test_item_keys_are_unique(life_action_result: HandlerResult) -> None:
    keys = [r["item_key"] for r in life_action_result.records]
    assert len(keys) == len(set(keys))


def test_slots_hold_a_life_skill_or_the_empty_type(life_action_result: HandlerResult) -> None:
    for r in life_action_result.records:
        assert len(r["life_action_types"]) == len(r["experiences"]) == SLOT_COUNT
        assert all(0 <= t <= EMPTY_LIFE_ACTION_TYPE for t in r["life_action_types"]), r["item_key"]


def test_an_empty_slot_has_no_life_skill_and_no_exp(life_action_result: HandlerResult) -> None:
    for r in life_action_result.records:
        if r["life_action_types"][1] == EMPTY_LIFE_ACTION_TYPE:
            assert r["life_skill_2"] is None and r["exp_2"] is None, r["item_key"]
            assert r["experiences"][1] == 0, r["item_key"]


def test_offset_rows_point_past_the_first_key() -> None:
    """Each index row starts at a row's `item_key_dup` and covers the rest of the row."""
    records = parse_lifeactionexperience_records(load_binary_fixture(FILE_NAME))
    expected = {
        r["item_key"]: (_COUNT_SIZE + i * _ROW_SIZE + _ITEM_KEY_SIZE, _ROW_SIZE - _ITEM_KEY_SIZE)
        for i, r in enumerate(records)
    }
    rows = parse_bare_u32_offset_rows(load_binary_fixture(OFFSET_FILE))
    assert {row.entry_id: (row.offset, row.size) for row in rows} == expected


def test_parser_rejects_a_size_that_does_not_fit_the_count() -> None:
    row = struct.pack("<IIBBqq", _IRON_ORE, _IRON_ORE, 0, EMPTY_LIFE_ACTION_TYPE, 0, 0)
    data = struct.pack("<I", 1) + row
    record = parse_lifeactionexperience_records(data)[0]
    assert record["item_key"] == _IRON_ORE
    assert record["life_action_types"] == [0, EMPTY_LIFE_ACTION_TYPE]
    with pytest.raises(ValueError):
        parse_lifeactionexperience_records(data + b"\x00")

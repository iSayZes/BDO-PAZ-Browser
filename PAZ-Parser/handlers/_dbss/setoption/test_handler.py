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

from .parser import FILE_NAME, OFFSET_FILE, SET_SLOTS, parse_setoptionoffset_rows


_COUNT_SIZE = 4
_OFFSET_ROW_SIZE = 10
_GEAR_SET = 0
_FURNITURE_SET = 1
# Key 1 is the Velia Interior Set: eight furniture pieces, the same on
# clients 1784 and 3482 and in the client 1784 EquipSetOption sheet.
_VELIA_INTERIOR_SET = 1
_VELIA_INTERIOR_PIECES = [2004, 2014, 2104, 2204, 2214, 2304, 2311, 2704]

CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["item_names"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(
            required_keys=[
                "set_key", "set_option_type", "skill_keys", "equip_items", "installation_items", "points",
                "set_type", "effects_text", "item_ids", "item_names", "item_count",
            ],
        ),
        DeclaredCountTest(declared=header_count(offset=0)),
        RangeTest(col="set_option_type", min_val=_GEAR_SET, max_val=_FURNITURE_SET),
        TargetTest(
            col="set_key",
            value=_VELIA_INTERIOR_SET,
            expected={
                "set_option_type": _FURNITURE_SET,
                "installation_items": _VELIA_INTERIOR_PIECES,
                "equip_items": [],
            },
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
        SchemaTest(required_keys=["set_key", "data_offset", "data_size"]),
        DeclaredCountTest(declared=header_count(offset=0)),
        DeclaredCountTest(declared=fixed_rows(_OFFSET_ROW_SIZE, header_size=_COUNT_SIZE)),
    ],
)


@pytest.fixture(scope="module")
def setoption_result(request: Any) -> HandlerResult:
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
def test_setoption_dbss(spec: Any, setoption_result: HandlerResult) -> None:
    setoption_result.check(spec)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_setoptionoffset_dbss(spec: Any, offset_result: HandlerResult) -> None:
    offset_result.check(spec)


def test_set_keys_are_unique(setoption_result: HandlerResult) -> None:
    keys = [record["set_key"] for record in setoption_result.records]
    assert len(keys) == len(set(keys))


def test_each_set_type_fills_its_own_lists(setoption_result: HandlerResult) -> None:
    """Gear sets keep skills and gear pieces, furniture sets points and furniture pieces."""
    wrong = []
    for record in setoption_result.records:
        is_gear = record["set_option_type"] == _GEAR_SET
        gear_parts = any(record["skill_keys"]) or record["equip_items"]
        furniture_parts = any(record["points"]) or record["installation_items"]
        if bool(gear_parts) != is_gear or bool(furniture_parts) == is_gear:
            wrong.append(record["set_key"])
    assert not wrong, wrong


def test_every_set_has_an_effect_and_pieces(setoption_result: HandlerResult) -> None:
    for record in setoption_result.records:
        assert len(record["skill_keys"]) == len(record["points"]) == SET_SLOTS
        assert record["effects_text"], record["set_key"]
        assert record["item_count"], record["set_key"]


def test_offset_rows_point_at_their_rows() -> None:
    rows = parse_setoptionoffset_rows(load_binary_fixture(OFFSET_FILE))
    problems = offset_row_problems(load_binary_fixture(FILE_NAME), rows, struct.Struct("<H"))
    assert not problems, problems

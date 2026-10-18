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
    UserLanguageTest,
    case_id,
    header_count,
    run_case,
)

from _bss.manufacture.actions import ACTION_NAME_KEYS
from _bss.manufacture.parser import action_hash, parse_manufacture_records
from _common.pabr_offset import parse_bare_u32_offset_rows
from .parser import FILE_NAME, OFFSET_FILE, parse_manufacturecondition_records


_COUNT_OFFSET = 0
_COUNT_SIZE = 4
_ACTION_HASH_SIZE = 4
# action_hash, action_hash_dup and the u64 lengths of the name and both conditions.
_FIXED_RECORD_SIZE = 32
_HEAT = "MANUFACTURE_HEAT"


CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["display_name"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=[
            "action_hash", "action_name", "action_hash_dup", "check_visible_condition",
            "check_enable_condition", "display_name",
        ]),
        DeclaredCountTest(declared=header_count(offset=_COUNT_OFFSET)),
        UserLanguageTest(fields=["display_name"]),
        TargetTest(col="action_name", value=_HEAT, expected={"action_hash": action_hash(_HEAT)}),
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
        SchemaTest(required_keys=["action_hash", "data_offset", "data_size"]),
        DeclaredCountTest(declared=header_count(offset=_COUNT_OFFSET)),
    ],
)


@pytest.fixture(scope="module")
def condition_result(request: Any) -> HandlerResult:
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
def test_manufacturecondition_dbss(spec: Any, condition_result: HandlerResult) -> None:
    condition_result.check(spec)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_manufactureconditionoffset_dbss(spec: Any, offset_result: HandlerResult) -> None:
    offset_result.check(spec)


def test_action_hash_is_the_hash_of_the_name_stored_twice(condition_result: HandlerResult) -> None:
    for r in condition_result.records:
        assert r["action_hash"] == action_hash(r["action_name"])
        assert r["action_hash_dup"] == r["action_hash"]


def test_known_actions_show_their_window_name(condition_result: HandlerResult) -> None:
    unnamed = {
        r["action_name"]
        for r in condition_result.records
        if r["action_name"] in ACTION_NAME_KEYS and r["display_name"] == r["action_name"]
    }
    assert not unnamed


def test_every_manufacture_action_has_a_condition_record(condition_result: HandlerResult) -> None:
    recipe_actions = {recipe.action for recipe in parse_manufacture_records(load_binary_fixture("manufacture.bss"))}
    assert recipe_actions <= {r["action_name"] for r in condition_result.records}


def test_offset_rows_point_past_the_first_hash() -> None:
    """Each index row starts at a record's `action_name` and covers the rest of the record."""
    expected = {}
    pos = _COUNT_SIZE
    for r in parse_manufacturecondition_records(load_binary_fixture(FILE_NAME)):
        text_bytes = len(r["action_name"]) + 2 * (len(r["check_visible_condition"]) + len(r["check_enable_condition"]))
        size = _FIXED_RECORD_SIZE + text_bytes
        expected[r["action_hash"]] = (pos + _ACTION_HASH_SIZE, size - _ACTION_HASH_SIZE)
        pos += size
    rows = parse_bare_u32_offset_rows(load_binary_fixture(OFFSET_FILE))
    assert {row.entry_id: (row.offset, row.size) for row in rows} == expected


def _str8(text: str) -> bytes:
    return struct.pack("<Q", len(text)) + text.encode("ascii")


def _str16(text: str) -> bytes:
    return struct.pack("<Q", len(text)) + text.encode("utf-16-le")


def test_parser_reads_both_conditions_and_rejects_trailing_bytes() -> None:
    key = action_hash(_HEAT)
    record = struct.pack("<I", key) + _str8(_HEAT) + struct.pack("<I", key) + _str16("getlevel()>0") + _str16("")
    data = struct.pack("<I", 1) + record
    parsed = parse_manufacturecondition_records(data)[0]
    assert parsed["check_visible_condition"] == "getlevel()>0"
    assert parsed["check_enable_condition"] == ""
    with pytest.raises(ValueError):
        parse_manufacturecondition_records(data + b"\x00")

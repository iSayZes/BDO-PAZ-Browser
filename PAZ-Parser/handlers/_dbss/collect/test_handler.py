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
    header_count,
    run_case,
)

from _common.character_link import CHARACTERSTATIC_OFFSET_FILE, character_key_cell
from _common.pabr_offset import parse_bare_offset_rows
from .parser import EMPTY_TOOL_TYPE, FILE_NAME, OFFSET_FILE, SLOT_COUNT, parse_collect_records
from .tools import tool_display_name


_COUNT_OFFSET = 0
_COUNT_SIZE = 4
_CHARACTER_KEY_SIZE = 2
_NAME_COUNT_SIZE = 8
# The row after the name text: key, kind, time, two HP floats, product drop,
# three tool slots and drop keys, 12 unknown bytes and three u32s.
_ROW_TAIL_SIZE = 58
_MAX_PRODUCT_DATA_TYPE = 7
# Snowfield Cedar Tree, a tree, so a Logging row.
_SNOWFIELD_CEDAR = 11983
_LOGGING = 6


CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={CHARACTERSTATIC_OFFSET_FILE: CHARACTERSTATIC_OFFSET_FILE},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["character_name"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=[
            "character_key", "name", "character_key_dup", "product_data_type", "product_time",
            "product_hp", "product_decrease_hp", "product_item_drop_key", "collect_tool_types",
            "collect_item_drop_keys", "unknown_name_22", "action_point", "spawn_delay_time",
            "spawn_variable_time", "character_name", "has_character_row", "product_type_name", "tools",
        ]),
        DeclaredCountTest(declared=header_count(offset=_COUNT_OFFSET)),
        RangeTest(col="product_data_type", min_val=0, max_val=_MAX_PRODUCT_DATA_TYPE),
        TargetTest(
            col="character_key",
            value=_SNOWFIELD_CEDAR,
            expected={"product_data_type": _LOGGING, "has_character_row": True},
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
        SchemaTest(required_keys=["character_key", "data_offset", "data_size"]),
        DeclaredCountTest(declared=header_count(offset=_COUNT_OFFSET)),
    ],
)


@pytest.fixture(scope="module")
def collect_result(request: Any) -> HandlerResult:
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
def test_collect_dbss(spec: Any, collect_result: HandlerResult) -> None:
    collect_result.check(spec)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_collectoffset_dbss(spec: Any, offset_result: HandlerResult) -> None:
    offset_result.check(spec)


def test_character_key_is_stored_twice(collect_result: HandlerResult) -> None:
    assert all(r["character_key_dup"] == r["character_key"] for r in collect_result.records)


def test_character_keys_are_unique(collect_result: HandlerResult) -> None:
    keys = [r["character_key"] for r in collect_result.records]
    assert len(keys) == len(set(keys))


def test_a_slot_is_empty_exactly_where_its_drop_key_is_zero(collect_result: HandlerResult) -> None:
    for r in collect_result.records:
        assert len(r["collect_tool_types"]) == len(r["collect_item_drop_keys"]) == SLOT_COUNT
        for tool_type, drop_key in zip(r["collect_tool_types"], r["collect_item_drop_keys"]):
            assert (tool_type == EMPTY_TOOL_TYPE) == (drop_key == 0), r["character_key"]


def test_offset_rows_point_at_the_name() -> None:
    """Each index row starts 2 bytes into a row, past the key, and covers the rest of it."""
    expected = {}
    pos = _COUNT_SIZE
    for r in parse_collect_records(load_binary_fixture(FILE_NAME)):
        size = _CHARACTER_KEY_SIZE + _NAME_COUNT_SIZE + 2 * len(r["name"]) + _ROW_TAIL_SIZE
        expected[r["character_key"]] = (pos + _CHARACTER_KEY_SIZE, size - _CHARACTER_KEY_SIZE)
        pos += size
    rows = parse_bare_offset_rows(load_binary_fixture(OFFSET_FILE))
    assert {row.entry_id: (row.offset, row.size) for row in rows} == expected


def test_parser_rejects_bytes_after_the_rows() -> None:
    row = (
        struct.pack("<HQ", _SNOWFIELD_CEDAR, 0)
        + struct.pack("<HBIffI", _SNOWFIELD_CEDAR, _LOGGING, 1, 1.0, 1.0, 1)
        + bytes((2, EMPTY_TOOL_TYPE, EMPTY_TOOL_TYPE))
        + struct.pack("<III", 1, 0, 0)
        + bytes(12)
        + struct.pack("<III", 1, 0, 0)
    )
    data = struct.pack("<I", 1) + row
    record = parse_collect_records(data)[0]
    assert record["character_key"] == _SNOWFIELD_CEDAR
    assert record["collect_tool_types"] == [2, EMPTY_TOOL_TYPE, EMPTY_TOOL_TYPE]
    with pytest.raises(ValueError):
        parse_collect_records(data + b"\x00")


def test_a_tool_without_a_name_key_shows_its_number() -> None:
    assert tool_display_name(EMPTY_TOOL_TYPE) == str(EMPTY_TOOL_TYPE)


def test_a_key_without_a_character_row_is_plain_text() -> None:
    assert character_key_cell(_SNOWFIELD_CEDAR, has_row=False) == str(_SNOWFIELD_CEDAR)
    assert "record-link" in character_key_cell(_SNOWFIELD_CEDAR, has_row=True)

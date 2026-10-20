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

from _common.character_link import CHARACTERSTATIC_OFFSET_FILE
from _common.pabr_offset import parse_bare_u32_offset_rows
from _common.quest.dialog import dialog_key
from .parser import FILE_NAME, OFFSET_FILE, parse_displayexchangeitemnpc_records


_COUNT_OFFSET = 0
_COUNT_SIZE = 4
_OFFSET_ROW_SIZE = 12
# npc_character_key and dialog_index, before the list count
_ROW_HEAD_SIZE = 4
# the list count, and the key pair again after the list
_ROW_FIXED_SIZE = _ROW_HEAD_SIZE + 8 + 4
_EXCHANGE_KEY_SIZE = 2
# Quina in Altinova, the NPC whose single exchange dialog has a row since client 1784.
_QUINA = 44010


CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={CHARACTERSTATIC_OFFSET_FILE: CHARACTERSTATIC_OFFSET_FILE},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["npc_name"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=[
            "npc_character_key", "dialog_index", "item_exchange_count", "item_exchange_keys",
            "npc_character_key_dup", "dialog_index_dup", "npc_name", "has_character_row",
            "dialog_key", "dialog_name", "item_exchange_keys_text",
        ]),
        DeclaredCountTest(declared=header_count(offset=_COUNT_OFFSET)),
        TargetTest(
            col="npc_character_key",
            value=_QUINA,
            expected={"dialog_index": 1, "dialog_key": dialog_key(_QUINA, 1), "has_character_row": True},
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
        SchemaTest(required_keys=["dialog_key", "data_offset", "data_size"]),
        DeclaredCountTest(declared=header_count(offset=_COUNT_OFFSET)),
        DeclaredCountTest(declared=fixed_rows(_OFFSET_ROW_SIZE, header_size=_COUNT_SIZE)),
    ],
)


@pytest.fixture(scope="module")
def display_exchange_result(request: Any) -> HandlerResult:
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
def test_displayexchangeitemnpc_dbss(spec: Any, display_exchange_result: HandlerResult) -> None:
    display_exchange_result.check(spec)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_displayexchangeitemnpcoffset_dbss(spec: Any, offset_result: HandlerResult) -> None:
    offset_result.check(spec)


def test_key_pair_is_stored_twice(display_exchange_result: HandlerResult) -> None:
    for r in display_exchange_result.records:
        assert r["npc_character_key_dup"] == r["npc_character_key"], r["dialog_key"]
        assert r["dialog_index_dup"] == r["dialog_index"], r["dialog_key"]


def test_dialog_keys_are_unique(display_exchange_result: HandlerResult) -> None:
    keys = [r["dialog_key"] for r in display_exchange_result.records]
    assert len(keys) == len(set(keys))


def test_every_dialog_lists_an_exchange(display_exchange_result: HandlerResult) -> None:
    for r in display_exchange_result.records:
        assert r["item_exchange_count"] == len(r["item_exchange_keys"]) > 0, r["dialog_key"]


def test_offset_rows_point_past_the_key_pair() -> None:
    """Each index row starts at a row's list count and covers the rest of the row."""
    records = parse_displayexchangeitemnpc_records(load_binary_fixture(FILE_NAME))
    expected = {}
    row_start = _COUNT_SIZE
    for r in records:
        row_size = _ROW_FIXED_SIZE + r["item_exchange_count"] * _EXCHANGE_KEY_SIZE
        key = dialog_key(r["npc_character_key"], r["dialog_index"])
        expected[key] = (row_start + _ROW_HEAD_SIZE, row_size - _ROW_HEAD_SIZE)
        row_start += row_size
    rows = parse_bare_u32_offset_rows(load_binary_fixture(OFFSET_FILE))
    assert {row.entry_id: (row.offset, row.size) for row in rows} == expected


def test_parser_reads_a_row_and_rejects_extra_or_missing_bytes() -> None:
    row = struct.pack("<HHQ3HHH", _QUINA, 1, 3, 16, 17, 18, _QUINA, 1)
    data = struct.pack("<I", 1) + row
    record = parse_displayexchangeitemnpc_records(data)[0]
    assert record["npc_character_key"] == _QUINA
    assert record["item_exchange_keys"] == [16, 17, 18]
    assert record["dialog_index_dup"] == 1
    with pytest.raises(ValueError):
        parse_displayexchangeitemnpc_records(data + b"\x00")
    with pytest.raises(ValueError):
        parse_displayexchangeitemnpc_records(data[:-1])

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
    header_count,
    run_case,
)
from tests.offset_rows import offset_row_problems

from _common.item_key import split_item_key
from .parser import FILE_NAME, KEY_FIELD, OFFSET_FILE, parse_customizeditem_records, parse_customizeditemoffset_rows


_KEY = struct.Struct("<H")
# The index points past the leading u16 key.
_KEY_SIZE = 2
# Key 497 (Mysterious Secret Note) picks its item by quest: chain 22226,
# parts 20 to 22, each giving one Secret Dispatch: The Giving Tree item.
_QUEST_BOX_KEY = 497
_QUEST_BOX_CONDITIONS = ["clearquest(22226,20);", "clearquest(22226,21);", "clearquest(22226,22);"]
_QUEST_BOX_ITEMS = [66298, 66299, 66300]
# checkClass(0) names the Warrior (class type 0, LOC type 21).
_WARRIOR_CONDITION = "checkClass(0);"
_WARRIOR = "Warrior"


CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=[],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=[KEY_FIELD, "item_count", "items", "customized_item_key_dup", "choices"]),
        DeclaredCountTest(declared=header_count(offset=0)),
        TargetTest(col=KEY_FIELD, value=_QUEST_BOX_KEY, expected={"item_count": len(_QUEST_BOX_ITEMS)}),
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
        SchemaTest(required_keys=[KEY_FIELD, "data_offset", "data_size"]),
        DeclaredCountTest(declared=header_count(offset=0)),
    ],
)


@pytest.fixture(scope="module")
def customized_item_result(request: Any) -> HandlerResult:
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
def test_customizeditem_dbss(spec: Any, customized_item_result: HandlerResult) -> None:
    customized_item_result.check(spec)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_customizeditemoffset_dbss(spec: Any, offset_result: HandlerResult) -> None:
    offset_result.check(spec)


def test_every_record_repeats_its_key_after_its_items(customized_item_result: HandlerResult) -> None:
    for r in customized_item_result.records:
        assert r["customized_item_key_dup"] == r[KEY_FIELD]
        assert len(r["items"]) == r["item_count"] == len(r["choices"])


def test_keys_are_unique(customized_item_result: HandlerResult) -> None:
    keys = [r[KEY_FIELD] for r in customized_item_result.records]
    assert len(keys) == len(set(keys))


def test_quest_box_gives_one_item_per_quest(customized_item_result: HandlerResult) -> None:
    record = next(r for r in customized_item_result.records if r[KEY_FIELD] == _QUEST_BOX_KEY)
    assert [item["condition"] for item in record["items"]] == _QUEST_BOX_CONDITIONS
    assert [split_item_key(item["item_key"]) for item in record["items"]] == [(item_id, 0) for item_id in _QUEST_BOX_ITEMS]


def test_check_class_conditions_show_the_class_name(customized_item_result: HandlerResult) -> None:
    choices = [
        choice
        for r in customized_item_result.records
        for item, choice in zip(r["items"], r["choices"])
        if item["condition"] == _WARRIOR_CONDITION
    ]
    assert choices
    assert all(choice.startswith(f"{_WARRIOR}: ") for choice in choices)


def test_offset_rows_point_past_each_key() -> None:
    data = load_binary_fixture(FILE_NAME)
    rows = parse_customizeditemoffset_rows(load_binary_fixture(OFFSET_FILE))
    assert offset_row_problems(data, rows, _KEY, lead=_KEY_SIZE) == []


def _str16(text: str) -> bytes:
    return struct.pack("<Q", len(text)) + text.encode("utf-16-le")


def test_parser_reads_packed_item_keys_and_rejects_trailing_bytes() -> None:
    item_key = 8 << 24 | 10005
    record = struct.pack("<HI", 16, 1) + _str16(_WARRIOR_CONDITION) + struct.pack("<IH", item_key, 16)
    data = struct.pack("<I", 1) + record
    parsed = parse_customizeditem_records(data)[0]
    assert parsed["items"] == [{"condition": _WARRIOR_CONDITION, "item_key": item_key}]
    assert split_item_key(parsed["items"][0]["item_key"]) == (10005, 8)
    with pytest.raises(ValueError):
        parse_customizeditem_records(data + b"\x00")

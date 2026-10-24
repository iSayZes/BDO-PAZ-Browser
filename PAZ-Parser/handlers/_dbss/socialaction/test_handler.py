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
    PaFieldTest,
    SchemaTest,
    TargetTest,
    UserLanguageTest,
    case_id,
    fixed_rows,
    header_count,
    run_case,
)
from tests.offset_rows import offset_row_problems

from _common.contents_group import contents_group_key
from _common.string_hash import ascii_key_hash, key_hash
from .parser import FILE_NAME, OFFSET_FILE, parse_socialaction_records, parse_socialactionoffset_rows


_COUNT_SIZE = 4
_OFFSET_ROW_SIZE = 10
# The index points past the u16 key that opens each row.
_KEY_LEAD = 2
# Wave, the first social action.
_WAVE = 1

CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["name", "command", "keywords"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(
            required_keys=[
                "social_action_key", "social_action_key_dup", "name_kr", "condition", "chatting_command_kr",
                "chatting_command_hash", "chatting_keywords_kr", "action_name", "action_hash", "icon_path",
                "condition_message_kr", "contents_group_hashes", "unknown_contents_group_hashes_00",
                "unknown_contents_group_hashes_04", "name", "command", "keywords", "condition_message",
                "contents_groups",
            ],
        ),
        DeclaredCountTest(declared=header_count(offset=0)),
        TargetTest(
            col="social_action_key",
            value=_WAVE,
            expected={
                "name": "Wave",
                "action_name": "SOCIAL_Bye",
                "_icon_file": "ui_texture/icon/new_icon/10_socialaction/socialaction0006.dds",
            },
        ),
        PaFieldTest(field="condition_message"),
        UserLanguageTest(fields=["name", "command", "keywords", "condition_message"]),
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
        SchemaTest(required_keys=["social_action_key", "data_offset", "data_size"]),
        DeclaredCountTest(declared=header_count(offset=0)),
        DeclaredCountTest(declared=fixed_rows(_OFFSET_ROW_SIZE, header_size=_COUNT_SIZE)),
    ],
)


@pytest.fixture(scope="module")
def social_result(request: Any) -> HandlerResult:
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
def test_socialaction_dbss(spec: Any, social_result: HandlerResult) -> None:
    social_result.check(spec)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_socialactionoffset_dbss(spec: Any, offset_result: HandlerResult) -> None:
    offset_result.check(spec)


def test_offset_rows_point_past_the_row_key() -> None:
    rows = parse_socialactionoffset_rows(load_binary_fixture(OFFSET_FILE))
    problems = offset_row_problems(load_binary_fixture(FILE_NAME), rows, struct.Struct("<H"), lead=_KEY_LEAD)
    assert not problems, problems


def test_hashes_are_of_the_stored_texts() -> None:
    for record in parse_socialaction_records(load_binary_fixture(FILE_NAME)):
        key = record["social_action_key"]
        assert record["social_action_key_dup"] == key
        assert record["chatting_command_hash"] == key_hash(record["chatting_command_kr"].lower()), key
        assert record["action_hash"] == ascii_key_hash(record["action_name"]), key
        assert all(contents_group_key(group_hash) is not None for group_hash in record["contents_group_hashes"]), key


def _text(value: str) -> bytes:
    return struct.pack("<Q", len(value)) + value.encode("utf-16-le")


def test_parse_reads_one_row() -> None:
    action = b"SOCIAL_Bye"
    row = (
        struct.pack("<HH", 1, 1) + _text("손 흔들기") + _text("") + _text("손") + struct.pack("<I", 0)
        + _text("하이") + struct.pack("<Q", len(action)) + action + struct.pack("<I", 0)
        + _text("Icon.dds") + _text("") + struct.pack("<II", 1, key_hash("0")) + struct.pack("<IB", 0, 1)
    )

    (record,) = parse_socialaction_records(struct.pack("<I", 1) + row)

    assert record["action_name"] == "SOCIAL_Bye"
    assert record["contents_group_hashes"] == [key_hash("0")]
    assert record["unknown_contents_group_hashes_04"] == 1

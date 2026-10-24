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
    RangeTest,
    SchemaTest,
    TargetTest,
    case_id,
    fixed_rows,
    header_count,
    run_case,
)
from tests.offset_rows import offset_row_problems

from _common.quest.reward_entry import REWARD_ENTRY_SIZE, REWARD_ITEM
from .parser import FILE_NAME, OFFSET_FILE, parse_challenge_records, parse_challengeoffset_rows
from .text import REWARD_COUPON, challenge_reward_texts, coupon_number


_COUNT_SIZE = 4
_KEY = struct.Struct("<H")
_OFFSET_ROW_SIZE = 10
# "Guardian Reached Lv. 45!": level 45 of class type 5, on clients 1784 and
# 3483 and in the client 1784 Challenge_Table sheet.
_GUARDIAN_45 = 8250
_GUARDIAN_CLASS = 5
_COMPLETE_ACHIEVE_LEVEL = 2
_COUPON_LABEL = "Coupon {number}"

CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["title", "description"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(
            required_keys=[
                "challenge_key",
                "challenge_type",
                "title_kr",
                "description_kr",
                "progress_condition",
                "reward_condition",
                "complete_condition_type",
                "condition_param1",
                "condition_param2",
                "reset_type",
                "reset_value",
                "base_reward_count",
                "base_rewards",
                "select_reward_count",
                "select_rewards",
                "unknown_select_rewards_00",
                "unknown_select_rewards_04",
                "is_reward_overlapable",
                "is_save_repository",
                "optional_type",
                "unknown_select_rewards_12",
                "is_show_icon",
                "unknown_select_rewards_14",
                "title",
                "description",
                "challenge_type_name",
                "complete_condition_type_name",
                "reset_type_name",
                "base_reward_texts",
                "select_reward_texts",
            ]
        ),
        DeclaredCountTest(declared=header_count(offset=0)),
        TargetTest(
            col="challenge_key",
            value=_GUARDIAN_45,
            expected={
                "complete_condition_type": _COMPLETE_ACHIEVE_LEVEL,
                "complete_condition_type_name": "AchieveLevel",
                "condition_param1": 45,
                "condition_param2": _GUARDIAN_CLASS,
                "reward_condition": f"checkClass({_GUARDIAN_CLASS});",
            },
        ),
        RangeTest(col="is_reward_overlapable", min_val=0, max_val=1),
        RangeTest(col="is_save_repository", min_val=0, max_val=1),
        RangeTest(col="is_show_icon", min_val=0, max_val=1),
        RangeTest(col="unknown_select_rewards_12", min_val=0, max_val=1),
        PaFieldTest(field="description"),
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
        SchemaTest(required_keys=["challenge_key", "data_offset", "data_size"]),
        DeclaredCountTest(declared=header_count(offset=0)),
        DeclaredCountTest(declared=fixed_rows(_OFFSET_ROW_SIZE, header_size=_COUNT_SIZE)),
    ],
)


@pytest.fixture(scope="module")
def challenge_result(request: Any) -> HandlerResult:
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
def test_challenge_dbss(spec: Any, challenge_result: HandlerResult) -> None:
    challenge_result.check(spec)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_challengeoffset_dbss(spec: Any, offset_result: HandlerResult) -> None:
    offset_result.check(spec)


def test_offset_rows_point_past_the_key_prefix() -> None:
    rows = parse_challengeoffset_rows(load_binary_fixture(OFFSET_FILE))
    problems = offset_row_problems(load_binary_fixture(FILE_NAME), rows, _KEY, lead=_KEY.size)
    assert not problems, problems


def test_reward_counts_match_their_lists(challenge_result: HandlerResult) -> None:
    for record in challenge_result.records:
        assert len(record["base_rewards"]) == record["base_reward_count"], record["challenge_key"]
        assert len(record["select_rewards"]) == record["select_reward_count"], record["challenge_key"]


def _text(value: str) -> bytes:
    return struct.pack("<Q", len(value)) + value.encode("utf-16-le")


def _reward(reward_type: int, *, item_key: int = 0, item_count: int = 0, coupon: int = 0) -> bytes:
    entry = bytearray(REWARD_ENTRY_SIZE)
    struct.pack_into("<I", entry, 0x00, reward_type)
    struct.pack_into("<IqHiiH", entry, 0x19, item_key, item_count, 0, 0, 0, coupon)
    return bytes(entry)


def test_parser_reads_a_row_and_rejects_extra_or_missing_bytes() -> None:
    row = struct.pack("<HHI", 3151, 3151, 8) + _text("쿠폰") + _text("설명") + _text("0") + _text("")
    row += struct.pack("<IiiIi", 2, 10, 0, 0, 0)
    row += struct.pack("<I", 2) + _reward(REWARD_COUPON, coupon=5) + _reward(REWARD_ITEM, item_key=1, item_count=7)
    row += struct.pack("<I", 0)
    row += struct.pack("<IqBBIBBI", 0, 0, 1, 1, 0, 1, 0, 0)
    data = struct.pack("<I", 1) + row

    [record] = parse_challenge_records(data)
    assert record["challenge_key"] == 3151
    assert record["challenge_type"] == 8
    assert (record["title_kr"], record["progress_condition"]) == ("쿠폰", "0")
    assert (record["complete_condition_type"], record["condition_param1"]) == (2, 10)
    assert [r["reward_type"] for r in record["base_rewards"]] == [REWARD_COUPON, REWARD_ITEM]
    assert coupon_number(record["base_rewards"][0]) == 5
    assert challenge_reward_texts(record["base_rewards"][:1], _COUPON_LABEL) == ["Coupon 5"]
    assert record["select_rewards"] == []
    assert (record["is_reward_overlapable"], record["unknown_select_rewards_12"], record["is_show_icon"]) == (1, 1, 0)
    with pytest.raises(ValueError):
        parse_challenge_records(data + b"\x00")
    with pytest.raises(ValueError):
        parse_challenge_records(data[:-1])
    with pytest.raises(ValueError):
        parse_challenge_records(struct.pack("<IH", 1, 3150) + row[2:])

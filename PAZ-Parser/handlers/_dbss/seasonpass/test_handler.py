from __future__ import annotations

import struct
from dataclasses import replace
from typing import Any

import pytest

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

from .parser import FILE_NAME, parse_seasonpass_file


_QUEST_SHIFT = 16
# Pass row 0 of every client: the first quest pair of the first season pass chain.
_FIRST_CHAIN = 50000
_FREE_QUEST = 1
_PREMIUM_QUEST = 2

CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["base_reward_quest_text", "premium_reward_quest_text"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(
            required_keys=[
                "pass_no",
                "base_reward_quest",
                "premium_reward_quest",
                "season_type",
                "changed_title_kr",
                "changed_desc_kr",
                "condition_quest",
                "unknown_changed_desc_kr_04",
                "base_reward_quest_text",
                "premium_reward_quest_text",
                "condition_quest_text",
            ],
        ),
        DeclaredCountTest(declared=header_count(offset=0)),
        TargetTest(
            col="pass_no",
            value=0,
            expected={
                "base_reward_quest": _FREE_QUEST << _QUEST_SHIFT | _FIRST_CHAIN,
                "premium_reward_quest": _PREMIUM_QUEST << _QUEST_SHIFT | _FIRST_CHAIN,
            },
        ),
    ],
)


@pytest.fixture(scope="module")
def seasonpass_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_seasonpass_dbss(spec: Any, seasonpass_result: HandlerResult) -> None:
    seasonpass_result.check(spec)


def test_pass_numbers_run_from_zero(seasonpass_result: HandlerResult) -> None:
    numbers = sorted(record["pass_no"] for record in seasonpass_result.records)
    assert numbers == list(range(len(numbers)))


def test_free_and_premium_quests_share_a_chain(seasonpass_result: HandlerResult) -> None:
    for record in seasonpass_result.records:
        assert record["base_reward_quest"] & 0xFFFF == record["premium_reward_quest"] & 0xFFFF, record


def test_every_row_chain_sits_in_one_season_range(seasonpass_result: HandlerResult) -> None:
    parsed = parse_seasonpass_file(seasonpass_result.source.data)
    assert parsed.season_ranges
    for row in parsed.rows:
        chain = row["base_reward_quest"] & 0xFFFF
        ranges = [r for r in parsed.season_ranges if r["first_quest_chain"] <= chain <= r["last_quest_chain"]]
        assert len(ranges) == 1, row


def _row(pass_no: int, title: str = "") -> bytes:
    text = struct.pack("<Q", len(title)) + title.encode("utf-16-le")
    return struct.pack("<IIIB", pass_no, 1 << 16 | 7, 2 << 16 | 7, 1) + text + struct.pack("<Q", 0) + struct.pack("<II", 0, 0)


def test_a_file_without_ranges_reads_as_layout_1() -> None:
    parsed = parse_seasonpass_file(struct.pack("<I", 1) + _row(0, "T"))
    assert parsed.unknown_rows_00 is None and parsed.season_ranges == []
    assert parsed.rows[0]["changed_title_kr"] == "T"


def test_the_ranges_follow_the_rows() -> None:
    ranges = struct.pack("<HI", 1, 1) + struct.pack("<HHH", 1, 7, 7)
    parsed = parse_seasonpass_file(struct.pack("<I", 1) + _row(0) + ranges)
    assert parsed.unknown_rows_00 == 1
    assert parsed.season_ranges == [{"unknown_00": 1, "first_quest_chain": 7, "last_quest_chain": 7}]


def test_bytes_after_the_ranges_raise() -> None:
    ranges = struct.pack("<HI", 0, 0) + b"\x00"
    with pytest.raises(ValueError, match="season ranges end"):
        parse_seasonpass_file(struct.pack("<I", 1) + _row(0) + ranges)

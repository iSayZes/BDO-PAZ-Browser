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
    fixed_rows,
    header_count,
    run_case,
)
from tests.offset_rows import offset_row_problems

from .parser import DAYS_PER_WEEK, FILE_NAME, OFFSET_FILE, parse_attendance_records, parse_attendanceoffset_rows


_COUNT_SIZE = 4
_OFFSET_ROW_SIZE = 10
# Key 1 "Party Everyday!!" and key 5 "Returning" match the client 1784
# Attendance_Table sheet (UserConnectionType 0 and 1).
_FIRST_EVENT = 1
_RETURNING_EVENT = 5

CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["name", "event_period", "claim_period"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(
            required_keys=[
                "attendance_key", "title_kr", "unknown_title_00", "start_date", "unknown_start_date_00",
                "attendance_end_date", "unknown_attendance_end_date_00", "reward_end_date",
                "unknown_reward_end_date_00", "event_period_kr", "event_expired_kr",
                "unknown_event_expired_kr_00", "user_connection_type", "rewards", "overlap_count",
                "overlap_waiting_time", "unknown_rewards_08", "day_of_week", "display_order",
                "unknown_rewards_17", "guild_level", "name", "event_period", "claim_period", "players",
            ],
        ),
        DeclaredCountTest(declared=header_count(offset=0)),
        TargetTest(
            col="attendance_key",
            value=_FIRST_EVENT,
            expected={"title_kr": "Party Everyday!!", "user_connection_type": 0},
        ),
        TargetTest(col="attendance_key", value=_RETURNING_EVENT, expected={"user_connection_type": 1}),
        UserLanguageTest(fields=["name", "event_period", "claim_period"]),
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
        SchemaTest(required_keys=["attendance_key", "data_offset", "data_size"]),
        DeclaredCountTest(declared=header_count(offset=0)),
        DeclaredCountTest(declared=fixed_rows(_OFFSET_ROW_SIZE, header_size=_COUNT_SIZE)),
    ],
)


@pytest.fixture(scope="module")
def attendance_result(request: Any) -> HandlerResult:
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
def test_attendance_dbss(spec: Any, attendance_result: HandlerResult) -> None:
    attendance_result.check(spec)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_attendanceoffset_dbss(spec: Any, offset_result: HandlerResult) -> None:
    offset_result.check(spec)


def test_offset_rows_point_at_each_event() -> None:
    rows = parse_attendanceoffset_rows(load_binary_fixture(OFFSET_FILE))
    problems = offset_row_problems(load_binary_fixture(FILE_NAME), rows, struct.Struct("<H"))
    assert not problems, problems


def test_every_event_has_one_flag_per_weekday() -> None:
    records = parse_attendance_records(load_binary_fixture(FILE_NAME))
    wrong = [r["attendance_key"] for r in records if len(r["day_of_week"]) != DAYS_PER_WEEK]
    assert not wrong, wrong


def _str16(text: str) -> bytes:
    return struct.pack("<Q", len(text)) + text.encode("utf-16-le")


_GAP = bytes(8)


def test_parse_reads_one_event() -> None:
    row = (
        struct.pack("<H", 7)
        + _str16("Title") + _GAP
        + _str16("2026-01-01 00:00") + _GAP
        + _str16("2026-01-31 23:59") + _GAP
        + _str16("2026-02-07 23:59") + _GAP
        + _str16("Period")
        + _str16("Expired") + _GAP
        + struct.pack("<BI", 2, 2)
        + struct.pack("<IIQB", 1, 16001, 3, 0) + _str16("")
        + struct.pack("<IIQB", 2, 16080, 1, 2) + _str16("Note")
        + struct.pack("<III", 1, 3600, 0)
        + bytes([1, 0, 0, 0, 0, 0, 1])
        + struct.pack("<I4s", 9, bytes(4))
        + struct.pack("<I3H", 3, 2, 3, 4)
    )

    (record,) = parse_attendance_records(struct.pack("<I", 1) + row)

    assert record["attendance_key"] == 7
    assert record["title_kr"] == "Title"
    assert record["reward_end_date"] == "2026-02-07 23:59"
    assert record["event_expired_kr"] == "Expired"
    assert record["user_connection_type"] == 2
    assert [(r["day"], r["item_id"], r["item_count"], r["grade_type"]) for r in record["rewards"]] == [
        (1, 16001, 3, 0),
        (2, 16080, 1, 2),
    ]
    assert record["rewards"][1]["desc_kr"] == "Note"
    assert record["overlap_waiting_time"] == 3600
    assert record["day_of_week"] == [1, 0, 0, 0, 0, 0, 1]
    assert record["display_order"] == 9
    assert record["guild_level"] == [2, 3, 4]


def test_parse_rejects_a_reward_count_past_the_file() -> None:
    row = (
        struct.pack("<H", 1)
        + (_str16("") + _GAP) * 4
        + _str16("") + _str16("") + _GAP
        + struct.pack("<BI", 0, 1000)
    )

    with pytest.raises(ValueError, match="reward count"):
        parse_attendance_records(struct.pack("<I", 1) + row)

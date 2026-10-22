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

from .parser import FILE_NAME, parse_seasonreward_records


# The repeatable season of panel_window_seasonreward_all.luac (`_seasonNoRewardRepeatable`).
_REPEATABLE_SEASON = 254

CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["season_name", "description"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(
            required_keys=[
                "season_no",
                "season_name_key",
                "description_key",
                "reward_item_keys",
                "season_name",
                "description",
                "reward_names",
            ],
        ),
        DeclaredCountTest(declared=header_count(offset=0)),
        TargetTest(
            col="season_no",
            value=_REPEATABLE_SEASON,
            expected={"season_name_key": f"LUA_SEASONSERVER_NAME{_REPEATABLE_SEASON}"},
        ),
    ],
)


@pytest.fixture(scope="module")
def seasonreward_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_seasonreward_dbss(spec: Any, seasonreward_result: HandlerResult) -> None:
    seasonreward_result.check(spec)


def test_every_season_has_a_reward_and_string_keys(seasonreward_result: HandlerResult) -> None:
    for record in seasonreward_result.records:
        assert record["reward_item_keys"], record
        assert record["season_name_key"].startswith("LUA_SEASONSERVER_NAME"), record
        assert record["description_key"].startswith("LUA_SEASONSERVER_DESC"), record


def test_season_numbers_are_unique(seasonreward_result: HandlerResult) -> None:
    numbers = [record["season_no"] for record in seasonreward_result.records]
    assert len(numbers) == len(set(numbers))


def _text(text: str) -> bytes:
    return struct.pack("<Q", len(text)) + text.encode("utf-16-le")


def test_a_row_reads_its_keys_and_rewards() -> None:
    row = struct.pack("<B", 3) + _text("NAME") + _text("DESC") + struct.pack("<III", 2, 11, 5 << 24 | 12)
    (record,) = parse_seasonreward_records(struct.pack("<I", 1) + row)
    assert record == {
        "season_no": 3,
        "season_name_key": "NAME",
        "description_key": "DESC",
        "reward_item_keys": [11, 5 << 24 | 12],
    }


def test_a_reward_count_past_the_file_raises() -> None:
    row = struct.pack("<B", 1) + _text("") + _text("") + struct.pack("<I", 4)
    with pytest.raises(ValueError, match="runs past the end"):
        parse_seasonreward_records(struct.pack("<I", 1) + row)

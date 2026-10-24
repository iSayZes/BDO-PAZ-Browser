from __future__ import annotations

import struct
from dataclasses import replace
from typing import Any

import pytest

from _common.binary import u32
from _common.quest.reward_entry import REWARD_ENTRY_SIZE
from tests.framework import HandlerCase, HandlerResult, RangeTest, SchemaTest, case_id, run_case

from .parser import FILE_NAME, parse_moonblessingss_records, parse_moonblessingss_rows


# gc::RewardType values a reward entry may hold (`_common/quest/reward_entry.py`).
_MAX_REWARD_TYPE = 18

CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["rewards_text"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(
            required_keys=[
                "key",
                "start_time",
                "end_time",
                "max_used_pearl",
                "unknown_1a",
                "description_kr",
                "unknown_description_kr_00",
                "title_kr",
                "base_rewards",
                "level_no",
                "target_used_pearl",
                "description",
                "rewards_text",
            ],
        ),
        RangeTest(col="level_no", min_val=1, max_val=0xFFFF),
    ],
)


@pytest.fixture(scope="module")
def moonblessing_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_moonblessingss_dbss(spec: Any, moonblessing_result: HandlerResult) -> None:
    moonblessing_result.check(spec)


def test_the_rows_match_the_declared_count(moonblessing_result: HandlerResult) -> None:
    data = moonblessing_result.source.data
    assert len(parse_moonblessingss_rows(data)) == u32(data, 0)


def test_levels_count_up_to_the_row_maximum(moonblessing_result: HandlerResult) -> None:
    for row in parse_moonblessingss_rows(moonblessing_result.source.data):
        levels = row["levels"]
        assert [level["level_no"] for level in levels] == list(range(1, len(levels) + 1)), row["key"]
        targets = [level["target_used_pearl"] for level in levels]
        assert targets == sorted(targets) and targets[-1] == row["max_used_pearl"], row["key"]
        assert row["start_time"] < row["end_time"], row["key"]


def test_every_reward_has_a_known_type(moonblessing_result: HandlerResult) -> None:
    for record in moonblessing_result.records:
        for reward in record["base_rewards"]:
            assert 0 <= reward["reward_type"] <= _MAX_REWARD_TYPE, record["key"]


def _text(text: str) -> bytes:
    return struct.pack("<Q", len(text)) + text.encode("utf-16-le")


def _item_reward(item_key: int, count: int) -> bytes:
    head = struct.pack("<IqiiBiIqHi", 3, 0, 0, 0, 0, 0, item_key, count, 0, 0)
    return head + bytes(REWARD_ENTRY_SIZE - len(head))


def _row(level: bytes, level_count: int = 1) -> bytes:
    head = struct.pack("<HQQQH", 5, 100, 200, 800, 2) + _text("D") + struct.pack("<BI", 1, level_count)
    return head + level


def test_a_level_reads_its_rewards_and_target() -> None:
    level = _text("800") + struct.pack("<I", 1) + _item_reward(16080, 2) + struct.pack("<HQ", 1, 800)
    (record,) = parse_moonblessingss_records(struct.pack("<I", 1) + _row(level))
    assert (record["key"], record["max_used_pearl"], record["description_kr"]) == (5, 800, "D")
    assert (record["title_kr"], record["level_no"], record["target_used_pearl"]) == ("800", 1, 800)
    assert [(r["item_key"], r["item_count"]) for r in record["base_rewards"]] == [(16080, 2)]


def test_a_reward_count_past_the_file_raises() -> None:
    level = _text("") + struct.pack("<I", 2) + _item_reward(1, 1)
    with pytest.raises(ValueError, match="runs past the file"):
        parse_moonblessingss_rows(struct.pack("<I", 1) + _row(level))

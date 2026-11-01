from __future__ import annotations

import struct
from dataclasses import replace
from typing import Any

import pytest

from tests.character_indexes import character_group_index
from tests.fixtures import load_binary_fixture
from tests.framework import (
    DeclaredCountTest,
    HandlerCase,
    HandlerResult,
    PaFieldTest,
    RangeTest,
    SchemaTest,
    TargetTest,
    UserLanguageTest,
    case_id,
    header_count,
    run_case,
)

from _common.contents_group import contents_group_key
from _common.lookup_index import IndexKind
from _common.quest.reward_entry import REWARD_ENTRY_LAYOUT_1, RewardEntryLayout
from .parser import FILE_NAME, OFFSET_FILE, REWARD_ENTRY_SIZE, parse_guildquest_records


_COUNT_OFFSET = 0
_COUNT_SIZE = 4
_REWARD_ITEM = 3
_SILVER = 1
# [Subjugation] Glorious Old Moon Guild's Monster Mission
_OLD_MOON_SUBJUGATION = 5001
_SUBJUGATION = 0
# [Hunting] Glorious Guild Supply Mission
_GUILD_SUPPLY_HUNTING = 5523
_LIFE = 1
# The highest guild_quest_type: Boss Subjugation.
_BOSS_SUBJUGATION = 4


CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["title", "objective", "description"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    lookup_indexes={IndexKind.CHARACTER_GROUP_MEMBERS: character_group_index},
    tests=[
        SchemaTest(
            required_keys=[
                "quest_no",
                "complete_condition",
                "complete_condition_text_kr",
                "quest_level",
                "title_kr",
                "description_kr",
                "icon_path",
                "limit_minute",
                "need_item_key",
                "need_item_count",
                "is_preoccupancy",
                "base_reward_count",
                "base_rewards",
                "contents_group_count",
                "contents_group_hashes",
                "guild_quest_type",
                "title",
                "objective",
                "description",
                "guild_quest_type_name",
                "rewards",
                "contents_groups",
                "kill_groups",
            ]
        ),
        DeclaredCountTest(declared=header_count(offset=_COUNT_OFFSET)),
        RangeTest(col="guild_quest_type", min_val=0, max_val=_BOSS_SUBJUGATION),
        RangeTest(col="is_preoccupancy", min_val=0, max_val=1),
        UserLanguageTest(fields=["title", "objective", "description"]),
        PaFieldTest(field="description"),
        TargetTest(
            col="quest_no",
            value=_OLD_MOON_SUBJUGATION,
            expected={"guild_quest_type": _SUBJUGATION, "guild_quest_type_name": "Subjugation"},
        ),
        TargetTest(
            col="quest_no",
            value=_GUILD_SUPPLY_HUNTING,
            expected={"guild_quest_type": _LIFE, "guild_quest_type_name": "Life"},
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
        SchemaTest(required_keys=["quest_no", "data_offset", "data_size"]),
        DeclaredCountTest(declared=header_count(offset=_COUNT_OFFSET)),
        TargetTest(col="quest_no", value=_OLD_MOON_SUBJUGATION, expected={"quest_no": _OLD_MOON_SUBJUGATION}),
    ],
)


@pytest.fixture(scope="module")
def guildquest_result(request: Any) -> HandlerResult:
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
def test_guildquest_dbss(spec: Any, guildquest_result: HandlerResult) -> None:
    guildquest_result.check(spec)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_guildquestoffset_dbss(spec: Any, offset_result: HandlerResult) -> None:
    offset_result.check(spec)


def test_quest_numbers_are_unique(guildquest_result: HandlerResult) -> None:
    keys = [r["quest_no"] for r in guildquest_result.records]
    assert len(keys) == len(set(keys))


def test_lists_follow_their_counts(guildquest_result: HandlerResult) -> None:
    for record in guildquest_result.records:
        assert len(record["base_rewards"]) == record["base_reward_count"] == len(record["rewards"])
        assert len(record["contents_group_hashes"]) == record["contents_group_count"]
        assert len(record["unknown_values"]) == record["unknown_value_count"]


def test_kill_groups_name_their_members(guildquest_result: HandlerResult) -> None:
    """A killMonsterGroup condition shows as `group (xcount)` and the names of the group's characters."""
    records = guildquest_result.records
    with_calls = [r for r in records if "killmonstergroup(" in r["complete_condition"].lower()]

    assert with_calls
    assert sum(1 for r in records if r["kill_groups"]) == len(with_calls)
    for record in with_calls:
        calls, texts = record["_kill_groups"], record["kill_groups"]
        assert calls and len(texts) == len(calls)
        assert all(text.startswith(f"{group} (x{count:,}): ") for (group, count), text in zip(calls, texts))


def test_item_rewards_name_an_item_and_a_count(guildquest_result: HandlerResult) -> None:
    item_rewards = [
        reward
        for record in guildquest_result.records
        for reward in record["base_rewards"]
        if reward["reward_type"] == _REWARD_ITEM
    ]
    assert item_rewards
    assert all(reward["item_key"] and reward["item_count"] > 0 for reward in item_rewards)


def test_contents_group_hashes_decode_to_keys(guildquest_result: HandlerResult) -> None:
    hashes = {h for record in guildquest_result.records for h in record["contents_group_hashes"]}
    assert hashes
    assert all(contents_group_key(h) is not None for h in hashes)


def test_offset_rows_tile_the_file_and_point_at_their_rows(
    guildquest_result: HandlerResult, offset_result: HandlerResult
) -> None:
    """Sorted by offset, the index rows cover the file after its count, each row starting with its key."""
    data = load_binary_fixture(FILE_NAME)
    rows = sorted(offset_result.records, key=lambda r: r["data_offset"])
    position = _COUNT_SIZE
    for row in rows:
        assert row["data_offset"] == position
        assert struct.unpack_from("<I", data, position)[0] == row["quest_no"]
        position += row["data_size"]
    assert position == len(data)
    assert {r["quest_no"] for r in rows} == {r["quest_no"] for r in guildquest_result.records}


def _str16(text: str) -> bytes:
    return struct.pack("<Q", len(text)) + text.encode("utf-16-le")


def _reward(item_key: int, item_count: int, entry_size: int = REWARD_ENTRY_SIZE) -> bytes:
    head = struct.pack("<IqiiBiIqHi", _REWARD_ITEM, 0, 0, 0, 15, 0, item_key, item_count, 0, 0)
    return head + bytes(entry_size - len(head))


def _row_head(quest_no: int, rewards: list[tuple[int, int]], groups: list[int], entry_size: int) -> bytes:
    """The fields both layouts share, up to and including guild_quest_type."""
    return b"".join(
        [
            struct.pack("<I", quest_no),
            _str16("killallmonster(10);"),
            _str16("처치;"),
            struct.pack("<H", 8),
            _str16("제목"),
            _str16("설명"),
            _str16("Icon/Quest/0_Guild_Combat.dds"),
            struct.pack("<IIqB", 120, _SILVER, 50_000, 0),
            struct.pack("<I", len(rewards)),
            *(_reward(key, count, entry_size) for key, count in rewards),
            # An empty select reward list, then unknown_select_rewards_00 and _04.
            struct.pack("<IIq", 0, 0, 6_800_000),
            struct.pack(f"<I{len(groups)}I", len(groups), *groups),
            struct.pack("<B", _SUBJUGATION),
        ]
    )


def _row(quest_no: int, rewards: list[tuple[int, int]], groups: list[int], values: list[int]) -> bytes:
    """A Layout 2 row."""
    return b"".join(
        [
            _row_head(quest_no, rewards, groups, REWARD_ENTRY_SIZE),
            struct.pack(f"<I{len(values)}I", len(values), *values),
            struct.pack("<II", 1 if values else 0, 0),
        ]
    )


def _row_layout_1(
    quest_no: int, rewards: list[tuple[int, int]], groups: list[int], boss: tuple[int, int],
    entry: RewardEntryLayout = REWARD_ENTRY_LAYOUT_1,
) -> bytes:
    return _row_head(quest_no, rewards, groups, entry.size) + struct.pack("<III", *boss, 0)


def test_parser_reads_rows_and_rejects_bytes_after_them() -> None:
    data = struct.pack("<I", 2) + _row(7, [(_SILVER, 1_000), (9, 3)], [11], [5]) + _row(8, [], [], [])
    records = parse_guildquest_records(data)
    assert [r["quest_no"] for r in records] == [7, 8]
    first = records[0]
    assert [(rw["item_key"], rw["item_count"]) for rw in first["base_rewards"]] == [(_SILVER, 1_000), (9, 3)]
    assert (first["quest_level"], first["limit_minute"], first["need_item_count"]) == (8, 120, 50_000)
    assert (first["contents_group_hashes"], first["unknown_values"], first["unknown_after_unknown_values"]) == ([11], [5], 1)
    assert first["title_kr"] == "제목"
    with pytest.raises(ValueError):
        parse_guildquest_records(data + b"\x00")


def test_parser_rejects_a_row_cut_short() -> None:
    row = _row(7, [(_SILVER, 1)], [], [])
    with pytest.raises(ValueError):
        parse_guildquest_records(struct.pack("<I", 1) + row[:-1])


def test_parser_reads_layout_1_rows_with_their_boss_fields() -> None:
    data = struct.pack("<I", 2) + _row_layout_1(1, [(_SILVER, 1_000), (9, 3)], [11], (3, 1)) + _row_layout_1(
        2, [], [], (0, 0)
    )

    records = parse_guildquest_records(data)

    assert [r["quest_no"] for r in records] == [1, 2]
    first = records[0]
    assert [(rw["item_key"], rw["item_count"]) for rw in first["base_rewards"]] == [(_SILVER, 1_000), (9, 3)]
    assert (first["contents_group_hashes"], first["boss_spawn_type"], first["boss_spawn_cost"]) == ([11], 3, 1)
    assert "unknown_values" not in first


def test_a_file_that_fits_no_layout_names_where_each_broke() -> None:
    data = struct.pack("<I", 1) + _row_layout_1(1, [(_SILVER, 1)], [], (0, 0)) + b"\x00"

    with pytest.raises(ValueError, match=r"fits no known layout \(Layout 2: .*; Layout 1: 1 bytes follow"):
        parse_guildquest_records(data)

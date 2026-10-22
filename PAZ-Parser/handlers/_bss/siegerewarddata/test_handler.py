from __future__ import annotations

import struct
from dataclasses import replace
from typing import Any

import pytest

from tests.framework import (
    CaseInput,
    DeclaredCountTest,
    HandlerCase,
    HandlerResult,
    RangeTest,
    SchemaTest,
    case_id,
    run_case,
)

from .parser import GRID_BLOCK, GRID_TIERS, RELEASE_MEDAL_COUNT, TIER_BLOCK, parse_siege_reward_blocks


_U32 = struct.Struct("<I")
_BLOCK_HEAD = struct.Struct("<IH")
_GRID_BLOCK_AT = 4
_TIER_GRID_SIZE = 48
_TIER_SIZE = 24
_MAJOR_SIZE = 64
# Slots per Tier Grid tier (medals, plus item), per Tier (three rewards,
# medals, plus item) and per Major Rewards (three medals, five release
# medals, the release win medal, the plus medals and the plus item).
_GRID_TIER_SLOTS = 2
_TIER_SLOTS = 5
_MAJOR_SLOTS = 3 + RELEASE_MEDAL_COUNT + 3


def _declared_slots(source: CaseInput) -> int:
    """The slots the two block counts give: grids times tiers, tiers, and one Major Rewards each."""
    data = source.data
    _medal, grid_count = _BLOCK_HEAD.unpack_from(data, _GRID_BLOCK_AT)
    tier_block_at = _GRID_BLOCK_AT + _BLOCK_HEAD.size + grid_count * _TIER_GRID_SIZE + _MAJOR_SIZE
    _medal, tier_count = _BLOCK_HEAD.unpack_from(data, tier_block_at)
    return grid_count * GRID_TIERS * _GRID_TIER_SLOTS + tier_count * _TIER_SLOTS + 2 * _MAJOR_SLOTS


CASE = HandlerCase(
    handler_name="siegerewarddata.bss",
    data_file="siegerewarddata.bss",
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["item_name"],
    internal_path="gamecommondata/binary/siegerewarddata.bss",
    tests=[
        SchemaTest(
            required_keys=[
                "block",
                "tier_grid",
                "tier",
                "slot",
                "item_id",
                "count",
                "unknown_00",
                "unknown_08",
                "unknown_10",
                "reward",
                "icon_path",
                "item_name",
            ],
        ),
        DeclaredCountTest(declared=_declared_slots),
        RangeTest(col="block", min_val=GRID_BLOCK, max_val=TIER_BLOCK),
    ],
)


@pytest.fixture(scope="module")
def reward_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_siegerewarddata_bss(spec: Any, reward_result: HandlerResult) -> None:
    reward_result.check(spec)


def test_every_item_has_a_name(reward_result: HandlerResult) -> None:
    for record in reward_result.records:
        assert record["item_name"], record


def test_both_blocks_give_the_same_medal_item(reward_result: HandlerResult) -> None:
    grid_block, tier_block = parse_siege_reward_blocks(reward_result.source.data)
    medals = {
        grid_block["medal_item_id"],
        grid_block["major_rewards"]["plus_medal_item_id"],
        tier_block["medal_item_id"],
        tier_block["major_rewards"]["plus_medal_item_id"],
    }
    assert len(medals) == 1


def test_only_grid_block_slots_have_a_tier_grid(reward_result: HandlerResult) -> None:
    for record in reward_result.records:
        if record["tier_grid"] is not None:
            assert record["block"] == GRID_BLOCK, record


def _pabr(values: bytes) -> bytes:
    table_start = _GRID_BLOCK_AT + len(values)
    return b"PABR" + values + _U32.pack(0) + _U32.pack(table_start) + _U32.pack(0)


def _major(win_item: int) -> bytes:
    head = struct.pack("<4H5I", 1, 1, 1, 5, 44391, win_item, 0, 0, 2)
    return head + struct.pack("<HI", 1, 0) * RELEASE_MEDAL_COUNT + struct.pack("<IH", 0, 1)


def test_the_blocks_read_their_grids_tiers_and_major_rewards() -> None:
    grid = struct.pack(f"<{4 * GRID_TIERS}H{GRID_TIERS}I", *range(16), 1, 2, 3, 4)
    tier = struct.pack("<4H4I", 1, 1, 1, 5, 7, 8, 8, 44392)
    data = _pabr(_BLOCK_HEAD.pack(2, 1) + grid + _major(10) + _BLOCK_HEAD.pack(2, 1) + tier + _major(20))
    grid_block, tier_block = parse_siege_reward_blocks(data)
    assert grid_block["tier_grids"] == [
        {
            "unknown_00": [0, 1, 2, 3],
            "unknown_08": [4, 5, 6, 7],
            "unknown_10": [8, 9, 10, 11],
            "plus_medal_counts": [12, 13, 14, 15],
            "plus_item_ids": [1, 2, 3, 4],
        }
    ]
    assert tier_block["tiers"][0]["win_reward_item_id"] == 7
    assert (grid_block["major_rewards"]["win_medal_item_id"], tier_block["major_rewards"]["win_medal_item_id"]) == (10, 20)


def test_a_tier_count_past_the_string_table_raises() -> None:
    with pytest.raises(ValueError, match="runs past the string table"):
        parse_siege_reward_blocks(_pabr(_BLOCK_HEAD.pack(2, 9)))


def test_blocks_that_stop_short_of_the_string_table_raise() -> None:
    blocks = _BLOCK_HEAD.pack(2, 0) + _major(0) + _BLOCK_HEAD.pack(2, 0) + _major(0) + b"\x00"
    with pytest.raises(ValueError, match="string table starts"):
        parse_siege_reward_blocks(_pabr(blocks))

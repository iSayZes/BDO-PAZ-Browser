from __future__ import annotations

import struct
from dataclasses import replace
from typing import Any

import pytest

from tests.fixtures import load_binary_fixture
from tests.framework import HandlerCase, HandlerResult, RangeTest, SchemaTest, UserLanguageTest, case_id, run_case

from .handler import EXCHANGE_TYPE_NAMES, INFO_CATEGORY_NAMES
from .parser import FILE_NAME, NO_LEVEL, parse_exchangecoin, parse_exchangecoin_records


CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["coin_name", "reward_text"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(
            required_keys=[
                "unknown_00", "coin_item_key", "info_category", "unknown_06", "accumulated_need_counts",
                "exchange_no", "need_coin_count", "item_key", "item_count", "exchange_type", "limit_count",
                "unknown_1a", "accumulated_need_level", "coin_name", "reward_text",
            ],
        ),
        RangeTest(col="exchange_type", min_val=0, max_val=len(EXCHANGE_TYPE_NAMES) - 1),
        UserLanguageTest(fields=["coin_name", "reward_text"]),
    ],
)


@pytest.fixture(scope="module")
def exchangecoin_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_exchangecoin_bss(spec: Any, exchangecoin_result: HandlerResult) -> None:
    exchangecoin_result.check(spec)


def test_coin_count_and_key_list_match_the_coins() -> None:
    data = load_binary_fixture(FILE_NAME)
    coins, order_keys = parse_exchangecoin(data)
    (declared,) = struct.unpack_from("<I", data, 0)
    assert len(coins) == declared
    assert sorted(order_keys) == sorted(coin["coin_item_key"] for coin in coins)


def test_every_info_category_has_a_name() -> None:
    coins, _ = parse_exchangecoin(load_binary_fixture(FILE_NAME))
    unnamed = {coin["info_category"] for coin in coins} - set(INFO_CATEGORY_NAMES)
    assert not unnamed, unnamed


def test_exchange_numbers_are_unique() -> None:
    numbers = [r["exchange_no"] for r in parse_exchangecoin_records(load_binary_fixture(FILE_NAME))]
    assert len(numbers) == len(set(numbers))


def test_need_levels_stay_within_the_coin_levels() -> None:
    for coin in parse_exchangecoin(load_binary_fixture(FILE_NAME))[0]:
        levels = {reward["accumulated_need_level"] for reward in coin["rewards"]} - {NO_LEVEL}
        assert all(level <= len(coin["accumulated_need_counts"]) for level in levels), coin["coin_item_key"]


def test_parse_reads_levels_rewards_and_the_key_list() -> None:
    coin = struct.pack("<BIBqQ", 0, 890085, 2, -1, 2) + struct.pack("<2q", 200, 1000) + struct.pack("<I", 1)
    reward = struct.pack("<IqIqBBqB", 2232, 300, 289200, 1, 3, 1, -1, 2)
    data = struct.pack("<I", 1) + coin + reward + struct.pack("<II", 1, 890085)

    coins, order_keys = parse_exchangecoin(data)

    assert order_keys == [890085]
    assert coins[0]["accumulated_need_counts"] == [200, 1000]
    (record,) = parse_exchangecoin_records(data)
    assert record["exchange_no"] == 2232
    assert record["need_coin_count"] == 300
    assert record["item_key"] == 289200
    assert record["accumulated_need_level"] == 2
    assert record["coin_item_key"] == 890085

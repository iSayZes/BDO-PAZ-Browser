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

from _dbss.houseinforeceipe.parser import FILE_NAME as RECEIPE_FILE
from _dbss.houseinforeceipe.parser import parse_houseinforeceipe_records
from .parser import FILE_NAME, parse_houseinfo, products_by_house


# Velia 3-2, 2F: the second floor of a house group, bought after the first floor.
_VELIA_2F = 2109
_VELIA_1F = 2108
# Receipe 2 is Storage, the first use of every house.
_STORAGE = 2
_MAX_HOUSE_LEVEL = 5


CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={RECEIPE_FILE: RECEIPE_FILE},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["name", "town", "node"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(
            required_keys=[
                "character_key",
                "need_explore_point",
                "affiliated_town",
                "parent_node_key",
                "unknown_0a",
                "house_group",
                "house_floor",
                "need_house_keys",
                "crafts",
                "unknown_after_crafts",
                "name",
                "town",
                "node",
                "product_item_keys",
            ],
        ),
        DeclaredCountTest(declared=header_count(offset=4)),
        TargetTest(col="character_key", value=_VELIA_2F, expected={"need_house_keys": [_VELIA_1F], "town": "Velia"}),
    ],
)


@pytest.fixture(scope="module")
def houseinfo_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_houseinfo_bss(spec: Any, houseinfo_result: HandlerResult) -> None:
    houseinfo_result.check(spec)


def test_house_keys_are_unique(houseinfo_result: HandlerResult) -> None:
    keys = [r["character_key"] for r in houseinfo_result.records]
    assert len(keys) == len(set(keys))


def test_need_and_product_house_keys_name_house_rows(houseinfo_result: HandlerResult) -> None:
    info = parse_houseinfo(houseinfo_result.source.data)
    keys = {house["character_key"] for house in info.houses}

    assert {key for house in info.houses for key in house["need_house_keys"]} <= keys
    assert {key for product in info.products for key in product["house_keys"]} <= keys


def test_every_house_starts_with_storage(houseinfo_result: HandlerResult) -> None:
    assert all(r["crafts"][0]["receipe_key"] == _STORAGE for r in houseinfo_result.records)


def test_crafts_name_receipes_at_a_house_level(houseinfo_result: HandlerResult) -> None:
    receipe_keys = {r["receipe_key"] for r in parse_houseinforeceipe_records(load_binary_fixture(RECEIPE_FILE))}
    crafts = [craft for r in houseinfo_result.records for craft in r["crafts"]]

    assert {craft["receipe_key"] for craft in crafts} <= receipe_keys
    assert all(1 <= craft["level"] <= _MAX_HOUSE_LEVEL for craft in crafts)


def test_product_houses_reach_an_exchange(houseinfo_result: HandlerResult) -> None:
    """A house in the product list has a use with an exchange at or below its level."""
    levels = {r["receipe_key"]: r["level_exchanges"] for r in parse_houseinforeceipe_records(load_binary_fixture(RECEIPE_FILE))}
    info = parse_houseinfo(houseinfo_result.source.data)
    makers = {key for product in info.products for key in product["house_keys"]}

    for house in info.houses:
        if house["character_key"] in makers:
            assert any(
                keys for craft in house["crafts"] for keys in levels[craft["receipe_key"]][: craft["level"]]
            ), house["character_key"]


def test_products_are_sorted_and_unique(houseinfo_result: HandlerResult) -> None:
    item_keys = [product["item_key"] for product in parse_houseinfo(houseinfo_result.source.data).products]
    assert item_keys == sorted(set(item_keys))


def _house_row(key: int, need: list[int], crafts: list[tuple[int, int]]) -> bytes:
    head = struct.pack("<hHIHHIiQ", 2, 5, 1, key, 0xFFFF, 0, 0, len(need))
    body = struct.pack(f"<{len(need)}H", *need) + struct.pack("<I", len(crafts))
    return head + body + b"".join(struct.pack("<II", *craft) for craft in crafts) + b"\x00"


def _file(rows: list[bytes], products: list[tuple[int, list[int]]]) -> bytes:
    body = b"PABR" + struct.pack("<I", len(rows)) + b"".join(rows) + struct.pack("<I", len(products))
    for item_key, houses in products:
        body += struct.pack("<IQ", item_key, len(houses)) + struct.pack(f"<{len(houses)}H", *houses)
    return body + struct.pack("<III", 0, len(body), 0)


def test_parse_reads_rows_and_products() -> None:
    data = _file(
        [_house_row(10, [], [(2, 1)]), _house_row(11, [10], [(2, 3), (15, 2)])],
        [(5000, [11, 10, 11])],
    )

    info = parse_houseinfo(data)

    assert [h["character_key"] for h in info.houses] == [10, 11]
    assert info.houses[1]["need_house_keys"] == [10]
    assert info.houses[1]["crafts"] == [{"receipe_key": 2, "level": 3}, {"receipe_key": 15, "level": 2}]
    assert products_by_house(info.products) == {11: [5000], 10: [5000]}


def test_parse_rejects_a_product_list_that_misses_the_string_table() -> None:
    data = bytearray(_file([_house_row(10, [], [(2, 1)])], [(5000, [10])]))
    # One byte short of the real string table start (len(data) - 12).
    struct.pack_into("<I", data, len(data) - 8, len(data) - 13)

    with pytest.raises(ValueError):
        parse_houseinfo(bytes(data))

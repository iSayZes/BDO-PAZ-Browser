from __future__ import annotations

import struct
from dataclasses import replace
from functools import cache
from typing import Any

import pytest

from tests.fixtures import load_binary_fixture
from tests.framework import (
    DeclaredCountTest,
    HandlerCase,
    HandlerResult,
    RangeTest,
    SchemaTest,
    TargetTest,
    case_id,
    fixed_rows,
    header_count,
    run_case,
)

from _bss.itemexchangesource.parser import build_exchange_name_kr_index, parse_itemexchangesource_records
from _common.lookup_index import IndexKind
from _common.pabr_offset import parse_bare_u32_offset_rows
from _common.skill import skill_key, split_skill_key
from .parser import FILE_NAME, OFFSET_FILE, REQUIRED_ITEM_SLOTS, parse_guildmanufacture_records


_COUNT_OFFSET = 0
_COUNT_SIZE = 4
_OFFSET_ROW_SIZE = 12
# product_item_key, before the exchange key the index points at
_ROW_HEAD_SIZE = 4
# Every fixed-size field of a row; the u16 guild house keys come on top.
_ROW_FIXED_SIZE = 117
_HOUSE_KEY_SIZE = 2
# The categories the Guild Crafting product window titles (0 to 3).
_MAX_CATEGORY = 3
# [Guild] Ship License: Galley, crafted since client 1784, in the License and
# Registration category with Building Boat (guild skill 65042).
_GALLEY_LICENSE = 49008
_BUILDING_BOAT_1 = skill_key(65042, 1)
_VELIA_GUILD_HOUSE = 2110
# Guild Crafting exchanges are itemexchangesource.bss rows of this type (GuildHouseLargeCraft).
_GUILD_HOUSE_LARGE_CRAFT = 8


@cache
def _exchange_names() -> dict[int, str]:
    """`EXCHANGE_NAME_KR` built from the installed table, the way the app builds it."""
    return build_exchange_name_kr_index(load_binary_fixture("itemexchangesource.bss"))


CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["product_name"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    lookup_indexes={IndexKind.EXCHANGE_NAME_KR: _exchange_names},
    tests=[
        SchemaTest(required_keys=[
            "product_item_key", "exchange_item_key", "exchange", "product_item_key_dup", "time", "price",
            "product_item_limit", "required_item_keys", "required_item_counts", "category",
            "guild_house_count", "guild_house_keys", "skill_key", "product_name", "category_name",
            "skill_name", "required_items", "guild_house_names",
        ]),
        DeclaredCountTest(declared=header_count(offset=_COUNT_OFFSET)),
        RangeTest(col="category", min_val=0, max_val=_MAX_CATEGORY),
        TargetTest(
            col="product_item_key",
            value=_GALLEY_LICENSE,
            expected={"product_item_key_dup": _GALLEY_LICENSE, "category": 0, "skill_key": _BUILDING_BOAT_1},
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
        SchemaTest(required_keys=["product_item_key", "data_offset", "data_size"]),
        DeclaredCountTest(declared=header_count(offset=_COUNT_OFFSET)),
        DeclaredCountTest(declared=fixed_rows(_OFFSET_ROW_SIZE, header_size=_COUNT_SIZE)),
    ],
)


@pytest.fixture(scope="module")
def guild_manufacture_result(request: Any) -> HandlerResult:
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
def test_guildmanufacture_dbss(spec: Any, guild_manufacture_result: HandlerResult) -> None:
    guild_manufacture_result.check(spec)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_guildmanufactureoffset_dbss(spec: Any, offset_result: HandlerResult) -> None:
    offset_result.check(spec)


def test_product_key_is_stored_twice_and_unique(guild_manufacture_result: HandlerResult) -> None:
    keys = [r["product_item_key"] for r in guild_manufacture_result.records]
    assert len(keys) == len(set(keys))
    for r in guild_manufacture_result.records:
        assert r["product_item_key_dup"] == r["product_item_key"]


def test_required_slots_fill_from_the_front(guild_manufacture_result: HandlerResult) -> None:
    """An empty slot has key 0 and count 0, and no filled slot follows it."""
    for r in guild_manufacture_result.records:
        keys, counts = r["required_item_keys"], r["required_item_counts"]
        assert len(keys) == len(counts) == REQUIRED_ITEM_SLOTS
        filled = sum(1 for key in keys if key)
        assert filled > 0, r["product_item_key"]
        assert all(keys[:filled]) and all(counts[:filled]), r["product_item_key"]
        assert not any(keys[filled:]) and not any(counts[filled:]), r["product_item_key"]


def test_guild_houses_are_sorted_and_skill_is_level_one(guild_manufacture_result: HandlerResult) -> None:
    for r in guild_manufacture_result.records:
        houses = r["guild_house_keys"]
        assert r["guild_house_count"] == len(houses) > 0, r["product_item_key"]
        assert houses == sorted(set(houses)), r["product_item_key"]
        assert split_skill_key(r["skill_key"])[1] == 1, r["product_item_key"]


def test_galley_license_needs_a_velia_guild_house(guild_manufacture_result: HandlerResult) -> None:
    galley = next(r for r in guild_manufacture_result.records if r["product_item_key"] == _GALLEY_LICENSE)
    assert _VELIA_GUILD_HOUSE in galley["guild_house_keys"]


def test_every_exchange_key_is_a_guild_house_large_craft_row(guild_manufacture_result: HandlerResult) -> None:
    exchange_types = {
        exchange.key: exchange.exchange_type
        for exchange in parse_itemexchangesource_records(load_binary_fixture("itemexchangesource.bss"))
    }
    for r in guild_manufacture_result.records:
        assert exchange_types.get(r["exchange_item_key"]) == _GUILD_HOUSE_LARGE_CRAFT, r["product_item_key"]


def test_exchange_text_names_the_exchange(guild_manufacture_result: HandlerResult) -> None:
    """With LOC loaded every exchange shows a name before its key."""
    for r in guild_manufacture_result.records:
        key_suffix = f" ({r['exchange_item_key']})"
        assert r["exchange"].endswith(key_suffix) and len(r["exchange"]) > len(key_suffix), r["product_item_key"]


def test_offset_rows_point_past_the_product_key() -> None:
    """Each index row starts at a row's exchange key and covers the rest of the row."""
    records = parse_guildmanufacture_records(load_binary_fixture(FILE_NAME))
    expected = {}
    row_start = _COUNT_SIZE
    for r in records:
        row_size = _ROW_FIXED_SIZE + r["guild_house_count"] * _HOUSE_KEY_SIZE
        expected[r["product_item_key"]] = (row_start + _ROW_HEAD_SIZE, row_size - _ROW_HEAD_SIZE)
        row_start += row_size
    rows = parse_bare_u32_offset_rows(load_binary_fixture(OFFSET_FILE))
    assert {row.entry_id: (row.offset, row.size) for row in rows} == expected


def _row(product: int, houses: list[int]) -> bytes:
    keys = [9901, 9906, 0, 0, 0, 0]
    counts = [300, 25, 0, 0, 0, 0]
    return (
        struct.pack("<IIIQQQ", product, 7901, product, 86400, 10000, 1)
        + struct.pack("<6I", *keys)
        + struct.pack("<6Q", *counts)
        + struct.pack("<BI", 0, len(houses))
        + struct.pack(f"<{len(houses)}H", *houses)
        + struct.pack("<I", _BUILDING_BOAT_1)
    )


def test_parser_reads_a_row_and_rejects_extra_or_missing_bytes() -> None:
    row = _row(_GALLEY_LICENSE, [_VELIA_GUILD_HOUSE, 2140])
    assert len(row) == _ROW_FIXED_SIZE + 2 * _HOUSE_KEY_SIZE
    data = struct.pack("<I", 1) + row
    record = parse_guildmanufacture_records(data)[0]
    assert record["product_item_key"] == _GALLEY_LICENSE
    assert record["exchange_item_key"] == 7901
    assert record["required_item_keys"][:2] == [9901, 9906]
    assert record["required_item_counts"][:2] == [300, 25]
    assert record["guild_house_keys"] == [_VELIA_GUILD_HOUSE, 2140]
    assert record["skill_key"] == _BUILDING_BOAT_1
    with pytest.raises(ValueError):
        parse_guildmanufacture_records(data + b"\x00")
    with pytest.raises(ValueError):
        parse_guildmanufacture_records(data[:-1])

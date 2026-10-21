from __future__ import annotations

import struct
from dataclasses import replace
from typing import Any

import pytest

from _bss.itemexchangesource.parser import Material, parse_itemexchangesource_records
from _common.work_ani_type import NO_WORK_ANI_TYPE
from tests.framework import (
    DeclaredCountTest,
    HandlerCase,
    HandlerResult,
    RangeTest,
    SchemaTest,
    TargetTest,
    UserLanguageTest,
    case_id,
    header_count,
    run_case,
)

_COMPANIONS = ("itemmaingroup.bss", "itemsubgroup.dbss", "itemsubgroupoffset.dbss")
# Exchange types (2016 gc::ItemExchangeType::Type).
_PLANT = 4
_NON_RECIPE_CRAFT = 5
_GUILD_HOUSE_LARGE_CRAFT = 8
# The worker exchange of production key 1928 (Lumbering), which drops its own group.
_LUMBERING = 42356
# House crafting: Azwell Longsword.
_AZWELL_LONGSWORD = 5026
# Guild Crafting: Galley registration, built as character 9097 (Galley under Construction).
_GUILD_GALLEY = 7901
_GALLEY_UNDER_CONSTRUCTION = 9097

CASE = HandlerCase(
    handler_name="itemexchangesource.bss",
    data_file="itemexchangesource.bss",
    companion_files={name: name for name in _COMPANIONS},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["Name", "Description"],
    internal_path="gamecommondata/binary/itemexchangesource.bss",
    tests=[
        SchemaTest(
            required_keys=[
                "key", "name", "exchange_type", "exchange_type_name", "material_keys", "material_counts",
                "materials", "product_category", "product_time", "workload", "product_drop_key",
                "product_items", "luck_drop_key", "luck_items", "craft_character_key", "detail_description",
                "work_ani_type", "repeat_group_key", "daily_working_count", "first_working_index",
                "contents_groups", "unknown_end",
            ]
        ),
        DeclaredCountTest(declared=header_count(offset=4)),
        RangeTest(col="exchange_type", min_val=0, max_val=10),
        RangeTest(col="product_category", min_val=0, max_val=8),
        RangeTest(col="work_ani_type", min_val=0, max_val=NO_WORK_ANI_TYPE),
        UserLanguageTest(fields=["name", "detail_description"]),
        TargetTest(
            col="key",
            value=_LUMBERING,
            expected={"exchange_type": _PLANT, "product_drop_key": _LUMBERING, "material_keys": []},
        ),
        TargetTest(col="key", value=_AZWELL_LONGSWORD, expected={"exchange_type": _NON_RECIPE_CRAFT}),
        TargetTest(
            col="key",
            value=_GUILD_GALLEY,
            expected={
                "exchange_type": _GUILD_HOUSE_LARGE_CRAFT,
                "craft_character_key": _GALLEY_UNDER_CONSTRUCTION,
            },
        ),
    ],
)


@pytest.fixture(scope="module")
def itemexchangesource_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_itemexchangesource_bss(spec: Any, itemexchangesource_result: HandlerResult) -> None:
    itemexchangesource_result.check(spec)


def test_keys_are_unique(itemexchangesource_result: HandlerResult) -> None:
    keys = [record["key"] for record in itemexchangesource_result.records]
    assert len(keys) == len(set(keys))


def test_every_contents_group_hash_resolves(itemexchangesource_result: HandlerResult) -> None:
    unresolved = [
        record["key"]
        for record in itemexchangesource_result.records
        if None in record["contents_groups"]
    ]
    assert not unresolved


def _text(text: str, *, wide: bool) -> bytes:
    payload = text.encode("utf-16-le" if wide else "utf-8")
    return struct.pack("<BI", wide, len(payload)) + payload


def _row(
    key: int,
    materials: list[tuple[int, int]],
    *,
    key_dup: int | None = None,
    list_count: int = 0,
    hashes: tuple[int, ...] = (),
) -> bytes:
    head = struct.pack("<IIBB36xI", key, key if key_dup is None else key_dup, 0, 5, len(materials))
    body = b"".join(struct.pack("<IQ", item_key, count) for item_key, count in materials)
    source = body[:12] if materials else bytes(12)
    # product_category 5, 750,000 ms, drop group 5026, no luck group, no
    # character, icon 1, description 2, no detail description, animation 4.
    middle = struct.pack("<B12xQhIIHIII60xBiI", 5, 750_000, 0, 5026, 0, 0, 1, 2, 0, 4, -1, list_count)
    slots = struct.pack(f"<{list_count}H", *([0] * list_count))
    tail = struct.pack("<HHiiI", 0, 5001, 0, -1, len(hashes)) + struct.pack(f"<{len(hashes)}I", *hashes)
    return head + body + source + middle + slots + tail + struct.pack("<I", 0)


def _file(rows: list[bytes], strings: list[tuple[str, bool]]) -> bytes:
    body = b"PABR" + struct.pack("<I", len(rows)) + b"".join(rows)
    table = struct.pack("<I", len(strings)) + b"".join(_text(text, wide=wide) for text, wide in strings)
    return body + table + struct.pack("<II", len(body), 0)


_STRINGS = [("", False), ("New_Icon/03_ETC/gold.dds", False), ("아스웰 장검", True)]


def test_parser_reads_materials_lists_and_strings() -> None:
    data = _file(
        [_row(5026, [(4077, 5), (10 << 24 | 14917, 1)], list_count=2, hashes=(7, 8)), _row(42356, [])],
        _STRINGS,
    )

    rows = parse_itemexchangesource_records(data)

    assert [row.key for row in rows] == [5026, 42356]
    first = rows[0]
    assert first.materials == (Material(4077, 5), Material(10 << 24 | 14917, 1))
    assert (first.product_category, first.product_time, first.product_drop_key) == (5, 750_000, 5026)
    assert (first.icon_path, first.description_kr, first.detail_description_kr) == (
        "New_Icon/03_ETC/gold.dds", "아스웰 장검", "",
    )
    assert (first.work_ani_type, first.repeat_group_key, first.first_working_index) == (4, 5001, -1)
    assert first.unknown_list == (0, 0)
    assert first.contents_group_hashes == (7, 8)
    assert rows[1].materials == ()


def test_parser_rejects_a_key_dup_that_differs() -> None:
    with pytest.raises(ValueError):
        parse_itemexchangesource_records(_file([_row(5026, [], key_dup=5027)], _STRINGS))


def test_parser_rejects_a_string_past_the_table() -> None:
    with pytest.raises(ValueError):
        parse_itemexchangesource_records(_file([_row(5026, [])], _STRINGS[:2]))


def test_parser_rejects_rows_that_miss_the_string_table() -> None:
    data = bytearray(_file([_row(5026, []), _row(5027, [])], _STRINGS))
    # Claim one row fewer: the walk stops before the string table.
    struct.pack_into("<I", data, 4, 1)
    with pytest.raises(ValueError):
        parse_itemexchangesource_records(bytes(data))

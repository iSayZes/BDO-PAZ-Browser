from __future__ import annotations

from collections.abc import Callable
from dataclasses import replace
from functools import cache
from typing import Any

import pytest

from _bss.exploration.parser import build_node_parent_index
from _bss.itemexchangesource.parser import (
    ItemExchange,
    build_exchange_name_kr_index,
    parse_itemexchangesource_records,
)
from _bss.itemmaingroup.parser import group_item_keys, parse_itemmaingroup_records
from _bss.plantexchangegroup.node_names import english_group_names
from _bss.plantexchangegroup.parser import (
    build_production_item_index,
    build_production_luck_item_index,
    parse_plantexchangegroup_records,
)
from _dbss.plantzone.parser import parse_plantzone_records
from _common.lookup_index import IndexKind
from _dbss.itemsubgroup.parser import parse_itemsubgroup_records
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
from tests.fixtures import load_binary_fixture


_EXCHANGE_FILE = "itemexchangesource.bss"
_MAINGROUP_FILE = "itemmaingroup.bss"
_SUBGROUP_FILE = "itemsubgroup.dbss"
_SUBGROUP_OFFSET_FILE = "itemsubgroupoffset.dbss"
_WORLDMAP_FILE = "mapdata_realexplore2.bwp"
# The build_production_*_index sources, in argument order.
_PRODUCTION_FILES = (
    "plantexchangegroup.bss",
    _EXCHANGE_FILE,
    _MAINGROUP_FILE,
    _SUBGROUP_FILE,
    _SUBGROUP_OFFSET_FILE,
)
# Platerra Mountains lumbering: Elder Tree Timber, Bloody Tree Knot, Elder Tree Sap.
# Exchange 42356 drops group 42356, which lists subgroup 42356, so the chain and
# the old subgroup reading of +0x06 agree on it.
_LUMBERING_KEY = 1928
_LUMBERING_EXCHANGE = 42356
_LUMBERING_ITEMS = (4611, 5005, 5014)
# Pohalam Farm teff: subgroup 40189 is missing from itemsubgroupoffset.dbss, so
# only the exchange chain finds its items.
_TEFF_KEY = 1539
_TEFF_EXCHANGE = 40189


@cache
def _node_parent_index() -> dict[int, int]:
    """`NODE_PARENT` built from the installed tables, the way the app builds it."""
    return build_node_parent_index(load_binary_fixture("exploration.bss"), load_binary_fixture(_WORLDMAP_FILE))


@cache
def _production_sources() -> tuple[bytes, ...]:
    return tuple(load_binary_fixture(name) for name in _PRODUCTION_FILES)


@cache
def _production_items() -> dict[int, tuple[int, ...]]:
    return build_production_item_index(*_production_sources())


@cache
def _production_luck_items() -> dict[int, tuple[int, ...]]:
    return build_production_luck_item_index(*_production_sources())


@cache
def _exchange_names() -> dict[int, str]:
    return build_exchange_name_kr_index(load_binary_fixture(_EXCHANGE_FILE))


CASE = HandlerCase(
    handler_name="plantexchangegroup.bss",
    data_file="plantexchangegroup.bss",
    companion_files={name: name for name in ("plantzone.dbss", "plantzoneoffset.dbss")},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["Name", "Exchange", "Items", "Luck Drops"],
    internal_path="gamecommondata/binary/plantexchangegroup.bss",
    lookup_indexes={
        IndexKind.PRODUCTION_ITEMS: _production_items,
        IndexKind.PRODUCTION_LUCK_ITEMS: _production_luck_items,
        IndexKind.EXCHANGE_NAME_KR: _exchange_names,
        IndexKind.NODE_PARENT: _node_parent_index,
    },
    tests=[
        SchemaTest(
            required_keys=[
                "production_key",
                "unknown_02",
                "unknown_04",
                "exchange_key",
                "exchange",
                "name_kr",
                "name_en",
                "name",
                "item_keys",
                "items",
                "luck_item_keys",
                "luck_items",
            ],
        ),
        DeclaredCountTest(declared=header_count(offset=4)),
        TargetTest(
            col="production_key",
            value=_LUMBERING_KEY,
            expected={
                "exchange_key": _LUMBERING_EXCHANGE,
                "exchange": f"Lumbering ({_LUMBERING_EXCHANGE})",
                "name_kr": "플라테르 산맥 - 벌목",
                "name_en": "Platerra Mountains - Lumbering",
                "name": "Platerra Mountains - Lumbering",
                "item_keys": list(_LUMBERING_ITEMS),
                "items": ["Elder Tree Timber", "Bloody Tree Knot", "Elder Tree Sap"],
            },
        ),
        # The zone's NODE_PARENT names the parent: Arehaza, not the Areha Palm
        # Forest of its manager family.
        TargetTest(col="production_key", value=992, expected={"name_en": "Arehaza - Specialties"}),
        # Godu Village has no main node in exploration.bss, only the worldmap link.
        TargetTest(col="production_key", value=1880, expected={"name_en": "Godu Village - Farming"}),
        TargetTest(
            col="production_key",
            value=_TEFF_KEY,
            expected={"exchange_key": _TEFF_EXCHANGE, "name_kr": "포할람 농장 - 테프"},
        ),
    ],
)


@pytest.fixture(scope="module")
def plantexchangegroup_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_plantexchangegroup_bss(spec: Any, plantexchangegroup_result: HandlerResult) -> None:
    plantexchangegroup_result.check(spec)


def test_every_zone_has_a_node_parent(plantexchangegroup_result: HandlerResult) -> None:
    """The English names rest on this: every production zone is a sub-node with a parent."""
    source = plantexchangegroup_result.source
    zones = parse_plantzone_records(source.file("plantzone.dbss"), source.file("plantzoneoffset.dbss"))
    node_parents = _node_parent_index()
    assert [zone["record_id"] for zone in zones if zone["record_id"] not in node_parents] == []


def test_name_is_english_or_the_korean_label(plantexchangegroup_result: HandlerResult) -> None:
    for record in plantexchangegroup_result.records:
        assert record["name"] == (record["name_en"] or record["name_kr"])


def test_every_exchange_key_has_an_exchange_row(plantexchangegroup_result: HandlerResult) -> None:
    """`+0x06` is an item exchange key: each one names an `itemexchangesource.bss` row."""
    names = _exchange_names()
    assert [r["exchange_key"] for r in plantexchangegroup_result.records if r["exchange_key"] not in names] == []


def test_records_carry_the_luck_drops(plantexchangegroup_result: HandlerResult) -> None:
    lucky = [r for r in plantexchangegroup_result.records if r["luck_item_keys"] is not None]
    assert lucky
    for record in lucky:
        assert len(record["luck_items"]) == len(record["luck_item_keys"]) > 0


_ZONE_NAMES = {2: "Town - Farm", 3: "Town - Mine", 4: "Other Town - Farm"}


def _names(zones: list[tuple[int, int]]) -> dict[int, str]:
    return english_group_names(
        [{"record_id": zone, "production_key": key} for zone, key in zones],
        lambda key: _ZONE_NAMES.get(key, ""),
    )


def test_group_name_is_the_name_of_its_zones() -> None:
    assert _names([(2, 100), (3, 101), (2, 102)]) == {100: "Town - Farm", 101: "Town - Mine", 102: "Town - Farm"}


def test_group_name_needs_one_name_across_its_zones() -> None:
    # Two zones under different parents: no single name.
    assert _names([(2, 100), (4, 100)]) == {}
    # One zone of the key has no name, so the other does not decide alone.
    assert _names([(2, 100), (9, 100)]) == {}


def _walk_drop_groups(drop_key: Callable[[ItemExchange], int]) -> dict[int, tuple[int, ...]]:
    """The production key -> exchange -> drop group -> items chain, walked over whole tables."""
    groups_data, exchange_data, maingroup_data, subgroup_data, offset_data = _production_sources()
    exchanges = {exchange.key: exchange for exchange in parse_itemexchangesource_records(exchange_data)}
    maingroups = {group.group_id: group for group in parse_itemmaingroup_records(maingroup_data)}
    subgroups = {subgroup.subgroup_key: subgroup for subgroup in parse_itemsubgroup_records(subgroup_data, offset_data)}
    walked: dict[int, tuple[int, ...]] = {}
    for record in parse_plantexchangegroup_records(groups_data):
        exchange = exchanges.get(record["exchange_key"])
        group = maingroups.get(drop_key(exchange)) if exchange is not None else None
        item_keys = tuple(group_item_keys(group, subgroups)) if group is not None else ()
        if item_keys:
            walked[record["production_key"]] = item_keys
    return walked


def test_production_items_follow_the_exchange_product_group() -> None:
    index = _production_items()
    assert index == _walk_drop_groups(lambda exchange: exchange.product_drop_key)
    assert index[_LUMBERING_KEY] == _LUMBERING_ITEMS
    # Only the exchange chain reaches the items of a subgroup the offset table lacks.
    assert index[_TEFF_KEY]


def test_production_luck_items_follow_the_exchange_luck_group() -> None:
    index = _production_luck_items()
    assert index == _walk_drop_groups(lambda exchange: exchange.luck_drop_key)
    assert index
    assert set(index) <= {record["production_key"] for record in parse_plantexchangegroup_records(_production_sources()[0])}


def test_old_subgroup_reading_agrees_on_the_lumbering_key() -> None:
    """Exchange 42356, its drop group and the group's subgroup share one number."""
    _, _, _, subgroup_data, offset_data = _production_sources()
    subgroups = {subgroup.subgroup_key: subgroup for subgroup in parse_itemsubgroup_records(subgroup_data, offset_data)}
    assert subgroups[_LUMBERING_EXCHANGE].item_keys == _production_items()[_LUMBERING_KEY]

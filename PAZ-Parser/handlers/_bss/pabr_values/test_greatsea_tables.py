"""Checks of the Great Ocean tables in `greatsea_tables.py` that the shared cases in test_handler.py do not cover."""

from __future__ import annotations

import math

from tests.fixtures import load_binary_fixture

from _common.vehicle_type import VEHICLE_TYPE_NAMES
from .greatsea_tables import GREAT_SEA_TABLES
from .parser import parse_value_table


_TABLES = {value_table.file_name: value_table for value_table in GREAT_SEA_TABLES}
_GREAT_SEA = "greatsea.bss"
_OPTION = "greatseaoption.bss"
_SHIP_CHANGE = "oceanshipchangeitemstaticstatus.bss"
_FLOAT_FIELDS = ("x", "y", "z", "magnification")
_OPTION_FLOATS = ("ship_management_range", "barter_range")


def _records(name: str) -> list[dict]:
    return parse_value_table(load_binary_fixture(name), _TABLES[name])


def test_every_map_color_is_unique() -> None:
    colors = [record["map_color"] for record in _records(_GREAT_SEA)]
    assert colors and len(colors) == len(set(colors))


def test_each_map_color_is_stored_twice() -> None:
    for record in _records(_GREAT_SEA):
        assert record["unknown_04"] == record["map_color"], record


def test_every_area_value_is_a_finite_float() -> None:
    for record in _records(_GREAT_SEA):
        assert all(math.isfinite(record[name]) for name in _FLOAT_FIELDS), record


def test_every_vehicle_type_is_a_named_vehicle_type() -> None:
    for record in _records(_GREAT_SEA):
        assert all(vehicle_type in VEHICLE_TYPE_NAMES for vehicle_type in record["vehicle_types"]), record


def test_the_option_ranges_are_finite_floats() -> None:
    (record,) = _records(_OPTION)
    assert all(math.isfinite(record[name]) for name in _OPTION_FLOATS), record


def test_every_ship_changes_into_its_own_item() -> None:
    records = _records(_SHIP_CHANGE)
    ships = [record["character_key"] for record in records]
    items = [record["item_id"] for record in records]
    assert ships and len(ships) == len(set(ships)) and len(items) == len(set(items))


def test_every_ship_row_holds_the_one_fee() -> None:
    fees = {record["fee_money"] for record in _records(_SHIP_CHANGE)}
    assert len(fees) == 1

"""Checks of the Magnus tables in `abyssone_tables.py` that the shared cases in test_handler.py do not cover."""

from __future__ import annotations

from tests.fixtures import load_binary_fixture

from .abyssone_names import equip_slot_text, move_text, preset_text
from .abyssone_tables import ABYSS_ONE_TABLES
from .parser import parse_value_table


_TABLES = {value_table.file_name: value_table for value_table in ABYSS_ONE_TABLES}
_WAREHOUSE = "abyssonewarehouse.bss"
_COIN = "abyssonecoin.bss"
_PRESET = "abyssoneequipmentpreset.bss"
_MOVE_COST = "abyssmovecost.bss"
# abyssoneequipmentpreset.bss entry: class type, equip slot copy, u8, item key, i32, coin.
_PRESET_SLOT = 1
# abyssmovecost.bss entry: cost, region key 1, region key 2.
_MOVE_REGION_1, _MOVE_REGION_2 = 1, 2
_BELT = 12
_ENCHANT_SHIFT = 24


def _records(name: str) -> list[dict]:
    return parse_value_table(load_binary_fixture(name), _TABLES[name])


def _unique(values: list[object]) -> bool:
    return bool(values) and len(values) == len(set(values))


def test_every_storage_region_is_listed_once() -> None:
    assert _unique([record["region_key"] for record in _records(_WAREHOUSE)])


def test_every_coin_key_is_listed_once() -> None:
    assert _unique([record["unknown_00"] for record in _records(_COIN)])


def test_every_equip_slot_is_listed_once() -> None:
    assert _unique([record["equip_slot"] for record in _records(_PRESET)])


def test_each_preset_repeats_its_equip_slot() -> None:
    for record in _records(_PRESET):
        assert record["presets"], record
        assert all(entry[_PRESET_SLOT] == record["equip_slot"] for entry in record["presets"]), record


def test_each_move_row_starts_from_one_region() -> None:
    first_regions = []
    for record in _records(_MOVE_COST):
        regions = {entry[_MOVE_REGION_1] for entry in record["moves"]}
        assert len(regions) == 1, record
        first_regions.extend(regions)
    assert _unique(first_regions)


def test_every_move_row_lists_the_same_regions() -> None:
    lists = {frozenset(entry[_MOVE_REGION_2] for entry in record["moves"]) for record in _records(_MOVE_COST)}
    assert len(lists) == 1


def test_an_equip_slot_shows_its_number_first() -> None:
    assert equip_slot_text(_BELT).startswith(f"{_BELT} ")


def test_a_preset_shows_its_level_and_price() -> None:
    entry = [0, 0, 0, 2 << _ENCHANT_SHIFT | 738501, -1, 1500]
    text = preset_text(entry)
    assert "+2 (738501)" in text and text.endswith(", 1,500 coins")
    assert preset_text([0, 0, 0, 738501, -1, 0]).endswith("(738501)")


def test_a_move_shows_both_regions_and_the_cost() -> None:
    text = move_text([5_000_000, 1733, 5])
    assert text.startswith("1733") and " / 5" in text and text.endswith(": 5,000,000")

"""Checks of the ocean siege tables in `oceansiege_tables.py` that the shared cases in test_handler.py do not cover."""

from __future__ import annotations

from tests.fixtures import load_binary_fixture

from .handler import PabrValuesBssHandler
from .oceansiege_names import siege_day_name, siege_days_text
from .oceansiege_tables import OCEAN_SIEGE_TABLES
from .parser import parse_value_table


_TABLES = {value_table.file_name: value_table for value_table in OCEAN_SIEGE_TABLES}
_INFO = "oceansiegeinfo.bss"
_TERRITORY_OPTION = "oceansiegeterritoryoption.bss"
# CppEnums.VillageSiegeType: Sunday 0 to Saturday 6, then _Count.
_DAY_COUNT = 7


def _records(name: str) -> list[dict]:
    return parse_value_table(load_binary_fixture(name), _TABLES[name])


def test_every_map_color_is_unique() -> None:
    colors = [record["map_color"] for record in _records(_INFO)]
    assert colors and len(colors) == len(set(colors))


def test_each_map_color_is_stored_twice() -> None:
    for record in _records(_INFO):
        assert record["unknown_04"] == record["map_color"], record


def test_the_number_after_the_regions_is_unique() -> None:
    numbers = [record["unknown_region_keys_00"] for record in _records(_INFO)]
    assert len(numbers) == len(set(numbers))


def test_no_island_belongs_to_two_areas() -> None:
    keys = [key for record in _records(_INFO) for key in record["region_keys"]]
    assert keys and len(keys) == len(set(keys))


def test_the_console_territory_is_one_of_the_pair() -> None:
    # getConsoleTerritoryKeyRaw() is compared with getTerritoryKey1Raw() and
    # getTerritoryKey2Raw() (panel_window_villagesiegemenu_all_1.luac).
    for record in _records(_TERRITORY_OPTION):
        assert record["console_territory_key"] in (record["territory_key_1"], record["territory_key_2"]), record


def test_every_battle_day_is_a_week_day() -> None:
    for record in _records(_TERRITORY_OPTION):
        assert record["start_days"], record
        assert all(0 <= day < _DAY_COUNT for day in record["start_days"]), record


def test_battle_days_read_as_day_names() -> None:
    assert siege_days_text([0, 5]) == "Sunday, Friday"
    assert siege_day_name(_DAY_COUNT) == str(_DAY_COUNT)


def test_the_territory_option_cells_show_names_and_days() -> None:
    handler = PabrValuesBssHandler(_TABLES[_TERRITORY_OPTION])
    handler.lang = "en"
    names = {"territory_name_1": "Balenos", "territory_name_2": "Calpheon", "console_territory_name": "Balenos"}
    record = {**_records(_TERRITORY_OPTION)[0], **names}
    html = handler.render_records_page([record], 0, 1)
    assert "Sunday" in html and "Max Participants (Friday)" in html

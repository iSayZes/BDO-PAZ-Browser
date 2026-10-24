"""Checks of the land siege tables in `siege_tables.py` that the shared cases in test_handler.py do not cover."""

from __future__ import annotations

import math

from tests.fixtures import load_binary_fixture

from .handler import PabrValuesBssHandler
from .parser import parse_value_table
from .siege_names import NO_TERRITORY, territories_text, territory_text
from .siege_tables import SIEGE_TABLES


_TABLES = {value_table.file_name: value_table for value_table in SIEGE_TABLES}
_SIEGE_INFO = "siegeinfo.bss"
_VILLAGE_SIEGE_INFO = "villagesiegeinfo.bss"
_DAY_OPTION = "siegedayoption.bss"
_TERRITORY_OPTION = "siegeterritoryoptionstaticstatus.bss"
_OCCUPY_COLOR = "siegeoccupycolor.bss"
_MAP_COLOR_TABLES = (_SIEGE_INFO, _VILLAGE_SIEGE_INFO)
_WEEK_DAYS = ("sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday")
# CppEnums.VillageSiegeType: Sunday 0 to Saturday 6, then _Count.
_DAY_COUNT = 7
# territoryinfo.bss keys past the LOC names, for the cell text checks.
_UNNAMED_TERRITORY = 9999
# Fully opaque: the alpha byte of every siegeoccupycolor.bss colour.
_OPAQUE = "ff"


def _records(name: str) -> list[dict]:
    return parse_value_table(load_binary_fixture(name), _TABLES[name])


def test_every_map_color_is_unique_and_stored_twice() -> None:
    for name in _MAP_COLOR_TABLES:
        records = _records(name)
        colors = [record["map_color"] for record in records]
        assert colors and len(colors) == len(set(colors)), name
        assert all(record["map_color_dup"] == record["map_color"] for record in records), name


def test_only_the_siege_areas_have_a_territory() -> None:
    for record in _records(_SIEGE_INFO):
        assert (record["territory_key"] != NO_TERRITORY) == bool(record["is_siege"]), record


def test_no_territory_has_two_siege_areas() -> None:
    keys = [record["territory_key"] for record in _records(_SIEGE_INFO) if record["is_siege"]]
    assert keys and len(keys) == len(set(keys))


def test_no_node_region_belongs_to_two_areas() -> None:
    records = _records(_VILLAGE_SIEGE_INFO)
    keys = [key for record in records for key in record["region_keys"]]
    numbers = [record["unknown_region_keys_00"] for record in records]
    assert keys and len(keys) == len(set(keys))
    assert len(numbers) == len(set(numbers))


def test_the_day_option_is_one_record_of_seven_day_lists() -> None:
    (record,) = _records(_DAY_OPTION)
    for day in _WEEK_DAYS:
        keys = record[f"{day}_territory_keys"]
        assert len(keys) == len(set(keys)), day
    assert any(record[f"{day}_territory_keys"] for day in _WEEK_DAYS)


def test_the_console_territory_is_one_of_the_pair() -> None:
    for record in _records(_TERRITORY_OPTION):
        assert record["console_territory_key"] in (record["territory_key_1"], record["territory_key_2"]), record


def test_every_battle_day_is_a_week_day() -> None:
    for record in _records(_TERRITORY_OPTION):
        assert record["start_days"], record
        assert all(0 <= day < _DAY_COUNT for day in record["start_days"]), record


def test_the_icon_positions_are_finite_and_on_the_panel() -> None:
    fields = ("territory_1_icon_x", "territory_1_icon_y", "territory_2_icon_x", "territory_2_icon_y")
    for record in _records(_TERRITORY_OPTION):
        assert all(math.isfinite(record[field]) and record[field] >= 0 for field in fields), record


def test_the_ap_limit_repeats_after_the_rate_block() -> None:
    for record in _records(_TERRITORY_OPTION):
        assert record["unknown_34"] == record["unknown_38"] == record["ap_limit"], record


def test_the_occupy_colors_count_up_and_are_opaque() -> None:
    records = _records(_OCCUPY_COLOR)
    assert [record["index"] for record in records] == list(range(1, len(records) + 1))
    colors = [record["color"] for record in records]
    assert len(colors) == len(set(colors))
    assert all(color.split(" ")[-1] == _OPAQUE for color in colors)


def test_territory_cells_show_keys_without_names() -> None:
    assert territory_text(NO_TERRITORY) == "-"
    assert territory_text(_UNNAMED_TERRITORY) == str(_UNNAMED_TERRITORY)
    assert territories_text([_UNNAMED_TERRITORY]) == str(_UNNAMED_TERRITORY)
    assert territories_text([]) == ""


def test_the_day_option_shows_a_column_per_day() -> None:
    handler = PabrValuesBssHandler(_TABLES[_DAY_OPTION])
    handler.lang = "en"
    html = handler.render_records_page(_records(_DAY_OPTION), 0, 1)
    assert "Sunday" in html and "Saturday" in html


def test_the_territory_option_shows_the_named_limits() -> None:
    handler = PabrValuesBssHandler(_TABLES[_TERRITORY_OPTION])
    handler.lang = "en"
    names = {"territory_name_1": "Balenos", "territory_name_2": "Serendia", "console_territory_name": "Serendia"}
    record = {**_records(_TERRITORY_OPTION)[0], **names}
    html = handler.render_records_page([record], 0, 1)
    assert "AP Limit" in html and "Stamina Limit" in html and "Territory 1 Icon X" in html

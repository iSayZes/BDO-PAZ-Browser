"""Checks of the server option tables in `server_tables.py` that the shared cases in test_handler.py do not cover."""

from __future__ import annotations

from tests.fixtures import load_binary_fixture

from .layout import ROW_INDEX_FIELD
from .parser import parse_value_table
from .server_names import light_user_reward_text
from .server_tables import LIGHT_USER_REWARD_SLOTS, SERVER_TABLES


_TABLES = {value_table.file_name: value_table for value_table in SERVER_TABLES}
_VARIED_PRICE = "variedprice.bss"
_VARIED_TRADE_COUNT = "variedtradecount.bss"
_DYNAMIC_BSS = "dynamicbssoption.bss"
_LIGHT_USER_BONUS = "lightuserbonus.bss"
_FAMILY_POINT_STAT = "familypointstat.bss"
_BITMAP_DROP_FILES = ("waterinfo.bss", "undergroundinfo.bss")
_FLAG_VALUES = {0, 1}


def _records(name: str) -> list[dict]:
    return parse_value_table(load_binary_fixture(name), _TABLES[name])


def _unique(values: list[object]) -> bool:
    return bool(values) and len(values) == len(set(values))


def _assert_ranges_follow_on(records: list[dict], start: str, end: str) -> None:
    """Each range starts one past the previous range's end."""
    assert records
    for previous, current in zip(records, records[1:]):
        assert current[start] == previous[end] + 1, (previous, current)
        assert current[start] <= current[end], current


def test_price_ranges_follow_on_from_zero() -> None:
    records = _records(_VARIED_PRICE)
    assert records[0]["start_range_price"] == 0
    _assert_ranges_follow_on(records, "start_range_price", "end_range_price")
    assert all(record["unit_price"] > 0 for record in records)


def test_family_point_ranges_follow_on_from_zero() -> None:
    records = _records(_VARIED_TRADE_COUNT)
    assert records[0]["min_family_point"] == 0
    _assert_ranges_follow_on(records, "min_family_point", "max_family_point")


def test_each_dynamic_bss_entry_is_a_flag_at_its_index() -> None:
    records = _records(_DYNAMIC_BSS)
    assert [record[ROW_INDEX_FIELD] for record in records] == list(range(len(records)))
    assert {record["real"] for record in records} <= _FLAG_VALUES


def test_each_light_user_bonus_row_has_ten_slots() -> None:
    records = _records(_LIGHT_USER_BONUS)
    assert _unique([record["key"] for record in records])
    for record in records:
        assert len(record["rewards"]) == LIGHT_USER_REWARD_SLOTS, record
        assert record["valid_reward_count"] <= LIGHT_USER_REWARD_SLOTS, record


def test_every_family_point_step_is_listed_once() -> None:
    assert _unique([record["index"] for record in _records(_FAMILY_POINT_STAT)])


def test_every_bitmap_colour_is_listed_once() -> None:
    for name in _BITMAP_DROP_FILES:
        assert _unique([record["color_key"] for record in _records(name)]), name


def test_a_light_user_reward_cell_lists_only_filled_slots() -> None:
    assert light_user_reward_text([[0, 0], [3600, 65001], [0, 0]]) == "3600: 65001"
    assert light_user_reward_text([[0, 0]] * LIGHT_USER_REWARD_SLOTS) == ""

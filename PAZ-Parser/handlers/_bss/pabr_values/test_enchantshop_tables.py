"""Checks of the enchant and shop tables in `enchantshop_tables.py` that the shared cases in test_handler.py do not cover."""

from __future__ import annotations

from tests.fixtures import load_binary_fixture

from .enchantshop_names import challenge_text, day_percent_text, reforge_level_text, stack_text
from .enchantshop_tables import ENCHANT_SHOP_TABLES
from .layout import ValueTable
from .parser import parse_value_table


_TABLES = {value_table.file_name: value_table for value_table in ENCHANT_SHOP_TABLES}
_STACK = _TABLES["enchant_blackstonestack.bss"]
_REFORGE = _TABLES["reforgestonestaticstatusmanager.bss"]
_DRAW = _TABLES["drawitemstaticstatus.bss"]
_CHALLENGE_GROUP = _TABLES["pearlusedchallengegroup.bss"]
_TAG_ORDER = _TABLES["cashproductcategorytagorder.dbss"]
_MANSION = _TABLES["mansionrentaldiscount.bss"]
# Positions in a stack entry (need_stack_item_count, stack, padding_0c) and a
# reforge level (item_enchant_key, unknown_04, material key, padding_0c, material count).
_STACK_VALUE = 1
_LEVEL_MATERIAL_KEY = 2
# tag_order of a product tag with no rank.
_NO_RANK = -1
# The mansion contract window takes 1 to 365 days (panel_window_mansioncontract_all).
_MAX_CONTRACT_DAYS = 365


def _records(value_table: ValueTable) -> list[dict]:
    return parse_value_table(load_binary_fixture(value_table.file_name), value_table)


def test_the_stack_steps_rise() -> None:
    for record in _records(_STACK):
        stacks = [entry[_STACK_VALUE] for entry in record["stacks"]]
        assert stacks and stacks == sorted(set(stacks)), record["need_stack_item_key"]


def test_the_stack_items_are_unique() -> None:
    keys = [record["need_stack_item_key"] for record in _records(_STACK)]
    assert keys and len(keys) == len(set(keys))


def test_only_level_zero_has_no_upgrade_material() -> None:
    for record in _records(_REFORGE):
        materials = [level[_LEVEL_MATERIAL_KEY] for level in record["levels"]]
        assert materials[0] == 0 and all(materials[1:]), record["index"]


def test_the_draw_index_numbers_every_prize_once() -> None:
    records = _records(_DRAW)
    assert sorted(record["index"] for record in records) == list(range(1, len(records) + 1))


def test_one_draw_event_shares_its_coin_and_lose_items() -> None:
    records = _records(_DRAW)
    assert len({(record["coin_item_key"], record["lose_item_key"]) for record in records}) <= 1


def test_each_group_lists_its_main_challenge() -> None:
    records = _records(_CHALLENGE_GROUP)
    assert records
    for record in records:
        assert record["main_challenge_key"] in record["challenge_keys"], record


def test_a_group_has_one_row_per_challenge() -> None:
    groups: dict[int, list[dict]] = {}
    for record in _records(_CHALLENGE_GROUP):
        groups.setdefault(record["main_challenge_key"], []).append(record)
    for rows in groups.values():
        assert len(rows) == len(rows[0]["challenge_keys"]) and all(row == rows[0] for row in rows)


def test_every_tag_rank_is_positive_or_none() -> None:
    orders = [record["tag_order"] for record in _records(_TAG_ORDER)]
    assert orders and all(order == _NO_RANK or order > 0 for order in orders)


def test_both_mansion_lists_share_their_days() -> None:
    (record,) = _records(_MANSION)
    rental_days = [day for day, _ in record["rental_percents"]]
    return_days = [day for day, _ in record["return_percents"]]
    assert rental_days == return_days == sorted(set(rental_days))
    assert 0 < rental_days[0] and rental_days[-1] <= _MAX_CONTRACT_DAYS


def test_the_cells_show_counts_items_and_percents() -> None:
    assert stack_text([5, 5, "00 00 00 00"]) == "x5: +5"
    assert day_percent_text([30, 50000]) == "30: 5%"
    assert reforge_level_text([0, 0, 0, "00 00 00 00", 7]) == "0"
    assert challenge_text(0) == "0"

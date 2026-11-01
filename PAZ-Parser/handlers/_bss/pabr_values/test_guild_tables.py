"""Checks of the guild tables in `guild_tables.py` that the shared cases in test_handler.py do not cover."""

from __future__ import annotations

import pytest

from tests.fixtures import load_binary_fixture

from .guild_names import grade_text, number_list_text
from .guild_tables import GUILD_TABLES
from .handler import PabrValuesBssHandler
from .layout import ValueField, ValueTable
from .parser import parse_value_table


_TABLES = {value_table.file_name: value_table for value_table in GUILD_TABLES}
_GRADE_TABLES = ("guildright.bss", "guildspecialskillright.bss")


def _records(name: str) -> list[dict]:
    return parse_value_table(load_binary_fixture(name), _TABLES[name])


@pytest.mark.parametrize("name", _GRADE_TABLES)
def test_every_grade_list_holds_one_flag_per_grade(name: str) -> None:
    lists = [record["grade"] for record in _records(name)]
    assert lists
    assert len({len(flags) for flags in lists}) == 1, name
    assert all(flag in (0, 1) for flags in lists for flag in flags)


def test_the_grade_tables_agree_on_the_grade_count() -> None:
    counts = {len(record["grade"]) for name in _GRADE_TABLES for record in _records(name)}
    assert len(counts) == 1


def test_the_rank_brackets_join_without_gaps() -> None:
    brackets = sorted((record["rank"], record["min_point"], record["max_point"]) for record in _records("guildmatchrank.bss"))
    assert brackets[-1][1] == 0
    for (_, upper_min, _), (_, _, lower_max) in zip(brackets, brackets[1:]):
        assert lower_max + 1 == upper_min


def test_every_combat_exp_list_has_the_same_length() -> None:
    assert len({len(record["combat_exp"]) for record in _records("guildmatchexp.bss")}) == 1


def test_every_reward_entry_holds_an_item_and_a_count() -> None:
    (option,) = _records("guildmatchoption.bss")
    for field in ("victory_reward_items", "defeat_reward_items"):
        assert option[field], field
        assert all(len(entry) == 2 and entry[0] and entry[1] > 0 for entry in option[field])


def test_grade_text_names_the_set_flags() -> None:
    assert grade_text([1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0]) == "0, 1, 6, 8, 9"
    assert grade_text([0, 0]) == ""


def test_a_list_display_draws_the_whole_list_in_one_cell() -> None:
    value_table = ValueTable(
        "test.bss",
        (ValueField("grade", "B", "grades", is_counted_list=True, list_display=grade_text),),
    )
    handler = PabrValuesBssHandler(value_table)
    handler.lang = "en"
    html = handler.render_records_page([{"grade": [1, 0, 1]}, {"grade": [0, 0, 0]}], 0, 2)
    assert "<td class=\"num\">0, 2</td>" in html.replace("'", '"')
    assert number_list_text([3, 400]) == "3, 400"


def test_a_list_display_needs_a_counted_list() -> None:
    with pytest.raises(ValueError, match="list_display"):
        ValueField("grade", "B", "grades", list_display=grade_text)

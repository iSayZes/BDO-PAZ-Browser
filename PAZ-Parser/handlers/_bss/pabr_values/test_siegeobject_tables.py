"""Checks of the siege object tables in `siegeobject_tables.py` that the shared cases in test_handler.py do not cover."""

from __future__ import annotations

import math
import struct

import pytest

from tests.fixtures import load_binary_fixture

from .handler import PabrValuesBssHandler
from .layout import RowCount, ValueField, ValueTable
from .parser import parse_value_table
from .siegeobject_tables import SIEGE_OBJECT_TABLES


_TABLES = {value_table.file_name: value_table for value_table in SIEGE_OBJECT_TABLES}
_OBJECT_KINDS = "siegeobjectkindlistcache.bss"
_GRAVITY = "siegegravity.bss"
_REVIVE_VALUE = "siegerevivevalue.bss"
_ANGER_SKILL = "siegeangerskill.bss"
_CARRIAGE_SPAWN = "siegegovernorcarriagespawn.bss"
_CARRIAGE_POSITION = "siegegovernorcarriagespawnposition.bss"
_POSITION_FIELDS = ("position_x", "position_y", "position_z")
_ANGER_POINT_FIELDS = tuple(field.name for field in _TABLES[_ANGER_SKILL].tail)
# The rows that cost the Spirit of Battle gauge; `0` costs nothing (siegeangerskill_bss.md).
_NO_RESOURCE = 0


def _records(name: str) -> list[dict]:
    return parse_value_table(load_binary_fixture(name), _TABLES[name])


def _pabr(values: bytes) -> bytes:
    """A PABR file of `values` with an empty string table."""
    table_start = 4 + len(values)
    return b"PABR" + values + struct.pack("<III", 0, table_start, 0)


def test_each_object_kind_has_one_character() -> None:
    records = _records(_OBJECT_KINDS)
    kinds = [record["object_kind"] for record in records]
    assert kinds and len(kinds) == len(set(kinds))
    assert all(record["character_key"] for record in records)


def test_each_gravity_territory_has_one_finite_position() -> None:
    records = _records(_GRAVITY)
    keys = [record["territory_key"] for record in records]
    assert keys and len(keys) == len(set(keys))
    for record in records:
        assert all(math.isfinite(record[field]) for field in _POSITION_FIELDS), record
        assert record["unknown_0e"] > 0, record


def test_the_revive_value_is_one_record_with_the_entry_outfit() -> None:
    (record,) = _records(_REVIVE_VALUE)
    assert record["major_siege_enter_clothes_item_key"]
    assert record["siege_revival_time"] and record["siege_death_revival_time"]


def test_every_anger_skill_costs_at_most_the_full_gauge() -> None:
    records = _records(_ANGER_SKILL)
    skill_nos = [record["skill_no"] for record in records]
    assert skill_nos and len(skill_nos) == len(set(skill_nos))
    for record in records:
        assert record["resource_point"] <= record["max_anger_point"], record
        assert (record["resource_point"] > 0) == (record["siege_skill_resource_type"] != _NO_RESOURCE), record


def test_the_anger_point_values_are_stored_once() -> None:
    records = _records(_ANGER_SKILL)
    gauges = {tuple(record[field] for field in _ANGER_POINT_FIELDS) for record in records}
    assert len(gauges) == 1


def test_every_wagon_spawn_points_at_a_spawn_position() -> None:
    indexes = {record["index"] for record in _records(_CARRIAGE_POSITION)}
    records = _records(_CARRIAGE_SPAWN)
    territories = [record["territory_key"] for record in records]
    assert len(territories) == len(set(territories))
    for record in records:
        assert record["spawn_position_list"], record
        assert set(record["spawn_position_list"]) <= indexes, record


def test_the_spawn_positions_count_up_from_zero() -> None:
    records = _records(_CARRIAGE_POSITION)
    assert [record["index"] for record in records] == list(range(len(records)))
    for record in records:
        assert all(math.isfinite(record[field]) for field in _POSITION_FIELDS), record


def test_tail_fields_are_read_after_the_rows_onto_every_record() -> None:
    table = ValueTable("test.bss", (ValueField("a", "B"),), RowCount.COUNTED, tail=(ValueField("b", "I"),))
    records = parse_value_table(_pabr(struct.pack("<IBBI", 2, 7, 8, 99)), table)
    assert records == [{"a": 7, "b": 99}, {"a": 8, "b": 99}]


def test_tail_fields_must_fill_the_values() -> None:
    table = ValueTable("test.bss", (ValueField("a", "B"),), RowCount.COUNTED, tail=(ValueField("b", "I"),))
    with pytest.raises(ValueError, match="values"):
        parse_value_table(_pabr(struct.pack("<IBB", 1, 7, 8)), table)


def test_tail_fields_need_a_row_count() -> None:
    with pytest.raises(ValueError, match="tail fields"):
        ValueTable("test.bss", (ValueField("a", "B"),), tail=(ValueField("b", "I"),))


def test_the_anger_skills_show_the_gauge_columns() -> None:
    handler = PabrValuesBssHandler(_TABLES[_ANGER_SKILL])
    handler.lang = "en"
    record = {**_records(_ANGER_SKILL)[0], "skill_name": "Breath of Life"}
    html = handler.render_records_page([record], 0, 1)
    assert "Max Spirit of Battle" in html and "Survival Decrease Rate" in html

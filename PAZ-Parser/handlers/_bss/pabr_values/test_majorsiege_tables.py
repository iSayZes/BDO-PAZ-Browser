"""Checks of the Conquest War tables in `majorsiege_tables.py` that the shared cases in test_handler.py do not cover."""

from __future__ import annotations

from tests.fixtures import load_binary_fixture

from .majorsiege_tables import MAJOR_SIEGE_TABLES
from .parser import parse_value_table


_TABLES = {value_table.file_name: value_table for value_table in MAJOR_SIEGE_TABLES}
_REWARD_RATE = "majorsiegecommonrewardratestaticstatusmanager.bss"
_OBJECT_POINT = "majorseigereleaseobjectpoint.bss"
# The 1,000,000 = 100% scale of a rate.
_FULL_RATE = 1_000_000


def _records(name: str) -> list[dict]:
    return parse_value_table(load_binary_fixture(name), _TABLES[name])


def test_every_reward_rate_is_on_the_rate_scale() -> None:
    records = _records(_REWARD_RATE)
    assert records
    for record in records:
        assert 0 < record["reward_rate"] <= _FULL_RATE, record


def test_each_reward_rate_row_has_its_own_u32() -> None:
    values = [record["unknown_00"] for record in _records(_REWARD_RATE)]
    assert len(values) == len(set(values))


def test_each_character_has_one_object_point_row() -> None:
    keys = [record["character_key"] for record in _records(_OBJECT_POINT)]
    assert keys and len(keys) == len(set(keys))

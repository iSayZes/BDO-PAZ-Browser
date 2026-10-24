"""Checks of the mount tables in `servant_tables.py` that the shared cases in test_handler.py do not cover."""

from __future__ import annotations

import pytest

from bdo_models import PazEntry
from tests.fixtures import load_binary_fixture

from _common.servant_kind import SERVANT_KIND_NAMES
from .handler import PabrValuesBssHandler
from .layout import ROW_INDEX_FIELD, ValueTable
from .parser import parse_value_table
from .servant_names import servant_kind_text
from .servant_tables import SERVANT_TABLES


_TABLES = {value_table.file_name: value_table for value_table in SERVANT_TABLES}
_HORSE_MAP = _TABLES["horsemap.bss"]
_FANTASY_MIX = _TABLES["servantfantasymix.bss"]
_DELEGATE = _TABLES["delegateservant.bss"]
_TRAINING = _TABLES["vehicletraining.bss"]
_TYPE_NAME = _TABLES["vehicletypename.bss"]
# A rate on the 1,000,000 = 100% scale.
_FULL_RATE = 1_000_000
_HORSE = SERVANT_KIND_NAMES.index("Horse")
_CARRACK = SERVANT_KIND_NAMES.index("Carrack")
# The Horse delegate: character 9909, "Horse" (delegateservant_bss.md).
_DELEGATE_HORSE = 9909
# The vehicletrainingskill.bss skills: Skill, Elegance, Strength (VehicleSkill keys 49 to 51).
_TRAINING_SKILLS = frozenset({49, 50, 51})
_RAINBOW_GEM_FRUIT = 50808


def _records(value_table: ValueTable) -> list[dict]:
    return parse_value_table(load_binary_fixture(value_table.file_name), value_table)


def _handler_records(value_table: ValueTable) -> list[dict]:
    """The records the view shows: the values with their names and icons."""
    path = f"gamecommondata/binary/{value_table.file_name}"
    entry = PazEntry(
        archive_name="",
        internal_path=path,
        offset=0,
        compressed_size=0,
        uncompressed_size=0,
        compression_type=0,
        encryption_type=0,
    )
    return PabrValuesBssHandler(value_table).get_records(load_binary_fixture(value_table.file_name), entry, {})


def _render(value_table: ValueTable, records: list[dict]) -> str:
    handler = PabrValuesBssHandler(value_table)
    handler.lang = "en"
    return handler.render_records_page(records, 0, len(records))


def test_each_horse_map_color_is_stored_twice() -> None:
    records = _records(_HORSE_MAP)
    assert records
    for record in records:
        assert record["map_color_dup"] == record["map_color"], record
        assert record["unknown_03"] == record["unknown_07"] == 0, record


def test_every_horse_map_color_is_unique_and_its_rate_a_share() -> None:
    records = _records(_HORSE_MAP)
    assert len({record["map_color"] for record in records}) == len(records)
    assert all(0 <= record["horse_speed_apply_rate"] <= _FULL_RATE for record in records)


def test_the_horse_map_rate_shows_as_a_percent() -> None:
    html = _render(_HORSE_MAP, [{**_handler_records(_HORSE_MAP)[0], "horse_speed_apply_rate": _FULL_RATE}])
    assert "100%" in html


def test_every_fantasy_mix_pair_makes_one_mythical_horse() -> None:
    records = _records(_FANTASY_MIX)
    assert records
    for record in records:
        assert record["result_character_count"] >= 1, record
        assert 0 < record["upgrade_rate"] <= _FULL_RATE, record
        assert record["male_character_key"] != record["upgrade_character_key"], record


def test_the_delegate_of_each_servant_kind_keeps_its_position() -> None:
    records = _records(_DELEGATE)
    assert [record[ROW_INDEX_FIELD] for record in records] == list(range(len(records)))
    assert records[_HORSE]["character_key"] == _DELEGATE_HORSE
    assert records[_CARRACK]["character_key"]


def test_the_delegate_rows_show_their_servant_kind() -> None:
    assert servant_kind_text(_HORSE) == f"{_HORSE} Horse"
    assert servant_kind_text(999) == "999"
    html = _render(_DELEGATE, _handler_records(_DELEGATE))
    assert f"{_CARRACK} Carrack" in html


def test_each_training_item_repeats_its_key_and_trains_a_training_skill() -> None:
    records = _records(_TRAINING)
    assert records
    for record in records:
        assert record["item_key_dup"] == record["item_key"], record
        assert record["skill_key"] in _TRAINING_SKILLS, record
        assert record["desc_kr"], record
        assert record["unknown_11"] == 0, record


def test_each_training_item_has_its_own_description() -> None:
    records = _records(_TRAINING)
    assert [record["desc_ref"] for record in records] == list(range(len(records)))


def test_the_rainbow_gem_fruit_trains_skill() -> None:
    record = next(record for record in _records(_TRAINING) if record["item_key"] == _RAINBOW_GEM_FRUIT)
    assert record["skill_key"] == min(_TRAINING_SKILLS)
    assert "무지개 보석과일" in record["desc_kr"]


def test_every_vehicle_character_has_one_type_name() -> None:
    records = _records(_TYPE_NAME)
    assert records
    assert len({record["character_key"] for record in records}) == len(records)
    assert all(record["vehicle_type_name"] for record in records)


@pytest.mark.parametrize("value_table", SERVANT_TABLES, ids=lambda table: table.file_name)
def test_every_mount_table_renders(value_table: ValueTable) -> None:
    records = _handler_records(value_table)
    assert _render(value_table, records).count("<tr") >= len(records)

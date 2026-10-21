"""Checks of the PvP tables in `pvp_tables.py` that the shared cases in test_handler.py do not cover."""

from __future__ import annotations

import pytest

from tests.fixtures import load_binary_fixture

from _common.string_hash import ascii_key_hash
from _dbss.instancefield.parser import build_instance_field_name_index
from . import pvp_names
from .parser import parse_value_table
from .pvp_names import action_hash_text, matching_condition_text
from .pvp_tables import PVP_TABLES


_TABLES = {value_table.file_name: value_table for value_table in PVP_TABLES}
# Every Atoraxxion instance field name starts with this (instancefield.dbss).
_ATORAXXION_PREFIX = "Atoraxion_"
# The PABR string-table sheet the banner text key belongs to.
_GAME_SHEET = "GAME"


def _records(name: str) -> list[dict]:
    return parse_value_table(load_binary_fixture(name), _TABLES[name])


def test_each_world_boss_row_repeats_its_character_key() -> None:
    records = _records("worldbossnonpkregion.bss")
    assert records
    for record in records:
        assert record["key"] == record["character_key"]
        assert record["region_keys"], record


def test_each_world_boss_has_one_row() -> None:
    keys = [record["character_key"] for record in _records("worldbossnonpkregion.bss")]
    assert len(keys) == len(set(keys))


def test_the_lost_region_stages_count_up_from_one() -> None:
    indexes = [record["index"] for record in _records("arshasetlostregion.bss")]
    assert indexes == list(range(1, len(indexes) + 1))


def test_each_lost_region_stage_starts_where_the_last_one_ended() -> None:
    records = _records("arshasetlostregion.bss")
    for earlier, later in zip(records, records[1:]):
        assert later["unknown_18"] == earlier["unknown_14"]
        assert later["unknown_14"] < later["unknown_18"]


def test_the_duel_tournament_table_has_one_row() -> None:
    (record,) = _records("sha_dueltournamentoption.bss")
    assert set(record) == {field.name for field in _TABLES["sha_dueltournamentoption.bss"].fields}


def test_an_action_hash_shows_as_hex() -> None:
    # SHA_DuelTournamentOption_Table GameStartAction on client 1784.
    assert action_hash_text(ascii_key_hash("BS_START")) == "0x0E907704"


def test_the_red_battlefield_banner_text_is_a_game_sheet_key() -> None:
    (record,) = _records("redbattlefieldstaticstatusmanager.bss")
    assert record["banner_text_sheet"] == _GAME_SHEET
    assert record["banner_text_key"].startswith("LUA_")
    assert record["banner_texture"] and record["map_texture"]


def test_every_red_battlefield_reward_holds_an_item_and_a_count() -> None:
    (record,) = _records("redbattlefieldstaticstatusmanager.bss")
    for field in ("win_reward_items", "lose_reward_items"):
        assert record[field], field
        assert all(len(entry) == 2 and entry[0] and entry[1] > 0 for entry in record[field])


def test_every_party_matching_key_is_an_atoraxxion_field() -> None:
    (record,) = _records("partymatchingcondition.bss")
    names = build_instance_field_name_index(load_binary_fixture("instancefield.dbss"))
    for field in ("matching_conditions", "unknown_conditions"):
        keys = [entry[0] for entry in record[field]]
        assert keys and len(keys) == len(set(keys)), field
        assert all(names[key].startswith(_ATORAXXION_PREFIX) for key in keys), field


def test_a_matching_condition_shows_its_field_and_ap_dp(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(pvp_names, "instance_field_name", lambda key: "Atoraxion_Desert_EZ")
    assert matching_condition_text([151, 220, 270]) == "151 Atoraxion_Desert_EZ: 220 / 270"


def test_the_matching_congestion_keys_count_up_from_zero() -> None:
    keys = [record["unknown_00"] for record in _records("matchingcongestionstaticstatusmanager.bss")]
    assert keys == list(range(len(keys)))


def test_every_relay_field_has_a_korean_name() -> None:
    records = _records("personalrelayoption.bss")
    assert records
    assert all(record["name_kr"] for record in records)

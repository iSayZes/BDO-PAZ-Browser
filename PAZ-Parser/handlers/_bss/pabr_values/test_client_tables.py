"""Checks of the client, sound and web tables in `client_tables.py` that the shared cases in test_handler.py do not cover."""

from __future__ import annotations

from collections import defaultdict

from tests.fixtures import load_binary_fixture

from .client_names import NO_RGB, rgb_text
from .client_tables import CLIENT_TABLES
from .parser import parse_value_table


_TABLES = {value_table.file_name: value_table for value_table in CLIENT_TABLES}
_CHARACTER_LOBBY = "characterlobby.bss"
_BGM_STATE = "bgmstate.bss"
_BGM_STATE_SA = "bgmstatesa.bss"
_SHA_WEB_URL = "sha_weburl.bss"
_LED_DEVICE = "leddevice.bss"
_BGM_EVENT_PREFIX = "BGM_STATE_"
# Every Shadow Arena event is this prefix and its game condition (bgmstatesa_bss.md, Conditions).
_SA_EVENT_PREFIX = "Set_State_SA_States_"
_SHA_URL_FIELDS = ("record_client", "cash_shop", "replay", "payment")
_SCHEME = "https://"
# The LED animations the client Lua starts: the boss notice and the client start (leddevice_bss.md).
_BOSS_NOTICE_ANIMATION = 12
_LOADING_ANIMATION = 6
_KEYBOARD = 0


def _records(name: str) -> list[dict]:
    return parse_value_table(load_binary_fixture(name), _TABLES[name])


def _unique(values: list[object]) -> bool:
    return bool(values) and len(values) == len(set(values))


def test_every_lobby_character_is_listed_once() -> None:
    assert _unique([record["character_key"] for record in _records(_CHARACTER_LOBBY)])


def test_every_music_state_has_a_key_and_an_event() -> None:
    records = _records(_BGM_STATE)
    assert _unique([record["index"] for record in records])
    assert all(record["event_name"].startswith(_BGM_EVENT_PREFIX) for record in records)


def test_every_shadow_arena_event_names_its_condition() -> None:
    records = _records(_BGM_STATE_SA)
    assert _unique([record["index"] for record in records])
    for record in records:
        assert record["game_condition"], record
        assert record["event_name"] == _SA_EVENT_PREFIX + record["game_condition"], record


def test_the_named_shadow_arena_urls_are_web_addresses() -> None:
    (record,) = _records(_SHA_WEB_URL)
    assert all(record[field].startswith(_SCHEME) for field in _SHA_URL_FIELDS), record


def test_every_animation_has_one_row_per_device_type() -> None:
    records = _records(_LED_DEVICE)
    assert _unique([(record["animation_no"], record["device_type"]) for record in records])
    devices: dict[int, set[int]] = defaultdict(set)
    for record in records:
        devices[record["animation_no"]].add(record["device_type"])
    assert len({frozenset(found) for found in devices.values()}) == 1, devices


def test_a_device_with_an_asus_effect_has_a_colour() -> None:
    for record in _records(_LED_DEVICE):
        assert (record["asus"] == "") == (record["real_rgb"] == NO_RGB), record


def test_the_lua_animations_are_the_boss_notice_and_loading() -> None:
    keyboard = {record["animation_no"]: record for record in _records(_LED_DEVICE) if record["device_type"] == _KEYBOARD}
    assert keyboard[_BOSS_NOTICE_ANIMATION]["razer"] == "BossNotice"
    assert keyboard[_LOADING_ANIMATION]["razer"] == "Loading"


def test_a_colour_shows_as_hex_and_no_colour_as_the_empty_mark() -> None:
    assert rgb_text(0xFF9B29) == "#FF9B29"
    assert rgb_text(0x0000FF) == "#0000FF"
    assert rgb_text(NO_RGB) == "-"

"""Checks of the tables in `ui_tables.py` that the shared cases in test_handler.py do not cover."""

from __future__ import annotations

import math

from tests.fixtures import load_binary_fixture

from _common.contents_group import contents_group_key
from _common.string_hash import ascii_key_hash
from .handler import VALUE_BYTES_FIELD, PabrValuesBssHandler
from .layout import ROW_INDEX_FIELD, ValueTable
from .parser import parse_value_rows, parse_value_table
from .ui_names import QUIZ_ACTION_NAMES, QUIZ_ANSWER_TYPES, quiz_action_text, quiz_answer_text
from .ui_tables import UI_TABLES


_TABLES = {value_table.file_name: value_table for value_table in UI_TABLES}
_QUIZ = _TABLES["quizactionstaticstatus.bss"]
_PHOTO_MODE = _TABLES["photomodestaticstatus.bss"]
_WORLD_MAP = _TABLES["worldmapoptionstaticstatusmanager.bss"]
# The GAME sheet key every photo mode weather name starts with (photomodestaticstatus_bss.md, Presets).
_WEATHER_KEY_PREFIX = "LUA_PHOTOMODE_WEATHER_"
# The territory key every client's first row holds: Balenos (worldmapoptionstaticstatusmanager_bss.md).
_FIRST_TERRITORY_KEY = 0


def _records(value_table: ValueTable) -> list[dict]:
    return parse_value_table(load_binary_fixture(value_table.file_name), value_table)


def _render(value_table: ValueTable, records: list[dict]) -> str:
    handler = PabrValuesBssHandler(value_table)
    handler.lang = "en"
    return handler.render_records_page(records, 0, len(records))


def test_every_quiz_answer_is_o_or_x() -> None:
    answers = [record["answer_type"] for record in _records(_QUIZ)]
    assert answers
    assert len(answers) == len(set(answers))
    assert set(answers) <= {QUIZ_ANSWER_TYPES.index("O"), QUIZ_ANSWER_TYPES.index("X")}


def test_every_quiz_action_is_a_sheet_action() -> None:
    sheet_hashes = {ascii_key_hash(name) for name in QUIZ_ACTION_NAMES}
    for record in _records(_QUIZ):
        assert record["action_hashes"], record
        assert set(record["action_hashes"]) <= sheet_hashes, record


def test_every_quiz_contents_group_is_a_group_key() -> None:
    for record in _records(_QUIZ):
        assert record["contents_group_hashes"], record
        assert all(contents_group_key(group_hash) is not None for group_hash in record["contents_group_hashes"]), record


def test_the_quiz_cells_show_names() -> None:
    assert quiz_answer_text(1) == "1 O"
    assert quiz_action_text(ascii_key_hash("SOCIAL_PutUP_L_Ing")) == "SOCIAL_PutUP_L_Ing"
    assert quiz_action_text(0x0E907704) == "0x0E907704"
    html = _render(_QUIZ, _records(_QUIZ))
    assert "SOCIAL_PutUP_R_Start" in html
    assert "1 O" in html


def test_every_weather_preset_names_a_photo_mode_weather_key() -> None:
    records = _records(_PHOTO_MODE)
    assert records
    assert all(record["weather_name"].startswith(_WEATHER_KEY_PREFIX) for record in records)
    assert len({record["weather_name"] for record in records}) == len(records)


def test_each_weather_preset_keeps_its_position() -> None:
    records = _records(_PHOTO_MODE)
    assert [record[ROW_INDEX_FIELD] for record in records] == list(range(len(records)))


def test_each_world_map_row_stores_its_position_twice() -> None:
    records = _records(_WORLD_MAP)
    assert records[0]["unknown_00"] == _FIRST_TERRITORY_KEY
    for position, record in enumerate(records):
        assert record["unknown_00"] == record["unknown_02"] == position, record
        assert len(record["unknown_04"]) == 3
        assert all(math.isfinite(axis) for axis in record["unknown_04"]), record


def test_the_world_map_view_shows_the_row_bytes() -> None:
    data = load_binary_fixture(_WORLD_MAP.file_name)
    rows = parse_value_rows(data, _WORLD_MAP)
    records = [{**record, VALUE_BYTES_FIELD: raw} for record, raw in rows]
    html = _render(_WORLD_MAP, records)
    assert all(raw in html for _record, raw in rows)

from __future__ import annotations

import struct
from dataclasses import replace
from typing import Any

import pytest

from tests.fixtures import load_binary_fixture
from tests.framework import (
    DeclaredCountTest,
    HandlerCase,
    HandlerResult,
    SchemaTest,
    TargetTest,
    case_id,
    header_count,
    run_case,
)

from _common.pabr_offset import parse_bare_offset_rows
from _common.skill import skill_key
from .parser import FILE_NAME, OFFSET_FILE, parse_weatheractor_records


_SANDSTORM = 27063
# gc::EWeatherType DesertWind.
_DESERT_WIND = 1
_DEBUFF_SANDSTORM = 40337
_CLOUDY_DAY = 45381
_COUNT_OFFSET = 0
_KEY_SIZE = 2
_ROW_SIZE = 75


CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["name"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=[
            "key", "character_key", "name", "title", "skill_key", "skill_no", "skill_level", "skill_name",
            "weather_type", "radius", "rain_amount", "cloud_rate", "damage_max", "damage_radius",
            "damage_radius_rate", "push_pull_speed", "skill_apply_rate",
            "unknown_3e", "unknown_40", "unknown_44", "unknown_4a",
        ]),
        DeclaredCountTest(declared=header_count(offset=_COUNT_OFFSET)),
        # The Sandstorm actor casts Debuff Sandstorm.
        TargetTest(
            col="character_key",
            value=_SANDSTORM,
            expected={
                "name": "Sandstorm",
                "skill_no": _DEBUFF_SANDSTORM,
                "skill_name": "Debuff Sandstorm",
                "weather_type": _DESERT_WIND,
            },
        ),
        TargetTest(col="character_key", value=_CLOUDY_DAY, expected={"name": "Cloudy Day", "skill_no": None}),
    ],
)

OFFSET_CASE = HandlerCase(
    handler_name=OFFSET_FILE,
    data_file=OFFSET_FILE,
    companion_files={},
    loc_file=None,
    uses_loc=False,
    loc_fields=[],
    internal_path=f"gamecommondata/binary/{OFFSET_FILE}",
    tests=[
        SchemaTest(required_keys=["character_key", "offset", "size"]),
        DeclaredCountTest(declared=header_count(offset=_COUNT_OFFSET)),
        TargetTest(col="character_key", value=_SANDSTORM, expected={"size": _ROW_SIZE - _KEY_SIZE}),
    ],
)


def _row(character_key: int, skill: int) -> bytes:
    """A row with the character key at both places and `skill` at +0x22."""
    row = bytearray(_ROW_SIZE)
    struct.pack_into("<HBH", row, 0, character_key, 1, character_key)
    struct.pack_into("<I", row, 0x22, skill)
    return bytes(row)


@pytest.fixture(scope="module")
def weather_actor_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.fixture(scope="module")
def offset_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_OFFSET_RESULT", None)
    if result is None:
        result = run_case(replace(OFFSET_CASE, tests=[]))
        request.module._OFFSET_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_weatheractor_dbss(spec: Any, weather_actor_result: HandlerResult) -> None:
    weather_actor_result.check(spec)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_weatheractoroffset_dbss(spec: Any, offset_result: HandlerResult) -> None:
    offset_result.check(spec)


def test_every_key_is_its_character_key(weather_actor_result: HandlerResult) -> None:
    assert all(r["key"] == r["character_key"] for r in weather_actor_result.records)


def test_every_offset_row_points_past_its_key() -> None:
    main = load_binary_fixture(FILE_NAME)
    for row in parse_bare_offset_rows(load_binary_fixture(OFFSET_FILE)):
        assert row.size == _ROW_SIZE - _KEY_SIZE
        assert (row.offset - _KEY_SIZE - 4) % _ROW_SIZE == 0
        assert struct.unpack_from("<H", main, row.offset - _KEY_SIZE)[0] == row.entry_id


def test_a_small_table_reads_back() -> None:
    sandstorm_skill = skill_key(_DEBUFF_SANDSTORM, 1)
    data = struct.pack("<I", 2) + _row(_SANDSTORM, sandstorm_skill) + _row(_CLOUDY_DAY, 0)
    records = parse_weatheractor_records(data)
    assert [(r["key"], r["character_key"], r["skill_key"]) for r in records] == [
        (_SANDSTORM, _SANDSTORM, sandstorm_skill),
        (_CLOUDY_DAY, _CLOUDY_DAY, 0),
    ]
    assert records[0]["unknown_32"] == "00" * 12


def test_a_short_file_raises() -> None:
    with pytest.raises(ValueError):
        parse_weatheractor_records(struct.pack("<I", 2) + _row(_SANDSTORM, 0))

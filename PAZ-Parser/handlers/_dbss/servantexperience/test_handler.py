from __future__ import annotations

import struct
from collections import defaultdict
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
    UserLanguageTest,
    case_id,
    header_count,
    run_case,
)

from _bss.servantexperiencemaxlevel.parser import FILE_NAME as MAX_LEVEL_FILE, parse_servantexperiencemaxlevel_records
from .parser import FILE_NAME, OFFSET_FILE, parse_servantexperience_records


_ARDUANATT = 9989
# Offset key `level << 16 | character_id` of Arduanatt's level 0 record.
_ARDUANATT_LEVEL_0_KEY = 0 << 16 | _ARDUANATT


CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={OFFSET_FILE: OFFSET_FILE},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["name"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(
            required_keys=[
                "servant_key", "character_id", "name", "level", "exp",
                "max_hp", "max_mp", "max_weight",
                "acceleration", "speed", "turn", "brake", "cannon_stats",
                "growth_dice", "hp_dice", "stamina_dice", "move_dice",
                "max_critical_rate", "max_drop_item_luck", "max_fishing_luck", "max_collection_luck",
                "max_varied_speed",
            ]
        ),
        DeclaredCountTest(declared=header_count()),
        TargetTest(
            col="servant_key",
            value=_ARDUANATT_LEVEL_0_KEY,
            expected={"character_id": _ARDUANATT, "level": 0, "name": "Arduanatt"},
        ),
        UserLanguageTest(fields=["name"]),
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
        SchemaTest(required_keys=["servant_key", "character_id", "level", "offset", "size"]),
        DeclaredCountTest(declared=header_count()),
        TargetTest(col="servant_key", value=_ARDUANATT_LEVEL_0_KEY, expected={"character_id": _ARDUANATT, "level": 0}),
    ],
)


@pytest.fixture(scope="module")
def servant_result(request: Any) -> HandlerResult:
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
def test_servantexperience_dbss(spec: Any, servant_result: HandlerResult) -> None:
    servant_result.check(spec)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_servantexperienceoffset_dbss(spec: Any, offset_result: HandlerResult) -> None:
    offset_result.check(spec)


def test_servant_and_level_pairs_are_unique(servant_result: HandlerResult) -> None:
    keys = [(r["character_id"], r["level"]) for r in servant_result.records]
    assert len(keys) == len(set(keys))


def test_the_offset_key_splits_into_servant_and_level(offset_result: HandlerResult) -> None:
    for record in offset_result.records:
        assert record["servant_key"] == record["level"] << 16 | record["character_id"]


def test_the_max_level_file_holds_each_servants_top_level(servant_result: HandlerResult) -> None:
    top_level: dict[int, int] = defaultdict(int)
    for record in servant_result.records:
        top_level[record["character_id"]] = max(top_level[record["character_id"]], record["level"])
    max_levels = parse_servantexperiencemaxlevel_records(load_binary_fixture(MAX_LEVEL_FILE))
    assert {r["character_id"]: r["max_level"] for r in max_levels} == top_level


def test_every_record_has_six_dice(servant_result: HandlerResult) -> None:
    assert all(len(r["growth_dice"]) == 6 for r in servant_result.records)


_OFFSET_ROW = struct.Struct("<III")


def _offset_table(*rows: tuple[int, int, int]) -> bytes:
    return struct.pack("<I", len(rows)) + b"".join(_OFFSET_ROW.pack(*row) for row in rows)


def test_a_count_that_misses_the_offset_table_raises() -> None:
    with pytest.raises(ValueError, match="count does not match"):
        parse_servantexperience_records(struct.pack("<I", 2), _offset_table((1, 4, 352)))


def test_a_record_whose_key_misses_its_offset_row_raises() -> None:
    record = struct.pack("<HH", 7, 0) + bytes(348)
    with pytest.raises(ValueError, match="starts with servant 7"):
        parse_servantexperience_records(struct.pack("<I", 1) + record, _offset_table((8, 4, 352)))

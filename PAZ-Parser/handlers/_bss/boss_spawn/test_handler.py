from __future__ import annotations

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

from _bss.boss_spawnlevel.parser import FILE_NAME as LEVEL_FILE, parse_boss_spawnlevel_records
from .parser import FILE_NAME

_GIANT_MUDSTER_KEY = 3

CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={LEVEL_FILE: LEVEL_FILE},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["boss_name"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=[
            "key", "max_level", "x", "y", "z", "range", "character_id", "boss_name",
            "unknown_08", "unknown_1c", "unknown_20", "unknown_21", "unknown_26",
            "unknown_28", "unknown_29",
        ]),
        DeclaredCountTest(declared=header_count(offset=4)),
        TargetTest(col="key", value=_GIANT_MUDSTER_KEY, expected={"boss_name": "Giant Mudster"}),
    ],
)


@pytest.fixture(scope="module")
def spawn_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_boss_spawn_bss(spec: Any, spawn_result: HandlerResult) -> None:
    spawn_result.check(spec)


def test_max_level_matches_the_level_entries(spawn_result: HandlerResult) -> None:
    levels: dict[int, int] = {}
    for entry in parse_boss_spawnlevel_records(load_binary_fixture(LEVEL_FILE)):
        levels[entry["boss_key"]] = levels.get(entry["boss_key"], 0) + 1
    for r in spawn_result.records:
        assert levels.get(r["key"]) == r["max_level"]

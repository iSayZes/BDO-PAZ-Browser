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
    UserLanguageTest,
    case_id,
    fixed_rows,
    header_count,
    run_case,
)

from _bss.boss_spawn.parser import FILE_NAME as BOSS_SPAWN_FILE, parse_boss_spawn_records
from _bss.boss_spawnlevel.parser import FILE_NAME as LEVEL_FILE
from .parser import FILE_NAME


_COUNT_SIZE = 4
_ROW_SIZE = 24
# Boss spawn key 8: Gumiho & Duoksini in boss_spawnlevel.bss.
_GUMIHO = 8

CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={LEVEL_FILE: LEVEL_FILE},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["boss_name"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=["boss_spawn_key", "x", "y", "z", "boss_spawn_key_dup", "unknown_14", "boss_name"]),
        DeclaredCountTest(declared=header_count(offset=0)),
        DeclaredCountTest(declared=fixed_rows(_ROW_SIZE, header_size=_COUNT_SIZE)),
        TargetTest(col="boss_spawn_key", value=_GUMIHO, expected={"boss_spawn_key_dup": _GUMIHO}),
        UserLanguageTest(fields=["boss_name"]),
    ],
)


@pytest.fixture(scope="module")
def field_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_guildbossfieldinfo_bss(spec: Any, field_result: HandlerResult) -> None:
    field_result.check(spec)


def test_every_key_is_a_boss_spawn(field_result: HandlerResult) -> None:
    """Each key is a `boss_spawn.bss` key and repeats as `boss_spawn_key_dup`."""
    spawn_keys = {r["key"] for r in parse_boss_spawn_records(load_binary_fixture(BOSS_SPAWN_FILE))}
    missing = [r["boss_spawn_key"] for r in field_result.records if r["boss_spawn_key"] not in spawn_keys]
    assert not missing, missing
    assert all(r["boss_spawn_key"] == r["boss_spawn_key_dup"] for r in field_result.records)

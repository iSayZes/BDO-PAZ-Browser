from __future__ import annotations

from dataclasses import replace
from typing import Any

import pytest

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

_OFFSET_FILE = "employeespawninfooffset.dbss"
_SPAWN_POSITION_FILE = "employeespawnposition.dbss"
_SPAWN_POSITION_OFFSET_FILE = "employeespawnpositionoffset.dbss"
# Sailor Contract Certificate, the item every port town hire takes.
_SAILOR_CONTRACT_CERTIFICATE = 752030

SPAWN_INFO_CASE = HandlerCase(
    handler_name="employeespawninfo.dbss",
    data_file="employeespawninfo.dbss",
    companion_files={
        _OFFSET_FILE: _OFFSET_FILE,
        _SPAWN_POSITION_FILE: _SPAWN_POSITION_FILE,
        _SPAWN_POSITION_OFFSET_FILE: _SPAWN_POSITION_OFFSET_FILE,
    },
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["name", "title", "towns", "hire_item", "accept_text", "refuse_text"],
    internal_path="gamecommondata/binary/employeespawninfo.dbss",
    tests=[
        SchemaTest(required_keys=[
            "character_key", "employee_key", "name", "title", "towns", "spawn_position_keys",
            "respawn_time_s", "hire_item_key", "hire_item_count", "hire_item", "accept_text_ko", "refuse_text_ko",
            "accept_text", "refuse_text",
        ]),
        DeclaredCountTest(declared=header_count()),
        DeclaredCountTest(declared=header_count(companion=_OFFSET_FILE)),
        UserLanguageTest(fields=["accept_text", "refuse_text", "towns"]),
        # Sailor IDs match employeestaticstatus.bss; spawn positions and their
        # towns come from employeespawnposition.dbss.
        TargetTest(col="character_key", value=59053, expected={
            "employee_key": 1,
            "name": "Sailor <Ambitious>",
            "title": "<Ambitious>",
            "spawn_position_keys": [1, 41],
            "towns": ["Velia", "Port Epheria"],
            "hire_item_key": _SAILOR_CONTRACT_CERTIFICATE,
            "hire_item": "Sailor Contract Certificate",
        }),
        TargetTest(col="character_key", value=59054, expected={
            "employee_key": 2,
            "spawn_position_keys": [46],
            "towns": ["Iliya Island"],
        }),
        TargetTest(col="character_key", value=59068, expected={
            "employee_key": 16,
            "spawn_position_keys": [44, 50],
            "towns": ["Port Epheria", "Iliya Island"],
        }),
    ],
)

OFFSET_CASE = HandlerCase(
    handler_name=_OFFSET_FILE,
    data_file=_OFFSET_FILE,
    companion_files={},
    loc_file=None,
    uses_loc=False,
    loc_fields=[],
    internal_path=f"gamecommondata/binary/{_OFFSET_FILE}",
    tests=[
        SchemaTest(required_keys=["character_key", "data_offset", "data_size"]),
        DeclaredCountTest(declared=header_count()),
    ],
)


@pytest.fixture(scope="module")
def spawn_info_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_SPAWN_INFO_RESULT", None)
    if result is None:
        result = run_case(replace(SPAWN_INFO_CASE, tests=[]))
        request.module._SPAWN_INFO_RESULT = result
    return result


@pytest.fixture(scope="module")
def offset_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_OFFSET_RESULT", None)
    if result is None:
        result = run_case(replace(OFFSET_CASE, tests=[]))
        request.module._OFFSET_RESULT = result
    return result


@pytest.mark.parametrize("spec", SPAWN_INFO_CASE.tests, ids=case_id)
def test_employeespawninfo_dbss(spec: Any, spawn_info_result: HandlerResult) -> None:
    spawn_info_result.check(spec)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_employeespawninfooffset_dbss(spec: Any, offset_result: HandlerResult) -> None:
    offset_result.check(spec)

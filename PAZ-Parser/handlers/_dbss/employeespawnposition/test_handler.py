from __future__ import annotations

from dataclasses import replace
from typing import Any

import pytest

from tests.framework import (
    DeclaredCountTest,
    HandlerCase,
    HandlerResult,
    RangeTest,
    SchemaTest,
    TargetTest,
    case_id,
    header_count,
    run_case,
)

from _dbss.employeespawninfo.parser import parse_employeespawninfo_records

_OFFSET_FILE = "employeespawnpositionoffset.dbss"
_SAILOR_FILE = "employeespawninfo.dbss"
_SAILOR_OFFSET_FILE = "employeespawninfooffset.dbss"
# The f32 parts of a unit facing vector.
_UNIT_MIN = -1.0
_UNIT_MAX = 1.0

SPAWN_POSITION_CASE = HandlerCase(
    handler_name="employeespawnposition.dbss",
    data_file="employeespawnposition.dbss",
    companion_files={
        _OFFSET_FILE: _OFFSET_FILE,
        _SAILOR_FILE: _SAILOR_FILE,
        _SAILOR_OFFSET_FILE: _SAILOR_OFFSET_FILE,
    },
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["region"],
    internal_path="gamecommondata/binary/employeespawnposition.dbss",
    tests=[
        SchemaTest(required_keys=[
            "spawn_position_key", "region_key", "region",
            "pos_x", "pos_y", "pos_z", "dir_x", "dir_y", "dir_z", "direction", "sailors",
        ]),
        DeclaredCountTest(declared=header_count()),
        DeclaredCountTest(declared=header_count(companion=_OFFSET_FILE)),
        RangeTest(col="dir_x", min_val=_UNIT_MIN, max_val=_UNIT_MAX),
        RangeTest(col="dir_y", min_val=_UNIT_MIN, max_val=_UNIT_MAX),
        RangeTest(col="dir_z", min_val=_UNIT_MIN, max_val=_UNIT_MAX),
        # Sailors stand in three port towns; region keys are LOC type 17.
        TargetTest(col="spawn_position_key", value=1, expected={"region_key": 5, "region": "Velia"}),
        TargetTest(col="spawn_position_key", value=41, expected={"region_key": 120, "region": "Port Epheria"}),
        TargetTest(col="spawn_position_key", value=46, expected={"region_key": 182, "region": "Iliya Island"}),
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
        SchemaTest(required_keys=["spawn_position_key", "data_offset", "data_size"]),
        DeclaredCountTest(declared=header_count()),
        RangeTest(col="data_size", min_val=34, max_val=34),
    ],
)


@pytest.fixture(scope="module")
def spawn_position_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_SPAWN_POSITION_RESULT", None)
    if result is None:
        result = run_case(replace(SPAWN_POSITION_CASE, tests=[]))
        request.module._SPAWN_POSITION_RESULT = result
    return result


@pytest.fixture(scope="module")
def offset_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_OFFSET_RESULT", None)
    if result is None:
        result = run_case(replace(OFFSET_CASE, tests=[]))
        request.module._OFFSET_RESULT = result
    return result


@pytest.mark.parametrize("spec", SPAWN_POSITION_CASE.tests, ids=case_id)
def test_employeespawnposition_dbss(spec: Any, spawn_position_result: HandlerResult) -> None:
    spawn_position_result.check(spec)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_employeespawnpositionoffset_dbss(spec: Any, offset_result: HandlerResult) -> None:
    offset_result.check(spec)


def test_sailors_list_every_sailor_that_spawns_there(spawn_position_result: HandlerResult) -> None:
    """Each position lists one sailor per employeespawninfo.dbss row whose spawn keys hold it."""
    source = spawn_position_result.source
    sailor_rows = parse_employeespawninfo_records(
        source.file(_SAILOR_FILE), source.file(_SAILOR_OFFSET_FILE)
    )
    listed = {r["spawn_position_key"]: r["sailors"] for r in spawn_position_result.records}
    expected = {
        key: sum(key in row["spawn_position_keys"] for row in sailor_rows) for key in listed
    }

    assert "Sailor <Ambitious>" in listed[1]
    assert {key: len(names) for key, names in listed.items()} == expected

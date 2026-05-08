from __future__ import annotations

from dataclasses import replace
from typing import Any

import pytest

from tests.framework import CountTest, HandlerCase, HandlerResult, PosTest, SchemaTest, TargetTest, case_id, run_case


def _spawn_type_record(record: dict) -> dict:
    mapped = dict(record)
    mapped["active_flags"] = [idx for idx, value in enumerate(record["flags"]) if value]
    return mapped


SPAWN_TYPE_CASE = HandlerCase(
    handler_name="characterspawntype.dbss",
    data_file="characterspawntype.dbss",
    companion_files={"characterspawntypeoffset.dbss": "characterspawntypeoffset.dbss"},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["Name"],
    internal_path="gamecommondata/binary/characterspawntype.dbss",
    record_mapper=_spawn_type_record,
    tests=[
        SchemaTest(required_keys=["entity_id", "name_en", "active_flags"]),
        CountTest(expected=24017),
        PosTest(pos=0, expected={"entity_id": 47759, "name_en": "Edania Merchant", "active_flags": [2]}),
        PosTest(pos=-1, expected={"entity_id": 82176, "name_en": "", "active_flags": []}),
    ],
)

OFFSET_CASE = HandlerCase(
    handler_name="characterspawntypeoffset.dbss",
    data_file="characterspawntypeoffset.dbss",
    companion_files={},
    loc_file=None,
    uses_loc=False,
    loc_fields=[],
    internal_path="gamecommondata/binary/characterspawntypeoffset.dbss",
    tests=[
        SchemaTest(required_keys=["id_low16", "offset", "size"]),
        CountTest(expected=24017),
        PosTest(pos=0, expected={"id_low16": 47759, "offset": 4, "size": 48}),
        PosTest(pos=-1, expected={"id_low16": 16640, "offset": 1152772, "size": 48}),
    ],
)


@pytest.fixture(scope="module")
def spawn_type_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_SPAWN_TYPE_RESULT", None)
    if result is None:
        result = run_case(replace(SPAWN_TYPE_CASE, tests=[]))
        request.module._SPAWN_TYPE_RESULT = result
    return result


@pytest.fixture(scope="module")
def offset_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_OFFSET_RESULT", None)
    if result is None:
        result = run_case(replace(OFFSET_CASE, tests=[]))
        request.module._OFFSET_RESULT = result
    return result


@pytest.mark.parametrize("spec", SPAWN_TYPE_CASE.tests, ids=case_id)
def test_characterspawntype_dbss(spec: Any, spawn_type_result: HandlerResult) -> None:
    spec.check(spawn_type_result.records)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_characterspawntypeoffset_dbss(spec: Any, offset_result: HandlerResult) -> None:
    spec.check(offset_result.records)

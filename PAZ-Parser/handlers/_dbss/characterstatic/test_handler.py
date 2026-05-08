from __future__ import annotations

from dataclasses import replace
from typing import Any

import pytest

from tests.framework import CountTest, HandlerCase, HandlerResult, PosTest, SchemaTest, TargetTest, case_id, run_case


STATIC_CASE = HandlerCase(
    handler_name="characterstatic.dbss",
    data_file="characterstatic.dbss",
    companion_files={"characterstaticoffset.dbss": "characterstaticoffset.dbss"},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["Name"],
    internal_path="gamecommondata/binary/characterstatic.dbss",
    tests=[
        SchemaTest(required_keys=["character_id", "name_en", "script", "knowledge_id", "payload_size", "unknown_type"]),
        CountTest(expected=24017),
        PosTest(
            pos=0,
            expected={
                "character_id": 47759,
                "name_en": "Edania Merchant",
                "script": "getknowledge(14469);",
                "knowledge_id": 14469,
                "payload_size": 586,
                "unknown_type": 2,
            },
        ),
        TargetTest(
            col="character_id",
            value=16640,
            expected={"name_en": "Dev Plant210", "script": "", "knowledge_id": None, "payload_size": 511, "unknown_type": 8},
        ),
    ],
)

OFFSET_CASE = HandlerCase(
    handler_name="characterstaticoffset.dbss",
    data_file="characterstaticoffset.dbss",
    companion_files={},
    loc_file=None,
    uses_loc=False,
    loc_fields=[],
    internal_path="gamecommondata/binary/characterstaticoffset.dbss",
    tests=[
        SchemaTest(required_keys=["id_low16", "offset", "size"]),
        CountTest(expected=24017),
        PosTest(pos=0, expected={"id_low16": 47759, "offset": 6, "size": 586}),
        PosTest(pos=-1, expected={"id_low16": 16640, "offset": 13563768, "size": 511}),
    ],
)


@pytest.fixture(scope="module")
def static_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_STATIC_RESULT", None)
    if result is None:
        result = run_case(replace(STATIC_CASE, tests=[]))
        request.module._STATIC_RESULT = result
    return result


@pytest.fixture(scope="module")
def offset_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_OFFSET_RESULT", None)
    if result is None:
        result = run_case(replace(OFFSET_CASE, tests=[]))
        request.module._OFFSET_RESULT = result
    return result


@pytest.mark.parametrize("spec", STATIC_CASE.tests, ids=case_id)
def test_characterstatic_dbss(spec: Any, static_result: HandlerResult) -> None:
    spec.check(static_result.records)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_characterstaticoffset_dbss(spec: Any, offset_result: HandlerResult) -> None:
    spec.check(offset_result.records)

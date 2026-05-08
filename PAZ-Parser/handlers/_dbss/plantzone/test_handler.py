from __future__ import annotations

from dataclasses import replace
from typing import Any

import pytest

from tests.framework import CountTest, HandlerCase, HandlerResult, PosTest, SchemaTest, TargetTest, case_id, run_case


PLANTZONE_CASE = HandlerCase(
    handler_name="plantzone.dbss",
    data_file="plantzone.dbss",
    companion_files={"plantzoneoffset.dbss": "plantzoneoffset.dbss"},
    loc_file=None,
    uses_loc=False,
    loc_fields=[],
    internal_path="gamecommondata/binary/plantzone.dbss",
    tests=[
        SchemaTest(required_keys=["record_id", "variant", "linked_id", "values", "data_size"]),
        CountTest(expected=394),
        PosTest(pos=0, expected={"record_id": 1030, "variant": 4, "linked_id": 2017, "values": [0, 1, 2, 3, 4, 5]}),
        PosTest(pos=-1, expected={"record_id": 405, "variant": 4, "linked_id": 914, "data_size": 37}),
    ],
)

OFFSET_CASE = HandlerCase(
    handler_name="plantzoneoffset.dbss",
    data_file="plantzoneoffset.dbss",
    companion_files={},
    loc_file=None,
    uses_loc=False,
    loc_fields=[],
    internal_path="gamecommondata/binary/plantzoneoffset.dbss",
    tests=[
        SchemaTest(required_keys=["record_id", "data_offset", "data_size"]),
        CountTest(expected=394),
        PosTest(pos=0, expected={"record_id": 1030, "data_offset": 8304, "data_size": 37}),
        PosTest(pos=-1, expected={"record_id": 405, "data_offset": 14335, "data_size": 37}),
    ],
)


@pytest.fixture(scope="module")
def plantzone_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_PLANTZONE_RESULT", None)
    if result is None:
        result = run_case(replace(PLANTZONE_CASE, tests=[]))
        request.module._PLANTZONE_RESULT = result
    return result


@pytest.fixture(scope="module")
def offset_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_OFFSET_RESULT", None)
    if result is None:
        result = run_case(replace(OFFSET_CASE, tests=[]))
        request.module._OFFSET_RESULT = result
    return result


@pytest.mark.parametrize("spec", PLANTZONE_CASE.tests, ids=case_id)
def test_plantzone_dbss(spec: Any, plantzone_result: HandlerResult) -> None:
    spec.check(plantzone_result.records)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_plantzoneoffset_dbss(spec: Any, offset_result: HandlerResult) -> None:
    spec.check(offset_result.records)

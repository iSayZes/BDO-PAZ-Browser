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


def _employee_name_record(record: dict) -> dict:
    return {
        "EmployeeNameId": record["employee_name_id"],
        "Name": record.get("name_en") or record["name_kr"],
        "KoreanName": record["name_kr"],
        "CharCount": record["char_count"],
        "Unknown08": record["unknown_08"],
        "UnknownAfterName": record["unknown_after_name"],
        "DataSize": record["data_size"],
    }


EMPLOYEENAME_CASE = HandlerCase(
    handler_name="employeename.dbss",
    data_file="employeename.dbss",
    companion_files={"employeenameoffset.dbss": "employeenameoffset.dbss"},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["Name"],
    internal_path="gamecommondata/binary/employeename.dbss",
    record_mapper=_employee_name_record,
    tests=[
        SchemaTest(required_keys=["EmployeeNameId", "Name", "KoreanName", "CharCount", "Unknown08", "UnknownAfterName", "DataSize"]),
        DeclaredCountTest(declared=header_count()),
        RangeTest(col="Unknown08", min_val=0, max_val=0),
        RangeTest(col="UnknownAfterName", min_val=0, max_val=0),
        TargetTest(col="EmployeeNameId", value=47, expected={"Name": "Guile", "KoreanName": "가일", "CharCount": 2}),
        TargetTest(col="EmployeeNameId", value=34, expected={"Name": "Pilgrave", "KoreanName": "필그레이브"}),
        TargetTest(col="EmployeeNameId", value=60, expected={"Name": "Tails"}),
    ],
)

OFFSET_CASE = HandlerCase(
    handler_name="employeenameoffset.dbss",
    data_file="employeenameoffset.dbss",
    companion_files={},
    loc_file=None,
    uses_loc=False,
    loc_fields=[],
    internal_path="gamecommondata/binary/employeenameoffset.dbss",
    tests=[
        SchemaTest(required_keys=["employee_name_id", "data_offset", "data_size"]),
        DeclaredCountTest(declared=header_count()),
        # The first record follows the 4-byte count; a 2-character name takes 16 + 2 * 2 bytes.
        TargetTest(col="employee_name_id", value=47, expected={"data_offset": 4, "data_size": 20}),
    ],
)


@pytest.fixture(scope="module")
def employeename_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_EMPLOYEENAME_RESULT", None)
    if result is None:
        result = run_case(replace(EMPLOYEENAME_CASE, tests=[]))
        request.module._EMPLOYEENAME_RESULT = result
    return result


@pytest.fixture(scope="module")
def offset_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_OFFSET_RESULT", None)
    if result is None:
        result = run_case(replace(OFFSET_CASE, tests=[]))
        request.module._OFFSET_RESULT = result
    return result


@pytest.mark.parametrize("spec", EMPLOYEENAME_CASE.tests, ids=case_id)
def test_employeename_dbss(spec: Any, employeename_result: HandlerResult) -> None:
    employeename_result.check(spec)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_employeenameoffset_dbss(spec: Any, offset_result: HandlerResult) -> None:
    offset_result.check(spec)

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
    case_id,
    fixed_rows,
    header_count,
    run_case,
)

from .parser import FILE_NAME


_COUNT_SIZE = 4
_ROW_SIZE = 22
_BYTE_BITS = 8
_BYTE_MASK = 0xFF
# Key 0x104: second byte 1, first byte 4.
_KEY_0X104 = 0x104

CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=False,
    loc_fields=[],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=[
            "key", "unknown_04", "unknown_08", "unknown_0c", "unknown_10", "unknown_14", "unknown_15",
        ]),
        DeclaredCountTest(declared=header_count(offset=0)),
        DeclaredCountTest(declared=fixed_rows(_ROW_SIZE, header_size=_COUNT_SIZE)),
        TargetTest(col="key", value=_KEY_0X104, expected={"unknown_14": 1, "unknown_15": 4}),
    ],
)


@pytest.fixture(scope="module")
def zone_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_monsterbuffzone_bss(spec: Any, zone_result: HandlerResult) -> None:
    zone_result.check(spec)


def test_tail_bytes_repeat_the_key(zone_result: HandlerResult) -> None:
    for record in zone_result.records:
        assert record["key"] == record["unknown_14"] << _BYTE_BITS | record["unknown_15"]
        assert record["unknown_15"] == record["key"] & _BYTE_MASK

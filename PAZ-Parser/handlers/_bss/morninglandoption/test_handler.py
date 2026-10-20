from __future__ import annotations

import struct
from dataclasses import replace
from typing import Any

import pytest

from tests.framework import DeclaredCountTest, HandlerCase, HandlerResult, SchemaTest, case_id, run_case

from .parser import FILE_NAME, parse_morning_land_option


# The file holds one set of values and no count, so it is always one record.
CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file=None,
    uses_loc=False,
    loc_fields=[],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=["stat_reset_cost", "light_orb_reset_cost", "unknown_10"]),
        DeclaredCountTest(declared=lambda _source: 1),
    ],
)


@pytest.fixture(scope="module")
def morninglandoption_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_morninglandoption_bss(spec: Any, morninglandoption_result: HandlerResult) -> None:
    morninglandoption_result.check(spec)


def test_values_read_as_two_u64_and_a_byte() -> None:
    data = struct.pack("<QQB", 7, 1 << 40, 3)
    assert parse_morning_land_option(data) == {
        "stat_reset_cost": 7,
        "light_orb_reset_cost": 1 << 40,
        "unknown_10": 3,
    }


@pytest.mark.parametrize("size", [16, 18, 0])
def test_a_file_of_another_size_raises(size: int) -> None:
    with pytest.raises(ValueError, match="expected 17 bytes"):
        parse_morning_land_option(bytes(size))

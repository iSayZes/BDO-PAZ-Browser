from __future__ import annotations

import struct
from dataclasses import replace
from typing import Any

import pytest

from tests.framework import DeclaredCountTest, HandlerCase, HandlerResult, SchemaTest, case_id, run_case

from _bss.blackspiritchangeformcondition.parser import FILE_NAME, parse_blackspiritchangeformcondition_records


# The file is one condition, so one record.
_ONE_RECORD = 1

CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file=None,
    uses_loc=False,
    loc_fields=[],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=["change_condition"]),
        DeclaredCountTest(declared=lambda _source: _ONE_RECORD),
    ],
)


@pytest.fixture(scope="module")
def condition_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_blackspiritchangeformcondition_bss(spec: Any, condition_result: HandlerResult) -> None:
    condition_result.check(spec)


def test_condition_is_a_script(condition_result: HandlerResult) -> None:
    # Checks the str16 reading: the text ends with the `;` every condition call closes with.
    assert condition_result.records[0]["change_condition"].endswith(";")


def test_parse_rejects_bytes_after_the_text() -> None:
    data = struct.pack("<Q", 2) + "a;".encode("utf-16-le") + b"\x00"
    with pytest.raises(ValueError):
        parse_blackspiritchangeformcondition_records(data)


def test_parse_rejects_a_text_past_the_file() -> None:
    with pytest.raises(ValueError):
        parse_blackspiritchangeformcondition_records(struct.pack("<Q", 40))

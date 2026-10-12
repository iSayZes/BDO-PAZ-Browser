from __future__ import annotations

import struct
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

from .parser import FILE_NAME, parse_servantexperiencemaxlevel_records


_ARDUANATT = 9989


CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["name"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=["character_id", "name", "max_level"]),
        DeclaredCountTest(declared=header_count()),
        TargetTest(col="character_id", value=_ARDUANATT, expected={"name": "Arduanatt"}),
        UserLanguageTest(fields=["name"]),
    ],
)


@pytest.fixture(scope="module")
def max_level_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_servantexperiencemaxlevel_bss(spec: Any, max_level_result: HandlerResult) -> None:
    max_level_result.check(spec)


def test_character_ids_are_unique(max_level_result: HandlerResult) -> None:
    ids = [r["character_id"] for r in max_level_result.records]
    assert len(ids) == len(set(ids))


def test_rows_that_do_not_fill_the_file_raise() -> None:
    with pytest.raises(ValueError, match="declares 2 rows"):
        parse_servantexperiencemaxlevel_records(struct.pack("<IHH", 2, 9989, 100))

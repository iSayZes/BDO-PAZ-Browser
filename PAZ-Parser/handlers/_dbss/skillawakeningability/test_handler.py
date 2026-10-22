from __future__ import annotations

import struct
from dataclasses import replace
from typing import Any

import pytest

from tests.fixtures import load_binary_fixture
from tests.framework import (
    DeclaredCountTest,
    HandlerCase,
    HandlerResult,
    SchemaTest,
    TargetTest,
    UserLanguageTest,
    case_id,
    fixed_rows,
    header_count,
    run_case,
)
from tests.offset_rows import offset_row_problems

from .parser import FILE_NAME, OFFSET_FILE, parse_skillawakeningabilityoffset_rows


_COUNT_SIZE = 4
_OFFSET_ROW_SIZE = 12
# The index points past the row's u32 ability index, at `ability_index_dup`.
_KEY = struct.Struct("<I")
# Ability indexes run from 1; LOC type 33 names each.
_FIRST_ABILITY = 1

CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["description"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=[
            "ability_index", "ability_index_dup", "buff_id", "description_kr", "unknown_description_kr_00",
            "buff", "description",
        ]),
        DeclaredCountTest(declared=header_count(offset=0)),
        TargetTest(col="ability_index", value=_FIRST_ABILITY, expected={"ability_index_dup": _FIRST_ABILITY}),
        UserLanguageTest(fields=["description"]),
    ],
)

OFFSET_CASE = HandlerCase(
    handler_name=OFFSET_FILE,
    data_file=OFFSET_FILE,
    companion_files={},
    loc_file=None,
    uses_loc=False,
    loc_fields=[],
    internal_path=f"gamecommondata/binary/{OFFSET_FILE}",
    tests=[
        SchemaTest(required_keys=["ability_index", "data_offset", "data_size"]),
        DeclaredCountTest(declared=header_count(offset=0)),
        DeclaredCountTest(declared=fixed_rows(_OFFSET_ROW_SIZE, header_size=_COUNT_SIZE)),
    ],
)


@pytest.fixture(scope="module")
def ability_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.fixture(scope="module")
def offset_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_OFFSET_RESULT", None)
    if result is None:
        result = run_case(replace(OFFSET_CASE, tests=[]))
        request.module._OFFSET_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_skillawakeningability_dbss(spec: Any, ability_result: HandlerResult) -> None:
    ability_result.check(spec)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_skillawakeningabilityoffset_dbss(spec: Any, offset_result: HandlerResult) -> None:
    offset_result.check(spec)


def test_index_dup_repeats_the_index(ability_result: HandlerResult) -> None:
    mismatched = [r["ability_index"] for r in ability_result.records if r["ability_index_dup"] != r["ability_index"]]
    assert not mismatched, mismatched


def test_every_row_names_a_buff(ability_result: HandlerResult) -> None:
    missing = [r["ability_index"] for r in ability_result.records if not r["buff_id"]]
    assert not missing, missing


def test_offset_rows_point_at_their_rows() -> None:
    rows = parse_skillawakeningabilityoffset_rows(load_binary_fixture(OFFSET_FILE))
    problems = offset_row_problems(load_binary_fixture(FILE_NAME), rows, _KEY, lead=_KEY.size)
    assert not problems, problems

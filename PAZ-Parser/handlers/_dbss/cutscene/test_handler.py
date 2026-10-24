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
    case_id,
    fixed_rows,
    header_count,
    run_case,
)
from tests.offset_rows import offset_row_problems

from _common.string_hash import key_hash
from .parser import FILE_NAME, OFFSET_FILE, parse_cutsceneoffset_rows


_COUNT_SIZE = 4
_KEY_PREFIX_SIZE = 4
_OFFSET_ROW_SIZE = 12
# Donat's diary in the Glish ruins; the same row on clients 1784 and 3482
# and in the client 1784 CutScene_Table sheet.
_DIARY_FILE = "CS_Serendia_01_Diary_0001.pas"

CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file=None,
    uses_loc=False,
    loc_fields=[],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(
            required_keys=["cutscene_key", "file_name", "cutscene_name_kr", "description_kr", "unknown_description_00"],
        ),
        DeclaredCountTest(declared=header_count(offset=0)),
        TargetTest(col="cutscene_key", value=key_hash(_DIARY_FILE), expected={"file_name": _DIARY_FILE}),
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
        SchemaTest(required_keys=["cutscene_key", "data_offset", "data_size"]),
        DeclaredCountTest(declared=header_count(offset=0)),
        DeclaredCountTest(declared=fixed_rows(_OFFSET_ROW_SIZE, header_size=_COUNT_SIZE)),
    ],
)


@pytest.fixture(scope="module")
def cutscene_result(request: Any) -> HandlerResult:
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
def test_cutscene_dbss(spec: Any, cutscene_result: HandlerResult) -> None:
    cutscene_result.check(spec)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_cutsceneoffset_dbss(spec: Any, offset_result: HandlerResult) -> None:
    offset_result.check(spec)


def test_every_key_is_the_hash_of_its_file_name(cutscene_result: HandlerResult) -> None:
    wrong = [r["file_name"] for r in cutscene_result.records if r["cutscene_key"] != key_hash(r["file_name"])]
    assert not wrong, wrong


def test_every_file_is_a_pas_cutscene(cutscene_result: HandlerResult) -> None:
    wrong = [r["file_name"] for r in cutscene_result.records if not r["file_name"].endswith(".pas")]
    assert not wrong, wrong


def test_offset_rows_point_past_the_key_prefix() -> None:
    rows = parse_cutsceneoffset_rows(load_binary_fixture(OFFSET_FILE))
    problems = offset_row_problems(
        load_binary_fixture(FILE_NAME), rows, struct.Struct("<I"), lead=_KEY_PREFIX_SIZE
    )
    assert not problems, problems

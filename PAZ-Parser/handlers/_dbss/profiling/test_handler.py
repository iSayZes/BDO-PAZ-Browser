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

from .parser import FILE_NAME, OFFSET_FILE, parse_profilingoffset_rows


_COUNT_SIZE = 4
_OFFSET_ROW_SIZE = 10
# Key 1 opens with the message on Rani, the Shai potion seller of Balenos;
# the same first message on clients 1784 and 3482 and in the client 1784
# Profiling sheet (DialogKey Profiling_Balenos_01).
_BALENOS = 1
_RANI = "라니"

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
            required_keys=[
                "profiling_key", "infos", "unknown_infos_00", "info_count", "subjects", "subjects_text",
                "messages_text", "execute_text",
            ],
        ),
        DeclaredCountTest(declared=header_count(offset=0)),
        TargetTest(col="profiling_key", value=_BALENOS, expected={"profiling_key": _BALENOS}),
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
        SchemaTest(required_keys=["profiling_key", "data_offset", "data_size"]),
        DeclaredCountTest(declared=header_count(offset=0)),
        DeclaredCountTest(declared=fixed_rows(_OFFSET_ROW_SIZE, header_size=_COUNT_SIZE)),
    ],
)


@pytest.fixture(scope="module")
def profiling_result(request: Any) -> HandlerResult:
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
def test_profiling_dbss(spec: Any, profiling_result: HandlerResult) -> None:
    profiling_result.check(spec)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_profilingoffset_dbss(spec: Any, offset_result: HandlerResult) -> None:
    offset_result.check(spec)


def test_every_message_names_its_subject(profiling_result: HandlerResult) -> None:
    """Each message opens with `[<subject>]`, so a misread string start loses it."""
    missing = [
        record["profiling_key"]
        for record in profiling_result.records
        for subject in record["subjects"]
        if not subject
    ]
    assert not missing, missing


def test_balenos_opens_with_rani(profiling_result: HandlerResult) -> None:
    record = next(r for r in profiling_result.records if r["profiling_key"] == _BALENOS)
    assert record["subjects"][0] == _RANI


def test_offset_rows_point_at_their_rows() -> None:
    rows = parse_profilingoffset_rows(load_binary_fixture(OFFSET_FILE))
    problems = offset_row_problems(load_binary_fixture(FILE_NAME), rows, struct.Struct("<H"))
    assert not problems, problems

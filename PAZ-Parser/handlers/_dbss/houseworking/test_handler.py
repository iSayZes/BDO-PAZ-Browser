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

from .parser import FILE_NAME, OFFSET_FILE, parse_houseworking_records, parse_houseworkingoffset_rows


_COUNT_SIZE = 4
_OFFSET_ROW_SIZE = 10
# The u16 row key closes every row.
_KEY_FROM_END = 2
_METAL_PROCESSING_TOOL = 1001

CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["name"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=["install_object_key", "works", "name", "works_text"]),
        DeclaredCountTest(declared=header_count(offset=0)),
        TargetTest(col="install_object_key", value=_METAL_PROCESSING_TOOL, expected={"name": "Metal Processing Tool"}),
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
        SchemaTest(required_keys=["install_object_key", "data_offset", "data_size"]),
        DeclaredCountTest(declared=header_count(offset=0)),
        DeclaredCountTest(declared=fixed_rows(_OFFSET_ROW_SIZE, header_size=_COUNT_SIZE)),
        TargetTest(
            col="install_object_key",
            value=_METAL_PROCESSING_TOOL,
            expected={"install_object_key": _METAL_PROCESSING_TOOL},
        ),
    ],
)


@pytest.fixture(scope="module")
def working_result(request: Any) -> HandlerResult:
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
def test_houseworking_dbss(spec: Any, working_result: HandlerResult) -> None:
    working_result.check(spec)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_houseworkingoffset_dbss(spec: Any, offset_result: HandlerResult) -> None:
    offset_result.check(spec)


def test_every_tool_has_a_work_with_an_exchange(working_result: HandlerResult) -> None:
    for record in working_result.records:
        assert record["works"], record["install_object_key"]
        assert all(work["exchange_key"] and work["unit_production"] for work in record["works"])


def test_offset_rows_point_at_their_rows() -> None:
    rows = parse_houseworkingoffset_rows(load_binary_fixture(OFFSET_FILE))
    problems = offset_row_problems(load_binary_fixture(FILE_NAME), rows, struct.Struct("<H"), key_from_end=_KEY_FROM_END)
    assert not problems, problems


def _row(works: list[tuple[int, int]], key: int) -> bytes:
    body = struct.pack("<I", len(works)) + b"".join(struct.pack("<II", *work) for work in works)
    return body + struct.pack("<H", key)


def test_parse_reads_the_key_after_the_works() -> None:
    data = struct.pack("<I", 2) + _row([(5001, 3)], 1001) + _row([(5001, 3), (5002, 1)], 1002)

    records = parse_houseworking_records(data)

    assert [r["install_object_key"] for r in records] == [1001, 1002]
    assert records[1]["works"] == [
        {"exchange_key": 5001, "unit_production": 3},
        {"exchange_key": 5002, "unit_production": 1},
    ]


def test_parse_rejects_a_work_list_past_the_file() -> None:
    with pytest.raises(ValueError):
        parse_houseworking_records(struct.pack("<I", 1) + struct.pack("<I", 2) + struct.pack("<II", 5001, 3))

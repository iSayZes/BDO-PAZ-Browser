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
    case_id,
    fixed_rows,
    header_count,
    run_case,
)
from tests.offset_rows import offset_row_problems

from _common.pabr_offset import PabrOffsetRow
from _dbss.emoticon.parser import FILE_NAME as EMOTICON_FILE, parse_emoticon_records
from .parser import FILE_NAME, OFFSET_FILE, parse_emoticonpackage_records, parse_emoticonpackageoffset_records


_COUNT_SIZE = 4
_OFFSET_ROW_SIZE = 16

CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={EMOTICON_FILE: EMOTICON_FILE},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["emoticons_text"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(
            required_keys=["package_key", "unknown_04", "name_kr", "emoticons", "emoticon_count", "emoticons_text"],
        ),
        DeclaredCountTest(declared=header_count(offset=0)),
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
        SchemaTest(required_keys=["package_key", "unknown_04", "data_offset", "data_size"]),
        DeclaredCountTest(declared=header_count(offset=0)),
        DeclaredCountTest(declared=fixed_rows(_OFFSET_ROW_SIZE, header_size=_COUNT_SIZE)),
    ],
)


@pytest.fixture(scope="module")
def package_result(request: Any) -> HandlerResult:
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
def test_emoticonpackage_dbss(spec: Any, package_result: HandlerResult) -> None:
    package_result.check(spec)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_emoticonpackageoffset_dbss(spec: Any, offset_result: HandlerResult) -> None:
    offset_result.check(spec)


def test_offset_rows_point_at_their_rows() -> None:
    rows = [
        PabrOffsetRow(row["package_key"], row["data_offset"], row["data_size"])
        for row in parse_emoticonpackageoffset_records(load_binary_fixture(OFFSET_FILE))
    ]
    problems = offset_row_problems(load_binary_fixture(FILE_NAME), rows, struct.Struct("<I"))
    assert not problems, problems


def test_every_package_lists_known_emoticons() -> None:
    emoticon_keys = {row["emoticon_key"] for row in parse_emoticon_records(load_binary_fixture(EMOTICON_FILE))}
    for record in parse_emoticonpackage_records(load_binary_fixture(FILE_NAME)):
        assert record["emoticons"], record["package_key"]
        assert all(emoticon["emoticon_key"] in emoticon_keys for emoticon in record["emoticons"]), record["package_key"]


def test_the_view_names_each_emoticon(package_result: HandlerResult) -> None:
    first = package_result.records[0]
    assert first["emoticon_count"] == len(first["emoticons"])
    assert all(label.endswith(")") for _path, label in first["_emoticon_entries"])


def test_parse_reads_the_emoticon_list() -> None:
    name = "무제한"
    row = (
        struct.pack("<II", 3, 0) + struct.pack("<Q", len(name)) + name.encode("utf-16-le")
        + struct.pack("<I", 2) + struct.pack("<IIII", 14, 0, 15, 0)
    )

    (record,) = parse_emoticonpackage_records(struct.pack("<I", 1) + row)

    assert record["package_key"] == 3
    assert [emoticon["emoticon_key"] for emoticon in record["emoticons"]] == [14, 15]

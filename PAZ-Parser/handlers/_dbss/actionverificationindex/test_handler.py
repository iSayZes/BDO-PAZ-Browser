from __future__ import annotations

import struct
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
    fixed_rows,
    header_count,
    run_case,
)

from _dbss.actionverificationindex.parser import (
    parse_actionverificationindex_records,
    parse_actionverificationindexoffset_records,
)


_OFFSET_FILE = "actionverificationindexoffset.dbss"
_HEADER_SIZE = 4
_KEY_PREFIX_SIZE = 1
_PAYLOAD_SIZE = 8
_RECORD_SIZE = _KEY_PREFIX_SIZE + _PAYLOAD_SIZE
_OFFSET_ROW_SIZE = 12
# The server loader rejects a class type of 101 or more.
_MAX_CLASS_TYPE = 100
_JORDINE = 52

CASE = HandlerCase(
    handler_name="actionverificationindex.dbss",
    data_file="actionverificationindex.dbss",
    companion_files={_OFFSET_FILE: _OFFSET_FILE},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["class_name"],
    internal_path="gamecommondata/binary/actionverificationindex.dbss",
    tests=[
        SchemaTest(required_keys=["class_type", "class_name", "unknown_01"]),
        DeclaredCountTest(declared=header_count()),
        DeclaredCountTest(declared=header_count(companion=_OFFSET_FILE)),
        # The header count fills the file exactly.
        DeclaredCountTest(declared=fixed_rows(_RECORD_SIZE, header_size=_HEADER_SIZE)),
        RangeTest(col="class_type", min_val=0, max_val=_MAX_CLASS_TYPE),
        TargetTest(col="class_type", value=_JORDINE, expected={"class_name": "Jordine"}),
    ],
)

OFFSET_CASE = HandlerCase(
    handler_name=_OFFSET_FILE,
    data_file=_OFFSET_FILE,
    companion_files={},
    loc_file=None,
    uses_loc=False,
    loc_fields=[],
    internal_path=f"gamecommondata/binary/{_OFFSET_FILE}",
    tests=[
        SchemaTest(required_keys=["class_type", "data_offset", "data_size"]),
        DeclaredCountTest(declared=header_count()),
        DeclaredCountTest(declared=fixed_rows(_OFFSET_ROW_SIZE, header_size=_HEADER_SIZE)),
        RangeTest(col="data_size", min_val=_PAYLOAD_SIZE, max_val=_PAYLOAD_SIZE),
    ],
)


@pytest.fixture(scope="module")
def actionverificationindex_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.fixture(scope="module")
def actionverificationindexoffset_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_OFFSET_RESULT", None)
    if result is None:
        result = run_case(replace(OFFSET_CASE, tests=[]))
        request.module._OFFSET_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_actionverificationindex_dbss(spec: Any, actionverificationindex_result: HandlerResult) -> None:
    actionverificationindex_result.check(spec)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_actionverificationindexoffset_dbss(
    spec: Any,
    actionverificationindexoffset_result: HandlerResult,
) -> None:
    actionverificationindexoffset_result.check(spec)


def test_class_types_are_unique(actionverificationindex_result: HandlerResult) -> None:
    class_types = [record["class_type"] for record in actionverificationindex_result.records]
    assert len(class_types) == len(set(class_types))


def test_offset_rows_point_past_the_key_prefix(actionverificationindex_result: HandlerResult) -> None:
    offset_rows = parse_actionverificationindexoffset_records(
        actionverificationindex_result.source.file(_OFFSET_FILE)
    )
    starts = sorted(row["data_offset"] for row in offset_rows)
    expected = [
        _HEADER_SIZE + index * _RECORD_SIZE + _KEY_PREFIX_SIZE for index in range(len(offset_rows))
    ]
    assert starts == expected


def _first_payload(result: HandlerResult) -> tuple[bytearray, bytes, int]:
    offset_data = result.source.file(_OFFSET_FILE)
    first_row = parse_actionverificationindexoffset_records(offset_data)[0]
    return bytearray(result.source.data), offset_data, first_row["data_offset"]


def test_a_payload_of_another_class_type_raises(actionverificationindex_result: HandlerResult) -> None:
    data, offset_data, payload_offset = _first_payload(actionverificationindex_result)
    data[payload_offset] += 1
    with pytest.raises(ValueError, match="payload holds class type"):
        parse_actionverificationindex_records(bytes(data), offset_data)


def test_a_key_prefix_other_than_the_class_type_raises(actionverificationindex_result: HandlerResult) -> None:
    data, offset_data, payload_offset = _first_payload(actionverificationindex_result)
    data[payload_offset - _KEY_PREFIX_SIZE] += 1
    with pytest.raises(ValueError, match="key prefix"):
        parse_actionverificationindex_records(bytes(data), offset_data)


def test_a_payload_of_another_size_raises() -> None:
    offset_data = struct.pack("<IIII", 1, 52, 5, _PAYLOAD_SIZE + 1)
    with pytest.raises(ValueError, match="payload size"):
        parse_actionverificationindex_records(bytes(32), offset_data)


def test_a_payload_past_the_file_end_raises() -> None:
    offset_data = struct.pack("<IIII", 1, 52, 5, _PAYLOAD_SIZE)
    with pytest.raises(ValueError, match="outside the file"):
        parse_actionverificationindex_records(bytes(8), offset_data)

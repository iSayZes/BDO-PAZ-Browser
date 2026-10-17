from __future__ import annotations

import struct
from dataclasses import replace
from typing import Any

import pytest

from tests.framework import (
    CaseInput,
    DeclaredCount,
    DeclaredCountTest,
    HandlerCase,
    HandlerResult,
    RangeTest,
    SchemaTest,
    TargetTest,
    case_id,
    run_case,
)

from _dbss.actionexp.parser import parse_actionexp_records, parse_actionexpoffset_records


_OFFSET_FILE = "actionexpoffset.dbss"
_KEY_PREFIX_SIZE = 4
_LEVEL_ROW_SIZE = 85
_LEVEL_ENTRY_SIZE = _KEY_PREFIX_SIZE + _LEVEL_ROW_SIZE
_OFFSET_ROW_SIZE = 12
_U32 = struct.Struct("<I")
_WARRIOR = 0


def _block_rows(entry_size: int, companion: str | None = None) -> DeclaredCount:
    """Rows the u32 block counts declare, block after block to the end of the
    file, checking the blocks fill the file exactly."""

    def read(source: CaseInput) -> int:
        raw = source.file(companion)
        cursor = 0
        total = 0
        while cursor < len(raw):
            (count,) = _U32.unpack_from(raw, cursor)
            cursor += _U32.size + count * entry_size
            total += count
        if cursor != len(raw):
            raise AssertionError(f"blocks end at {cursor}, file holds {len(raw)} bytes")
        return total

    return read


CASE = HandlerCase(
    handler_name="actionexp.dbss",
    data_file="actionexp.dbss",
    companion_files={_OFFSET_FILE: _OFFSET_FILE},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["class_name"],
    internal_path="gamecommondata/binary/actionexp.dbss",
    tests=[
        SchemaTest(required_keys=["class_type", "class_name", "level", "unknown_05"]),
        DeclaredCountTest(declared=_block_rows(_LEVEL_ENTRY_SIZE)),
        DeclaredCountTest(declared=_block_rows(_OFFSET_ROW_SIZE, companion=_OFFSET_FILE)),
        TargetTest(col="class_type", value=_WARRIOR, expected={"class_name": "Warrior", "level": 1}),
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
        SchemaTest(required_keys=["class_type", "level", "data_offset", "data_size"]),
        DeclaredCountTest(declared=_block_rows(_OFFSET_ROW_SIZE)),
        RangeTest(col="data_size", min_val=_LEVEL_ROW_SIZE, max_val=_LEVEL_ROW_SIZE),
        # The first Warrior row follows its block's level count and its key prefix.
        TargetTest(col="class_type", value=_WARRIOR, expected={"level": 1, "data_offset": 8}),
    ],
)


@pytest.fixture(scope="module")
def actionexp_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_ACTIONEXP_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._ACTIONEXP_RESULT = result
    return result


@pytest.fixture(scope="module")
def offset_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_OFFSET_RESULT", None)
    if result is None:
        result = run_case(replace(OFFSET_CASE, tests=[]))
        request.module._OFFSET_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_actionexp_dbss(spec: Any, actionexp_result: HandlerResult) -> None:
    actionexp_result.check(spec)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_actionexpoffset_dbss(spec: Any, offset_result: HandlerResult) -> None:
    offset_result.check(spec)


def test_each_class_runs_from_level_one(actionexp_result: HandlerResult) -> None:
    levels: dict[int, list[int]] = {}
    for record in actionexp_result.records:
        levels.setdefault(record["class_type"], []).append(record["level"])
    for class_type, class_levels in levels.items():
        assert class_levels == list(range(1, len(class_levels) + 1)), class_type


def test_a_row_of_another_class_raises(actionexp_result: HandlerResult) -> None:
    offset_data = actionexp_result.source.file(_OFFSET_FILE)
    first_row = parse_actionexpoffset_records(offset_data)[0]
    data = bytearray(actionexp_result.source.data)
    data[first_row["data_offset"]] += 1
    with pytest.raises(ValueError, match="row holds class type"):
        parse_actionexp_records(bytes(data), offset_data)


def test_a_key_prefix_other_than_the_level_raises(actionexp_result: HandlerResult) -> None:
    offset_data = actionexp_result.source.file(_OFFSET_FILE)
    first_row = parse_actionexpoffset_records(offset_data)[0]
    data = bytearray(actionexp_result.source.data)
    key_offset = first_row["data_offset"] - _KEY_PREFIX_SIZE
    _U32.pack_into(data, key_offset, first_row["level"] + 1)
    with pytest.raises(ValueError, match="key prefix"):
        parse_actionexp_records(bytes(data), offset_data)


def test_offset_rows_past_the_file_end_raise() -> None:
    with pytest.raises(ValueError, match="rows exceed"):
        parse_actionexpoffset_records(_U32.pack(1) + bytes(4))

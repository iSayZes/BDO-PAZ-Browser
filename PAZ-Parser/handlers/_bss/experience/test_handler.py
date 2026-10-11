from __future__ import annotations

import struct
from dataclasses import replace
from typing import Any

import pytest

from tests.case_input import CaseInput
from tests.framework import (
    DeclaredCountTest,
    HandlerCase,
    HandlerResult,
    SchemaTest,
    TargetTest,
    UserLanguageTest,
    case_id,
    run_case,
)

from .parser import FILE_NAME, parse_experience_records
from .stat_body import STAT_FIELDS


_RECORD_SIZE = 236
_PADDING_SIZE = 200
_FIRST_GROUP = 0x04
_COUNT = struct.Struct("<I")


def _declared_records(source: CaseInput) -> int:
    """Sum of the level counts the class groups declare."""
    data = source.file(None)
    (table_start,) = _COUNT.unpack_from(data, len(data) - 8)
    pos, total = _FIRST_GROUP, 0
    while pos < table_start - _PADDING_SIZE:
        (level_count,) = _COUNT.unpack_from(data, pos)
        pos += _COUNT.size + level_count * _RECORD_SIZE
        total += level_count
    return total


CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["class_name"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=["class_type", "class_name", "level", *STAT_FIELDS]),
        DeclaredCountTest(declared=_declared_records),
        TargetTest(col="class_type", value=0, expected={"class_name": "Warrior", "level": 0}),
        TargetTest(col="class_type", value=25, expected={"class_name": "Kunoichi", "level": 0}),
        UserLanguageTest(fields=["class_name"]),
    ],
)


@pytest.fixture(scope="module")
def experience_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_experience_bss(spec: Any, experience_result: HandlerResult) -> None:
    experience_result.check(spec)


def test_class_and_level_pairs_are_unique(experience_result: HandlerResult) -> None:
    keys = [(r["class_type"], r["level"]) for r in experience_result.records]
    assert len(keys) == len(set(keys))


def _record(class_type: int, level: int) -> bytes:
    return struct.pack("<II", class_type, level) + bytes(_RECORD_SIZE - 8)


def _file(*groups: bytes, padding: bytes = bytes(_PADDING_SIZE)) -> bytes:
    """PABR, the given class groups, the zero run and an empty string table."""
    body = b"PABR" + b"".join(groups) + padding
    return body + _COUNT.pack(0) + _COUNT.pack(len(body)) + bytes(4)


def _group(*records: bytes) -> bytes:
    return _COUNT.pack(len(records)) + b"".join(records)


def test_groups_are_read_until_the_zero_run() -> None:
    data = _file(_group(_record(0, 0), _record(0, 1)), _group(_record(1, 0), _record(1, 1)))
    records = parse_experience_records(data)
    assert [(r["class_type"], r["level"]) for r in records] == [(0, 0), (0, 1), (1, 0), (1, 1)]


def test_a_record_out_of_place_is_rejected() -> None:
    data = _file(_group(_record(0, 0), _record(0, 2)))
    with pytest.raises(ValueError, match="group 0 record 1 holds class 0 level 2"):
        parse_experience_records(data)


def test_a_group_that_runs_into_the_zero_run_is_rejected() -> None:
    # Two records declared, one stored.
    data = _file(_COUNT.pack(2) + _record(0, 0))
    with pytest.raises(ValueError, match="runs past"):
        parse_experience_records(data)


def test_data_in_the_zero_run_is_rejected() -> None:
    data = _file(_group(_record(0, 0)), padding=bytes(_PADDING_SIZE - 1) + b"\x01")
    with pytest.raises(ValueError, match="has data in the 200 bytes"):
        parse_experience_records(data)

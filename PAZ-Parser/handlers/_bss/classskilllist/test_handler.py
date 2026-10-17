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

from .parser import FILE_NAME, parse_classskilllist_records

# Ground Roar, the Warrior skill the Warrior row starts with.
_GROUND_ROAR = 216
_WARRIOR = 0

CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["class_name", "skills"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=["class_type", "class_name", "skill_count", "skill_nos", "skills"]),
        DeclaredCountTest(declared=header_count(offset=4)),
        TargetTest(col="class_type", value=_WARRIOR, expected={"class_name": "Warrior"}),
        TargetTest(col="class_type", value=25, expected={"class_name": "Kunoichi"}),
        UserLanguageTest(fields=["class_name"]),
    ],
)


@pytest.fixture(scope="module")
def classskilllist_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_classskilllist_bss(spec: Any, classskilllist_result: HandlerResult) -> None:
    classskilllist_result.check(spec)


def test_class_types_are_unique(classskilllist_result: HandlerResult) -> None:
    types = [r["class_type"] for r in classskilllist_result.records]
    assert len(types) == len(set(types))


def test_every_row_lists_skills(classskilllist_result: HandlerResult) -> None:
    assert all(r["skill_count"] == len(r["skill_nos"]) > 0 for r in classskilllist_result.records)


def test_warrior_row_holds_ground_roar(classskilllist_result: HandlerResult) -> None:
    warrior = next(r for r in classskilllist_result.records if r["class_type"] == _WARRIOR)
    assert _GROUND_ROAR in warrior["skill_nos"]
    assert f"{_GROUND_ROAR} Ground Roar I" in warrior["skills"]


_U32 = struct.Struct("<I")


def _row(class_type: int, *skill_nos: int) -> bytes:
    return struct.pack(f"<BQ{len(skill_nos)}H", class_type, len(skill_nos), *skill_nos)


def _file(count: int, *rows: bytes) -> bytes:
    """PABR, a row count, the given rows and an empty string table."""
    body = b"PABR" + _U32.pack(count) + b"".join(rows)
    return body + _U32.pack(0) + _U32.pack(len(body)) + bytes(4)


def test_rows_are_read_up_to_the_string_table() -> None:
    rows = parse_classskilllist_records(_file(2, _row(0, 216, 1021), _row(4, 1015)))
    assert [(r.class_type, r.skill_nos) for r in rows] == [(0, (216, 1021)), (4, (1015,))]


def test_rows_short_of_the_string_table_are_rejected() -> None:
    with pytest.raises(ValueError, match="string table starts"):
        parse_classskilllist_records(_file(1, _row(0, 216), _row(4, 1015)))


def test_a_row_past_the_string_table_is_rejected() -> None:
    with pytest.raises(ValueError, match="more than fit"):
        parse_classskilllist_records(_file(1, struct.pack("<BQH", 0, 5, 216)))

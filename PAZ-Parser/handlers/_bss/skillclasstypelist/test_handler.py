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
    header_count,
    run_case,
)

from _bss.privateskill.parser import FILE_NAME as PRIVATESKILL_FILE, parse_privateskill_records
from _bss.publicskill.parser import FILE_NAME as PUBLICSKILL_FILE, parse_publicskill_keys
from _common.class_type import is_all_classes
from _common.skill import skill_key
from .parser import FILE_NAME, parse_skillclasstypelist_rows

# Ground Roar, a Warrior active skill (privateskill.bss), and "Warrior:
# Awakening: Goyen's Greatsword", an item skill (publicskill.bss).
_GROUND_ROAR = 216
_GOYENS_GREATSWORD = 16501

CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["skill"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=["skill_key", "skill_no", "level", "skill", "unknown_04"]),
        DeclaredCountTest(declared=header_count(offset=4)),
        TargetTest(
            col="skill_key",
            value=skill_key(_GROUND_ROAR, 1),
            expected={"skill_no": _GROUND_ROAR, "level": 1, "skill": "Ground Roar I"},
        ),
        TargetTest(
            col="skill_key",
            value=skill_key(_GOYENS_GREATSWORD, 1),
            expected={"skill_no": _GOYENS_GREATSWORD, "level": 1, "skill": "Warrior: Awakening: Goyen's Greatsword"},
        ),
    ],
)


@pytest.fixture(scope="module")
def skillclasstypelist_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_skillclasstypelist_bss(spec: Any, skillclasstypelist_result: HandlerResult) -> None:
    skillclasstypelist_result.check(spec)


def test_keys_are_the_publicskill_and_privateskill_keys() -> None:
    public = parse_publicskill_keys(load_binary_fixture(PUBLICSKILL_FILE))
    private = [r["skill_key"] for r in parse_privateskill_records(load_binary_fixture(PRIVATESKILL_FILE))]
    keys = [r["skill_key"] for r in parse_skillclasstypelist_rows(load_binary_fixture(FILE_NAME))]
    assert len(set(keys)) == len(keys)
    assert set(keys) == set(public) | set(private)


def test_every_row_holds_the_every_class_mask() -> None:
    narrow = [r["skill_key"] for r in parse_skillclasstypelist_rows(load_binary_fixture(FILE_NAME)) if not is_all_classes(r["unknown_04"])]
    assert not narrow, narrow


_U32 = struct.Struct("<I")
_ROW = struct.Struct("<IQ")


def _file(count: int, *rows: tuple[int, int]) -> bytes:
    """PABR, a row count, the given rows and an empty string table."""
    body = b"PABR" + _U32.pack(count) + b"".join(_ROW.pack(*row) for row in rows)
    return body + _U32.pack(0) + _U32.pack(len(body)) + bytes(4)


def test_rows_are_read_in_file_order() -> None:
    rows = [(skill_key(57005, 1), 0x7FFF_FFFF_FFFF), (skill_key(_GROUND_ROAR, 1), 0x1)]
    assert parse_skillclasstypelist_rows(_file(2, *rows)) == [
        {"skill_key": key, "unknown_04": value} for key, value in rows
    ]


def test_rows_short_of_the_string_table_are_rejected() -> None:
    with pytest.raises(ValueError, match="string table starts"):
        parse_skillclasstypelist_rows(_file(1, (1, 1), (2, 2)))


def test_a_bad_magic_is_rejected() -> None:
    with pytest.raises(ValueError, match="invalid magic"):
        parse_skillclasstypelist_rows(b"XXXX" + _file(0)[4:])

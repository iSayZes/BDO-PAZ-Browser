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

from _common.skill import skill_key
from _dbss.skillsimply.parser import parse_skillsimply_records
from .parser import FILE_NAME, parse_publicskill_keys

# "Warrior: Awakening: Goyen's Greatsword", an item skill in the file since client 1784.
_GOYENS_GREATSWORD = 16501
_ITEM_SKILL_KIND = 0
_SKILLSIMPLY_FILE = "skillsimply.dbss"
_SKILLSIMPLY_OFFSET_FILE = "skillsimplyoffset.dbss"

CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["skill"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=["skill_key", "skill_no", "level", "skill"]),
        DeclaredCountTest(declared=header_count(offset=8)),
        TargetTest(
            col="skill_key",
            value=skill_key(_GOYENS_GREATSWORD, 1),
            expected={"skill_no": _GOYENS_GREATSWORD, "level": 1, "skill": "Warrior: Awakening: Goyen's Greatsword"},
        ),
    ],
)


@pytest.fixture(scope="module")
def publicskill_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_publicskill_bss(spec: Any, publicskill_result: HandlerResult) -> None:
    publicskill_result.check(spec)


def test_every_key_is_level_1_of_a_unique_skill(publicskill_result: HandlerResult) -> None:
    records = publicskill_result.records
    assert {r["level"] for r in records} == {1}
    assert len({r["skill_no"] for r in records}) == len(records)


def test_every_key_is_an_item_skill() -> None:
    kinds = {
        record.skill_key: record.kind
        for record in parse_skillsimply_records(
            load_binary_fixture(_SKILLSIMPLY_FILE), load_binary_fixture(_SKILLSIMPLY_OFFSET_FILE)
        )
    }
    keys = parse_publicskill_keys(load_binary_fixture(FILE_NAME))
    wrong = [key for key in keys if kinds.get(key) != _ITEM_SKILL_KIND]
    assert not wrong, wrong


_U32 = struct.Struct("<I")


def _file(head: int, count: int, *keys: int) -> bytes:
    """PABR, `head`, a key count, the given keys and an empty string table."""
    body = b"PABR" + _U32.pack(head) + _U32.pack(count) + b"".join(_U32.pack(key) for key in keys)
    return body + _U32.pack(0) + _U32.pack(len(body)) + bytes(4)


def test_keys_are_read_up_to_the_string_table() -> None:
    keys = (skill_key(57005, 1), skill_key(16501, 1))
    assert parse_publicskill_keys(_file(0, 2, *keys)) == list(keys)


def test_a_non_zero_unknown_04_is_rejected() -> None:
    with pytest.raises(ValueError, match="unknown_04"):
        parse_publicskill_keys(_file(1, 1, skill_key(57005, 1)))


def test_keys_short_of_the_string_table_are_rejected() -> None:
    with pytest.raises(ValueError, match="string table starts"):
        parse_publicskill_keys(_file(0, 1, skill_key(57005, 1), skill_key(16501, 1)))


def test_a_count_past_the_string_table_is_rejected() -> None:
    with pytest.raises(ValueError, match="runs past the end"):
        parse_publicskill_keys(_file(0, 3, skill_key(57005, 1)))

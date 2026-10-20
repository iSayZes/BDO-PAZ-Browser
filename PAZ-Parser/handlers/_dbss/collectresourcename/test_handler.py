from __future__ import annotations

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

from _common.character_link import CHARACTERSTATIC_OFFSET_FILE
from _common.pabr_offset import parse_bare_u32_offset_rows
from _common.string_hash import ascii_key_hash
from .parser import FILE_NAME, OFFSET_FILE, parse_collectresourcename_records


_COUNT_OFFSET = 0
_COUNT_SIZE = 4
_NAME_HASH_SIZE = 4
# name_hash, name_hash_dup, the u64 name length and the u16 character key.
_FIXED_RECORD_SIZE = 18
# A Feldspar rock model; the 1784 sheet maps it to the same character.
_BAL_STONE = "01_nature/rocks/01_bal_stone_set01_03"
_FELDSPAR = 10004


CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={CHARACTERSTATIC_OFFSET_FILE: CHARACTERSTATIC_OFFSET_FILE},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["character_name"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=[
            "name_hash", "resource_file_name", "character_key", "character_name", "has_character_row",
            "name_hash_dup",
        ]),
        DeclaredCountTest(declared=header_count(offset=_COUNT_OFFSET)),
        TargetTest(
            col="resource_file_name",
            value=_BAL_STONE,
            expected={"character_key": _FELDSPAR, "has_character_row": True},
        ),
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
        SchemaTest(required_keys=["name_hash", "data_offset", "data_size"]),
        DeclaredCountTest(declared=header_count(offset=_COUNT_OFFSET)),
    ],
)


@pytest.fixture(scope="module")
def collect_result(request: Any) -> HandlerResult:
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
def test_collectresourcename_dbss(spec: Any, collect_result: HandlerResult) -> None:
    collect_result.check(spec)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_collectresourcenameoffset_dbss(spec: Any, offset_result: HandlerResult) -> None:
    offset_result.check(spec)


def test_name_hash_is_the_lookup3_hash_of_the_name(collect_result: HandlerResult) -> None:
    for r in collect_result.records:
        assert r["name_hash"] == ascii_key_hash(r["resource_file_name"])


def test_name_hash_is_stored_twice(collect_result: HandlerResult) -> None:
    assert all(r["name_hash_dup"] == r["name_hash"] for r in collect_result.records)


def test_names_are_unique_and_lower_case(collect_result: HandlerResult) -> None:
    names = [r["resource_file_name"] for r in collect_result.records]
    assert len(names) == len(set(names))
    assert all(name == name.lower() for name in names)


def test_offset_rows_point_past_the_first_hash() -> None:
    """Each index row starts at a record's `name_hash_dup` and covers the rest of the record."""
    expected = {}
    pos = _COUNT_SIZE
    for r in parse_collectresourcename_records(load_binary_fixture(FILE_NAME)):
        size = _FIXED_RECORD_SIZE + len(r["resource_file_name"])
        expected[r["name_hash"]] = (pos + _NAME_HASH_SIZE, size - _NAME_HASH_SIZE)
        pos += size
    rows = parse_bare_u32_offset_rows(load_binary_fixture(OFFSET_FILE))
    assert {row.entry_id: (row.offset, row.size) for row in rows} == expected


def test_parser_rejects_bytes_after_the_records() -> None:
    record = (1).to_bytes(4, "little") * 2 + (1).to_bytes(8, "little") + b"a" + (10004).to_bytes(2, "little")
    data = (1).to_bytes(4, "little") + record
    assert parse_collectresourcename_records(data)[0]["character_key"] == _FELDSPAR
    with pytest.raises(ValueError):
        parse_collectresourcename_records(data + b"\x00")

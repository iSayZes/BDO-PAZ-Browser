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
    UserLanguageTest,
    case_id,
    header_count,
    run_case,
)

from _dbss.guildhousecraftskill.parser import FILE_NAME as SKILL_FILE, parse_guildhousecraftskill_records
from .parser import FILE_NAME, OFFSET_FILE, ROW_SIZE, parse_guildhousecraftstorage_records


_COUNT_OFFSET = 0
_COUNT_SIZE = 4
# The index points past the row's leading key, at receipe_key_dup.
_INDEXED_KEY_SIZE = 4
_STORAGE = 2
_GUILD_STORAGE_LEVEL_2 = 50001


CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["name"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=["receipe_key", "receipe_key_dup", "storage_count", "name"]),
        DeclaredCountTest(declared=header_count(offset=_COUNT_OFFSET)),
        UserLanguageTest(fields=["name"]),
        TargetTest(col="receipe_key", value=_STORAGE, expected={"name": "Storage"}),
        TargetTest(col="receipe_key", value=_GUILD_STORAGE_LEVEL_2, expected={"name": "Guild Storage level 2"}),
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
        SchemaTest(required_keys=["receipe_key", "data_offset", "data_size"]),
        DeclaredCountTest(declared=header_count(offset=_COUNT_OFFSET)),
        TargetTest(col="receipe_key", value=_STORAGE, expected={"receipe_key": _STORAGE}),
    ],
)


@pytest.fixture(scope="module")
def storage_result(request: Any) -> HandlerResult:
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
def test_guildhousecraftstorage_dbss(spec: Any, storage_result: HandlerResult) -> None:
    storage_result.check(spec)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_guildhousecraftstorageoffset_dbss(spec: Any, offset_result: HandlerResult) -> None:
    offset_result.check(spec)


def test_keys_are_unique_and_repeated(storage_result: HandlerResult) -> None:
    keys = [r["receipe_key"] for r in storage_result.records]
    assert len(keys) == len(set(keys))
    assert all(r["receipe_key_dup"] == r["receipe_key"] for r in storage_result.records)


def test_every_key_has_a_guild_skill_row(storage_result: HandlerResult) -> None:
    """Each storage house use also has a guildhousecraftskill.dbss row."""
    skill_keys = {r["receipe_key"] for r in parse_guildhousecraftskill_records(load_binary_fixture(SKILL_FILE))}
    assert {r["receipe_key"] for r in storage_result.records} <= skill_keys


def test_offset_rows_point_past_each_leading_key(offset_result: HandlerResult) -> None:
    """Each index row starts 4 bytes into the row with its key and runs to its end."""
    records = parse_guildhousecraftstorage_records(load_binary_fixture(FILE_NAME))
    expected = {
        r["receipe_key"]: (_COUNT_SIZE + index * ROW_SIZE + _INDEXED_KEY_SIZE, ROW_SIZE - _INDEXED_KEY_SIZE)
        for index, r in enumerate(records)
    }
    actual = {r["receipe_key"]: (r["data_offset"], r["data_size"]) for r in offset_result.records}
    assert actual == expected


def _row(key: int, storage_count: int) -> bytes:
    return struct.pack("<iiH", key, key, storage_count)


def test_parser_reads_rows_and_rejects_bytes_after_them() -> None:
    data = struct.pack("<I", 2) + _row(_GUILD_STORAGE_LEVEL_2, 3) + _row(_STORAGE, 2)
    records = parse_guildhousecraftstorage_records(data)
    assert [(r["receipe_key"], r["storage_count"]) for r in records] == [
        (_GUILD_STORAGE_LEVEL_2, 3),
        (_STORAGE, 2),
    ]
    with pytest.raises(ValueError):
        parse_guildhousecraftstorage_records(data + b"\x00")


def test_parser_rejects_a_row_cut_short() -> None:
    data = struct.pack("<I", 1) + _row(_STORAGE, 2)[:-1]
    with pytest.raises(ValueError):
        parse_guildhousecraftstorage_records(data)

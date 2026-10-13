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

from _common.pabr_offset import parse_bare_offset_rows
from .parser import FILE_NAME, OFFSET_FILE, parse_fieldboss_records


_GARMOTH = 23120
_COUNT_OFFSET = 0
_KEY_SIZE = 2
_ROW_SIZE = 33


def _row(character_id: int) -> bytes:
    return struct.pack("<HBH12xB15x", character_id, 1, character_id, 1)


CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["name"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=["key", "character_id", "unknown_02", "unknown_11", "name", "title"]),
        DeclaredCountTest(declared=header_count(offset=_COUNT_OFFSET)),
        TargetTest(col="character_id", value=_GARMOTH, expected={"name": "Garmoth"}),
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
        SchemaTest(required_keys=["character_id", "offset", "size"]),
        DeclaredCountTest(declared=header_count(offset=_COUNT_OFFSET)),
        TargetTest(col="character_id", value=_GARMOTH, expected={"size": _ROW_SIZE - _KEY_SIZE}),
    ],
)


@pytest.fixture(scope="module")
def field_boss_result(request: Any) -> HandlerResult:
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
def test_fieldboss_dbss(spec: Any, field_boss_result: HandlerResult) -> None:
    field_boss_result.check(spec)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_fieldbossoffset_dbss(spec: Any, offset_result: HandlerResult) -> None:
    offset_result.check(spec)


def test_key_repeats_the_character_id(field_boss_result: HandlerResult) -> None:
    for r in field_boss_result.records:
        assert r["key"] == r["character_id"]


def test_character_ids_are_unique(field_boss_result: HandlerResult) -> None:
    ids = [r["character_id"] for r in field_boss_result.records]
    assert len(ids) == len(set(ids))


def test_every_offset_row_points_past_its_key() -> None:
    main = load_binary_fixture(FILE_NAME)
    for row in parse_bare_offset_rows(load_binary_fixture(OFFSET_FILE)):
        assert row.size == _ROW_SIZE - _KEY_SIZE
        key_at = row.offset - _KEY_SIZE
        assert struct.unpack_from("<H", main, key_at)[0] == row.entry_id
        assert struct.unpack_from("<H", main, key_at + 3)[0] == row.entry_id


def test_a_small_table_reads_back() -> None:
    assert parse_fieldboss_records(struct.pack("<I", 1) + _row(_GARMOTH)) == [
        {"key": _GARMOTH, "character_id": _GARMOTH, "unknown_02": 1, "unknown_11": 1},
    ]


def test_a_short_file_raises() -> None:
    with pytest.raises(ValueError):
        parse_fieldboss_records(struct.pack("<I", 2) + _row(_GARMOTH))

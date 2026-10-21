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
    RangeTest,
    SchemaTest,
    TargetTest,
    case_id,
    fixed_rows,
    header_count,
    run_case,
)

from _common.character_link import CHARACTERSTATIC_OFFSET_FILE
from _common.pabr_offset import parse_bare_offset_rows
from .parser import FILE_NAME, OFFSET_FILE, parse_guildboss_records


_COUNT_SIZE = 4
_ROW_SIZE = 17
# The offset file points past the leading character_key, at unknown_02.
_KEY_PREFIX_SIZE = 2
# Black Shadow <Boss>: the only row since client 1784.
_BLACK_SHADOW = 23014


CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={CHARACTERSTATIC_OFFSET_FILE: CHARACTERSTATIC_OFFSET_FILE},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["name"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(
            required_keys=[
                "character_key",
                "unknown_02",
                "character_key_dup",
                "skill_point_exp",
                "guild_money",
                "name",
                "has_character_row",
            ]
        ),
        DeclaredCountTest(declared=header_count(offset=0)),
        DeclaredCountTest(declared=fixed_rows(_ROW_SIZE, header_size=_COUNT_SIZE)),
        TargetTest(
            col="character_key",
            value=_BLACK_SHADOW,
            expected={"character_key_dup": _BLACK_SHADOW, "name": "Black Shadow", "has_character_row": True},
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
        SchemaTest(required_keys=["character_key", "offset", "size"]),
        DeclaredCountTest(declared=header_count(offset=0)),
        RangeTest(col="size", min_val=_ROW_SIZE - _KEY_PREFIX_SIZE, max_val=_ROW_SIZE - _KEY_PREFIX_SIZE),
    ],
)


@pytest.fixture(scope="module")
def guild_boss_result(request: Any) -> HandlerResult:
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
def test_guildboss_dbss(spec: Any, guild_boss_result: HandlerResult) -> None:
    guild_boss_result.check(spec)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_guildbossoffset_dbss(spec: Any, offset_result: HandlerResult) -> None:
    offset_result.check(spec)


def test_character_keys_are_unique(guild_boss_result: HandlerResult) -> None:
    keys = [r["character_key"] for r in guild_boss_result.records]
    assert len(keys) == len(set(keys))


def test_character_key_dup_repeats_the_key(guild_boss_result: HandlerResult) -> None:
    bad = [r["character_key"] for r in guild_boss_result.records if r["character_key_dup"] != r["character_key"]]
    assert not bad, f"rows whose character_key_dup differs: {bad[:5]}"


def test_offset_rows_point_at_each_row() -> None:
    """Each index row starts at its row's unknown_02 and covers the rest of the row."""
    records = parse_guildboss_records(load_binary_fixture(FILE_NAME))
    expected = {
        r["character_key"]: (_COUNT_SIZE + index * _ROW_SIZE + _KEY_PREFIX_SIZE, _ROW_SIZE - _KEY_PREFIX_SIZE)
        for index, r in enumerate(records)
    }
    rows = parse_bare_offset_rows(load_binary_fixture(OFFSET_FILE))
    assert {row.entry_id: (row.offset, row.size) for row in rows} == expected


def test_parser_reads_a_row_and_rejects_extra_or_missing_bytes() -> None:
    data = struct.pack("<IHBHiq", 1, _BLACK_SHADOW, 1, _BLACK_SHADOW, 7, 2**40)
    assert parse_guildboss_records(data) == [
        {
            "character_key": _BLACK_SHADOW,
            "unknown_02": 1,
            "character_key_dup": _BLACK_SHADOW,
            "skill_point_exp": 7,
            "guild_money": 2**40,
        }
    ]
    with pytest.raises(ValueError):
        parse_guildboss_records(data + b"\x00")
    with pytest.raises(ValueError):
        parse_guildboss_records(data[:-1])

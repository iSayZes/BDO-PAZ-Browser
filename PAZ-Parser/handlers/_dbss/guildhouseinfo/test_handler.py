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
    fixed_rows,
    header_count,
    run_case,
)
from tests.offset_rows import offset_row_problems

from _dbss.houseinforeceipe.parser import FILE_NAME as RECEIPE_FILE, parse_houseinforeceipe_records
from .parser import FILE_NAME, OFFSET_FILE, parse_guildhouseinfo_records, parse_guildhouseinfooffset_rows


_COUNT_SIZE = 4
_OFFSET_ROW_SIZE = 10
# The row key and the u16 after it close every row.
_KEY_FROM_END = 4
_VELIA_GUILD_HOUSE = 2110
_MAX_HOUSE_LEVEL = 5

CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={RECEIPE_FILE: RECEIPE_FILE},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["name", "town", "node"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(
            required_keys=[
                "character_key", "affiliated_town", "parent_node_key", "crafts", "unknown_crafts_02",
                "name", "town", "node", "crafts_text",
            ],
        ),
        DeclaredCountTest(declared=header_count(offset=0)),
        TargetTest(col="character_key", value=_VELIA_GUILD_HOUSE, expected={"name": "Velia Guild House", "town": "Velia"}),
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
        SchemaTest(required_keys=["character_key", "data_offset", "data_size"]),
        DeclaredCountTest(declared=header_count(offset=0)),
        DeclaredCountTest(declared=fixed_rows(_OFFSET_ROW_SIZE, header_size=_COUNT_SIZE)),
        TargetTest(col="character_key", value=_VELIA_GUILD_HOUSE, expected={"character_key": _VELIA_GUILD_HOUSE}),
    ],
)


@pytest.fixture(scope="module")
def guild_house_result(request: Any) -> HandlerResult:
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
def test_guildhouseinfo_dbss(spec: Any, guild_house_result: HandlerResult) -> None:
    guild_house_result.check(spec)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_guildhouseinfooffset_dbss(spec: Any, offset_result: HandlerResult) -> None:
    offset_result.check(spec)


def test_house_keys_are_unique(guild_house_result: HandlerResult) -> None:
    keys = [r["character_key"] for r in guild_house_result.records]
    assert len(keys) == len(set(keys))


def test_crafts_name_receipes_at_a_house_level(guild_house_result: HandlerResult) -> None:
    receipe_keys = {r["receipe_key"] for r in parse_houseinforeceipe_records(load_binary_fixture(RECEIPE_FILE))}
    crafts = [craft for r in guild_house_result.records for craft in r["crafts"]]

    assert crafts
    assert {craft["receipe_key"] for craft in crafts} <= receipe_keys
    assert all(1 <= craft["level"] <= _MAX_HOUSE_LEVEL for craft in crafts)


def test_offset_rows_point_at_their_rows() -> None:
    rows = parse_guildhouseinfooffset_rows(load_binary_fixture(OFFSET_FILE))
    problems = offset_row_problems(load_binary_fixture(FILE_NAME), rows, struct.Struct("<H"), key_from_end=_KEY_FROM_END)
    assert not problems, problems


def _row(town: int, node: int, crafts: list[tuple[int, int]], key: int) -> bytes:
    body = struct.pack("<HII", town, node, len(crafts)) + b"".join(struct.pack("<II", *craft) for craft in crafts)
    return body + struct.pack("<HH", key, 0xFFFF)


def test_parse_reads_the_key_after_the_crafts() -> None:
    data = struct.pack("<I", 2) + _row(5, 1, [(2, 5)], 10) + _row(32, 301, [(1601, 2), (2, 5)], 11)

    records = parse_guildhouseinfo_records(data)

    assert [r["character_key"] for r in records] == [10, 11]
    assert records[1]["crafts"] == [{"receipe_key": 1601, "level": 2}, {"receipe_key": 2, "level": 5}]
    assert records[1]["affiliated_town"] == 32


def test_parse_rejects_bytes_after_the_rows() -> None:
    with pytest.raises(ValueError):
        parse_guildhouseinfo_records(struct.pack("<I", 1) + _row(5, 1, [], 10) + b"\x00")

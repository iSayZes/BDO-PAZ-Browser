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
    case_id,
    header_count,
    run_case,
)

from _bss.playercharacterstatic.parser import FILE_NAME, parse_playercharacterstatic_records


# PABR magic, then the u32 key count.
_COUNT_OFFSET = 4
_WARRIOR = 1

CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={"characterstaticoffset.dbss": "characterstaticoffset.dbss"},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["name"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=["character_key", "name", "has_character_row"]),
        DeclaredCountTest(declared=header_count(offset=_COUNT_OFFSET)),
        TargetTest(col="character_key", value=_WARRIOR, expected={"name": "Warrior", "has_character_row": True}),
    ],
)


@pytest.fixture(scope="module")
def player_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_playercharacterstatic_bss(spec: Any, player_result: HandlerResult) -> None:
    player_result.check(spec)


def test_keys_are_unique(player_result: HandlerResult) -> None:
    keys = [r["character_key"] for r in player_result.records]
    assert len(keys) == len(set(keys))


def test_every_key_has_a_character_row(player_result: HandlerResult) -> None:
    assert all(r["has_character_row"] for r in player_result.records)


def _file(keys: list[int]) -> bytes:
    body = b"PABR" + struct.pack(f"<I{len(keys)}H", len(keys), *keys)
    return body + struct.pack("<III", 0, len(body), 0)


def test_parse_reads_the_keys_before_the_string_table() -> None:
    assert parse_playercharacterstatic_records(_file([1, 2, 31])) == [
        {"character_key": 1},
        {"character_key": 2},
        {"character_key": 31},
    ]


def test_parse_rejects_a_count_past_the_string_table() -> None:
    data = bytearray(_file([1, 2]))
    struct.pack_into("<I", data, _COUNT_OFFSET, 3)
    with pytest.raises(ValueError):
        parse_playercharacterstatic_records(bytes(data))

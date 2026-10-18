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

from _common.character_link import CHARACTERSTATIC_OFFSET_FILE
from _common.pabr_offset import PABR_MAGIC
from .parser import FILE_NAME, parse_cutscenecharacterdata_records


# PABR magic, then the u32 count.
_COUNT_OFFSET = 4
# The cutscene stand-in for the player character, in the file since client 1784.
_CUTSCENE_PC = 401

CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={CHARACTERSTATIC_OFFSET_FILE: CHARACTERSTATIC_OFFSET_FILE},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["character_name"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=["character_key", "character_name", "has_character_row"]),
        DeclaredCountTest(declared=header_count(offset=_COUNT_OFFSET)),
        TargetTest(col="character_key", value=_CUTSCENE_PC, expected={"has_character_row": True}),
    ],
)


def _file(keys: tuple[int, ...], rows_end_delta: int = 0) -> bytes:
    """PABR, the count, the u16 keys, an empty string table and the trailer pointing at it."""
    rows = struct.pack(f"<I{len(keys)}H", len(keys), *keys)
    rows_end = len(PABR_MAGIC) + len(rows) + rows_end_delta
    return PABR_MAGIC + rows + struct.pack("<III", 0, rows_end, 0)


@pytest.fixture(scope="module")
def cutscene_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_cutscenecharacterdata_bss(spec: Any, cutscene_result: HandlerResult) -> None:
    cutscene_result.check(spec)


def test_character_keys_are_unique(cutscene_result: HandlerResult) -> None:
    keys = [r["character_key"] for r in cutscene_result.records]
    assert len(keys) == len(set(keys))


def test_the_keys_read_back_in_file_order() -> None:
    records = parse_cutscenecharacterdata_records(_file((410, 400, 62001)))
    assert [r["character_key"] for r in records] == [410, 400, 62001]


@pytest.mark.parametrize(
    "data",
    [_file((400, 401), rows_end_delta=2), b"XXXX" + _file((400,))[4:]],
    ids=["rows_end_mismatch", "bad_magic"],
)
def test_a_changed_file_raises(data: bytes) -> None:
    with pytest.raises(ValueError):
        parse_cutscenecharacterdata_records(data)

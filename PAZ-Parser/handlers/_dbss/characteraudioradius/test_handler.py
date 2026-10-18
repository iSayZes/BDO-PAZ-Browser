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
from _common.pabr_offset import parse_pabr_offset_rows
from .parser import FILE_NAME, OFFSET_FILE, parse_characteraudioradius_records


_COUNT_SIZE = 4
_ROW_SIZE = 6
# Khan: a row since client 1784.
_KHAN = 59050
# Lekrashan: a row since client 1784.
_LEKRASHAN = 21477


CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={CHARACTERSTATIC_OFFSET_FILE: CHARACTERSTATIC_OFFSET_FILE},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["name"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=["character_key", "sound_radius", "name", "has_character_row"]),
        DeclaredCountTest(declared=header_count(offset=0)),
        DeclaredCountTest(declared=fixed_rows(_ROW_SIZE, header_size=_COUNT_SIZE)),
        TargetTest(col="character_key", value=_KHAN, expected={"name": "Khan", "has_character_row": True}),
        TargetTest(col="character_key", value=_LEKRASHAN, expected={"name": "Lekrashan", "has_character_row": True}),
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
        DeclaredCountTest(declared=header_count(offset=4)),
        RangeTest(col="size", min_val=_ROW_SIZE, max_val=_ROW_SIZE),
    ],
)


@pytest.fixture(scope="module")
def audio_radius_result(request: Any) -> HandlerResult:
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
def test_characteraudioradius_dbss(spec: Any, audio_radius_result: HandlerResult) -> None:
    audio_radius_result.check(spec)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_characteraudioradiusoffset_dbss(spec: Any, offset_result: HandlerResult) -> None:
    offset_result.check(spec)


def test_character_keys_are_unique(audio_radius_result: HandlerResult) -> None:
    keys = [r["character_key"] for r in audio_radius_result.records]
    assert len(keys) == len(set(keys))


def test_sound_radius_is_positive(audio_radius_result: HandlerResult) -> None:
    bad = [r["character_key"] for r in audio_radius_result.records if not r["sound_radius"] > 0]
    assert not bad, f"rows without a positive sound_radius: {bad[:5]}"


def test_offset_rows_point_at_each_row() -> None:
    """Each index row starts at its row's character_key and covers the whole row."""
    records = parse_characteraudioradius_records(load_binary_fixture(FILE_NAME))
    expected = {
        r["character_key"]: (_COUNT_SIZE + index * _ROW_SIZE, _ROW_SIZE)
        for index, r in enumerate(records)
    }
    rows = parse_pabr_offset_rows(load_binary_fixture(OFFSET_FILE))
    assert {row.entry_id: (row.offset, row.size) for row in rows} == expected


def test_parser_reads_a_row_and_rejects_extra_or_missing_bytes() -> None:
    data = struct.pack("<IHf", 1, _KHAN, 100000.0)
    assert parse_characteraudioradius_records(data) == [{"character_key": _KHAN, "sound_radius": 100000}]
    with pytest.raises(ValueError):
        parse_characteraudioradius_records(data + b"\x00")
    with pytest.raises(ValueError):
        parse_characteraudioradius_records(data[:-1])

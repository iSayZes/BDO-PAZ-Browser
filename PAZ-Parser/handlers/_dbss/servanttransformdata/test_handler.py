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
from .parser import FILE_NAME, OFFSET_FILE, parse_servanttransformdata_records


_COUNT_SIZE = 4
_ROW_SIZE = 8
# The offset file points past the leading form_key, at form_key_dup.
_KEY_PREFIX_SIZE = 2
# Epheria Sailboat to Epheria Galleon: form 1 since client 519.
_SAILBOAT_FORM = 1
_EPHERIA_SAILBOAT = 31001
_EPHERIA_GALLEON = 31020
# Epheria Frigate to Panokseon: form 2 since client 519.
_FRIGATE_FORM = 2
_EPHERIA_FRIGATE = 31003
_PANOKSEON = 31025


CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={CHARACTERSTATIC_OFFSET_FILE: CHARACTERSTATIC_OFFSET_FILE},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["from_name", "to_name"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(
            required_keys=[
                "form_key",
                "form_key_dup",
                "from_character_key",
                "to_character_key",
                "from_name",
                "to_name",
                "from_has_character_row",
                "to_has_character_row",
            ]
        ),
        DeclaredCountTest(declared=header_count(offset=0)),
        DeclaredCountTest(declared=fixed_rows(_ROW_SIZE, header_size=_COUNT_SIZE)),
        TargetTest(
            col="form_key",
            value=_SAILBOAT_FORM,
            expected={
                "from_character_key": _EPHERIA_SAILBOAT,
                "to_character_key": _EPHERIA_GALLEON,
                "from_name": "Epheria Sailboat",
                "to_name": "Epheria Galleon",
                "from_has_character_row": True,
                "to_has_character_row": True,
            },
        ),
        TargetTest(
            col="form_key",
            value=_FRIGATE_FORM,
            expected={
                "from_character_key": _EPHERIA_FRIGATE,
                "to_character_key": _PANOKSEON,
                "from_name": "Epheria Frigate",
                "to_name": "Panokseon",
            },
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
        SchemaTest(required_keys=["form_key", "offset", "size"]),
        DeclaredCountTest(declared=header_count(offset=0)),
        RangeTest(col="size", min_val=_ROW_SIZE - _KEY_PREFIX_SIZE, max_val=_ROW_SIZE - _KEY_PREFIX_SIZE),
    ],
)


@pytest.fixture(scope="module")
def servant_transform_result(request: Any) -> HandlerResult:
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
def test_servanttransformdata_dbss(spec: Any, servant_transform_result: HandlerResult) -> None:
    servant_transform_result.check(spec)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_servanttransformdataoffset_dbss(spec: Any, offset_result: HandlerResult) -> None:
    offset_result.check(spec)


def test_form_keys_are_unique(servant_transform_result: HandlerResult) -> None:
    keys = [r["form_key"] for r in servant_transform_result.records]
    assert len(keys) == len(set(keys))


def test_form_key_dup_repeats_the_key(servant_transform_result: HandlerResult) -> None:
    bad = [r["form_key"] for r in servant_transform_result.records if r["form_key_dup"] != r["form_key"]]
    assert not bad, f"rows whose form_key_dup differs: {bad[:5]}"


def test_from_and_to_differ(servant_transform_result: HandlerResult) -> None:
    """The 1784 server rejects a row whose two character keys are equal."""
    same = [r["form_key"] for r in servant_transform_result.records if r["from_character_key"] == r["to_character_key"]]
    assert not same, f"rows that change a character into itself: {same[:5]}"


def test_offset_rows_point_at_each_row() -> None:
    """Each index row starts at its row's form_key_dup and covers the rest of the row."""
    records = parse_servanttransformdata_records(load_binary_fixture(FILE_NAME))
    expected = {
        r["form_key"]: (_COUNT_SIZE + index * _ROW_SIZE + _KEY_PREFIX_SIZE, _ROW_SIZE - _KEY_PREFIX_SIZE)
        for index, r in enumerate(records)
    }
    rows = parse_bare_offset_rows(load_binary_fixture(OFFSET_FILE))
    assert {row.entry_id: (row.offset, row.size) for row in rows} == expected


def test_parser_reads_a_row_and_rejects_extra_or_missing_bytes() -> None:
    data = struct.pack("<IHHHH", 1, _SAILBOAT_FORM, _SAILBOAT_FORM, _EPHERIA_SAILBOAT, _EPHERIA_GALLEON)
    assert parse_servanttransformdata_records(data) == [
        {
            "form_key": _SAILBOAT_FORM,
            "form_key_dup": _SAILBOAT_FORM,
            "from_character_key": _EPHERIA_SAILBOAT,
            "to_character_key": _EPHERIA_GALLEON,
        }
    ]
    with pytest.raises(ValueError):
        parse_servanttransformdata_records(data + b"\x00")
    with pytest.raises(ValueError):
        parse_servanttransformdata_records(data[:-1])

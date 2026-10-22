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
from tests.offset_rows import offset_row_problems

from .parser import FILE_NAME, OFFSET_FILE, parse_form_records, parse_formoffset_rows


_COUNT_SIZE = 4
_OFFSET_ROW_SIZE = 10
# The index points past the u16 row key, at `index_dup`.
_KEY_SIZE = 2
# gc::FormType: eFormType_Horse 0, eFormType_Count 1 (the sheet's blank).
_LAST_FORM_TYPE = 1
_FIRST_FORM = 1
_DDS = ".dds"

CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={"characterstaticoffset.dbss": "characterstaticoffset.dbss"},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=[],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(
            required_keys=[
                "index",
                "index_dup",
                "type",
                "action_index",
                "tier",
                "icon_1",
                "icon_2",
                "character_keys",
                "type_name",
                "characters",
                "characters_text",
            ]
        ),
        DeclaredCountTest(declared=header_count(offset=0)),
        RangeTest(col="type", min_val=0, max_val=_LAST_FORM_TYPE),
        TargetTest(col="index", value=_FIRST_FORM, expected={"index_dup": _FIRST_FORM}),
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
        SchemaTest(required_keys=["index", "data_offset", "data_size"]),
        DeclaredCountTest(declared=header_count(offset=0)),
        DeclaredCountTest(declared=fixed_rows(_OFFSET_ROW_SIZE, header_size=_COUNT_SIZE)),
        TargetTest(col="index", value=_FIRST_FORM, expected={"index": _FIRST_FORM}),
    ],
)


@pytest.fixture(scope="module")
def form_result(request: Any) -> HandlerResult:
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
def test_form_dbss(spec: Any, form_result: HandlerResult) -> None:
    form_result.check(spec)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_formoffset_dbss(spec: Any, offset_result: HandlerResult) -> None:
    offset_result.check(spec)


def test_index_dup_repeats_the_index(form_result: HandlerResult) -> None:
    assert all(r["index"] == r["index_dup"] for r in form_result.records)


def test_icons_are_dds_paths(form_result: HandlerResult) -> None:
    for record in form_result.records:
        for icon in (record["icon_1"], record["icon_2"]):
            assert not icon or icon.lower().endswith(_DDS), record["index"]


def test_listed_characters_have_names(form_result: HandlerResult) -> None:
    for record in form_result.records:
        assert all(character["name"] for character in record["characters"]), record["index"]


def test_offset_rows_point_at_their_rows() -> None:
    rows = parse_formoffset_rows(load_binary_fixture(OFFSET_FILE))
    problems = offset_row_problems(load_binary_fixture(FILE_NAME), rows, struct.Struct("<H"), lead=_KEY_SIZE)
    assert not problems, problems


def _text(value: str) -> bytes:
    return struct.pack("<Q", len(value)) + value.encode("utf-16-le")


def _row(index: int, character_keys: list[int]) -> bytes:
    head = struct.pack("<HHBIH", index, index, 0, 510, 9) + _text("Horse_95.dds") + _text("")
    return head + struct.pack(f"<I{len(character_keys)}H", len(character_keys), *character_keys)


def test_parse_reads_the_character_key_list() -> None:
    data = struct.pack("<I", 2) + _row(1, []) + _row(260, [31562])

    records = parse_form_records(data)

    assert [r["index"] for r in records] == [1, 260]
    assert records[1]["character_keys"] == [31562]
    assert records[1]["icon_1"] == "Horse_95.dds"
    assert records[1]["icon_2"] == ""


def test_parse_rejects_a_list_past_the_file() -> None:
    with pytest.raises(ValueError):
        parse_form_records(struct.pack("<I", 1) + _row(1, [1, 2])[:-2])

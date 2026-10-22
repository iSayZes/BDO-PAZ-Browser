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
    fixed_rows,
    header_count,
    run_case,
)
from tests.offset_rows import offset_row_problems

from _common.pabr_offset import PabrOffsetRow
from .parser import FILE_NAME, OFFSET_FILE, parse_emoticon_records, parse_emoticonoffset_records
from .text import texture_file


_COUNT_SIZE = 4
_OFFSET_ROW_SIZE = 16
# The item link icon sheet and the Angry Black Spirit emoticon.
_ITEM_LINK = 1
_ANGRY_BLACK_SPIRIT = 2

CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["name", "keyword"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(
            required_keys=[
                "emoticon_key", "unknown_04", "icon_path", "icon_count", "row_count", "column_count",
                "keyword_kr", "sequence_path", "group", "name_kr", "unknown_name_kr_00", "name", "keyword", "sequence",
            ],
        ),
        DeclaredCountTest(declared=header_count(offset=0)),
        TargetTest(
            col="emoticon_key",
            value=_ANGRY_BLACK_SPIRIT,
            expected={
                "name": "Angry Black Spirit",
                "keyword": "Angry",
                "_icon_file": "ui_texture/renewal/sequence/pc_sequence_imojimini_angry.dds",
            },
        ),
        TargetTest(col="emoticon_key", value=_ITEM_LINK, expected={"name": "Item Link", "keyword": ""}),
        UserLanguageTest(fields=["name", "keyword"]),
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
        SchemaTest(required_keys=["emoticon_key", "unknown_04", "data_offset", "data_size"]),
        DeclaredCountTest(declared=header_count(offset=0)),
        DeclaredCountTest(declared=fixed_rows(_OFFSET_ROW_SIZE, header_size=_COUNT_SIZE)),
    ],
)


@pytest.fixture(scope="module")
def emoticon_result(request: Any) -> HandlerResult:
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
def test_emoticon_dbss(spec: Any, emoticon_result: HandlerResult) -> None:
    emoticon_result.check(spec)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_emoticonoffset_dbss(spec: Any, offset_result: HandlerResult) -> None:
    offset_result.check(spec)


def test_offset_rows_point_at_their_rows() -> None:
    rows = [
        PabrOffsetRow(row["emoticon_key"], row["data_offset"], row["data_size"])
        for row in parse_emoticonoffset_records(load_binary_fixture(OFFSET_FILE))
    ]
    problems = offset_row_problems(load_binary_fixture(FILE_NAME), rows, struct.Struct("<I"))
    assert not problems, problems


def test_every_icon_sheet_holds_its_grid() -> None:
    for record in parse_emoticon_records(load_binary_fixture(FILE_NAME)):
        assert 0 < record["icon_count"] <= record["row_count"] * record["column_count"], record["emoticon_key"]


def _text(value: str) -> bytes:
    return struct.pack("<Q", len(value)) + value.encode("utf-16-le")


def test_parse_reads_one_row() -> None:
    row = (
        struct.pack("<II", 7, 0) + _text("Mini.dds") + struct.pack("<BII", 1, 1, 1)
        + _text("키") + _text("Seq.dds") + struct.pack("<B", 1) + _text("이름") + struct.pack("<I", 0)
    )

    (record,) = parse_emoticon_records(struct.pack("<I", 1) + row)

    assert record["emoticon_key"] == 7
    assert (record["icon_path"], record["keyword_kr"], record["sequence_path"], record["name_kr"]) == (
        "Mini.dds", "키", "Seq.dds", "이름",
    )


def test_parse_rejects_a_row_past_the_file() -> None:
    with pytest.raises(ValueError):
        parse_emoticon_records(struct.pack("<I", 1) + struct.pack("<II", 7, 0) + struct.pack("<Q", 50))


def test_texture_file_turns_backslashes_and_drops_the_null_text() -> None:
    assert texture_file("Emoticon\\Emoticon_Item.dds") == "ui_texture/emoticon/emoticon_item.dds"
    assert texture_file("<NULL>") == ""

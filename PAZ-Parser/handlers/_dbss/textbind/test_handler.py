from __future__ import annotations

from dataclasses import replace
from typing import Any

import pytest

from _common.string_hash import key_hash
from tests.fixtures import load_binary_fixture
from tests.framework import (
    DeclaredCountTest,
    HandlerCase,
    HandlerResult,
    RangeTest,
    SchemaTest,
    TargetTest,
    case_id,
    header_count,
    run_case,
)
from .parser import VARIANT_COUNT, build_text_bind_kr_index, parse_textbind_offset_rows, parse_textbind_records

# Quest 4470 / 3 of the Growth Pass names this text (docs/file-formats/dbss/textbind_dbss.md).
_GROWTH_PASS_NAME = "GROWTHPASS_PC_CONSOLE_SEP1"
_GROWTH_PASS_KEY = key_hash(_GROWTH_PASS_NAME)


def _text_bind_record(record: dict) -> dict:
    return {
        "Key": record["key"],
        "Text": record["text"],
        "Korean": record["korean"],
        "Variant1": record["variant_1"],
        "UnknownPreVariant3": record["unknown_pre_variant_3"],
    }


TEXTBIND_CASE = HandlerCase(
    handler_name="textbind.dbss",
    data_file="textbind.dbss",
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["Text", "Variant1"],
    internal_path="gamecommondata/binary/textbind.dbss",
    record_mapper=_text_bind_record,
    tests=[
        SchemaTest(required_keys=["Key", "Text", "Korean", "Variant1", "UnknownPreVariant3"]),
        DeclaredCountTest(declared=header_count()),
        RangeTest(col="UnknownPreVariant3", min_val=0, max_val=0),
        # Variant 0 is the PC text, variant 1 the console one.
        TargetTest(
            col="Key",
            value=_GROWTH_PASS_KEY,
            expected={"Text": "[Menu] Quick Hotkey Settings", "Variant1": "[Menu] Ring Menu Setting"},
        ),
    ],
)

OFFSET_CASE = HandlerCase(
    handler_name="textbindoffset.dbss",
    data_file="textbindoffset.dbss",
    companion_files={},
    loc_file=None,
    uses_loc=False,
    loc_fields=[],
    internal_path="gamecommondata/binary/textbindoffset.dbss",
    tests=[
        SchemaTest(required_keys=["key", "offset", "size"]),
        DeclaredCountTest(declared=header_count()),
    ],
)


@pytest.fixture(scope="module")
def textbind_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_TEXTBIND_RESULT", None)
    if result is None:
        result = run_case(replace(TEXTBIND_CASE, tests=[]))
        request.module._TEXTBIND_RESULT = result
    return result


@pytest.fixture(scope="module")
def offset_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_OFFSET_RESULT", None)
    if result is None:
        result = run_case(replace(OFFSET_CASE, tests=[]))
        request.module._OFFSET_RESULT = result
    return result


@pytest.mark.parametrize("spec", TEXTBIND_CASE.tests, ids=case_id)
def test_textbind_dbss(spec: Any, textbind_result: HandlerResult) -> None:
    textbind_result.check(spec)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_textbindoffset_dbss(spec: Any, offset_result: HandlerResult) -> None:
    offset_result.check(spec)


def test_offset_rows_point_at_their_records() -> None:
    data = load_binary_fixture("textbind.dbss")
    rows = parse_textbind_offset_rows(load_binary_fixture("textbindoffset.dbss"))
    keys_in_file_order = [record.key for record in parse_textbind_records(data)]

    assert sorted(row.entry_id for row in rows) == sorted(keys_in_file_order)
    for row in rows:
        assert int.from_bytes(data[row.offset:row.offset + 4], "little") == row.entry_id
    # The rows in offset order tile the file after its count.
    ends = 4
    for row in sorted(rows, key=lambda r: r.offset):
        assert row.offset == ends
        ends = row.offset + row.size
    assert ends == len(data)


def test_every_record_has_four_variants_and_a_pc_text() -> None:
    records = parse_textbind_records(load_binary_fixture("textbind.dbss"))

    assert all(len(record.variants) == VARIANT_COUNT for record in records)
    assert all(record.variants[0] for record in records)


def test_korean_index_holds_the_pc_text() -> None:
    index = build_text_bind_kr_index(load_binary_fixture("textbind.dbss"))

    assert "간편 단축키 설정" in index[_GROWTH_PASS_KEY]

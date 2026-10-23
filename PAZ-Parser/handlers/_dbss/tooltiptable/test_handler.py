from __future__ import annotations

import re
import struct
from dataclasses import replace
from typing import Any

import pytest

from tests.fixtures import load_binary_fixture
from tests.framework import (
    CaseInput,
    DeclaredCount,
    DeclaredCountTest,
    HandlerCase,
    HandlerResult,
    PaFieldTest,
    RangeTest,
    SchemaTest,
    TargetTest,
    case_id,
    run_case,
)

from _common.string_hash import key_hash
from .parser import FILE_NAME, OFFSET_FILE, icon_bits, parse_tooltip_offset_rows, parse_tooltip_records


_U32 = struct.Struct("<I")
_MAGIC_SIZE = 4
_TRAILER_SIZE = 8
_ROW_SIZE = 21
_INDEX_ROW_SIZE = 12
# One key of each tooltip type, from the client 1784 sheet; on clients 1784
# and 3483 each sits in the section of its type and in no other.
_SKILL_KEY = key_hash("DAM_ATT")
_ITEM_EFFECT_KEY = key_hash("ITEM_EFFECT")
_ITEM_TEXT_KEY = key_hash("ITEM_WEAR_EFFECT_COOK")
_HANGUL = re.compile("[가-힣]")
_PLACEHOLDER = re.compile(r"\{p(\d)\}")


def _section_total(row_size: int, companion: str | None = None) -> DeclaredCount:
    """The sum of the section row counts, read up to the string table the trailer names."""

    def read(source: CaseInput) -> int:
        raw = source.file(companion)
        (table_start,) = _U32.unpack_from(raw, len(raw) - _TRAILER_SIZE)
        pos, total = _MAGIC_SIZE, 0
        while pos < table_start:
            (count,) = _U32.unpack_from(raw, pos)
            total += count
            pos += _U32.size + count * row_size
        if pos != table_start:
            raise AssertionError(f"sections end at 0x{pos:X}, the string table starts at 0x{table_start:X}")
        return total

    return read


CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={OFFSET_FILE: OFFSET_FILE},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["text"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(
            required_keys=[
                "key_hash",
                "format_ref",
                "format_kr",
                "param_count",
                "tooltip_type",
                "unknown_10",
                "icon_flags",
                "text",
                "icons",
            ]
        ),
        DeclaredCountTest(declared=_section_total(_ROW_SIZE)),
        DeclaredCountTest(declared=_section_total(_INDEX_ROW_SIZE, companion=OFFSET_FILE)),
        TargetTest(col="key_hash", value=_SKILL_KEY, expected={"tooltip_type": 0}),
        TargetTest(col="key_hash", value=_ITEM_EFFECT_KEY, expected={"tooltip_type": 1}),
        TargetTest(col="key_hash", value=_ITEM_TEXT_KEY, expected={"tooltip_type": 2}),
        RangeTest(col="unknown_10", min_val=0, max_val=0),
        PaFieldTest(field="text"),
    ],
)

OFFSET_CASE = HandlerCase(
    handler_name=OFFSET_FILE,
    data_file=OFFSET_FILE,
    companion_files={FILE_NAME: FILE_NAME},
    loc_file=None,
    uses_loc=False,
    loc_fields=[],
    internal_path=f"gamecommondata/binary/{OFFSET_FILE}",
    tests=[
        SchemaTest(required_keys=["tooltip_type", "key_hash", "data_offset", "unknown_08"]),
        DeclaredCountTest(declared=_section_total(_INDEX_ROW_SIZE)),
        DeclaredCountTest(declared=_section_total(_ROW_SIZE, companion=FILE_NAME)),
        RangeTest(col="unknown_08", min_val=0, max_val=0),
    ],
)


@pytest.fixture(scope="module")
def tooltip_result(request: Any) -> HandlerResult:
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
def test_tooltiptable_dbss(spec: Any, tooltip_result: HandlerResult) -> None:
    tooltip_result.check(spec)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_tooltiptableoffset_dbss(spec: Any, offset_result: HandlerResult) -> None:
    offset_result.check(spec)


def test_index_points_at_every_row_of_its_section() -> None:
    """Each index row points at a row with its key hash and its section's tooltip type, every row once."""
    data = load_binary_fixture(FILE_NAME)
    index = parse_tooltip_offset_rows(load_binary_fixture(OFFSET_FILE))
    problems = []
    for row in index:
        key_at, = _U32.unpack_from(data, row["data_offset"])
        type_at, = _U32.unpack_from(data, row["data_offset"] + 0x0C)
        if (key_at, type_at) != (row["key_hash"], row["tooltip_type"]):
            problems.append(f"{row} points at key {key_at}, type {type_at}")
    offsets = {row["data_offset"] for row in index}
    assert not problems, problems[:5]
    assert len(offsets) == len(index) == len(parse_tooltip_records(data))


def test_param_count_is_the_highest_placeholder_plus_one() -> None:
    wrong = [
        record["key_hash"]
        for record in parse_tooltip_records(load_binary_fixture(FILE_NAME))
        if record["param_count"] != max((int(n) + 1 for n in _PLACEHOLDER.findall(record["format_kr"])), default=0)
    ]
    assert not wrong, wrong[:10]


def test_keys_repeat_only_across_types() -> None:
    records = parse_tooltip_records(load_binary_fixture(FILE_NAME))
    pairs = [(record["tooltip_type"], record["key_hash"]) for record in records]
    assert len(set(pairs)) == len(pairs)


def test_every_type_shows_loc_text(tooltip_result: HandlerResult) -> None:
    """A wrong LOC key would leave every line of a type in Korean."""
    types = {record["tooltip_type"] for record in tooltip_result.records}
    translated = {record["tooltip_type"] for record in tooltip_result.records if not _HANGUL.search(record["text"])}
    assert translated == types


def test_parser_reads_sections_and_rejects_a_short_or_long_file() -> None:
    def pstr(text: str) -> bytes:
        raw = text.encode("utf-16-le")
        return b"\x01" + struct.pack("<I", len(raw)) + raw

    rows = struct.pack("<I", 1) + struct.pack("<IIIIBI", 7, 1, 1, 0, 0, 0b11)
    rows += struct.pack("<I", 1) + struct.pack("<IIIIBI", 8, 0, 0, 1, 0, 0)
    body = b"PABR" + rows
    strings = struct.pack("<I", 2) + pstr("효과") + pstr("피해 {p0}%")
    data = body + strings + struct.pack("<II", len(body), 0)
    records = parse_tooltip_records(data)
    assert [(r["key_hash"], r["tooltip_type"], r["format_kr"], r["icon_flags"]) for r in records] == [
        (7, 0, "피해 {p0}%", 3),
        (8, 1, "효과", 0),
    ]
    assert icon_bits(records[0]["icon_flags"]) == [0, 1]
    bad_end = body[:-1] + strings + struct.pack("<II", len(body) - 1, 0)
    with pytest.raises(ValueError):
        parse_tooltip_records(bad_end)
    with pytest.raises(ValueError):
        parse_tooltip_records(b"XXXX" + data[4:])

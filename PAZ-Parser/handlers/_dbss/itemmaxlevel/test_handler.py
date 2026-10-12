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
    UserLanguageTest,
    case_id,
    header_count,
    run_case,
)

from _common.pabr_offset import parse_pabr_u32_offset_rows
from .parser import FILE_NAME, OFFSET_FILE, parse_itemmaxlevel_records


_KZARKA_LONGSWORD = 10010
# PABR magic, then the u32 count.
_COUNT_OFFSET = 4
_FIRST_ROW = 8
_ROW_SIZE = 5
# The highest enhancement level, DEC.
_TOP_LEVEL = 25


CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["item_name"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=["item_id", "item_name", "icon_path", "max_enchant_level"]),
        DeclaredCountTest(declared=header_count(offset=_COUNT_OFFSET)),
        RangeTest(col="max_enchant_level", min_val=0, max_val=_TOP_LEVEL),
        TargetTest(
            col="item_id",
            value=_KZARKA_LONGSWORD,
            expected={"item_id": _KZARKA_LONGSWORD, "item_name": "Kzarka Longsword"},
        ),
        UserLanguageTest(fields=["item_name"]),
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
        SchemaTest(required_keys=["item_id", "offset", "size"]),
        DeclaredCountTest(declared=header_count(offset=_COUNT_OFFSET)),
        TargetTest(col="item_id", value=_KZARKA_LONGSWORD, expected={"item_id": _KZARKA_LONGSWORD, "size": 0}),
    ],
)


@pytest.fixture(scope="module")
def max_level_result(request: Any) -> HandlerResult:
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
def test_itemmaxlevel_dbss(spec: Any, max_level_result: HandlerResult) -> None:
    max_level_result.check(spec)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_itemmaxleveloffset_dbss(spec: Any, offset_result: HandlerResult) -> None:
    offset_result.check(spec)


def test_item_ids_are_unique(max_level_result: HandlerResult) -> None:
    item_ids = [r["item_id"] for r in max_level_result.records]
    assert len(item_ids) == len(set(item_ids))


def test_every_offset_row_points_at_its_items_row() -> None:
    records = parse_itemmaxlevel_records(load_binary_fixture(FILE_NAME))
    row_starts = {r["item_id"]: _FIRST_ROW + index * _ROW_SIZE for index, r in enumerate(records)}
    rows = parse_pabr_u32_offset_rows(load_binary_fixture(OFFSET_FILE))
    assert {row.entry_id: row.offset for row in rows} == row_starts


def _table(*rows: tuple[int, int]) -> bytes:
    """A PABR table of the given rows with an empty string table."""
    body = b"".join(struct.pack("<IB", *row) for row in rows)
    rows_end = _FIRST_ROW + len(body)
    return b"PABR" + struct.pack("<I", len(rows)) + body + struct.pack("<III", 0, rows_end, 0)


def test_a_small_table_reads_back() -> None:
    assert parse_itemmaxlevel_records(_table((7, 20), (8, 0))) == [
        {"item_id": 7, "max_enchant_level": 20},
        {"item_id": 8, "max_enchant_level": 0},
    ]


def test_a_missing_magic_raises() -> None:
    with pytest.raises(ValueError):
        parse_itemmaxlevel_records(b"XXXX" + _table((7, 20))[4:])

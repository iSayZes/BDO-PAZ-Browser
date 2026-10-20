from __future__ import annotations

import struct
from dataclasses import replace
from typing import Any

import pytest

from bdo_models import PazEntry
from tests.fixtures import load_binary_fixture
from tests.framework import (
    DeclaredCountTest,
    HandlerCase,
    HandlerResult,
    RangeTest,
    SchemaTest,
    case_id,
    fixed_rows,
    header_count,
    run_case,
)

from .handler import ItemCollectionScrollHandler
from .parser import FILE_NAME, OFFSET_FILE, ROW_SIZE, parse_itemcollectionscroll_records


_COUNT_OFFSET = 0
_COUNT_SIZE = 4
_ROW = struct.Struct("<Iiii")
_ENTRY = PazEntry("", f"gamecommondata/binary/{FILE_NAME}", 0, 0, 0, 0, 0)


CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file=None,
    uses_loc=False,
    loc_fields=[],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=["grade", "drop_rate", "count_rate", "cost_percent"]),
        DeclaredCountTest(declared=header_count(offset=_COUNT_OFFSET)),
        DeclaredCountTest(declared=fixed_rows(ROW_SIZE, header_size=_COUNT_SIZE)),
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
        SchemaTest(required_keys=["grade", "data_offset", "data_size"]),
        DeclaredCountTest(declared=header_count(offset=_COUNT_OFFSET)),
        RangeTest(col="data_size", min_val=ROW_SIZE, max_val=ROW_SIZE),
    ],
)


@pytest.fixture(scope="module")
def level_result(request: Any) -> HandlerResult:
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
def test_itemcollectionscroll_dbss(spec: Any, level_result: HandlerResult) -> None:
    level_result.check(spec)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_itemcollectionscrolloffset_dbss(spec: Any, offset_result: HandlerResult) -> None:
    offset_result.check(spec)


def test_grades_are_unique(level_result: HandlerResult) -> None:
    grades = [r["grade"] for r in level_result.records]
    assert len(grades) == len(set(grades))


def test_offset_rows_point_at_each_row(offset_result: HandlerResult) -> None:
    """Each index row starts at the row with its grade and covers the whole row."""
    records = parse_itemcollectionscroll_records(load_binary_fixture(FILE_NAME))
    expected = {record["grade"]: (_COUNT_SIZE + pos * ROW_SIZE, ROW_SIZE) for pos, record in enumerate(records)}
    actual = {r["grade"]: (r["data_offset"], r["data_size"]) for r in offset_result.records}
    assert actual == expected


def _file(rows: list[tuple[int, int, int, int]]) -> bytes:
    return struct.pack("<I", len(rows)) + b"".join(_ROW.pack(*row) for row in rows)


def test_parser_reads_rows_in_file_order() -> None:
    data = _file([(2, 1_000_000, 1_000_000, 2_000_000), (1, 1_000_000, 500_000, 1_000_000)])
    assert parse_itemcollectionscroll_records(data) == [
        {"grade": 2, "drop_rate": 1_000_000, "count_rate": 1_000_000, "cost_percent": 2_000_000},
        {"grade": 1, "drop_rate": 1_000_000, "count_rate": 500_000, "cost_percent": 1_000_000},
    ]


def test_parser_rejects_a_size_that_does_not_match_the_count() -> None:
    data = _file([(1, 1_000_000, 500_000, 1_000_000)])
    with pytest.raises(ValueError):
        parse_itemcollectionscroll_records(data + b"\x00")
    with pytest.raises(ValueError):
        parse_itemcollectionscroll_records(data[:-1])
    with pytest.raises(ValueError):
        parse_itemcollectionscroll_records(b"\x01\x00")


def test_rates_render_as_percent() -> None:
    handler = ItemCollectionScrollHandler()
    handler.lang = "en"
    records = handler.get_records(_file([(1, 1_000_000, 500_000, 2_000_000)]), _ENTRY, {})
    html = handler.render_records_page(records, 0, 50)
    assert "100%" in html
    assert "50%" in html
    assert "200%" in html


def test_bad_file_renders_an_error() -> None:
    handler = ItemCollectionScrollHandler()
    handler.lang = "en"
    records = handler.get_records(b"\x01\x00", _ENTRY, {})
    assert "_error" in records[0]

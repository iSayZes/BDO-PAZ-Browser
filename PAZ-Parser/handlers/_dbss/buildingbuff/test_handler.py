from __future__ import annotations

import struct
from dataclasses import replace
from typing import Any

import pytest

from bdo_models import PazEntry
from tests.fixtures import load_binary_fixture
from tests.framework import (
    CaseInput,
    DeclaredCount,
    DeclaredCountTest,
    HandlerCase,
    HandlerResult,
    RangeTest,
    SchemaTest,
    TargetTest,
    case_id,
    run_case,
)

from .handler import BuildingBuffHandler
from .parser import (
    BUFF_INDEX_SIZE,
    FILE_NAME,
    OFFSET_FILE,
    OFFSET_ROW,
    ROW,
    parse_buildingbuff_records,
    parse_buildingbuffoffset_records,
)


_COUNT = struct.Struct("<I")
# Count_Villa runs 1 to 4: the server loader rejects a list index above 3.
_MAX_VILLA_COUNT = 4
# What an index row covers: `skill_no` and `cost`.
_DATA_SIZE = ROW.size - BUFF_INDEX_SIZE
_ENTRY = PazEntry("", f"gamecommondata/binary/{FILE_NAME}", 0, 0, 0, 0, 0)


def declared_list_rows(row_size: int) -> DeclaredCount:
    """Rows in a list file: its bytes minus the list count and one row count
    per list, `row_size` bytes per row."""

    def read(source: CaseInput) -> int:
        raw = source.data
        (list_count,) = _COUNT.unpack_from(raw, 0)
        row_bytes = len(raw) - _COUNT.size * (1 + list_count)
        if row_bytes < 0 or row_bytes % row_size:
            raise AssertionError(f"{len(raw)} bytes do not hold {list_count} lists of {row_size}-byte rows")
        return row_bytes // row_size

    return read


CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["skill_name"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=["villa_count", "buff_index", "skill_no", "cost", "skill_name"]),
        DeclaredCountTest(declared=declared_list_rows(ROW.size)),
        RangeTest(col="villa_count", min_val=1, max_val=_MAX_VILLA_COUNT),
        # Turning Gates (60 min) is skill 55744 on clients 1784 and 3474.
        TargetTest(
            col="skill_no",
            value=55744,
            expected={"villa_count": 1, "skill_name": "[Villa] Turning Gates (60 min)"},
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
        SchemaTest(required_keys=["villa_count", "buff_index", "offset", "size"]),
        DeclaredCountTest(declared=declared_list_rows(OFFSET_ROW.size)),
        RangeTest(col="size", min_val=_DATA_SIZE, max_val=_DATA_SIZE),
    ],
)


@pytest.fixture(scope="module")
def buff_result(request: Any) -> HandlerResult:
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
def test_buildingbuff_dbss(spec: Any, buff_result: HandlerResult) -> None:
    buff_result.check(spec)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_buildingbuffoffset_dbss(spec: Any, offset_result: HandlerResult) -> None:
    offset_result.check(spec)


def test_buff_index_counts_up_from_zero_in_each_list(buff_result: HandlerResult) -> None:
    by_list: dict[int, list[int]] = {}
    for r in buff_result.records:
        by_list.setdefault(r["villa_count"], []).append(r["buff_index"])
    for indexes in by_list.values():
        assert indexes == list(range(len(indexes)))


def test_offset_rows_point_at_each_skill_no(offset_result: HandlerResult) -> None:
    """Each index row starts past the buff_index of the row with its key."""
    data = load_binary_fixture(FILE_NAME)
    for r in offset_result.records:
        buff_index_at = r["offset"] - BUFF_INDEX_SIZE
        assert ROW.unpack_from(data, buff_index_at)[0] == r["buff_index"], r
    keys = {(r["villa_count"], r["buff_index"]) for r in parse_buildingbuff_records(data)}
    assert {(r["villa_count"], r["buff_index"]) for r in offset_result.records} == keys


def _file(*lists: list[tuple[int, int, int]]) -> bytes:
    body = b"".join(_COUNT.pack(len(rows)) + b"".join(ROW.pack(*row) for row in rows) for rows in lists)
    return _COUNT.pack(len(lists)) + body


def test_parser_reads_lists_in_file_order() -> None:
    data = _file([(0, 55744, 200_000)], [], [(0, 53657, 300_000), (1, 53659, 1_500_000)])
    assert parse_buildingbuff_records(data) == [
        {"villa_count": 1, "buff_index": 0, "skill_no": 55744, "cost": 200_000},
        {"villa_count": 3, "buff_index": 0, "skill_no": 53657, "cost": 300_000},
        {"villa_count": 3, "buff_index": 1, "skill_no": 53659, "cost": 1_500_000},
    ]


def test_offset_parser_reads_lists_in_file_order() -> None:
    data = _COUNT.pack(2) + _COUNT.pack(0) + _COUNT.pack(1) + OFFSET_ROW.pack(0, 0x0E, _DATA_SIZE)
    assert parse_buildingbuffoffset_records(data) == [
        {"villa_count": 2, "buff_index": 0, "offset": 0x0E, "size": _DATA_SIZE},
    ]


def test_parser_rejects_a_size_that_does_not_match_the_counts() -> None:
    data = _file([(0, 55744, 200_000)])
    with pytest.raises(ValueError):
        parse_buildingbuff_records(data + b"\x00")
    with pytest.raises(ValueError):
        parse_buildingbuff_records(data[:-1])
    with pytest.raises(ValueError):
        parse_buildingbuff_records(b"\x01\x00")


def test_cost_renders_with_thousands_separators() -> None:
    handler = BuildingBuffHandler()
    handler.lang = "en"
    records = handler.get_records(_file([(0, 52908, 10_000_000)]), _ENTRY, {})
    assert "10,000,000" in handler.render_records_page(records, 0, 50)


def test_bad_file_renders_an_error() -> None:
    handler = BuildingBuffHandler()
    handler.lang = "en"
    records = handler.get_records(b"\x01\x00", _ENTRY, {})
    assert "could not be parsed" in handler.render_records_page(records, 0, 50)

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
    header_count,
    run_case,
)

from .handler import PurchaseLimitGroupHandler
from .parser import FILE_NAME, OFFSET_FILE, ROW_SIZE, parse_purchaselimitgroup_records


_COUNT_OFFSET = 0
_COUNT_SIZE = 4
# CppEnums.CashPurchaseLimitType: None, AtCharacter, AtAccount.
_LIMIT_TYPE_MAX = 2
_EN_LIMIT_TYPE_NAMES = {0: "None", 1: "Character", 2: "Family"}
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
        SchemaTest(required_keys=["group_no", "purchase_type", "purchase_count", "purchase_type_name"]),
        DeclaredCountTest(declared=header_count(offset=_COUNT_OFFSET)),
        RangeTest(col="purchase_type", min_val=0, max_val=_LIMIT_TYPE_MAX),
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
        SchemaTest(required_keys=["group_no", "data_offset", "data_size"]),
        DeclaredCountTest(declared=header_count(offset=_COUNT_OFFSET)),
    ],
)


@pytest.fixture(scope="module")
def group_result(request: Any) -> HandlerResult:
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
def test_purchaselimitgroup_dbss(spec: Any, group_result: HandlerResult) -> None:
    group_result.check(spec)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_purchaselimitgroupoffset_dbss(spec: Any, offset_result: HandlerResult) -> None:
    offset_result.check(spec)


def test_group_numbers_are_unique(group_result: HandlerResult) -> None:
    keys = [r["group_no"] for r in group_result.records]
    assert len(keys) == len(set(keys))


def test_offset_rows_point_at_each_row(offset_result: HandlerResult) -> None:
    """Each index row starts at the row with its group number and covers the whole row."""
    records = parse_purchaselimitgroup_records(load_binary_fixture(FILE_NAME))
    expected = {
        record["group_no"]: (_COUNT_SIZE + pos * ROW_SIZE, ROW_SIZE) for pos, record in enumerate(records)
    }
    actual = {r["group_no"]: (r["data_offset"], r["data_size"]) for r in offset_result.records}
    assert actual == expected


def _file(rows: list[tuple[int, int, int]]) -> bytes:
    return struct.pack("<I", len(rows)) + b"".join(struct.pack("<IBi", *row) for row in rows)


def test_parser_reads_packed_rows() -> None:
    data = _file([(2, 2, 1), (1, 1, 3)])
    assert parse_purchaselimitgroup_records(data) == [
        {"group_no": 2, "purchase_type": 2, "purchase_count": 1},
        {"group_no": 1, "purchase_type": 1, "purchase_count": 3},
    ]


def test_parser_rejects_a_size_that_does_not_match_the_count() -> None:
    data = _file([(2, 2, 1)])
    with pytest.raises(ValueError):
        parse_purchaselimitgroup_records(data + b"\x00")
    with pytest.raises(ValueError):
        parse_purchaselimitgroup_records(data[:-1])
    with pytest.raises(ValueError):
        parse_purchaselimitgroup_records(b"\x01\x00")


@pytest.mark.parametrize("purchase_type", sorted(_EN_LIMIT_TYPE_NAMES))
def test_limit_type_names_follow_the_enum(purchase_type: int) -> None:
    handler = PurchaseLimitGroupHandler()
    handler.lang = "en"
    records = handler.get_records(_file([(1, purchase_type, 1)]), _ENTRY, {})
    assert records[0]["purchase_type_name"] == _EN_LIMIT_TYPE_NAMES[purchase_type]


def test_limit_type_outside_the_enum_shows_the_value() -> None:
    handler = PurchaseLimitGroupHandler()
    handler.lang = "en"
    records = handler.get_records(_file([(1, 7, 1)]), _ENTRY, {})
    assert records[0]["purchase_type_name"] == "7"

from __future__ import annotations

import struct
from dataclasses import replace
from typing import Any

import pytest

from tests.framework import (
    DeclaredCountTest,
    HandlerCase,
    HandlerResult,
    SchemaTest,
    case_id,
    header_count,
    run_case,
)

from _dbss.maincategory.parser import OFFSET_FILE, parse_maincategory_records, parse_maincategoryoffset_records


_COUNT_SIZE = 4
_RECORD_KEYS = [
    "category_id",
    "unknown_02",
    "unknown_06",
    "unknown_0a",
    "icon_path",
    "unknown_after_icon_path",
    "unknown_icon_path_04",
]

CASE = HandlerCase(
    handler_name="maincategory.dbss",
    data_file="maincategory.dbss",
    companion_files={OFFSET_FILE: OFFSET_FILE},
    loc_file=None,
    uses_loc=False,
    loc_fields=[],
    internal_path="gamecommondata/binary/maincategory.dbss",
    tests=[
        SchemaTest(required_keys=_RECORD_KEYS),
        DeclaredCountTest(declared=header_count(offset=0)),
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
        SchemaTest(required_keys=["category_id", "record_offset", "record_size", "unknown_08"]),
        DeclaredCountTest(declared=header_count(offset=0)),
    ],
)


@pytest.fixture(scope="module")
def category_result(request: Any) -> HandlerResult:
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
def test_maincategory_dbss(spec: Any, category_result: HandlerResult) -> None:
    category_result.check(spec)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_maincategoryoffset_dbss(spec: Any, offset_result: HandlerResult) -> None:
    offset_result.check(spec)


def test_records_fill_the_file(category_result: HandlerResult) -> None:
    """Sorted by offset, the records cover every byte after the count."""
    source = category_result.source
    rows = sorted(parse_maincategoryoffset_records(source.file(OFFSET_FILE)), key=lambda row: row["record_offset"])
    position = _COUNT_SIZE
    for row in rows:
        assert row["record_offset"] == position, f"gap or overlap before category {row['category_id']}"
        position += row["record_size"]
    assert position == len(source.data)


def test_every_icon_is_a_dds_texture(category_result: HandlerResult) -> None:
    paths = [r["_icon_file"] for r in category_result.records]
    assert all(path.startswith("ui_texture/") and path.endswith(".dds") for path in paths), paths


def _record(category_id: int, icon_path: bytes) -> bytes:
    """A Category Record: the key, three u32, the str8 icon path, a u32 and the u8."""
    return struct.pack("<HIIIQ", category_id, 0, 0, 0, len(icon_path)) + icon_path + struct.pack("<IB", 0, 1)


def _tables(record: bytes, record_size: int) -> tuple[bytes, bytes]:
    """The main file with one record and its offset file."""
    return struct.pack("<I", 1) + record, struct.pack("<IHIHH", 1, 1, _COUNT_SIZE, record_size, 0)


def test_a_record_reads_back() -> None:
    record = _record(1, b"a.dds")
    data, offsets = _tables(record, len(record))
    assert parse_maincategory_records(data, offsets) == [{
        "category_id": 1,
        "unknown_02": 0,
        "unknown_06": 0,
        "unknown_0a": 0,
        "icon_path": "a.dds",
        "unknown_after_icon_path": 0,
        "unknown_icon_path_04": 1,
    }]


@pytest.mark.parametrize("size_change", [-1, 1], ids=["row_too_short", "row_too_long"])
def test_a_record_that_does_not_fill_its_row_raises(size_change: int) -> None:
    record = _record(1, b"a.dds")
    data, offsets = _tables(record + b"\x00", len(record) + size_change)
    with pytest.raises(ValueError):
        parse_maincategory_records(data, offsets)

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

from _dbss.growthpasspointshop.parser import (
    FILE_NAME,
    OFFSET_FILE,
    RECORD,
    parse_growthpasspointshop_records,
)

# Client 3473 ships both files as a count of 0; the Layout 1 tests below build
# client 1784 records from the doc.
_RECORD_KEYS = ["key", "key_dup", "unknown_08", "unknown_0c", "unknown_10", "unknown_14", "unknown_18"]


def _case(name: str, required_keys: list[str]) -> HandlerCase:
    return HandlerCase(
        handler_name=name,
        data_file=name,
        companion_files={},
        loc_file=None,
        uses_loc=False,
        loc_fields=[],
        internal_path=f"gamecommondata/binary/{name}",
        tests=[SchemaTest(required_keys=required_keys), DeclaredCountTest(declared=header_count(offset=0))],
    )


CASES = {
    FILE_NAME: _case(FILE_NAME, _RECORD_KEYS),
    OFFSET_FILE: _case(OFFSET_FILE, ["key", "offset", "size"]),
}
_RESULTS: dict[str, HandlerResult] = {}


def _result(name: str) -> HandlerResult:
    if name not in _RESULTS:
        _RESULTS[name] = run_case(replace(CASES[name], tests=[]))
    return _RESULTS[name]


@pytest.mark.parametrize(
    ("name", "spec"),
    [pytest.param(name, spec, id=f"{name}-{case_id(spec)}") for name, case in CASES.items() for spec in case.tests],
)
def test_growthpasspointshop_dbss(name: str, spec: Any) -> None:
    _result(name).check(spec)


def _table(*records: tuple[int, ...]) -> bytes:
    return struct.pack("<I", len(records)) + b"".join(RECORD.pack(*record) for record in records)


def test_layout_1_records_read_back() -> None:
    records = parse_growthpasspointshop_records(_table((15, 15, 750367, 2, 0, 10, 1), (14, 14, 750367, 2, 0, 100, 10)))
    assert [(r["key"], r["key_dup"], r["unknown_14"], r["unknown_18"]) for r in records] == [
        (15, 15, 10, 1),
        (14, 14, 100, 10),
    ]


@pytest.mark.parametrize(
    "data",
    [b"", _table((1, 1, 0, 0, 0, 0, 0))[:-1], _table((1, 1, 0, 0, 0, 0, 0)) + b"\x00", struct.pack("<I", 1)],
    ids=["no_count", "short_record", "trailing_bytes", "missing_record"],
)
def test_a_file_that_is_not_its_count_of_records_raises(data: bytes) -> None:
    with pytest.raises(ValueError):
        parse_growthpasspointshop_records(data)


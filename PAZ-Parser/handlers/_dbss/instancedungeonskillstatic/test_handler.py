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

from _dbss.instancedungeonskillstatic.parser import FILE_NAME, OFFSET_FILE, parse_instancedungeonskillstatic_records

# Client 3473 ships both files as a count of 0; the Layout 1 tests below build
# client 1784 records from the doc.


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
    FILE_NAME: _case(FILE_NAME, ["key", "unknown_04", "unknown_04_00"]),
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
def test_instancedungeonskillstatic_dbss(name: str, spec: Any) -> None:
    _result(name).check(spec)


def _record(key: int, text: str) -> bytes:
    """A Skill Static Record: the key, the str16 text and the u32 after it."""
    encoded = text.encode("utf-16-le")
    return struct.pack("<IQ", key, len(encoded) // 2) + encoded + struct.pack("<I", 0)


def _table(*records: bytes) -> bytes:
    return struct.pack("<I", len(records)) + b"".join(records)


# Key 0x44AD0001 reads as two u16: 1, then 17581 (client 1784).
_KEY = 0x44AD0001
_TEXT = "<PAColor0xffe9bd23>바운드<PAOldColor>"


def test_layout_1_records_read_back() -> None:
    records = parse_instancedungeonskillstatic_records(_table(_record(_KEY, _TEXT), _record(_KEY + 1, "")))
    assert records == [
        {"key": _KEY, "unknown_04": _TEXT, "unknown_04_00": 0},
        {"key": _KEY + 1, "unknown_04": "", "unknown_04_00": 0},
    ]


@pytest.mark.parametrize(
    "data",
    [b"", _table(_record(_KEY, _TEXT))[:-1], _table(_record(_KEY, _TEXT)) + b"\x00", struct.pack("<I", 1)],
    ids=["no_count", "short_record", "trailing_bytes", "missing_record"],
)
def test_a_broken_table_raises(data: bytes) -> None:
    with pytest.raises(ValueError):
        parse_instancedungeonskillstatic_records(data)

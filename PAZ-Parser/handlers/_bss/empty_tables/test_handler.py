from __future__ import annotations

from dataclasses import replace
from typing import Any

import pytest

from tests.framework import HandlerCase, HandlerResult, SchemaTest, TargetTest, case_id, run_case

from _bss.empty_tables.parser import parse_empty_pabr_table
from _bss.empty_tables.tables import EMPTY_PABR_TABLES

# PABR, count 0, string count 0, table_start 0x08, zero.
_EMPTY_FILE = b"PABR" + bytes(8) + (8).to_bytes(4, "little") + bytes(4)


def _case(name: str) -> HandlerCase:
    return HandlerCase(
        handler_name=name,
        data_file=name,
        companion_files={},
        loc_file=None,
        uses_loc=False,
        loc_fields=[],
        internal_path=f"gamecommondata/binary/{name}",
        tests=[
            SchemaTest(required_keys=["count", "status", "extra_bytes"]),
            # One status row for the zero count, nothing past the empty layout.
            TargetTest(col="count", value=0, expected=[{"extra_bytes": 0}]),
        ],
    )


CASES = {name: _case(name) for name in EMPTY_PABR_TABLES}
_RESULTS: dict[str, HandlerResult] = {}


def _result(name: str) -> HandlerResult:
    if name not in _RESULTS:
        _RESULTS[name] = run_case(replace(CASES[name], tests=[]))
    return _RESULTS[name]


@pytest.mark.parametrize(
    ("name", "spec"),
    [pytest.param(name, spec, id=f"{name}-{case_id(spec)}") for name, case in CASES.items() for spec in case.tests],
)
def test_empty_pabr_tables(name: str, spec: Any) -> None:
    _result(name).check(spec)


def test_the_empty_layout_reads_one_status_row() -> None:
    rows = parse_empty_pabr_table(_EMPTY_FILE, "x.bss", "No records")
    assert rows == [{"count": 0, "status": "No records", "extra_bytes": 0}]


def test_a_declared_record_raises() -> None:
    data = _EMPTY_FILE[:4] + (1).to_bytes(4, "little") + _EMPTY_FILE[8:]
    with pytest.raises(ValueError, match="declares 1 records"):
        parse_empty_pabr_table(data, "x.bss", "No records")


def test_a_string_raises() -> None:
    # String count 1 and one empty UTF-8 entry (u8 is_wide, u32 length 0).
    data = _EMPTY_FILE[:8] + (1).to_bytes(4, "little") + bytes(5) + _EMPTY_FILE[12:]
    with pytest.raises(ValueError, match="holds 1 strings"):
        parse_empty_pabr_table(data, "x.bss", "No records")


def test_a_bad_magic_raises() -> None:
    with pytest.raises(ValueError, match="invalid magic"):
        parse_empty_pabr_table(b"XXXX" + _EMPTY_FILE[4:], "x.bss", "No records")

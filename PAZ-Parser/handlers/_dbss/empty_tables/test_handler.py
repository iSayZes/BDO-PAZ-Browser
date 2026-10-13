from __future__ import annotations

from dataclasses import replace
from typing import Any

import pytest

from tests.framework import HandlerCase, HandlerResult, SchemaTest, TargetTest, case_id, run_case

from _common.empty_table import parse_empty_table
from _dbss.empty_tables.tables import EMPTY_TABLES


# Bytes after the count; every other table is only its count.
_EXTRA_BYTES = {"itemcouponreward.dbss": 12}


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
            # One status row for the zero count.
            TargetTest(col="count", value=0, expected=[{"extra_bytes": _EXTRA_BYTES.get(name, 0)}]),
        ],
    )


CASES = {name: _case(name) for name in EMPTY_TABLES}
_RESULTS: dict[str, HandlerResult] = {}


def _result(name: str) -> HandlerResult:
    if name not in _RESULTS:
        _RESULTS[name] = run_case(replace(CASES[name], tests=[]))
    return _RESULTS[name]


@pytest.mark.parametrize(
    ("name", "spec"),
    [pytest.param(name, spec, id=f"{name}-{case_id(spec)}") for name, case in CASES.items() for spec in case.tests],
)
def test_empty_tables(name: str, spec: Any) -> None:
    _result(name).check(spec)


def test_a_declared_record_raises() -> None:
    with pytest.raises(ValueError, match="declares 1 records"):
        parse_empty_table((1).to_bytes(4, "little"), "x.dbss", "No records")


def test_a_short_header_raises() -> None:
    with pytest.raises(ValueError, match="too short"):
        parse_empty_table(bytes(3), "x.dbss", "No records")

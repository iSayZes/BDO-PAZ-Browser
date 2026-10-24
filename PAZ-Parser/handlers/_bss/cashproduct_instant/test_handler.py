from __future__ import annotations

import struct
from dataclasses import replace
from typing import Any

import pytest

from tests.fixtures import load_binary_fixture
from tests.framework import HandlerCase, HandlerResult, RangeTest, SchemaTest, case_id, run_case

from .parser import FILE_NAME, INSTANT_TYPE_COUNT, parse_cashproduct_instant_records


CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file=None,
    uses_loc=False,
    loc_fields=[],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(
            required_keys=["instant_type", "instant_type_name", "unknown_00", "minute", "padding_02", "pearl_count"],
        ),
        RangeTest(col="instant_type", min_val=0, max_val=INSTANT_TYPE_COUNT - 1),
    ],
)


@pytest.fixture(scope="module")
def instant_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_cashproduct_instant_bss(spec: Any, instant_result: HandlerResult) -> None:
    instant_result.check(spec)


def test_every_instant_type_has_entries() -> None:
    records = parse_cashproduct_instant_records(load_binary_fixture(FILE_NAME))
    assert {record["instant_type"] for record in records} == set(range(INSTANT_TYPE_COUNT))


def _pabr(body: bytes) -> bytes:
    # Empty string table, then the trailer: where the table starts and a zero.
    return b"PABR" + body + struct.pack("<III", 0, 4 + len(body), 0)


def test_parse_reads_each_group_in_type_order() -> None:
    groups = b"".join(
        struct.pack("<BQ", 0, 1) + struct.pack("<H6sq", 10 * (kind + 1), b"\xaa" * 6, 5 * (kind + 1))
        for kind in range(INSTANT_TYPE_COUNT)
    )

    records = parse_cashproduct_instant_records(_pabr(groups))

    assert [(r["instant_type"], r["minute"], r["pearl_count"]) for r in records] == [
        (0, 10, 5), (1, 20, 10), (2, 30, 15), (3, 40, 20),
    ]


def test_parse_rejects_groups_that_miss_the_string_table() -> None:
    groups = b"".join(struct.pack("<BQ", 0, 0) for _ in range(INSTANT_TYPE_COUNT)) + b"\0"
    with pytest.raises(ValueError):
        parse_cashproduct_instant_records(_pabr(groups))

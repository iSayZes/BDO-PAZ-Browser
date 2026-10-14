from __future__ import annotations

import struct
from dataclasses import replace
from typing import Any

import pytest

from tests.fixtures import load_binary_fixture
from tests.framework import (
    CaseInput,
    DeclaredCountTest,
    HandlerCase,
    HandlerResult,
    SchemaTest,
    case_id,
    run_case,
)

from _common.pabr_offset import PABR_MAGIC
from _dbss.itemtradegrouptonpc.parser import FILE_NAME as TRADE_GROUP_FILE
from _dbss.itemtradegrouptonpc.parser import parse_itemtradegrouptonpc_records
from .parser import COUNT, FILE_NAME, GROUP_HEADER, PAIR, ROW, parse_itemtradeetc


_GROUP_COUNT_OFFSET = 4


def _declared_pairs(source: CaseInput) -> int:
    """Pairs the group headers declare, walked by header and pair size alone."""
    data = source.file(None)
    pos = len(PABR_MAGIC) + COUNT.size
    total = 0
    for _ in range(COUNT.unpack_from(data, _GROUP_COUNT_OFFSET)[0]):
        _, pair_count = GROUP_HEADER.unpack_from(data, pos)
        total += pair_count
        pos += GROUP_HEADER.size + pair_count * PAIR.size
    return total


CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file=None,
    uses_loc=False,
    loc_fields=[],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=["from_group", "to_group", "distance", "add_rate"]),
        DeclaredCountTest(declared=_declared_pairs),
    ],
)


@pytest.fixture(scope="module")
def itemtradeetc_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_itemtradeetc_bss(spec: Any, itemtradeetc_result: HandlerResult) -> None:
    itemtradeetc_result.check(spec)


def test_pair_codes_are_trade_group_types_of_the_trade_goods(itemtradeetc_result: HandlerResult) -> None:
    group_types = {
        r["trade_group_type"]
        for r in parse_itemtradegrouptonpc_records(load_binary_fixture(TRADE_GROUP_FILE))
    }
    pair_codes = {r[side] for r in itemtradeetc_result.records for side in ("from_group", "to_group")}
    assert pair_codes <= group_types, f"codes missing from {TRADE_GROUP_FILE}: {pair_codes - group_types}"


def test_no_pair_repeats(itemtradeetc_result: HandlerResult) -> None:
    keys = [(r["from_group"], r["to_group"]) for r in itemtradeetc_result.records]
    assert len(keys) == len(set(keys))


def _file(groups: list[tuple[int, list[tuple[int, int, float, int]]]], rows: list[tuple[int, int]]) -> bytes:
    body = bytearray(PABR_MAGIC + COUNT.pack(len(groups)))
    for code, pairs in groups:
        body += GROUP_HEADER.pack(code, len(pairs))
        for pair in pairs:
            body += PAIR.pack(*pair)
    body += COUNT.pack(len(rows))
    for row in rows:
        body += ROW.pack(*row)
    table_start = len(body)
    # Empty string table: count 0, then the trailer's table start and zero.
    return bytes(body + struct.pack("<III", 0, table_start, 0))


_SMALL = _file(
    [(1, [(1, 2, 700_000.0, 1_000_000)]), (2, [(2, 1, 700_000.0, 1_000_000), (2, 99, 700_000.0, 500_000)])],
    [(0, 1_000_000), (4_500_000, 750_000)],
)


def test_a_small_file_reads_back() -> None:
    parsed = parse_itemtradeetc(_SMALL)
    assert [(r["from_group"], r["to_group"], r["distance"], r["add_rate"]) for r in parsed.pairs] == [
        (1, 2, 700_000.0, 1_000_000),
        (2, 1, 700_000.0, 1_000_000),
        (2, 99, 700_000.0, 500_000),
    ]
    assert parsed.rows == [
        {"unknown_00": 0, "unknown_08": 1_000_000},
        {"unknown_00": 4_500_000, "unknown_08": 750_000},
    ]


@pytest.mark.parametrize(
    "data",
    [
        b"PABX" + _SMALL[4:],
        _file([(1, [(2, 1, 700_000.0, 1_000_000)])], []),
        _SMALL[:8] + b"\x00" + _SMALL[8:],
        _SMALL[:-16] + _SMALL[-12:],
    ],
    ids=["bad_magic", "pair_in_another_group", "shifted_rows", "short_rows"],
)
def test_a_broken_file_raises(data: bytes) -> None:
    with pytest.raises(ValueError):
        parse_itemtradeetc(data)

from __future__ import annotations

from dataclasses import replace
from typing import Any

import pytest

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

from _bss.nodeexperience.handler import energy_to_next_level
from _bss.nodeexperience.parser import ROW, ROWS_START, TRAILER, parse_nodeexperience_records


CASE = HandlerCase(
    handler_name="nodeexperience.bss",
    data_file="nodeexperience.bss",
    companion_files={},
    loc_file=None,
    uses_loc=False,
    loc_fields=[],
    internal_path="gamecommondata/binary/nodeexperience.bss",
    tests=[
        SchemaTest(required_keys=["level", "exp", "energy", "is_integrity", "node_exp_type"]),
        # The u32 row count after the PABR magic.
        DeclaredCountTest(declared=header_count(offset=4)),
        RangeTest(col="exp", min_val=0, max_val=2**63 - 1),
    ],
)


@pytest.fixture(scope="module")
def nodeexperience_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_nodeexperience(spec: Any, nodeexperience_result: HandlerResult) -> None:
    nodeexperience_result.check(spec)


def test_rows_run_from_level_0_in_level_order(nodeexperience_result: HandlerResult) -> None:
    levels = [record["level"] for record in nodeexperience_result.records]
    assert levels == list(range(len(levels)))


def _file(row_count: int, rows: bytes, end_of_data: int) -> bytes:
    return b"PABR" + row_count.to_bytes(4, "little") + rows + TRAILER.pack(0, end_of_data, 0)


def test_a_row_reads_level_and_exp() -> None:
    data = _file(1, ROW.pack(1, 0, 3, 40_000), ROWS_START + ROW.size)
    assert parse_nodeexperience_records(data) == [{"level": 3, "exp": 40_000, "is_integrity": 1, "node_exp_type": 0}]


def test_energy_is_exp_over_100() -> None:
    assert energy_to_next_level({"level": 1, "exp": 10_000}) == 100
    assert energy_to_next_level({"level": 19, "exp": 200_000}) == 2_000


def test_the_not_invested_row_has_no_energy_cost() -> None:
    assert energy_to_next_level({"level": 0, "exp": 1}) is None


def test_a_trailer_that_misses_the_rows_end_raises() -> None:
    with pytest.raises(ValueError, match="trailer says"):
        parse_nodeexperience_records(_file(1, ROW.pack(1, 0, 0, 1), ROWS_START + ROW.size - 1))


def test_a_count_the_rows_do_not_fill_raises() -> None:
    with pytest.raises(ValueError, match="trailer says"):
        parse_nodeexperience_records(_file(2, ROW.pack(1, 0, 0, 1), ROWS_START + ROW.size))


def test_a_missing_magic_raises() -> None:
    with pytest.raises(ValueError, match="PABR"):
        parse_nodeexperience_records(bytes(ROWS_START + TRAILER.size))

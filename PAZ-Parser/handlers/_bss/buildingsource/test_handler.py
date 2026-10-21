from __future__ import annotations

import struct
from dataclasses import replace
from typing import Any

import pytest

from tests.framework import (
    DeclaredCountTest,
    HandlerCase,
    HandlerResult,
    RangeTest,
    SchemaTest,
    TargetTest,
    case_id,
    header_count,
    run_case,
)

from .parser import COUNT_OFFSET, FILE_NAME, parse_buildingsource_records


# gc::EWorkAniType runs from 0 to eWorkAniType_Count (9).
_MAX_WORK_ANI_TYPE = 9
_COMMAND_POST = 56006
_FIELD_HQ = 56073
_POLISHED_STONE = 4068
_EMPTY_REST = (0, 0)


CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["name"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(
            required_keys=[
                "item_key", "item_key_dup", "unknown_08", "build_time", "work_ani_type",
                "repair_item_keys_count", "repair_item_keys", "repair_item_counts_count",
                "repair_item_counts", "repair_time", "repair_percents_count", "repair_percents",
                "unknown_repair_percents_00", "name", "work_ani_type_name", "repair_items",
            ]
        ),
        DeclaredCountTest(declared=header_count(offset=COUNT_OFFSET)),
        RangeTest(col="work_ani_type", min_val=0, max_val=_MAX_WORK_ANI_TYPE),
        TargetTest(col="item_key", value=_COMMAND_POST, expected={"name": "[Conquest] Command Post"}),
        TargetTest(col="item_key", value=_FIELD_HQ, expected={"name": "[Conquest] Field HQ"}),
    ],
)


def _row(key: int, items: list[tuple[int, int, int]], rest: tuple[int, int] = _EMPTY_REST) -> bytes:
    unknown_08, tail = rest
    keys = [item[0] for item in items]
    counts = [item[1] for item in items]
    percents = [item[2] for item in items]
    return (
        struct.pack("<IIHIB", key, key, unknown_08, 50000, 5)
        + struct.pack(f"<Q{len(keys)}I", len(keys), *keys)
        + struct.pack(f"<Q{len(counts)}q", len(counts), *counts)
        + struct.pack("<Q", 40000)
        + struct.pack(f"<Q{len(percents)}I", len(percents), *percents)
        + struct.pack("<I", tail)
    )


def _table(rows: list[bytes], after_rows: int = 0, extra: bytes = b"") -> bytes:
    body = b"PABR" + struct.pack("<I", len(rows)) + b"".join(rows) + struct.pack("<I", after_rows) + extra
    return body + struct.pack("<III", 0, len(body), 0)


@pytest.fixture(scope="module")
def source_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_buildingsource_bss(spec: Any, source_result: HandlerResult) -> None:
    source_result.check(spec)


def test_keys_are_unique_and_doubled(source_result: HandlerResult) -> None:
    keys = [r["item_key"] for r in source_result.records]
    assert len(keys) == len(set(keys))
    assert all(r["item_key_dup"] == r["item_key"] for r in source_result.records)


def test_repair_lists_run_in_step(source_result: HandlerResult) -> None:
    """Each repair item has one count and one percent."""
    for r in source_result.records:
        assert r["repair_item_keys_count"] == r["repair_item_counts_count"] == r["repair_percents_count"]


def test_a_small_table_reads_back() -> None:
    data = _table([
        _row(_COMMAND_POST, [(8184, 1, 7500), (4901, 5, 5000)]),
        _row(_FIELD_HQ, [], rest=(3, 7)),
    ])
    records = parse_buildingsource_records(data)
    assert [r["item_key"] for r in records] == [_COMMAND_POST, _FIELD_HQ]
    assert records[0]["repair_item_keys"] == [8184, 4901]
    assert records[0]["repair_item_counts"] == [1, 5]
    assert records[0]["repair_percents"] == [7500, 5000]
    assert records[0]["repair_time"] == 40000
    assert records[1]["repair_item_keys_count"] == 0
    assert (records[1]["unknown_08"], records[1]["unknown_repair_percents_00"]) == (3, 7)


def test_a_cut_row_raises() -> None:
    row = _row(_COMMAND_POST, [(_POLISHED_STONE, 1, 10000)])
    with pytest.raises(ValueError):
        parse_buildingsource_records(_table([row[:-1]]))


def test_bytes_before_the_string_table_raise() -> None:
    with pytest.raises(ValueError):
        parse_buildingsource_records(_table([_row(_COMMAND_POST, [])], extra=b"\x00"))


def test_a_nonzero_after_rows_raises() -> None:
    with pytest.raises(ValueError):
        parse_buildingsource_records(_table([_row(_COMMAND_POST, [])], after_rows=1))


def test_a_list_count_past_the_rows_raises() -> None:
    bad = struct.pack("<IIHIB", _COMMAND_POST, _COMMAND_POST, 0, 0, 5) + struct.pack("<Q", 0xFFFFFFFF)
    with pytest.raises(ValueError):
        parse_buildingsource_records(_table([bad]))

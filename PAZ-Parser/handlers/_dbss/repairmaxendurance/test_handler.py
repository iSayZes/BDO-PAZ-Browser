from __future__ import annotations

import struct
from dataclasses import replace
from typing import Any

import pytest

from tests.fixtures import load_binary_fixture
from tests.framework import (
    DeclaredCountTest,
    HandlerCase,
    HandlerResult,
    SchemaTest,
    TargetTest,
    UserLanguageTest,
    case_id,
    header_count,
    run_case,
)

from .parser import FILE_NAME, MATERIAL_SIZE, OFFSET_FILE, ROW_HEAD_SIZE, parse_repairmaxendurance_records


_COUNT_OFFSET = 0
_COUNT_SIZE = 4
# The index points past the row's leading key, at item_key_dup.
_INDEXED_KEY_SIZE = 4
_MEMORY_FRAGMENT = 44195
_AZWELL_LONGSWORD = 10020


CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["item_name"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(
            required_keys=[
                "item_key",
                "item_key_dup",
                "only_need_money",
                "only_money_repair_count",
                "material_count",
                "material_item_keys",
                "material_repair_counts",
                "material_need_money",
                "item_name",
                "materials",
            ]
        ),
        DeclaredCountTest(declared=header_count(offset=_COUNT_OFFSET)),
        UserLanguageTest(fields=["item_name"]),
        TargetTest(
            col="item_key",
            value=_AZWELL_LONGSWORD,
            expected={"item_key_dup": _AZWELL_LONGSWORD, "item_name": "Azwell Longsword of Crimson Flame"},
        ),
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
        SchemaTest(required_keys=["item_key", "data_offset", "data_size"]),
        DeclaredCountTest(declared=header_count(offset=_COUNT_OFFSET)),
        TargetTest(col="item_key", value=_AZWELL_LONGSWORD, expected={"item_key": _AZWELL_LONGSWORD}),
    ],
)


@pytest.fixture(scope="module")
def repair_result(request: Any) -> HandlerResult:
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
def test_repairmaxendurance_dbss(spec: Any, repair_result: HandlerResult) -> None:
    repair_result.check(spec)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_repairmaxenduranceoffset_dbss(spec: Any, offset_result: HandlerResult) -> None:
    offset_result.check(spec)


def test_keys_are_unique_and_repeated(repair_result: HandlerResult) -> None:
    keys = [r["item_key"] for r in repair_result.records]
    assert len(keys) == len(set(keys))
    assert all(r["item_key_dup"] == r["item_key"] for r in repair_result.records)


def test_material_lists_follow_the_count(repair_result: HandlerResult) -> None:
    for record in repair_result.records:
        count = record["material_count"]
        assert len(record["material_item_keys"]) == count
        assert len(record["material_repair_counts"]) == count
        assert len(record["material_need_money"]) == count
        assert len(record["materials"]) == count


def test_rows_start_with_the_item_and_end_with_memory_fragment(repair_result: HandlerResult) -> None:
    """The item itself is the first material of its row, Memory Fragment the last."""
    for record in repair_result.records:
        assert record["material_item_keys"][0] == record["item_key"]
        assert record["material_item_keys"][-1] == _MEMORY_FRAGMENT


def test_offset_rows_point_past_each_leading_key(offset_result: HandlerResult) -> None:
    """Each index row starts 4 bytes into the row with its key and runs to its end."""
    records = parse_repairmaxendurance_records(load_binary_fixture(FILE_NAME))
    expected: dict[int, tuple[int, int]] = {}
    row_start = _COUNT_SIZE
    for record in records:
        row_size = ROW_HEAD_SIZE + record["material_count"] * MATERIAL_SIZE
        expected[record["item_key"]] = (row_start + _INDEXED_KEY_SIZE, row_size - _INDEXED_KEY_SIZE)
        row_start += row_size
    actual = {r["item_key"]: (r["data_offset"], r["data_size"]) for r in offset_result.records}
    assert actual == expected


def _row(key: int, materials: list[tuple[int, int, int]]) -> bytes:
    head = struct.pack("<IIqhI", key, key, 0, 0, len(materials))
    return head + b"".join(struct.pack("<Ihq", *material) for material in materials)


def test_parser_reads_rows_and_rejects_bytes_after_them() -> None:
    data = (
        struct.pack("<I", 2)
        + _row(_AZWELL_LONGSWORD, [(_AZWELL_LONGSWORD, 10, 0), (_MEMORY_FRAGMENT, 1, 0)])
        + _row(1, [(2, 5, 300)])
    )
    records = parse_repairmaxendurance_records(data)
    assert [(r["item_key"], r["material_item_keys"], r["material_repair_counts"]) for r in records] == [
        (_AZWELL_LONGSWORD, [_AZWELL_LONGSWORD, _MEMORY_FRAGMENT], [10, 1]),
        (1, [2], [5]),
    ]
    assert records[1]["material_need_money"] == [300]
    with pytest.raises(ValueError):
        parse_repairmaxendurance_records(data + b"\x00")


def test_parser_rejects_a_row_cut_short() -> None:
    row = _row(_AZWELL_LONGSWORD, [(_MEMORY_FRAGMENT, 1, 0)])
    with pytest.raises(ValueError):
        parse_repairmaxendurance_records(struct.pack("<I", 1) + row[:-1])
    with pytest.raises(ValueError):
        parse_repairmaxendurance_records(struct.pack("<I", 1) + row[: ROW_HEAD_SIZE - 1])

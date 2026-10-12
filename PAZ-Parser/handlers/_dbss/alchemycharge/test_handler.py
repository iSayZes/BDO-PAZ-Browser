from __future__ import annotations

import struct
from dataclasses import replace
from typing import Any

import pytest

from tests.fixtures import load_binary_fixture
from tests.framework import (
    CaseInput,
    DeclaredCount,
    DeclaredCountTest,
    HandlerCase,
    HandlerResult,
    SchemaTest,
    TargetTest,
    UserLanguageTest,
    case_id,
    run_case,
)

from .parser import (
    FILE_NAME,
    OFFSET_FILE,
    parse_alchemycharge_records,
    parse_alchemychargeoffset_records,
    parse_grouped_rows,
)


_OIL_OF_REGENERATION = 6601
_DESTRUCTION = 0
_ROW_SIZE = 12
_WORDS_PER_ROW = 3


def _declared_rows() -> DeclaredCount:
    """Rows in a grouped file: its u32 words minus the group count and one
    row count per group, three words per row."""

    def read(source: CaseInput) -> int:
        raw = source.data
        group_count = int.from_bytes(raw[:4], "little")
        row_words = len(raw) // 4 - 1 - group_count
        if len(raw) % 4 or row_words < 0 or row_words % _WORDS_PER_ROW:
            raise AssertionError(f"{len(raw)} bytes do not hold {group_count} groups of 12-byte rows")
        return row_words // _WORDS_PER_ROW

    return read


CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["item_name"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=["stone_type", "stone_type_name", "item_id", "item_name", "icon_path", "charge_point"]),
        DeclaredCountTest(declared=_declared_rows()),
        TargetTest(col="stone_type", value=_DESTRUCTION, expected={"stone_type_name": "Destruction"}),
        TargetTest(
            col="item_id",
            value=_OIL_OF_REGENERATION,
            expected={"item_id": _OIL_OF_REGENERATION, "item_name": "Oil of Regeneration"},
        ),
        UserLanguageTest(fields=["item_name", "stone_type_name"]),
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
        SchemaTest(required_keys=["stone_type", "item_id", "offset", "size"]),
        DeclaredCountTest(declared=_declared_rows()),
        TargetTest(col="item_id", value=_OIL_OF_REGENERATION, expected={"item_id": _OIL_OF_REGENERATION, "size": _ROW_SIZE}),
    ],
)


@pytest.fixture(scope="module")
def charge_result(request: Any) -> HandlerResult:
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
def test_alchemycharge_dbss(spec: Any, charge_result: HandlerResult) -> None:
    charge_result.check(spec)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_alchemychargeoffset_dbss(spec: Any, offset_result: HandlerResult) -> None:
    offset_result.check(spec)


def test_every_row_sits_in_the_group_of_its_stone_type() -> None:
    rows = parse_grouped_rows(load_binary_fixture(FILE_NAME), FILE_NAME)
    assert all(group == stone_type for group, (stone_type, _item, _point) in rows)


def test_items_are_unique_per_stone_type(charge_result: HandlerResult) -> None:
    keys = [(r["stone_type"], r["item_id"]) for r in charge_result.records]
    assert len(keys) == len(set(keys))


def test_every_offset_row_points_at_its_material_row() -> None:
    data = load_binary_fixture(FILE_NAME)
    for row in parse_alchemychargeoffset_records(load_binary_fixture(OFFSET_FILE)):
        assert row["size"] == _ROW_SIZE
        assert struct.unpack_from("<II", data, row["offset"]) == (row["stone_type"], row["item_id"])


def _grouped(*groups: list[tuple[int, int, int]]) -> bytes:
    """A grouped file of the given groups of rows."""
    body = b"".join(
        struct.pack("<I", len(rows)) + b"".join(struct.pack("<III", *row) for row in rows) for rows in groups
    )
    return struct.pack("<I", len(groups)) + body


def test_a_small_table_reads_back() -> None:
    data = _grouped([(0, 6601, 10)], [], [(2, 5301, 1)])
    assert parse_alchemycharge_records(data) == [
        {"stone_type": 0, "item_id": 6601, "charge_point": 10},
        {"stone_type": 2, "item_id": 5301, "charge_point": 1},
    ]


def test_an_offset_row_takes_its_group_as_stone_type() -> None:
    data = _grouped([], [(6601, 8, 12)])
    assert parse_alchemychargeoffset_records(data) == [
        {"stone_type": 1, "item_id": 6601, "offset": 8, "size": 12},
    ]


def test_a_cut_group_raises() -> None:
    with pytest.raises(ValueError):
        parse_alchemycharge_records(_grouped([(0, 6601, 10)])[:-4])


def test_bytes_after_the_last_group_raise() -> None:
    with pytest.raises(ValueError):
        parse_alchemycharge_records(_grouped([(0, 6601, 10)]) + b"\0\0\0\0")

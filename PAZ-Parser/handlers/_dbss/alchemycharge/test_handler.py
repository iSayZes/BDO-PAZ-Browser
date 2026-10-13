from __future__ import annotations

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
    run_case,
)

from _dbss.alchemystone.test_grouped import (
    ROW_SIZE,
    check_offset_rows_point_at_main_rows,
    check_rows_sit_in_their_stone_group,
    declared_grouped_rows,
    grouped_file,
)
from .parser import (
    FILE_NAME,
    OFFSET_FILE,
    parse_alchemycharge_records,
    parse_alchemychargeoffset_records,
)


_OIL_OF_REGENERATION = 6601
_DESTRUCTION = 0


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
        DeclaredCountTest(declared=declared_grouped_rows()),
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
        DeclaredCountTest(declared=declared_grouped_rows()),
        TargetTest(col="item_id", value=_OIL_OF_REGENERATION, expected={"item_id": _OIL_OF_REGENERATION, "size": ROW_SIZE}),
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
    check_rows_sit_in_their_stone_group(load_binary_fixture(FILE_NAME), FILE_NAME)


def test_items_are_unique_per_stone_type(charge_result: HandlerResult) -> None:
    keys = [(r["stone_type"], r["item_id"]) for r in charge_result.records]
    assert len(keys) == len(set(keys))


def test_every_offset_row_points_at_its_material_row() -> None:
    check_offset_rows_point_at_main_rows(
        load_binary_fixture(FILE_NAME),
        parse_alchemychargeoffset_records(load_binary_fixture(OFFSET_FILE)),
    )


def test_a_small_table_reads_back() -> None:
    data = grouped_file([(0, 6601, 10)], [], [(2, 5301, 1)])
    assert parse_alchemycharge_records(data) == [
        {"stone_type": 0, "item_id": 6601, "charge_point": 10},
        {"stone_type": 2, "item_id": 5301, "charge_point": 1},
    ]

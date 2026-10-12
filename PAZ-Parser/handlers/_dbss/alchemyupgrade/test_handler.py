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
from .handler import experience_text
from .parser import (
    FILE_NAME,
    OFFSET_FILE,
    parse_alchemyupgrade_records,
    parse_alchemyupgradeoffset_records,
)


_IRON_INGOT = 4052
_ASH_PLYWOOD = 4652
_DESTRUCTION = 0
_PROTECTION = 1


CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["item_name"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=["stone_type", "stone_type_name", "item_id", "item_name", "icon_path", "experience"]),
        DeclaredCountTest(declared=declared_grouped_rows()),
        # Pure metals polish Destruction, plywood polishes Protection
        # (LUA_ALCHEMYSTONE_PURESTONE2 "Metal Ingot", LUA_ALCHEMYSTONE_HARDWOOD2 "Plywood").
        TargetTest(
            col="item_id",
            value=_IRON_INGOT,
            expected={"stone_type": _DESTRUCTION, "stone_type_name": "Destruction", "item_name": "Iron Ingot"},
        ),
        TargetTest(
            col="item_id",
            value=_ASH_PLYWOOD,
            expected={"stone_type": _PROTECTION, "stone_type_name": "Protection", "item_name": "Ash Plywood"},
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
        TargetTest(col="item_id", value=_ASH_PLYWOOD, expected={"stone_type": _PROTECTION, "size": ROW_SIZE}),
    ],
)


@pytest.fixture(scope="module")
def upgrade_result(request: Any) -> HandlerResult:
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
def test_alchemyupgrade_dbss(spec: Any, upgrade_result: HandlerResult) -> None:
    upgrade_result.check(spec)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_alchemyupgradeoffset_dbss(spec: Any, offset_result: HandlerResult) -> None:
    offset_result.check(spec)


def test_every_row_sits_in_the_group_of_its_stone_type() -> None:
    check_rows_sit_in_their_stone_group(load_binary_fixture(FILE_NAME), FILE_NAME)


def test_items_are_unique_per_stone_type(upgrade_result: HandlerResult) -> None:
    keys = [(r["stone_type"], r["item_id"]) for r in upgrade_result.records]
    assert len(keys) == len(set(keys))


def test_every_material_gives_experience(upgrade_result: HandlerResult) -> None:
    assert all(r["experience"] > 0 for r in upgrade_result.records)


def test_every_offset_row_points_at_its_material_row() -> None:
    check_offset_rows_point_at_main_rows(
        load_binary_fixture(FILE_NAME),
        parse_alchemyupgradeoffset_records(load_binary_fixture(OFFSET_FILE)),
    )


def test_a_small_table_reads_back() -> None:
    data = grouped_file([(0, 4052, 20408)], [(1, 4652, 18182)])
    assert parse_alchemyupgrade_records(data) == [
        {"stone_type": 0, "item_id": 4052, "experience": 20408},
        {"stone_type": 1, "item_id": 4652, "experience": 18182},
    ]


def test_experience_shows_as_a_percent() -> None:
    assert experience_text(20408) == "2.0408%"
    assert experience_text(250000) == "25%"

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
    case_id,
    header_count,
    run_case,
)

from _bss.houseinfo.parser import FILE_NAME as HOUSEINFO_FILE, parse_houseinfo
from _bss.mansionpartinfo.parser import parse_mansionpartinfo_records
from .parser import FILE_NAME


_MANSIONPARTINFO_FILE = "mansionpartinfo.bss"
# Blue Maned Lion's Manor: land 3814, building 3815; `_hidelOut` in the manor contract Lua.
_BLUE_MANED_LION_LAND = 3814
_BLUE_MANED_LION_BUILDING = 3815
_SECTOR_SCALE = 3


CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={_MANSIONPARTINFO_FILE: _MANSIONPARTINFO_FILE},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["name", "region", "quest"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(
            required_keys=[
                "land_character_key",
                "building_character_key",
                "need_point",
                "region_key",
                "sector_start",
                "sector_end",
                "unknown_20",
                "unknown_2c",
                "condition_quest_chain_id",
                "condition_quest_id",
                "day_pay",
                "unknown_40",
                "unknown_44",
                "unknown_48",
                "unknown_4c",
                "unknown_50",
                "unknown_51",
                "name",
                "region",
                "quest",
                "part_count",
            ],
        ),
        DeclaredCountTest(declared=header_count(offset=4)),
        TargetTest(
            col="land_character_key",
            value=_BLUE_MANED_LION_LAND,
            expected={
                "building_character_key": _BLUE_MANED_LION_BUILDING,
                "name": "Blue Maned Lion's Manor",
                "region": "Blue Maned Lion's Manor",
            },
        ),
    ],
)


@pytest.fixture(scope="module")
def mansionlandinfo_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_mansionlandinfo_bss(spec: Any, mansionlandinfo_result: HandlerResult) -> None:
    mansionlandinfo_result.check(spec)


def test_land_and_building_are_house_rows(mansionlandinfo_result: HandlerResult) -> None:
    house_keys = {house["character_key"] for house in parse_houseinfo(load_binary_fixture(HOUSEINFO_FILE)).houses}
    for record in mansionlandinfo_result.records:
        assert record["land_character_key"] in house_keys
        assert record["building_character_key"] in house_keys


def test_buildings_have_manor_parts(mansionlandinfo_result: HandlerResult) -> None:
    manors = {r["character_id"] for r in parse_mansionpartinfo_records(load_binary_fixture(_MANSIONPARTINFO_FILE))}
    assert {r["building_character_key"] for r in mansionlandinfo_result.records} <= manors
    assert all(r["part_count"] for r in mansionlandinfo_result.records)


def test_second_sector_box_is_the_first_times_three(mansionlandinfo_result: HandlerResult) -> None:
    for record in mansionlandinfo_result.records:
        assert record["unknown_20"] == [value * _SECTOR_SCALE for value in record["sector_start"]]
        assert record["unknown_2c"] == [value * _SECTOR_SCALE for value in record["sector_end"]]


def test_unlock_quest_has_a_title(mansionlandinfo_result: HandlerResult) -> None:
    """Each condition pair is a quest key with a LOC type 18 title."""
    for record in mansionlandinfo_result.records:
        prefix = f"{record['condition_quest_chain_id']}/{record['condition_quest_id']}"
        assert record["quest"].startswith(prefix + " "), record["quest"]

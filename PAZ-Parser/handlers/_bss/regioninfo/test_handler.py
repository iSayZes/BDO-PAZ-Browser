from __future__ import annotations

from dataclasses import replace
from typing import Any

import pytest

from _bss.regioninfo.parser import REGION_TYPE_NAMES
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


_MAIN_TOWN = REGION_TYPE_NAMES.index("MainTown")
_FLAGS = (
    "is_desert", "is_safe_zone", "is_arena_zone", "is_sea", "is_not_dig", "is_ocean",
    "is_prison", "is_accessible_area", "is_node_access", "is_locator", "is_ancient_dungeon",
    "is_escape", "is_special_zone", "is_vehicle_dead_zone", "is_free_revival_area",
    "is_world_boss_reward",
)

CASE = HandlerCase(
    handler_name="regioninfo.bss",
    data_file="regioninfo.bss",
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["Region", "Territory", "Capital", "Node", "Day Skill", "Night Skill", "Return Point", "Guild Wharf Manager"],
    internal_path="gamecommondata/binary/regioninfo.bss",
    tests=[
        SchemaTest(
            required_keys=[
                "region_key",
                "region_name",
                "name_kr",
                "region_type",
                "region_type_name",
                "node_war_day",
                "node_war_day_name",
                "is_desert",
                "territory_key",
                "territory",
                "capital_region_key",
                "capital",
                "region_group_key",
                "node_key",
                "node",
                "guild_wharf_manager_key",
                "guild_wharf_manager",
                "color",
                "is_safe_zone",
                "is_sea",
                "is_not_dig",
                "is_ocean",
                "is_prison",
                "is_accessible_area",
                "villain_respawn_node_key",
                "villain_respawn_position",
                "skill_no",
                "skill_apply_rate",
                "night_skill_no",
                "night_skill_apply_rate",
                "return_position_name",
                "return_position",
                "trade_origin_region_key",
                "waypoint_key",
                "is_free_revival_area",
                "is_world_boss_reward",
                "unknown_d2_keys",
                "unknown_d2_vectors",
                "max_participants",
                "siege_ap_limit",
                "siege_dr_rate_limit",
                "siege_resistance_limits",
                "unknown_tail_55",
            ],
        ),
        DeclaredCountTest(declared=header_count(offset=4)),
        # CppEnums.VillageSiegeType: Sunday 0 to Saturday 6, 7 for none.
        RangeTest(col="node_war_day", min_val=0, max_val=7),
        *[RangeTest(col=flag, min_val=0, max_val=1) for flag in _FLAGS],
        TargetTest(
            col="region_key",
            value=5,
            expected={
                "region_name": "Velia",
                "name_kr": "벨리아 마을",
                "is_safe_zone": 1,
                "return_position_name": "벨리아 마을",
                "return_point": "Velia",
                "trade_origin_region_key": 5,
                "region_type_name": "MainTown",
                "territory_key": 0,
                "territory": "Balenos",
                "capital_region_key": 5,
                "node_key": 1,
                "node": "1 Velia",
                "guild_wharf_manager_key": 40145,
                "guild_wharf_manager": "40145 Robert",
            },
        ),
        TargetTest(
            col="region_key",
            value=724,
            expected={
                "region_name": "Kamasylvia Castle",
                "region_type_name": "CastleInSiege",
                "territory": "Kamasylvia",
                "capital": "Grána",
                "guild_wharf_manager_key": 50989,
            },
        ),
        TargetTest(
            col="region_key",
            value=230,
            expected={
                "region_name": "The Great Desert of Valencia (Black Desert)",
                "is_desert": 1,
                "territory": "Valencia",
            },
        ),
    ],
)


@pytest.fixture(scope="module")
def regioninfo_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_regioninfo(spec: Any, regioninfo_result: HandlerResult) -> None:
    regioninfo_result.check(spec)


def test_region_keys_are_unique(regioninfo_result: HandlerResult) -> None:
    keys = [record["region_key"] for record in regioninfo_result.records]
    assert len(keys) == len(set(keys))


def test_each_territory_has_one_main_town_capital(regioninfo_result: HandlerResult) -> None:
    """The capital is the same for every region of a territory and is its MainTown."""
    records = {record["region_key"]: record for record in regioninfo_result.records}
    capitals: dict[int, set[int]] = {}
    for record in records.values():
        capitals.setdefault(record["territory_key"], set()).add(record["capital_region_key"])

    for territory_key, keys in capitals.items():
        assert len(keys) == 1, f"territory {territory_key} has capitals {sorted(keys)}"
        capital = records[next(iter(keys))]
        assert capital["region_type"] == _MAIN_TOWN
        assert capital["territory_key"] == territory_key



def test_node_war_limits_are_real_values(regioninfo_result: HandlerResult) -> None:
    """Regions with a participant cap carry limits, not the FLT_MAX / INT32_MAX filler."""
    for record in regioninfo_result.records:
        if not record["max_participants"]:
            continue
        assert record["siege_ap_limit"] < 3.0e38, record["region_key"]
        assert record["siege_dr_rate_limit"] != 0x7FFFFFFF, record["region_key"]

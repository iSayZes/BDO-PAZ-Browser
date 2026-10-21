from __future__ import annotations

from dataclasses import replace
from typing import Any

import pytest

from tests.fixtures import load_binary_fixture
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
from tests.hunting_ground_indexes import character_hunting_ground_index, hunting_ground_name_kr_index
from tests.runner import load_case

from _bss.dropuihuntinggroundinfo.parser import parse_hunting_ground_records
from _common.hunting_ground import DROPUIHUNTINGGROUNDINFO_PATH
from _common.lookup_index import IndexKind


_OFFSET_FILE = "monstergroupoffset.dbss"
# The 1,000,000 = 100% scale; the last member of a group always holds it.
_FULL_PERCENT = 1_000_000
# Group 1 is the Altar Imp test group of the source sheet.
_ALTAR_IMP_GROUP = 1
_ALTAR_IMP = 20066
# Group 2 is the Abandoned Iron Mine group of the source sheet (`#GroupName`).
_IRON_MINE_GROUP = 2
_IRON_MINE = "Abandoned Iron Mine"

GROUP_CASE = HandlerCase(
    handler_name="monstergroup.dbss",
    data_file="monstergroup.dbss",
    companion_files={_OFFSET_FILE: _OFFSET_FILE},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["monsters"],
    internal_path="gamecommondata/binary/monstergroup.dbss",
    lookup_indexes={
        IndexKind.CHARACTER_HUNTING_GROUNDS: character_hunting_ground_index,
        IndexKind.HUNTING_GROUND_NAME_KR: hunting_ground_name_kr_index,
    },
    tests=[
        SchemaTest(
            required_keys=[
                "group_key",
                "member_count",
                "members",
                "monsters",
                "hunting_ground_keys",
                "hunting_grounds",
            ]
        ),
        DeclaredCountTest(declared=header_count(offset=0)),
        DeclaredCountTest(declared=header_count(offset=0, companion=_OFFSET_FILE)),
        TargetTest(col="group_key", value=_ALTAR_IMP_GROUP, expected={"group_key": _ALTAR_IMP_GROUP}),
    ],
)

OFFSET_CASE = HandlerCase(
    handler_name=_OFFSET_FILE,
    data_file=_OFFSET_FILE,
    companion_files={},
    loc_file=None,
    uses_loc=False,
    loc_fields=[],
    internal_path=f"gamecommondata/binary/{_OFFSET_FILE}",
    tests=[
        SchemaTest(required_keys=["group_key", "offset", "size"]),
        DeclaredCountTest(declared=header_count(offset=0)),
        RangeTest(col="group_key", min_val=1, max_val=0xFFFF),
        TargetTest(col="group_key", value=_ALTAR_IMP_GROUP, expected={}),
    ],
)


@pytest.fixture(scope="module")
def group_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_GROUP_RESULT", None)
    if result is None:
        result = run_case(replace(GROUP_CASE, tests=[]))
        request.module._GROUP_RESULT = result
    return result


@pytest.fixture(scope="module")
def offset_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_OFFSET_RESULT", None)
    if result is None:
        result = run_case(replace(OFFSET_CASE, tests=[]))
        request.module._OFFSET_RESULT = result
    return result


@pytest.mark.parametrize("spec", GROUP_CASE.tests, ids=case_id)
def test_monstergroup_dbss(spec: Any, group_result: HandlerResult) -> None:
    group_result.check(spec)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_monstergroupoffset_dbss(spec: Any, offset_result: HandlerResult) -> None:
    offset_result.check(spec)


def test_member_count_matches_the_member_list(group_result: HandlerResult) -> None:
    for record in group_result.records:
        assert len(record["members"]) == record["member_count"], record["group_key"]
        assert len(record["monsters"]) == record["member_count"], record["group_key"]


def test_every_group_ends_on_a_full_percent(group_result: HandlerResult) -> None:
    """The last member is picked for sure; no member goes past 100%."""
    for record in group_result.records:
        percents = [member["percent"] for member in record["members"]]
        assert all(0 < percent <= _FULL_PERCENT for percent in percents), record["group_key"]
        if percents:
            assert percents[-1] == _FULL_PERCENT, record["group_key"]


def test_altar_imp_is_named(group_result: HandlerResult) -> None:
    group = next(r for r in group_result.records if r["group_key"] == _ALTAR_IMP_GROUP)
    index = [m["character_key"] for m in group["members"]].index(_ALTAR_IMP)
    assert group["monsters"][index].startswith("Altar Imp (")


def _group(result: HandlerResult, group_key: int) -> dict:
    return next(r for r in result.records if r["group_key"] == group_key)


def test_hunting_grounds_are_the_zones_that_list_a_member(group_result: HandlerResult) -> None:
    """Every dropuihuntinggroundinfo.bss zone whose monster list holds a member, ascending, and no other."""
    zones = parse_hunting_ground_records(load_binary_fixture("dropuihuntinggroundinfo.bss"))
    for record in group_result.records:
        members = {member["character_key"] for member in record["members"]}
        expected = sorted(zone["key"] for zone in zones if members.intersection(zone["monster_ids"]))
        assert record["hunting_ground_keys"] == expected, record["group_key"]
        assert len(record["hunting_grounds"]) == len(expected), record["group_key"]
        assert all(record["hunting_grounds"]), record["group_key"]


def test_iron_mine_group_names_its_zone(group_result: HandlerResult) -> None:
    group = _group(group_result, _IRON_MINE_GROUP)
    assert any(_IRON_MINE in name for name in group["hunting_grounds"]), group["hunting_grounds"]


def test_hunting_ground_cell_links_each_zone_to_its_row(group_result: HandlerResult) -> None:
    group = _group(group_result, _IRON_MINE_GROUP)

    html = load_case(GROUP_CASE).handler.render_records_page([group], 0, 1)

    for key in group["hunting_ground_keys"]:
        assert (
            f'data-path="{DROPUIHUNTINGGROUNDINFO_PATH}" data-field="key" data-value="{key}"'
        ) in html


def test_group_without_a_zone_shows_an_empty_cell(group_result: HandlerResult) -> None:
    """The Altar Imp test group shares no member with a drop window hunting ground."""
    group = _group(group_result, _ALTAR_IMP_GROUP)
    assert group["hunting_ground_keys"] == []
    assert group["hunting_grounds"] == []

    html = load_case(GROUP_CASE).handler.render_records_page([group], 0, 1)

    # The Hunting Grounds column is the last cell of the row.
    assert DROPUIHUNTINGGROUNDINFO_PATH not in html
    assert '<td class="">-</td></tr>' in html

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
    TargetTest,
    case_id,
    header_count,
    run_case,
)


_OFFSET_FILE = "monstergroupoffset.dbss"
# The 1,000,000 = 100% scale; the last member of a group always holds it.
_FULL_PERCENT = 1_000_000
# Group 1 is the Altar Imp test group of the source sheet.
_ALTAR_IMP_GROUP = 1
_ALTAR_IMP = 20066

GROUP_CASE = HandlerCase(
    handler_name="monstergroup.dbss",
    data_file="monstergroup.dbss",
    companion_files={_OFFSET_FILE: _OFFSET_FILE},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["monsters"],
    internal_path="gamecommondata/binary/monstergroup.dbss",
    tests=[
        SchemaTest(required_keys=["group_key", "member_count", "members", "monsters"]),
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

from __future__ import annotations

import re
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

from .parser import FILE_NAME


# PABR magic, then the u32 count.
_COUNT_OFFSET = 4
# The Tuvala main weapons; quest 41009 / 1 tests it with both condition calls.
_TUVALA_MAIN_WEAPONS = 11
# The files whose condition scripts name a group key here.
_CONDITION_FILES = ("quest.dbss", "detail_dialog.dbss")
_GROUP_CALL = re.compile(r"(?:checkequipitemgroup|checkinventoryitemgroup)\((\d+),", re.IGNORECASE)

CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["items"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=["group_key", "group_key_dup", "item_count", "item_ids", "items"]),
        DeclaredCountTest(declared=header_count(offset=_COUNT_OFFSET)),
        TargetTest(
            col="group_key",
            value=_TUVALA_MAIN_WEAPONS,
            expected={"group_key_dup": _TUVALA_MAIN_WEAPONS},
        ),
        UserLanguageTest(fields=["items"]),
    ],
)


@pytest.fixture(scope="module")
def itemequipgroup_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_itemequipgroup_bss(spec: Any, itemequipgroup_result: HandlerResult) -> None:
    itemequipgroup_result.check(spec)


def test_group_keys_are_unique(itemequipgroup_result: HandlerResult) -> None:
    keys = [r["group_key"] for r in itemequipgroup_result.records]
    assert len(keys) == len(set(keys)), "a group key has two groups"


def test_every_group_repeats_its_key(itemequipgroup_result: HandlerResult) -> None:
    differing = [r["group_key"] for r in itemequipgroup_result.records if r["group_key_dup"] != r["group_key"]]
    assert not differing, f"groups whose key copy differs: {differing}"


def test_item_names_follow_the_item_ids(itemequipgroup_result: HandlerResult) -> None:
    for r in itemequipgroup_result.records:
        assert len(r["item_ids"]) == r["item_count"] == len(r["items"]), r["group_key"]


def test_every_condition_group_is_in_the_file(itemequipgroup_result: HandlerResult) -> None:
    keys = {r["group_key"] for r in itemequipgroup_result.records}
    named: set[int] = set()
    for name in _CONDITION_FILES:
        text = load_binary_fixture(name).decode("utf-16-le", errors="replace")
        named.update(int(key) for key in _GROUP_CALL.findall(text))
    assert named, "no condition names an equipment group"
    assert named <= keys, f"condition groups missing from {FILE_NAME}: {sorted(named - keys)}"

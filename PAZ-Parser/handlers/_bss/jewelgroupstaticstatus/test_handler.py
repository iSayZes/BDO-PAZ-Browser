from __future__ import annotations

from dataclasses import replace
from typing import Any

import pytest

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


_DATA_FILE = "jewelgroupstaticstatus.bss"
# The rows start after the PABR magic with this count.
_COUNT_OFFSET = 4
# The group the Dawn crystals of the Kharazad accessory slots belong to.
_DAWN = 103

CASE = HandlerCase(
    handler_name=_DATA_FILE,
    data_file=_DATA_FILE,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["name"],
    internal_path=f"gamecommondata/binary/{_DATA_FILE}",
    tests=[
        SchemaTest(required_keys=["group", "max_count", "name_kr", "name"]),
        DeclaredCountTest(declared=header_count(offset=_COUNT_OFFSET)),
        TargetTest(col="group", value=_DAWN, expected={"name_kr": "새벽", "name": "Dawn"}),
        # LOC type 121 keys every name by (group, max_count).
        UserLanguageTest(fields=["name"]),
    ],
)


@pytest.fixture(scope="module")
def group_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_jewelgroupstaticstatus_bss(spec: Any, group_result: HandlerResult) -> None:
    group_result.check(spec)


def test_groups_are_unique(group_result: HandlerResult) -> None:
    groups = [r["group"] for r in group_result.records]
    assert len(groups) == len(set(groups)), "a crystal group has two rows"


def test_every_group_has_a_limit(group_result: HandlerResult) -> None:
    # The crystal window only checks a limit above 0 (panel_window_jewelinven_all_1.luac).
    unlimited = [r["group"] for r in group_result.records if r["max_count"] <= 0]
    assert not unlimited, f"groups without a limit: {unlimited}"

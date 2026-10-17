from __future__ import annotations

from dataclasses import replace
from typing import Any

import pytest

from _common.lookup_index import IndexKind
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

# Grave Digging I to IV, one skill number per rank.
_GRAVE_DIGGING_GROUP = 578
_GRAVE_DIGGING_ICON = "ui_texture/icon/new_icon/04_pc_skill/01_pc_skill/01_phm_skill/phm_skill_1759.dds"

CASE = HandlerCase(
    handler_name="skillgroup.bss",
    data_file="skillgroup.bss",
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["Name", "Skills"],
    internal_path="gamecommondata/binary/skillgroup.bss",
    # The group's icon is its first rank's, Grave Digging I (skill 1759).
    lookup_indexes={IndexKind.SKILL_ICON: {1759: _GRAVE_DIGGING_ICON}},
    tests=[
        SchemaTest(required_keys=["group_no", "icon_path", "name", "ranks", "skill_keys", "skill_nos", "skills"]),
        DeclaredCountTest(declared=header_count(offset=0)),
        TargetTest(
            col="group_no",
            value=_GRAVE_DIGGING_GROUP,
            expected={
                "name": "Grave Digging I",
                "skill_nos": [1759, 1760, 1761, 1762],
                "icon_path": _GRAVE_DIGGING_ICON,
            },
        ),
    ],
)


@pytest.fixture(scope="module")
def skillgroup_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_skillgroup_bss(spec: Any, skillgroup_result: HandlerResult) -> None:
    skillgroup_result.check(spec)


def test_group_numbers_are_unique(skillgroup_result: HandlerResult) -> None:
    numbers = [r["group_no"] for r in skillgroup_result.records]
    assert len(numbers) == len(set(numbers))


def test_every_group_has_a_rank(skillgroup_result: HandlerResult) -> None:
    assert all(r["ranks"] >= 1 and 0 not in r["skill_keys"] for r in skillgroup_result.records)

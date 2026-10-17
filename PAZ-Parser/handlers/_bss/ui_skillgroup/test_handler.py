from __future__ import annotations

from dataclasses import replace
from typing import Any

import pytest

from _common.lookup_index import IndexKind
from tests.framework import (
    HandlerCase,
    HandlerResult,
    RangeTest,
    SchemaTest,
    TargetTest,
    case_id,
    run_case,
)

_COMPANIONS = {"skillgroup.bss": "skillgroup.bss", "stringtable.bss": "stringtable.bss"}
_CLASS_TYPE_DRAKANIA = 7
# Granted by Taebaek's Belt; every class lists it in the Ascension Skill tab.
_BLESSING_OF_TAEBAEK_GROUP = 186
# Drakania awakening: the Main Skills entry usable with the Elvia weapon buff,
# and the two Tip of the Scale groups, one per blood tab.
_ELVIA_EDICT_UNBOUND_GROUP = 12607
_HEXEBLOOD_TIP_OF_THE_SCALE_GROUP = 12568
_DRAGONBLOOD_TIP_OF_THE_SCALE_GROUP = 12583
_BLESSING_OF_TAEBAEK_SKILL = 10189
_BLESSING_OF_TAEBAEK_ICON = "ui_texture/icon/new_icon/04_pc_skill/01_pc_skill/00_common/common_skill_10189.dds"
_SUBGROUP_MAIN = 0
_SUBGROUP_HEXEBLOOD = 1
_SUBGROUP_DRAGONBLOOD = 2

_REQUIRED_KEYS = [
    "class_type", "class", "subgroup", "tab", "card_column", "card_column_label",
    "row", "column", "group_no", "skill_no", "icon_path", "skill",
]


def _window_case(window: str, tests: list) -> HandlerCase:
    name = f"ui_skillgroup_{window}.bss"
    return HandlerCase(
        handler_name=name,
        data_file=name,
        companion_files=_COMPANIONS,
        loc_file="languagedata_en.loc",
        uses_loc=True,
        loc_fields=["Class", "Tab", "Skill"],
        internal_path=f"gamecommondata/binary/{name}",
        lookup_indexes={IndexKind.SKILL_ICON: {_BLESSING_OF_TAEBAEK_SKILL: _BLESSING_OF_TAEBAEK_ICON}},
        tests=tests,
    )


COMBAT_CASE = _window_case("combat", [
    SchemaTest(required_keys=_REQUIRED_KEYS),
    RangeTest(col="card_column", min_val=0, max_val=2),
    RangeTest(col="class_type", min_val=0, max_val=100),
    TargetTest(
        col="group_no",
        value=_BLESSING_OF_TAEBAEK_GROUP,
        expected={"tab": "Ascension Skill", "skill": "Blessing of Taebaek", "icon_path": _BLESSING_OF_TAEBAEK_ICON},
    ),
])

AWAKENING_CASE = _window_case("awakening", [
    SchemaTest(required_keys=_REQUIRED_KEYS),
    RangeTest(col="card_column", min_val=0, max_val=2),
    TargetTest(
        col="group_no",
        value=_ELVIA_EDICT_UNBOUND_GROUP,
        expected={"class_type": _CLASS_TYPE_DRAKANIA, "subgroup": _SUBGROUP_MAIN, "tab": "Main Skills"},
    ),
    TargetTest(
        col="group_no",
        value=_HEXEBLOOD_TIP_OF_THE_SCALE_GROUP,
        expected={"class_type": _CLASS_TYPE_DRAKANIA, "subgroup": _SUBGROUP_HEXEBLOOD},
    ),
    TargetTest(
        col="group_no",
        value=_DRAGONBLOOD_TIP_OF_THE_SCALE_GROUP,
        expected={"class_type": _CLASS_TYPE_DRAKANIA, "subgroup": _SUBGROUP_DRAGONBLOOD},
    ),
])


def _result(request: Any, attr: str, case: HandlerCase) -> HandlerResult:
    result = getattr(request.module, attr, None)
    if result is None:
        result = run_case(replace(case, tests=[]))
        setattr(request.module, attr, result)
    return result


@pytest.fixture(scope="module")
def combat_result(request: Any) -> HandlerResult:
    return _result(request, "_COMBAT_RESULT", COMBAT_CASE)


@pytest.fixture(scope="module")
def awakening_result(request: Any) -> HandlerResult:
    return _result(request, "_AWAKENING_RESULT", AWAKENING_CASE)


@pytest.mark.parametrize("spec", COMBAT_CASE.tests, ids=case_id)
def test_ui_skillgroup_combat_bss(spec: Any, combat_result: HandlerResult) -> None:
    combat_result.check(spec)


@pytest.mark.parametrize("spec", AWAKENING_CASE.tests, ids=case_id)
def test_ui_skillgroup_awakening_bss(spec: Any, awakening_result: HandlerResult) -> None:
    awakening_result.check(spec)


def test_records_follow_the_skill_window_order(awakening_result: HandlerResult) -> None:
    order = [
        (r["class_type"], r["subgroup"], r["card_column"], r["row"], r["column"])
        for r in awakening_result.records
    ]
    assert order == sorted(order)


@pytest.mark.parametrize("result_name", ["combat_result", "awakening_result"])
def test_every_placed_group_is_a_skill_group(result_name: str, request: Any) -> None:
    # Every group a grid places is in skillgroup.bss, so each cell has a skill.
    result: HandlerResult = request.getfixturevalue(result_name)
    assert all(r["skill_no"] is not None for r in result.records)

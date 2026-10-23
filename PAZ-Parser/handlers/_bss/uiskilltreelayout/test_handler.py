from __future__ import annotations

import struct
from dataclasses import replace
from typing import Any

import pytest

from tests.framework import (
    DeclaredCountTest,
    HandlerCase,
    HandlerResult,
    RangeTest,
    SchemaTest,
    UserLanguageTest,
    case_id,
    run_case,
)
from tests.case_input import CaseInput

from .parser import SKILL_TREE_FILES, TERRITORY_POLICY_FILES


_GUILD_FILE = "uiguildskilltreelayout.bss"
# The trees whose skill cells name real skills; the fusion cells hold 0.
_NAMED_TREES = (_GUILD_FILE, *TERRITORY_POLICY_FILES)
_GRID_SIZE = struct.Struct("<II")
_GRID_SIZE_AT = 4
_CELL_SIZE = 4
_CELL_TYPE_AT = 0
_CELL_TYPE_SKILL = 2
# ge::UISkillTreeLayout_CellValueArrowType: None to Bottom.
_ARROW_TYPE_MAX = 4
_REQUIRED_KEYS = ["column", "row", "arrow_type", "skill_no", "icon_path", "skill"]


def _skill_cells(case_input: CaseInput) -> int:
    """Cells whose type byte is Skill, over the `width * height` cells the header declares."""
    data = case_input.data
    width, height = _GRID_SIZE.unpack_from(data, _GRID_SIZE_AT)
    start = _GRID_SIZE_AT + _GRID_SIZE.size
    return sum(
        1 for index in range(width * height) if data[start + index * _CELL_SIZE + _CELL_TYPE_AT] == _CELL_TYPE_SKILL
    )


def _tests(name: str) -> list:
    tests: list = [
        SchemaTest(required_keys=_REQUIRED_KEYS),
        DeclaredCountTest(declared=_skill_cells),
        RangeTest(col="arrow_type", min_val=0, max_val=_ARROW_TYPE_MAX),
    ]
    if name in _NAMED_TREES:
        tests.append(UserLanguageTest(fields=["skill"]))
    return tests


def _case(name: str) -> HandlerCase:
    return HandlerCase(
        handler_name=name,
        data_file=name,
        companion_files={},
        loc_file="languagedata_en.loc",
        uses_loc=True,
        loc_fields=["skill"],
        internal_path=f"gamecommondata/binary/{name}",
        tests=_tests(name),
    )


# Module-level cases, so tests/handler_cases.py finds each one.
GUILD_CASE = _case(_GUILD_FILE)
FUSION_CASE = _case("uifusionskilltreelayout.bss")
PRODUCT_CASE = _case("uiproductskilltreelayout.bss")
BALENOS_CASE, SERENDIA_CASE, CALPHEON_CASE, MEDIA_CASE, VALENCIA_CASE = (
    _case(name) for name in TERRITORY_POLICY_FILES
)
CASES = {
    case.data_file: case
    for case in (
        GUILD_CASE, FUSION_CASE, PRODUCT_CASE, BALENOS_CASE, SERENDIA_CASE, CALPHEON_CASE, MEDIA_CASE, VALENCIA_CASE
    )
}
_RESULTS: dict[str, HandlerResult] = {}


def _result(name: str) -> HandlerResult:
    if name not in _RESULTS:
        _RESULTS[name] = run_case(replace(CASES[name], tests=[]))
    return _RESULTS[name]


@pytest.mark.parametrize(
    ("name", "spec"),
    [(name, spec) for name, case in CASES.items() for spec in case.tests],
    ids=[f"{name}: {case_id(spec)}" for name, case in CASES.items() for spec in case.tests],
)
def test_uiskilltreelayout_bss(name: str, spec: Any) -> None:
    _result(name).check(spec)


@pytest.mark.parametrize("name", _NAMED_TREES)
def test_skill_cells_sit_on_slot_rows_and_columns(name: str) -> None:
    # The guild window treats even rows and columns as slots, odd ones as gaps.
    off_slot = [(r["column"], r["row"]) for r in _result(name).records if r["column"] % 2 or r["row"] % 2]
    assert not off_slot, off_slot


@pytest.mark.parametrize("name", _NAMED_TREES)
def test_every_skill_cell_names_a_skill(name: str) -> None:
    unnamed = [r["skill_no"] for r in _result(name).records if not r["skill"]]
    assert not unnamed, unnamed


def test_every_file_has_a_case() -> None:
    assert sorted(CASES) == sorted(SKILL_TREE_FILES)

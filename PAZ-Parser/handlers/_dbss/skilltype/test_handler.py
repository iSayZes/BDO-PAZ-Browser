from __future__ import annotations

from dataclasses import replace
from typing import Any

import pytest

from _dbss.commandtooltip.parser import FILE_NAME as COMMAND_TOOLTIP_FILE
from _dbss.skillsimply.parser import parse_skillsimply_records
from _dbss.skilltype.parser import build_skill_icon_index, build_skill_name_index
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
from tests.fixtures import load_binary_fixture

_OFFSET_FILE = "skilltypeoffset.dbss"
# A Warrior active skill and a guild passive, each with its icon folder.
_SEISMIC_STRIKE = 2733 << 16 | 1
_CALPHEON_FISHING_EXP = 62380 << 16 | 1
# The Archer's Awakening weapon skill.
_GREATBOW_OF_LIGHT = 3458 << 16 | 1
_AWAKENING_WEAPON = 1
_AWAKENING_BRANCH = 1
_ICON_ROOT = "ui_texture/icon/"
# The Archer's Evasion, whose key command is only in commandtooltip.dbss.
_EVASION = 3347 << 16 | 1

CASE = HandlerCase(
    handler_name="skilltype.dbss",
    data_file="skilltype.dbss",
    companion_files={_OFFSET_FILE: _OFFSET_FILE, COMMAND_TOOLTIP_FILE: COMMAND_TOOLTIP_FILE},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["Name", "PC Command", "Console Command"],
    internal_path="gamecommondata/binary/skilltype.dbss",
    tests=[
        SchemaTest(required_keys=[
            "skill_key", "skill_no", "icon_path", "name", "name_kr", "kind", "kind_label", "awakening_type",
            "awakening_type_label", "pattern_control", "pc_command", "console_command",
        ]),
        DeclaredCountTest(declared=header_count(offset=0)),
        DeclaredCountTest(declared=header_count(offset=4, companion=_OFFSET_FILE)),
        RangeTest(col="kind", min_val=0, max_val=2),
        RangeTest(col="awakening_type", min_val=_AWAKENING_WEAPON, max_val=_AWAKENING_WEAPON),
        TargetTest(
            col="skill_key", value=_SEISMIC_STRIKE, expected={"skill_no": 2733, "kind": 1, "awakening_type": None}
        ),
        TargetTest(
            col="skill_key",
            value=_GREATBOW_OF_LIGHT,
            expected={"awakening_type": _AWAKENING_WEAPON, "awakening_type_label": "Awakening Weapon"},
        ),
        TargetTest(col="skill_key", value=_CALPHEON_FISHING_EXP, expected={"skill_no": 62380, "kind": 2}),
        TargetTest(col="skill_key", value=_EVASION, expected={"pattern_control": "ARCHER_20"}),
    ],
)


@pytest.fixture(scope="module")
def skilltype_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_skilltype_dbss(spec: Any, skilltype_result: HandlerResult) -> None:
    skilltype_result.check(spec)


def test_icons_are_dds_under_the_icon_root(skilltype_result: HandlerResult) -> None:
    icons = [r["icon_path"] for r in skilltype_result.records if r["icon_path"]]
    assert icons
    assert all(path.startswith(_ICON_ROOT) and path == path.lower() and path.endswith(".dds") for path in icons)


@pytest.mark.parametrize(
    ("skill_key", "folder"),
    [(_SEISMIC_STRIKE, "/04_pc_skill/01_pc_skill/"), (_CALPHEON_FISHING_EXP, "/04_pc_skill/07_guild_skill/")],
)
def test_icon_folder(skill_key: int, folder: str, skilltype_result: HandlerResult) -> None:
    record = next(r for r in skilltype_result.records if r["skill_key"] == skill_key)
    assert folder in record["icon_path"]


def test_skill_icon_index_matches_the_icon_column(skilltype_result: HandlerResult) -> None:
    """IndexKind.SKILL_ICON is this table's icons by skill number."""
    source = skilltype_result.source
    index = build_skill_icon_index(source.data, source.file(_OFFSET_FILE))

    assert index == {r["skill_no"]: r["icon_path"] for r in skilltype_result.records if r["icon_path"]}


def test_skill_name_index_holds_the_korean_names(skilltype_result: HandlerResult) -> None:
    """IndexKind.SKILL_NAME_KR is this table's Korean names by skill number."""
    source = skilltype_result.source
    index = build_skill_name_index(source.data, source.file(_OFFSET_FILE))

    assert index == {r["skill_no"]: r["name_kr"] for r in skilltype_result.records if r["name_kr"]}


def test_records_open_in_skill_key_order(skilltype_result: HandlerResult) -> None:
    keys = [r["skill_key"] for r in skilltype_result.records]
    assert keys == sorted(keys)


def test_awakening_weapon_skills_are_on_the_awakening_branch(skilltype_result: HandlerResult) -> None:
    """`awakening_type` 1 implies `skillsimply.dbss` `branch` 1 (the reverse does not hold)."""
    simply = parse_skillsimply_records(
        load_binary_fixture("skillsimply.dbss"), load_binary_fixture("skillsimplyoffset.dbss")
    )
    branches = {record.skill_key: record.branch for record in simply}
    awakening = [r["skill_key"] for r in skilltype_result.records if r["awakening_type"] == _AWAKENING_WEAPON]

    assert awakening
    assert all(branches.get(key, _AWAKENING_BRANCH) == _AWAKENING_BRANCH for key in awakening)


def test_every_pattern_control_has_its_command(skilltype_result: HandlerResult) -> None:
    """`key_hash(pattern_control)` is a commandtooltip.dbss row, so each keyed skill shows a command."""
    keyed = [r for r in skilltype_result.records if r["pattern_control"]]

    assert keyed
    assert all(r["pc_command"] for r in keyed)

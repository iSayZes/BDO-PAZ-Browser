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

from _bss.pabr_values.guild_tables import GUILD_TABLES
from _bss.pabr_values.parser import parse_value_table
from _bss.uiskilltreelayout.parser import parse_skill_tree
from .parser import FILE_NAME, TREE_FILE_NAME


_ROW_COUNT_AT = 4
_COMMAND_TO_GATHER = 65070
_SPECIAL_RIGHT_FILE = "guildspecialskillright.bss"
_REQUIRED_KEYS = ["skill_level", "skill_no", "icon_path", "skill", "tree_column", "tree_row"]

CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={TREE_FILE_NAME: TREE_FILE_NAME},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["skill"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=_REQUIRED_KEYS),
        DeclaredCountTest(declared=header_count(offset=_ROW_COUNT_AT)),
        # The first guild skill with a grade list on every client (GuildSpecialSkillRight_Table, client 1784).
        TargetTest(col="skill_no", value=_COMMAND_TO_GATHER, expected={"skill_level": 1, "skill": "Command to Gather"}),
    ],
)


@pytest.fixture(scope="module")
def guildskill_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_guildskill_bss(spec: Any, guildskill_result: HandlerResult) -> None:
    guildskill_result.check(spec)


def test_every_skill_number_is_one_row(guildskill_result: HandlerResult) -> None:
    skill_nos = [record["skill_no"] for record in guildskill_result.records]
    assert len(skill_nos) == len(set(skill_nos))


def test_every_tree_skill_gets_its_cell(guildskill_result: HandlerResult) -> None:
    tree = parse_skill_tree(guildskill_result.source.companions[TREE_FILE_NAME], TREE_FILE_NAME)
    by_skill = {record["skill_no"]: record for record in guildskill_result.records}
    # Reversed, so a skill on several cells keeps its first one, as the handler does.
    cells = {cell.skill_no: (cell.column, cell.row) for cell in reversed(tree.skill_cells)}
    assert cells
    assert set(cells) <= set(by_skill), set(cells) - set(by_skill)
    for skill_no, record in by_skill.items():
        expected = cells.get(skill_no, (None, None))
        assert (record["tree_column"], record["tree_row"]) == expected, skill_no


def test_without_the_tree_no_skill_has_a_cell() -> None:
    result = run_case(replace(CASE, companion_files={}, tests=[]))
    assert result.records
    assert all(record["tree_column"] is None and record["tree_row"] is None for record in result.records)


def test_every_special_skill_is_a_guild_skill(guildskill_result: HandlerResult) -> None:
    (special_table,) = [table for table in GUILD_TABLES if table.file_name == _SPECIAL_RIGHT_FILE]
    special = {record["guild_skill_no"] for record in parse_value_table(load_binary_fixture(_SPECIAL_RIGHT_FILE), special_table)}
    guild_skills = {record["skill_no"] for record in guildskill_result.records}
    assert special and special <= guild_skills

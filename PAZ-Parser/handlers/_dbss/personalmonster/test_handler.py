from __future__ import annotations

import struct
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
    UserLanguageTest,
    case_id,
    fixed_rows,
    header_count,
    run_case,
)
from tests.offset_rows import offset_row_problems

from _common.character_link import CHARACTERSTATIC_OFFSET_FILE
from .parser import FILE_NAME, OFFSET_FILE, parse_personalmonsteroffset_rows


_COUNT_SIZE = 4
_OFFSET_ROW_SIZE = 10
# Red Nose and Dastard Bheg: CharacterKey 25501 and 25503 in the PersonalMonster_Table sheet of client 1784.
_RED_NOSE = 25501
_DASTARD_BHEG = 25503

CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={CHARACTERSTATIC_OFFSET_FILE: CHARACTERSTATIC_OFFSET_FILE},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["name", "description", "difficulty_name"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=[
            "character_key", "description_kr", "difficulty", "monster_image", "drop_item_count",
            "drop_item_keys", "unknown_drop_item_keys_00", "name", "difficulty_name", "description",
            "drop_item_names", "has_character_row",
        ]),
        DeclaredCountTest(declared=header_count(offset=0)),
        RangeTest(col="difficulty", min_val=1, max_val=3),
        TargetTest(col="character_key", value=_RED_NOSE, expected={"name": "Red Nose"}),
        TargetTest(col="character_key", value=_DASTARD_BHEG, expected={"name": "Dastard Bheg"}),
        UserLanguageTest(fields=["name", "description", "drop_item_names"]),
    ],
)

OFFSET_CASE = HandlerCase(
    handler_name=OFFSET_FILE,
    data_file=OFFSET_FILE,
    companion_files={},
    loc_file=None,
    uses_loc=False,
    loc_fields=[],
    internal_path=f"gamecommondata/binary/{OFFSET_FILE}",
    tests=[
        SchemaTest(required_keys=["character_key", "data_offset", "data_size"]),
        DeclaredCountTest(declared=header_count(offset=0)),
        DeclaredCountTest(declared=fixed_rows(_OFFSET_ROW_SIZE, header_size=_COUNT_SIZE)),
        TargetTest(col="character_key", value=_RED_NOSE, expected={"character_key": _RED_NOSE}),
    ],
)


@pytest.fixture(scope="module")
def monster_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.fixture(scope="module")
def offset_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_OFFSET_RESULT", None)
    if result is None:
        result = run_case(replace(OFFSET_CASE, tests=[]))
        request.module._OFFSET_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_personalmonster_dbss(spec: Any, monster_result: HandlerResult) -> None:
    monster_result.check(spec)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_personalmonsteroffset_dbss(spec: Any, offset_result: HandlerResult) -> None:
    offset_result.check(spec)


def test_drop_lists_match_their_counts(monster_result: HandlerResult) -> None:
    for record in monster_result.records:
        assert len(record["drop_item_keys"]) == record["drop_item_count"]
        assert len(record["drop_item_names"]) == record["drop_item_count"]


def test_every_difficulty_has_a_label(monster_result: HandlerResult) -> None:
    """Each difficulty reads its `LUA_PERSONALMONSTER_DIFFICULTY_<n>` text, not the bare number."""
    bare = [r["character_key"] for r in monster_result.records if r["difficulty_name"] == str(r["difficulty"])]
    assert not bare, bare


def test_every_boss_has_a_character_row(monster_result: HandlerResult) -> None:
    """Each key is a `characterstatic.dbss` character."""
    missing = [r["character_key"] for r in monster_result.records if not r["has_character_row"]]
    assert not missing, missing


def test_offset_rows_point_at_their_rows() -> None:
    rows = parse_personalmonsteroffset_rows(load_binary_fixture(OFFSET_FILE))
    problems = offset_row_problems(load_binary_fixture(FILE_NAME), rows, struct.Struct("<H"))
    assert not problems, problems

from __future__ import annotations

import struct
from collections import defaultdict
from dataclasses import replace
from typing import Any

import pytest

from tests.case_input import CaseInput
from tests.framework import (
    DeclaredCountTest,
    HandlerCase,
    HandlerResult,
    RangeTest,
    SchemaTest,
    TargetTest,
    UserLanguageTest,
    case_id,
    header_count,
    run_case,
)

from .parser import FILE_NAME


_COUNT_SIZE = 4
_GROUP_HEAD = struct.Struct("<III")
_ENTRY_SIZE = 21
_BLACK_STONE = 16001


def _declared_entries(source: CaseInput) -> int:
    """The entry counts the group heads declare, summed over the groups."""
    data = source.file(None)
    pos, total = _COUNT_SIZE, 0
    for _ in range(header_count(offset=0)(source)):
        _, weapon_count, armor_count = _GROUP_HEAD.unpack_from(data, pos)
        total += weapon_count + armor_count
        pos += _GROUP_HEAD.size + (weapon_count + armor_count) * _ENTRY_SIZE
    return total


CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["result_item_name"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(
            required_keys=[
                "difficulty", "is_weapon", "enchant_level", "result_item_key", "unknown_05", "unknown_0d",
                "difficulty_name", "gear", "result_item_name",
            ]
        ),
        DeclaredCountTest(declared=_declared_entries),
        # The difficulties the extraction window accepts: Easy, Normal and Hard.
        RangeTest(col="difficulty", min_val=1, max_val=3),
        TargetTest(col="result_item_key", value=_BLACK_STONE, expected={"result_item_name": "Black Stone"}),
        UserLanguageTest(fields=["result_item_name"]),
    ],
)


@pytest.fixture(scope="module")
def extract_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_extractblackstone_bss(spec: Any, extract_result: HandlerResult) -> None:
    extract_result.check(spec)


def test_each_list_counts_levels_up_from_one(extract_result: HandlerResult) -> None:
    """Every weapon and armor list of a difficulty holds levels 1, 2, 3, ... in order."""
    levels: dict[tuple[int, bool], list[int]] = defaultdict(list)
    for r in extract_result.records:
        levels[(r["difficulty"], r["is_weapon"])].append(r["enchant_level"])
    bad = {key: found for key, found in levels.items() if found != list(range(1, len(found) + 1))}
    assert not bad, bad


def test_every_difficulty_has_both_lists(extract_result: HandlerResult) -> None:
    kinds: dict[int, set[bool]] = defaultdict(set)
    for r in extract_result.records:
        kinds[r["difficulty"]].add(r["is_weapon"])
    assert all(found == {True, False} for found in kinds.values()), kinds


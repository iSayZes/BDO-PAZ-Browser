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
    case_id,
    fixed_rows,
    run_case,
)

from _bss.lifeexpmaxlevel.parser import parse_lifeexpmaxlevel_records
from _dbss.lifeexp.labels import LIFE_SKILLS
from _dbss.lifeexp.parser import parse_lifeexp_records


_U32 = struct.Struct("<I")

CASE = HandlerCase(
    handler_name="lifeexpmaxlevel.bss",
    data_file="lifeexpmaxlevel.bss",
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["life_skill_name", "max_rank"],
    internal_path="gamecommondata/binary/lifeexpmaxlevel.bss",
    tests=[
        SchemaTest(required_keys=["life_skill", "life_skill_name", "max_level", "max_rank"]),
        DeclaredCountTest(declared=fixed_rows(_U32.size)),
        RangeTest(col="life_skill", min_val=min(LIFE_SKILLS), max_val=max(LIFE_SKILLS)),
        TargetTest(col="life_skill", value=1, expected={"life_skill_name": "Fishing"}),
        TargetTest(col="life_skill", value=11, expected={"life_skill_name": "Barter"}),
    ],
)


@pytest.fixture(scope="module")
def lifeexpmaxlevel_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_lifeexpmaxlevel_bss(spec: Any, lifeexpmaxlevel_result: HandlerResult) -> None:
    lifeexpmaxlevel_result.check(spec)


def test_each_max_level_is_the_top_row_of_its_lifeexp_block(lifeexpmaxlevel_result: HandlerResult) -> None:
    rows = parse_lifeexp_records(load_binary_fixture("lifeexp.dbss"), load_binary_fixture("lifeexpoffset.dbss"))
    top_levels: dict[int, int] = {}
    for row in rows:
        top_levels[row["life_skill"]] = max(top_levels.get(row["life_skill"], 0), row["level"])
    max_levels = {record["life_skill"]: record["max_level"] for record in lifeexpmaxlevel_result.records}
    assert max_levels == top_levels


def test_a_partial_value_raises() -> None:
    with pytest.raises(ValueError, match="whole number"):
        parse_lifeexpmaxlevel_records(bytes(6))

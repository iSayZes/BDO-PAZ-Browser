from __future__ import annotations

from dataclasses import replace
from typing import Any

import pytest

from tests.fixtures import load_binary_fixture
from tests.framework import HandlerCase, HandlerResult, RangeTest, SchemaTest, TargetTest, case_id, run_case

from _dbss.skillfusion.parser import parse_skillfusion_records
from .parser import FILE_NAME, SLOT_COUNT


_WARRIOR = 0
_SKILLFUSION_FILE = "skillfusion.dbss"

CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["class"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=["class_type", "class", "slot", "skill_fusion_keys", "choice_count", "skill_nos", "skills"]),
        RangeTest(col="slot", min_val=0, max_val=SLOT_COUNT - 1),
        TargetTest(col="class_type", value=_WARRIOR, expected={"class": "Warrior"}),
    ],
)


@pytest.fixture(scope="module")
def slot_list_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_skillfusionslotlist_bss(spec: Any, slot_list_result: HandlerResult) -> None:
    slot_list_result.check(spec)


def test_keys_are_skillfusion_keys_in_their_slot(slot_list_result: HandlerResult) -> None:
    slot_by_key = {r["skill_fusion_key"]: r["slot_no"] for r in parse_skillfusion_records(load_binary_fixture(_SKILLFUSION_FILE))}
    misplaced = [
        (r["class_type"], r["slot"], key)
        for r in slot_list_result.records
        for key in r["skill_fusion_keys"]
        if slot_by_key.get(key) != r["slot"]
    ]
    assert not misplaced, misplaced[:5]


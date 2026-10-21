from __future__ import annotations

from dataclasses import replace
from typing import Any

import pytest

from _dbss.yachtdice.parser import FILE_NAME as DICE_FILE, KEY_FIELD as DICE_KEY, parse_yachtdice_records
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

from .parser import FILE_NAME


# Preset 26 rolls the five dice 1 to 5 (the DicePreset sheet of client 1784).
_PRESET_26 = 26

CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file=None,
    uses_loc=False,
    loc_fields=[],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=["dice_preset_key", "dice_preset_key_dup", "dice_keys", "dice_text"]),
        DeclaredCountTest(declared=header_count(offset=0)),
        TargetTest(col="dice_preset_key", value=_PRESET_26, expected={"dice_preset_key_dup": _PRESET_26}),
    ],
)


@pytest.fixture(scope="module")
def yachtdicepreset_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_yachtdicepreset_dbss(spec: Any, yachtdicepreset_result: HandlerResult) -> None:
    yachtdicepreset_result.check(spec)


def test_keys_repeat_inside_each_row(yachtdicepreset_result: HandlerResult) -> None:
    for r in yachtdicepreset_result.records:
        assert r["dice_preset_key_dup"] == r["dice_preset_key"], r["dice_preset_key"]


def test_every_die_is_in_the_dice_table(yachtdicepreset_result: HandlerResult) -> None:
    dice = {record[DICE_KEY] for record in parse_yachtdice_records(load_binary_fixture(DICE_FILE))}
    used = {key for r in yachtdicepreset_result.records for key in r["dice_keys"]}
    assert used <= dice, f"dice missing from {DICE_FILE}: {sorted(used - dice)}"

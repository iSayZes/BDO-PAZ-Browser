from __future__ import annotations

import struct
from dataclasses import replace
from typing import Any

import pytest

from tests.fixtures import load_binary_fixture
from tests.framework import HandlerCase, HandlerResult, RangeTest, SchemaTest, TargetTest, case_id, run_case

from .commands import command_tagged
from .parser import FILE_NAME


_CLASS_COUNT = struct.Struct("<I")
_CLASS_COUNT_AT = 4
# The Skill_Combo sheet of client 1784 has the columns Combo1 to Combo10.
_MAX_STEPS = 10
# Class type 1, the first class list of clients 1784 and 3482.
_HASHASHIN = 1

CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={"stringtable.bss": "stringtable.bss"},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["class"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=[
            "class_type", "class", "combo_no", "combo_skill_count", "skill_nos", "skills", "command_indexes", "commands",
        ]),
        RangeTest(col="combo_skill_count", min_val=1, max_val=_MAX_STEPS),
        TargetTest(col="class_type", value=_HASHASHIN, expected={"class": "Hashashin"}),
    ],
)


@pytest.fixture(scope="module")
def combo_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_skillcomboguide_bss(spec: Any, combo_result: HandlerResult) -> None:
    combo_result.check(spec)


def test_one_class_list_per_class(combo_result: HandlerResult) -> None:
    (class_count,) = _CLASS_COUNT.unpack_from(load_binary_fixture(FILE_NAME), _CLASS_COUNT_AT)
    assert len({r["class_type"] for r in combo_result.records}) == class_count


def test_combo_skill_count_is_the_step_count(combo_result: HandlerResult) -> None:
    mismatched = [
        (r["class_type"], r["combo_no"]) for r in combo_result.records if r["combo_skill_count"] != len(r["skill_nos"])
    ]
    assert not mismatched, mismatched


def test_combos_count_from_one_per_class(combo_result: HandlerResult) -> None:
    by_class: dict[int, list[int]] = {}
    for r in combo_result.records:
        by_class.setdefault(r["class_type"], []).append(r["combo_no"])
    gaps = {class_type: numbers for class_type, numbers in by_class.items() if numbers != list(range(1, len(numbers) + 1))}
    assert not gaps, gaps


def test_commands_keep_no_string_keys_or_brackets(combo_result: HandlerResult) -> None:
    unresolved = [command for r in combo_result.records for command in r["commands"] if "ComboSheet_" in command or "<" in command]
    assert not unresolved, unresolved[:5]


def test_command_tagged_unwraps_key_binds_and_keeps_unknown_keys() -> None:
    raw = "<{KeyBind:MoveLeft}> [/] <{KeyBind:MoveRight}> + [NoSuchKey]"
    assert command_tagged(raw, {}) == "{KeyBind:MoveLeft} [/] {KeyBind:MoveRight} + [NoSuchKey]"

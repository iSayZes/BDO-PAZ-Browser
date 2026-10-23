from __future__ import annotations

from dataclasses import replace
from typing import Any

import pytest

from tests.case_input import CaseInput
from tests.fixtures import load_binary_fixture
from tests.framework import DeclaredCountTest, HandlerCase, HandlerResult, RangeTest, SchemaTest, case_id, run_case

from .handler import COURSE_MODE_NAMES, course_mode_text
from .parser import FILE_NAME, parse_checkpoint_records, parse_snowboard


# Snowfall Crasher: Alpine Glide, the region of every course (snowboard_bss.md).
_ALPINE_GLIDE = 1176
_EFFECT_FILE_PREFIXES = ("fN_Event_Object_", "fCO_")
_ITEM_MODE = COURSE_MODE_NAMES.index("Item")


def _declared_checkpoints(source: CaseInput) -> int:
    return sum(course["checkpoint_count"] for course in parse_snowboard(source.data)["courses"])


CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file=None,
    uses_loc=False,
    loc_fields=[],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(
            required_keys=[
                "course_key",
                "name_ref",
                "name_kr",
                "mode",
                "checkpoint_count",
                "checkpoint_index",
                "next_checkpoint_index",
                "unknown_08",
                "unknown_30",
                "unknown_31",
            ]
        ),
        DeclaredCountTest(declared=_declared_checkpoints),
        RangeTest(col="mode", min_val=0, max_val=len(COURSE_MODE_NAMES) - 1),
    ],
)


@pytest.fixture(scope="module")
def snowboard_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_snowboard(spec: Any, snowboard_result: HandlerResult) -> None:
    snowboard_result.check(spec)


def test_every_course_has_a_name_and_a_unique_key() -> None:
    courses = parse_snowboard(load_binary_fixture(FILE_NAME))["courses"]
    assert courses
    assert len({course["course_key"] for course in courses}) == len(courses)
    assert all(course["name_kr"] for course in courses)


def test_one_course_is_the_item_mode_course() -> None:
    courses = parse_snowboard(load_binary_fixture(FILE_NAME))["courses"]
    assert sum(course["mode"] == _ITEM_MODE for course in courses) == 1


def test_each_course_chains_its_checkpoints_back_to_the_first() -> None:
    for course in parse_snowboard(load_binary_fixture(FILE_NAME))["courses"]:
        checkpoints = course["checkpoints"]
        indexes = [checkpoint["checkpoint_index"] for checkpoint in checkpoints]
        assert indexes == list(range(1, len(checkpoints) + 1)), course["course_key"]
        nexts = [checkpoint["next_checkpoint_index"] for checkpoint in checkpoints]
        assert nexts == indexes[1:] + indexes[:1], course["course_key"]


def test_the_head_names_the_alpine_glide_region() -> None:
    head = parse_snowboard(load_binary_fixture(FILE_NAME))["head"]
    assert head["region_key"] == _ALPINE_GLIDE
    assert head["effect_name"].startswith(_EFFECT_FILE_PREFIXES)


def test_every_effect_reference_names_an_effect_file() -> None:
    parsed = parse_snowboard(load_binary_fixture(FILE_NAME))
    assert parsed["items"] and parsed["effects"]
    for entry in parsed["items"] + parsed["effects"]:
        assert entry["first_effect_name"].startswith(_EFFECT_FILE_PREFIXES), entry
        second = entry["second_effect_name"]
        assert not second or second.startswith(_EFFECT_FILE_PREFIXES), entry


def test_the_mode_cell_shows_its_enum_name() -> None:
    assert course_mode_text(1) == "1 Speed"
    assert course_mode_text(7) == "7"


def test_a_short_string_table_start_raises() -> None:
    data = bytearray(load_binary_fixture(FILE_NAME))
    data[-8:-4] = (int.from_bytes(data[-8:-4], "little") - 1).to_bytes(4, "little")
    with pytest.raises(ValueError):
        parse_checkpoint_records(bytes(data))

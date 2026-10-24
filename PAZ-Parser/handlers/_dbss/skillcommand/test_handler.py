from __future__ import annotations

import struct
from dataclasses import replace
from typing import Any

import pytest

from tests.fixtures import load_binary_fixture
from tests.framework import (
    CaseInput,
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

from _bss.classskilllist.parser import FILE_NAME as CLASSSKILLLIST_FILE
from _bss.classskilllist.parser import parse_classskilllist_records
from .parser import FILE_NAME, OFFSET_FILE, parse_skillcommand_records, parse_skillcommandoffset_rows
from .records import skill_classes


_COUNT_SIZE = 4
_OFFSET_ROW_SIZE = 10
# The index points past the row's u16 skill number, at `skill_no_dup`.
_KEY = struct.Struct("<H")
_STR16_COUNT = struct.Struct("<Q")
# Ground Roar, the first Warrior skill of classskilllist.bss; its command uses Dash and Attack2.
_GROUND_ROAR = 216
# Wizard and Witch share Fireball's skill number.
_FIREBALL = 819
_WIZARD = 28
_WITCH = 31
# Tectonic Slam of Drakania's awakening, in the dragon form and the normal form (getExtraParam 2 and 1).
_TECTONIC_SLAM_DRAGON = 7036
_TECTONIC_SLAM_NORMAL = 7000
_DRAKANIA = 7
# War Cry of the old Shadow Arena rows; skill.dbss gives this number to another skill.
_SHADOW_ARENA_WAR_CRY = 17062
_FORM_NONE = 0
_FORM_DRAGON = 2


def _declared_rows(source: CaseInput) -> int:
    """The rows the index declares: one per index row."""
    return len(parse_skillcommandoffset_rows(source.file(OFFSET_FILE)))


CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={CLASSSKILLLIST_FILE: CLASSSKILLLIST_FILE, OFFSET_FILE: OFFSET_FILE},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["name", "command", "console_command", "classes"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=[
            "skill_no", "skill_no_dup", "command_kr", "name_kr", "icon_path", "pc_level_for_learning",
            "show_check", "awaken_command", "extra_param", "unknown_icon_path_07", "console_command_kr",
            "has_skill_link", "name", "icon", "command", "console_command", "class_types", "classes", "form",
        ]),
        DeclaredCountTest(declared=header_count(offset=0)),
        DeclaredCountTest(declared=_declared_rows),
        RangeTest(col="show_check", min_val=0, max_val=1),
        RangeTest(col="awaken_command", min_val=0, max_val=1),
        RangeTest(col="extra_param", min_val=_FORM_NONE, max_val=_FORM_DRAGON),
        TargetTest(
            col="skill_no",
            value=_GROUND_ROAR,
            expected={"skill_no_dup": _GROUND_ROAR, "classes": "Warrior", "awaken_command": 0, "has_skill_link": True},
        ),
        TargetTest(col="skill_no", value=_SHADOW_ARENA_WAR_CRY, expected={"has_skill_link": False}),
        TargetTest(col="skill_no", value=_FIREBALL, expected={"class_types": [_WIZARD, _WITCH]}),
        TargetTest(
            col="skill_no",
            value=_TECTONIC_SLAM_DRAGON,
            expected={"extra_param": _FORM_DRAGON, "form": "Dragon Form", "awaken_command": 1, "class_types": [_DRAKANIA]},
        ),
        TargetTest(
            col="skill_no",
            value=_TECTONIC_SLAM_NORMAL,
            expected={"extra_param": 1, "form": "Normal Form", "awaken_command": 1, "class_types": [_DRAKANIA]},
        ),
        UserLanguageTest(fields=["name", "command", "console_command"]),
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
        SchemaTest(required_keys=["skill_no", "data_offset", "data_size"]),
        DeclaredCountTest(declared=header_count(offset=0)),
        DeclaredCountTest(declared=fixed_rows(_OFFSET_ROW_SIZE, header_size=_COUNT_SIZE)),
    ],
)


@pytest.fixture(scope="module")
def skill_command_result(request: Any) -> HandlerResult:
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
def test_skillcommand_dbss(spec: Any, skill_command_result: HandlerResult) -> None:
    skill_command_result.check(spec)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_skillcommandoffset_dbss(spec: Any, offset_result: HandlerResult) -> None:
    offset_result.check(spec)


def test_offset_rows_point_at_their_rows() -> None:
    rows = parse_skillcommandoffset_rows(load_binary_fixture(OFFSET_FILE))
    problems = offset_row_problems(load_binary_fixture(FILE_NAME), rows, _KEY, lead=_KEY.size)
    assert not problems, problems


def test_every_row_repeats_its_skill_number() -> None:
    records = parse_skillcommand_records(load_binary_fixture(FILE_NAME))
    assert all(record["skill_no"] == record["skill_no_dup"] for record in records)
    assert len({record["skill_no"] for record in records}) == len(records)


def test_every_classskilllist_skill_has_a_row() -> None:
    """The Skill Guide reads each listed skill's command here, so every listed number is a key."""
    keys = {record["skill_no"] for record in parse_skillcommand_records(load_binary_fixture(FILE_NAME))}
    listed = {no for row in parse_classskilllist_records(load_binary_fixture(CLASSSKILLLIST_FILE)) for no in row.skill_nos}
    assert listed <= keys


def _str16(text: str) -> bytes:
    raw = text.encode("utf-16-le")
    return _STR16_COUNT.pack(len(raw) // 2) + raw


def _row(skill_no: int, extra_param: int) -> bytes:
    return (
        struct.pack("<HH", skill_no, skill_no)
        + _str16("<{KeyBind:Attack1}>")
        + _str16("화염구")
        + _str16("New_Icon/a.dds")
        + struct.pack("<IBBBI", 7, 1, 0, extra_param, 0)
        + _str16("")
    )


def test_parse_reads_each_field() -> None:
    data = struct.pack("<I", 2) + _row(819, 0) + _row(6820, 2)

    records = parse_skillcommand_records(data)

    assert [record["skill_no"] for record in records] == [819, 6820]
    assert records[0] == {
        "skill_no": 819,
        "skill_no_dup": 819,
        "command_kr": "<{KeyBind:Attack1}>",
        "name_kr": "화염구",
        "icon_path": "New_Icon/a.dds",
        "pc_level_for_learning": 7,
        "show_check": 1,
        "awaken_command": 0,
        "extra_param": 0,
        "unknown_icon_path_07": 0,
        "console_command_kr": "",
    }
    assert records[1]["extra_param"] == 2


def test_parse_rejects_rows_that_end_early() -> None:
    with pytest.raises(ValueError):
        parse_skillcommand_records(struct.pack("<I", 2) + _row(819, 0))


def test_parse_rejects_bytes_after_the_rows() -> None:
    with pytest.raises(ValueError):
        parse_skillcommand_records(struct.pack("<I", 1) + _row(819, 0) + b"\0")


def test_skill_classes_lists_each_class_once_per_skill() -> None:
    rows = struct.pack("<BQ3H", _WIZARD, 3, _FIREBALL, 820, _FIREBALL) + struct.pack("<BQH", _WITCH, 1, _FIREBALL)
    body = b"PABR" + struct.pack("<I", 2) + rows
    # An empty string table, then its start and the closing 0.
    data = body + struct.pack("<I", 0) + struct.pack("<II", len(body), 0)

    assert skill_classes(data) == {_FIREBALL: (_WIZARD, _WITCH), 820: (_WIZARD,)}
    assert skill_classes(None) == {}

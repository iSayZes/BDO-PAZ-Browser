from __future__ import annotations

import struct
from dataclasses import replace
from typing import Any

import pytest

from tests.case_input import CaseInput
from tests.fixtures import load_binary_fixture
from tests.framework import DeclaredCountTest, HandlerCase, HandlerResult, SchemaTest, TargetTest, UserLanguageTest, case_id, run_case

from _common.class_type import PLAYABLE_CLASSES_MASK, class_types_in_mask
from .parser import FILE_NAME, parse_class_lists, parse_cooltime_records


_U32 = struct.Struct("<I")
_LISTS_START = 4
_SKILL_SIZE = 4
_TRAILER_SIZE = 8
_NOVA = 9
_WIZARD = 28
_WITCH = 31
# Succession: Magical Evasion, the one skill of the Wizard and Witch lists (client 1784 and later).
_MAGICAL_EVASION = 4980
# Accel: Twisted Orbit, a Nova skill of every client's Nova list.
_TWISTED_ORBIT = 5879


def _declared_skills(source: CaseInput) -> int:
    """The skills the list counts declare between the magic and the string table."""
    data = source.data
    (table_start,) = _U32.unpack_from(data, len(data) - _TRAILER_SIZE)
    pos, skills = _LISTS_START, 0
    while pos < table_start:
        (skill_count,) = _U32.unpack_from(data, pos)
        pos += _U32.size + skill_count * _SKILL_SIZE
        skills += skill_count
    return skills


CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["class_name", "skill_name"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=["class_type", "skill_index", "show_type", "skill_no", "class_name", "skill_name"]),
        DeclaredCountTest(declared=_declared_skills),
        TargetTest(col="skill_no", value=_MAGICAL_EVASION, expected={"skill_name": "Succession: Magical Evasion"}),
        TargetTest(col="skill_no", value=_TWISTED_ORBIT, expected={"class_type": _NOVA, "class_name": "Nova"}),
        UserLanguageTest(fields=["class_name"]),
    ],
)


@pytest.fixture(scope="module")
def cooltime_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_classcooltimeuilist(spec: Any, cooltime_result: HandlerResult) -> None:
    cooltime_result.check(spec)


def test_there_is_a_list_for_every_playable_class_type() -> None:
    lists = parse_class_lists(load_binary_fixture(FILE_NAME))
    assert len(lists) > max(class_types_in_mask(PLAYABLE_CLASSES_MASK))


def test_wizard_and_witch_list_magical_evasion() -> None:
    lists = parse_class_lists(load_binary_fixture(FILE_NAME))
    for class_type in (_WIZARD, _WITCH):
        assert _MAGICAL_EVASION in [skill["skill_no"] for skill in lists[class_type]]


def test_each_skill_keeps_its_place_in_its_list(cooltime_result: HandlerResult) -> None:
    by_class: dict[int, list[int]] = {}
    for record in cooltime_result.records:
        by_class.setdefault(record["class_type"], []).append(record["skill_index"])
    for indexes in by_class.values():
        assert indexes == list(range(len(indexes)))


def _pabr(values: bytes) -> bytes:
    table_start = _LISTS_START + len(values)
    return b"PABR" + values + _U32.pack(0) + _U32.pack(table_start) + _U32.pack(0)


def test_an_empty_list_keeps_the_next_class_type() -> None:
    data = _pabr(_U32.pack(0) + _U32.pack(1) + struct.pack("<HH", 1, _MAGICAL_EVASION))
    (record,) = parse_cooltime_records(data)
    assert record == {"class_type": 1, "skill_index": 0, "show_type": 1, "skill_no": _MAGICAL_EVASION}


def test_a_skill_count_past_the_string_table_raises() -> None:
    with pytest.raises(ValueError, match="runs past"):
        parse_cooltime_records(_pabr(_U32.pack(2) + struct.pack("<HH", 1, _MAGICAL_EVASION)))

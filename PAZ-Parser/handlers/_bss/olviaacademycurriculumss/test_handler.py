from __future__ import annotations

import struct
from dataclasses import replace
from typing import Any

import pytest

from tests.case_input import CaseInput
from tests.framework import DeclaredCountTest, HandlerCase, HandlerResult, SchemaTest, TargetTest, case_id, run_case
from tests.quest_list_cases import quest_list_case

from _bss.allquestlist.olvia_academy import CURRICULUM_LIST, REWARD_LIST
from .handler import OlviaAcademyCurriculumBssHandler
from .parser import CURRICULUM_SECTION, FILE_NAME, REWARD_SECTION, parse_curriculum_records, row_ref


_U32 = struct.Struct("<I")
_U64 = struct.Struct("<Q")
# A str16 counts UTF-16 code units, a str8 bytes.
_WIDE, _ASCII = 2, 1
# Basic Tactics, the first Combat subject, starts at Sign Up for Course: (1 << 16) | 2310.
_COMBAT_SIGN_UP = 1 << 16 | 2310
_SUB_ID_DIGITS = 2


class _Walk:
    """Steps over the strings and counted lists of the file, for the declared row count."""

    def __init__(self, data: bytes) -> None:
        self.data, self.pos = data, 0

    def u32(self) -> int:
        (value,) = _U32.unpack_from(self.data, self.pos)
        self.pos += _U32.size
        return value

    def skip_text(self, unit: int) -> None:
        (length,) = _U64.unpack_from(self.data, self.pos)
        self.pos += _U64.size + length * unit


def _skip_subject(walk: _Walk) -> None:
    texts = walk.u32()
    for _ in range(texts):
        walk.skip_text(_WIDE)
    if texts:
        for unit in (_WIDE, _WIDE, _ASCII):
            walk.skip_text(unit)
    walk.u32()
    walk.skip_text(_WIDE)
    walk.skip_text(_WIDE)
    for _ in range(walk.u32()):
        walk.u32()
        walk.skip_text(_ASCII)


def _skip_curriculum(walk: _Walk) -> int:
    """Steps over one curriculum; its subject count."""
    walk.skip_text(_WIDE)
    walk.skip_text(_ASCII)
    subjects = walk.u32()
    for _ in range(subjects):
        _skip_subject(walk)
    return subjects


def _skip_reward(walk: _Walk) -> int:
    """Steps over one family reward; its reward group count."""
    for unit in (_WIDE, _WIDE, _WIDE, _ASCII):
        walk.skip_text(unit)
    groups = walk.u32()
    for _ in range(groups):
        walk.skip_text(_WIDE)
        quests = walk.u32()
        walk.pos += quests * _U32.size
    return groups


def _declared_rows(source: CaseInput) -> int:
    """The subjects and reward groups the counts declare, walked count by count."""
    walk = _Walk(source.data)
    rows = sum(_skip_curriculum(walk) for _ in range(walk.u32()))
    return rows + sum(_skip_reward(walk) for _ in range(walk.u32()))


CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["parent_text", "title_text", "start_quest_text"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(
            required_keys=[
                "section", "row_ref", "parent_index", "parent_text", "index", "title_text",
                "start_quest_text", "quest_count", "quests",
            ]
        ),
        DeclaredCountTest(declared=_declared_rows),
        TargetTest(
            col="row_ref",
            value=row_ref(CURRICULUM_SECTION, 0, 0),
            expected={
                "curriculum_title": "PANEL_OLVIA_ACADEMY_CURRICULM_BATTLE_TITLE",
                "subject_title": "PANEL_OLVIA_ACADEMY_SUBJECT_BATTLE_TITLE_1",
                "start_quest": _COMBAT_SIGN_UP,
                "parent_text": "Combat",
            },
        ),
        TargetTest(
            col="row_ref",
            value=row_ref(REWARD_SECTION, 0, 0),
            expected={"reward_title": "PANEL_OLVIA_ACADEMY_FAMILYREWARD_TITLE_BATTLE", "start_quest_text": None},
        ),
    ],
)


@pytest.fixture(scope="module")
def curriculum_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


def _section(result: HandlerResult, section: str) -> list[dict]:
    records = [record for record in result.records if record["section"] == section]
    assert records, section
    return records


def _list_quests(name: str) -> set[int]:
    return {record["packed_quest_id"] for record in run_case(replace(quest_list_case(name), tests=[])).records}


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_olviaacademycurriculumss(spec: Any, curriculum_result: HandlerResult) -> None:
    curriculum_result.check(spec)


def test_every_row_has_its_own_key(curriculum_result: HandlerResult) -> None:
    keys = [record["row_ref"] for record in curriculum_result.records]
    assert len(keys) == len(set(keys))


def test_every_subject_starts_at_its_first_quest(curriculum_result: HandlerResult) -> None:
    for record in _section(curriculum_result, CURRICULUM_SECTION):
        assert record["quests"] and record["start_quest"] == record["quests"][0], record["row_ref"]


def test_every_quest_texture_ends_in_its_sub_id(curriculum_result: HandlerResult) -> None:
    for record in _section(curriculum_result, CURRICULUM_SECTION):
        for quest, texture in zip(record["quests"], record["quest_texture_ids"], strict=True):
            assert texture.endswith(f"_{quest >> 16:0{_SUB_ID_DIGITS}d}"), (record["row_ref"], texture)


def test_a_preview_page_comes_with_its_texts(curriculum_result: HandlerResult) -> None:
    for record in _section(curriculum_result, CURRICULUM_SECTION):
        has_page = bool(record["preview_title"] and record["preview_desc"] and record["preview_texture_id"])
        assert has_page == bool(record["preview_texts"]), record["row_ref"]


def test_every_subject_quest_is_a_curriculum_list_quest(curriculum_result: HandlerResult) -> None:
    quests = {quest for record in _section(curriculum_result, CURRICULUM_SECTION) for quest in record["quests"]}
    assert quests <= _list_quests(CURRICULUM_LIST)


def test_the_reward_groups_hold_the_reward_list(curriculum_result: HandlerResult) -> None:
    quests = [quest for record in _section(curriculum_result, REWARD_SECTION) for quest in record["quests"]]
    assert len(quests) == len(set(quests))
    assert set(quests) == _list_quests(REWARD_LIST)


def test_every_quest_links_to_its_list(curriculum_result: HandlerResult) -> None:
    handler = OlviaAcademyCurriculumBssHandler()
    handler.lang = "en"
    html = handler.render_records_page(curriculum_result.records, 0, len(curriculum_result.records))
    assert f'data-path="gamecommondata/binary/{CURRICULUM_LIST}"' in html
    assert f'data-path="gamecommondata/binary/{REWARD_LIST}"' in html


def test_a_count_past_the_file_raises() -> None:
    with pytest.raises(ValueError, match="runs past"):
        parse_curriculum_records(_U32.pack(1))


def test_bytes_after_the_rewards_raise() -> None:
    with pytest.raises(ValueError, match="rewards end"):
        parse_curriculum_records(_U32.pack(0) + _U32.pack(0) + b"\x00")

from __future__ import annotations

from dataclasses import replace
from typing import Any

import pytest

from tests.fixtures import load_binary_fixture
from tests.framework import HandlerCase, HandlerResult, SchemaTest, TargetTest, case_id, run_case
from tests.quest_list_cases import QUEST_CASE, quest_list_case

from _bss.olviaacademycurriculumss.parser import CURRICULUM_SECTION, REWARD_SECTION, parse_curriculum_records
from _bss.olviaacademypassstaticstatusmanager.parser import parse_pass_records
from .handler import PLACE_FIELD, PLACE_REF_FIELD
from .olvia_academy import CURRICULUM_LIST as _CURRICULUM, LIST_PLACES, PASS_LIST as _PASS, REWARD_LIST as _REWARD

# The quest.dbss category whose records are exactly each list.
_CATEGORY = {_PASS: 17, _REWARD: 18, _CURRICULUM: 19}


def _academy_case(name: str, *extra: Any) -> HandlerCase:
    """A quest list case with the academy table that places its quests."""
    case = quest_list_case(name, SchemaTest(required_keys=[PLACE_FIELD, PLACE_REF_FIELD]), *extra)
    companion = LIST_PLACES[name].file_name
    return replace(case, companion_files={companion: companion})


CASES = {
    # Your First Steps In: (1 << 16) | 2308, the enrollment quest no subject lists.
    _CURRICULUM: _academy_case(
        _CURRICULUM,
        TargetTest(col="packed_quest_id", value=67844, expected={"quest_chain_id": 2308, "quest_id": 1, PLACE_FIELD: None}),
        # Sign Up for Course: (1 << 16) | 2310, the start of the first Combat subject.
        TargetTest(col="packed_quest_id", value=67846, expected={PLACE_FIELD: "Combat / Basic Tactics", PLACE_REF_FIELD: "curriculum:0:0"}),
    ),
    # Gathering Time! 1.: (101 << 16) | 2324, and its pass quest at sub ID 102.
    _PASS: _academy_case(
        _PASS,
        TargetTest(
            col="packed_quest_id",
            value=6621460,
            expected={"quest_chain_id": 2324, "quest_id": 101, PLACE_FIELD: "Collect / 1", PLACE_REF_FIELD: 6621460},
        ),
        TargetTest(col="packed_quest_id", value=6686996, expected={PLACE_FIELD: "Collect / 1", PLACE_REF_FIELD: 6621460}),
    ),
    # Combat Family Reward: (1 << 16) | 2323.
    _REWARD: _academy_case(
        _REWARD,
        TargetTest(
            col="packed_quest_id",
            value=67859,
            expected={"quest_chain_id": 2323, "quest_id": 1, PLACE_REF_FIELD: "reward:0:0"},
        ),
    ),
}


@pytest.fixture(scope="module")
def results(request: Any) -> dict[str, HandlerResult]:
    cached = getattr(request.module, "_HANDLER_RESULTS", None)
    if cached is None:
        cached = {name: run_case(replace(case, tests=[])) for name, case in CASES.items()}
        request.module._HANDLER_RESULTS = cached
    return cached


@pytest.mark.parametrize(
    ("name", "spec"),
    [(name, spec) for name, case in CASES.items() for spec in case.tests],
    ids=lambda value: value if isinstance(value, str) else case_id(value),
)
def test_olvia_academy_lists(name: str, spec: Any, results: dict[str, HandlerResult]) -> None:
    results[name].check(spec)


@pytest.mark.parametrize("name", list(_CATEGORY))
def test_each_list_is_its_quest_category_in_record_order(name: str, results: dict[str, HandlerResult]) -> None:
    quests = run_case(QUEST_CASE).records
    category = [
        record["packed_quest_id"]
        for record in quests
        if record["quest_category"] == _CATEGORY[name]
    ]
    assert [record["packed_quest_id"] for record in results[name].records] == category


def test_each_pass_base_quest_has_its_pass_quest_next(results: dict[str, HandlerResult]) -> None:
    # A pass step is the base quest at an odd sub ID and the pass quest at the next one.
    quest_ids = {record["quest_id"] for record in results[_PASS].records}
    base_ids = {quest_id for quest_id in quest_ids if quest_id % 2 == 1}
    pass_ids = quest_ids - base_ids
    assert {quest_id + 1 for quest_id in base_ids} == pass_ids


def _places(name: str, results: dict[str, HandlerResult]) -> dict[int, tuple[object, object]]:
    return {record["packed_quest_id"]: (record[PLACE_FIELD], record[PLACE_REF_FIELD]) for record in results[name].records}


def test_every_subject_quest_has_its_subject(results: dict[str, HandlerResult]) -> None:
    places = _places(_CURRICULUM, results)
    curriculum = parse_curriculum_records(load_binary_fixture(LIST_PLACES[_CURRICULUM].file_name))
    for record in curriculum:
        if record["section"] == CURRICULUM_SECTION:
            assert all(places[quest][1] == record["row_ref"] for quest in record["quests"]), record["row_ref"]


def test_every_reward_quest_has_its_reward_group(results: dict[str, HandlerResult]) -> None:
    places = _places(_REWARD, results)
    curriculum = parse_curriculum_records(load_binary_fixture(LIST_PLACES[_REWARD].file_name))
    groups = {quest: record["row_ref"] for record in curriculum if record["section"] == REWARD_SECTION for quest in record["quests"]}
    assert {quest: ref for quest, (_, ref) in places.items()} == groups


def test_every_pass_quest_has_its_step(results: dict[str, HandlerResult]) -> None:
    places = _places(_PASS, results)
    steps = parse_pass_records(load_binary_fixture(LIST_PLACES[_PASS].file_name))
    expected = {quest: step["base_quest"] for step in steps for quest in (step["base_quest"], step["pass_quest"])}
    assert {quest: ref for quest, (_, ref) in places.items()} == expected


def test_a_list_without_its_academy_table_shows_no_places() -> None:
    result = run_case(replace(CASES[_PASS], companion_files={}, tests=[]))
    assert result.records and all(record[PLACE_FIELD] is None for record in result.records)

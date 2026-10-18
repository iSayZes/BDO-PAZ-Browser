from __future__ import annotations

from dataclasses import replace
from typing import Any

import pytest

from tests.framework import (
    DeclaredCountTest,
    HandlerCase,
    HandlerResult,
    SchemaTest,
    TargetTest,
    TestSpec as Spec,
    case_id,
    header_count,
    run_case,
)


_CURRICULUM = "olviaacademycurriculumquestlist.bss"
_PASS = "olviaacademypassquestlist.bss"
_REWARD = "olviaacademyrewardquestlist.bss"

# The quest.dbss category whose records are exactly each list.
_CATEGORY = {_PASS: 17, _REWARD: 18, _CURRICULUM: 19}


def _case(name: str, *extra: Spec) -> HandlerCase:
    return HandlerCase(
        handler_name=name,
        data_file=name,
        companion_files={},
        loc_file="languagedata_en.loc",
        uses_loc=True,
        loc_fields=["Title"],
        internal_path=f"gamecommondata/binary/{name}",
        tests=[
            SchemaTest(required_keys=["slot", "packed_quest_id", "quest_chain_id", "quest_id", "title"]),
            # The u32 count after the PABR magic.
            DeclaredCountTest(declared=header_count(offset=4)),
            *extra,
        ],
    )


CASES = {
    # Your First Steps In: (1 << 16) | 2308.
    _CURRICULUM: _case(
        _CURRICULUM,
        TargetTest(col="packed_quest_id", value=67844, expected={"quest_chain_id": 2308, "quest_id": 1}),
    ),
    # Gathering Time! 1.: (101 << 16) | 2324.
    _PASS: _case(
        _PASS,
        TargetTest(col="packed_quest_id", value=6621460, expected={"quest_chain_id": 2324, "quest_id": 101}),
    ),
    # Combat Family Reward: (1 << 16) | 2323.
    _REWARD: _case(
        _REWARD,
        TargetTest(col="packed_quest_id", value=67859, expected={"quest_chain_id": 2323, "quest_id": 1}),
    ),
}

QUEST_CASE = HandlerCase(
    handler_name="quest.dbss",
    data_file="quest.dbss",
    companion_files={"allquestlist.bss": "allquestlist.bss"},
    loc_file=None,
    uses_loc=False,
    loc_fields=[],
    internal_path="gamecommondata/binary/quest.dbss",
    tests=[],
)


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

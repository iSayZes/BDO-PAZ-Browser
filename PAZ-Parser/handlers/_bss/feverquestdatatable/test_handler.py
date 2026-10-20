from __future__ import annotations

import re
from dataclasses import replace
from typing import Any

import pytest

from tests.framework import (
    DeclaredCountTest,
    HandlerCase,
    HandlerResult,
    SchemaTest,
    TargetTest,
    UserLanguageTest,
    case_id,
    header_count,
    run_case,
)

from .parser import FILE_NAME


# PABR magic, then the u32 count.
_COUNT_OFFSET = 4
_QUEST_FILE = "quest.dbss"
# Agris: Challenging the Bashims, the first Agris Fever quest.
_BASHIM_CHAIN = 9026
_BASHIM_QUEST = 1
_FEVER_CHECK = re.compile(r"checkFeverPoint\(\)>(\d+)")

CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["title"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(
            required_keys=[
                "quest_chain_id",
                "quest_id",
                "packed_quest_id",
                "consumption_fever_point",
                "title",
            ],
        ),
        DeclaredCountTest(declared=header_count(offset=_COUNT_OFFSET)),
        UserLanguageTest(fields=["title"]),
        TargetTest(
            col="packed_quest_id",
            value=_BASHIM_QUEST << 16 | _BASHIM_CHAIN,
            expected={
                "quest_chain_id": _BASHIM_CHAIN,
                "quest_id": _BASHIM_QUEST,
                "title": "Agris: Challenging the Bashims",
            },
        ),
    ],
)

QUEST_CASE = HandlerCase(
    handler_name=_QUEST_FILE,
    data_file=_QUEST_FILE,
    companion_files={"allquestlist.bss": "allquestlist.bss"},
    loc_file=None,
    uses_loc=False,
    loc_fields=[],
    internal_path=f"gamecommondata/binary/{_QUEST_FILE}",
    tests=[],
)


@pytest.fixture(scope="module")
def feverquestdatatable_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.fixture(scope="module")
def quests_by_id() -> dict[int, dict]:
    return {r["packed_quest_id"]: r for r in run_case(QUEST_CASE).records}


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_feverquestdatatable_bss(spec: Any, feverquestdatatable_result: HandlerResult) -> None:
    feverquestdatatable_result.check(spec)


def test_each_quest_has_one_row(feverquestdatatable_result: HandlerResult) -> None:
    keys = [r["packed_quest_id"] for r in feverquestdatatable_result.records]
    assert len(keys) == len(set(keys)), "a quest has two rows"


def test_every_row_is_a_quest_record(
    feverquestdatatable_result: HandlerResult,
    quests_by_id: dict[int, dict],
) -> None:
    listed = {r["packed_quest_id"] for r in feverquestdatatable_result.records}
    assert listed, f"{FILE_NAME} lists no quest"
    assert listed <= quests_by_id.keys(), f"quests missing from {_QUEST_FILE}: {sorted(listed - quests_by_id.keys())}"


def test_fever_check_matches_the_cost(
    feverquestdatatable_result: HandlerResult,
    quests_by_id: dict[int, dict],
) -> None:
    """A quest that checks its Agris Fever points checks for at least the row's cost."""
    for row in feverquestdatatable_result.records:
        script = quests_by_id[row["packed_quest_id"]]["condition_script"]
        for threshold in _FEVER_CHECK.findall(script):
            assert int(threshold) + 1 == row["consumption_fever_point"], row["packed_quest_id"]

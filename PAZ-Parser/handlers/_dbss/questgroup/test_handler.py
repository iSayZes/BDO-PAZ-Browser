from __future__ import annotations

from dataclasses import replace
from typing import Any

import pytest

from tests.framework import CountTest, HandlerCase, HandlerResult, PosTest, SchemaTest, TargetTest, case_id, run_case


CASE = HandlerCase(
    handler_name="questgroup.dbss",
    data_file="questgroup.dbss",
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["Name", "Quest Titles"],
    internal_path="gamecommondata/binary/questgroup.dbss",
    tests=[
        SchemaTest(required_keys=["group_id", "name", "quest_count", "quest_titles", "quest_titles_text"]),
        CountTest(expected=110),
        PosTest(
            pos=0,
            expected={
                "group_id": 1022,
                "name": "Sorceress, Beginning of the Journey",
                "quest_count": 3,
                "quest_titles": [
                    "Chiara's Kindness",
                    "Tom the Vigilante",
                    "A Skill Instructor of Olvia",
                ],
            },
        ),
        TargetTest(
            col="group_id",
            value=5801,
            expected={
                "name": "To the Wild Desert!",
                "quest_count": 4,
                "quest_titles_text": (
                    "Rest Area on the Barren Sand, Token of Lavania League, "
                    "Have You Ever Done This Before?, To the Wild Desert!"
                ),
            },
        ),
    ],
)


@pytest.fixture(scope="module")
def questgroup_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_questgroup_dbss(spec: Any, questgroup_result: HandlerResult) -> None:
    spec.check(questgroup_result.records)

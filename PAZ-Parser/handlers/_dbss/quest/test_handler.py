from __future__ import annotations

from dataclasses import replace
from typing import Any

import pytest

from tests.framework import CountTest, HandlerCase, HandlerResult, PosTest, SchemaTest, TargetTest, case_id, run_case


def _quest_record(record: dict) -> dict:
    loc_texts = record.get("loc_texts_en", [])
    mapped = dict(record)
    mapped["title_en"] = loc_texts[0] if loc_texts else ""
    mapped["objective_en"] = loc_texts[3] if len(loc_texts) > 3 else ""
    return mapped


CASE = HandlerCase(
    handler_name="quest.dbss",
    data_file="quest.dbss",
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["Title", "Objective"],
    internal_path="gamecommondata/binary/quest.dbss",
    record_mapper=_quest_record,
    tests=[
        SchemaTest(required_keys=["row", "packed_quest_id", "quest_chain_id", "quest_id", "title_en", "icon_path"]),
        CountTest(expected=19481),
        PosTest(
            pos=0,
            expected={
                "row": 0,
                "packed_quest_id": 1050655,
                "quest_chain_id": 2079,
                "quest_id": 16,
                "title_en": "[Elvia Weekly] Gigagord",
                "objective_en": "Defeat <Shadow of Nightmares> Gigagord;",
                "icon_path": "Icon/Quest/Hadum08.dds",
            },
        ),
        TargetTest(
            col="row",
            value=100,
            expected={
                "packed_quest_id": 1510453,
                "quest_chain_id": 3125,
                "quest_id": 23,
                "title_en": "Puzzling Words",
                "icon_path": "Icon/Quest/BalenosExplore_01.dds",
                "parse_status": "Icon-only",
            },
        ),
    ],
)


@pytest.fixture(scope="module")
def quest_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_quest_dbss(spec: Any, quest_result: HandlerResult) -> None:
    spec.check(quest_result.records)

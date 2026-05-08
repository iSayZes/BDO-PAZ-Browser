from __future__ import annotations

from dataclasses import replace
from typing import Any

import pytest

from tests.framework import CountTest, HandlerCase, HandlerResult, PosTest, SchemaTest, TargetTest, case_id, run_case


CASE = HandlerCase(
    handler_name="zodiacsign.dbss",
    data_file="zodiacsign.dbss",
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["Name", "Traits"],
    internal_path="gamecommondata/binary/zodiacsign.dbss",
    tests=[
        SchemaTest(required_keys=["zodiac_id", "name", "float_count", "pairs_count", "constellation_name", "en_trait"]),
        CountTest(expected=12),
        PosTest(
            pos=0,
            expected={
                "zodiac_id": 1,
                "name": "Hammer",
                "float_count": 6,
                "pairs_count": 5,
                "constellation_name": "망치자리",
                "en_trait": "Brave, Conservative, Righteous, Collaborative, Hot-Blooded.  ",
            },
        ),
        TargetTest(
            col="zodiac_id",
            value=6,
            expected={
                "name": "Black Dragon",
                "float_count": 7,
                "pairs_count": 7,
                "constellation_name": "검은용자리",
                "en_trait": "Wealth and Fame, Noble, Delicate, Sensitive, Sociable.",
            },
        ),
        PosTest(
            pos=-1,
            expected={
                "zodiac_id": 12,
                "name": "Goblin",
                "float_count": 6,
                "pairs_count": 6,
                "constellation_name": "고블린자리",
                "en_trait": "Linguist, Strong Beliefs, Intellectual, Materialistic, Wise.",
            },
        ),
    ],
)


@pytest.fixture(scope="module")
def zodiacsign_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_zodiacsign_dbss(spec: Any, zodiacsign_result: HandlerResult) -> None:
    spec.check(zodiacsign_result.records)

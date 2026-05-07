from __future__ import annotations

from dataclasses import replace
from typing import Any

import pytest

from tests.framework import CountTest, HandlerCase, HandlerResult, PosTest, SchemaTest, TargetTest, case_id, run_case


CASE = HandlerCase(
    handler_name="mentaltheme.dbss",
    data_file="mentaltheme.dbss",
    companion_files={"mentalthemeoffset.dbss": "mentalthemeoffset.dbss"},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["Name", "Parent Name"],
    internal_path="gamecommondata/binary/mentaltheme.dbss",
    tests=[
        SchemaTest(required_keys=["theme_id", "name", "parent_id", "parent_name", "entry_count", "child_count"]),
        CountTest(expected=902),
        PosTest(
            pos=0,
            expected={
                "theme_id": 20120,
                "name": "Morning Light - Hwanghae Logs I",
                "parent_id": 20119,
                "parent_name": "Morning Light Logs - Hwanghae Province",
                "entry_count": 47,
                "child_count": 0,
            },
        ),
        TargetTest(
            col="theme_id",
            value=20304,
            expected={
                "name": "Calpheon City Adventure Log I",
                "parent_id": 20030,
                "parent_name": "Calpheon Logs",
                "energy_reward_1": "+1 at 3 entries",
                "energy_reward_2": "+3 at 10 entries",
                "entry_count": 10,
            },
        ),
    ],
)


@pytest.fixture(scope="module")
def mentaltheme_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_mentaltheme_dbss(spec: Any, mentaltheme_result: HandlerResult) -> None:
    spec.check(mentaltheme_result.records)

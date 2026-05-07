from __future__ import annotations

from dataclasses import replace
from typing import Any

import pytest

from tests.framework import CountTest, HandlerCase, HandlerResult, PosTest, SchemaTest, TargetTest, case_id, run_case


CASE = HandlerCase(
    handler_name="mentalcard.dbss",
    data_file="mentalcard.dbss",
    companion_files={"mentalcardoffset.dbss": "mentalcardoffset.dbss"},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["Knowledge Name", "Category Name"],
    internal_path="gamecommondata/binary/mentalcard.dbss",
    tests=[
        SchemaTest(required_keys=["entry_id", "entry_name", "node_id", "node_name"]),
        CountTest(expected=12087),
        PosTest(
            pos=0,
            expected={
                "entry_id": 15055,
                "entry_name": "Altar of Blood - The 11th Illusion",
                "node_id": 24114,
                "node_name": "Altar of Blood",
            },
        ),
        TargetTest(
            col="entry_id",
            value=304,
            expected={
                "entry_name": "Granbill",
                "node_id": 155,
                "node_name": "Elionism & the Delphe Knights",
            },
        ),
    ],
)


@pytest.fixture(scope="module")
def mentalcard_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_mentalcard_dbss(spec: Any, mentalcard_result: HandlerResult) -> None:
    spec.check(mentalcard_result.records)

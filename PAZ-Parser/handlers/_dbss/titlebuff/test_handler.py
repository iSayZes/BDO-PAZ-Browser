from __future__ import annotations

from dataclasses import replace
from typing import Any

import pytest

from tests.framework import CountTest, HandlerCase, HandlerResult, PosTest, SchemaTest, TargetTest, case_id, run_case


BUFF_CASE = HandlerCase(
    handler_name="titlebufflist.dbss",
    data_file="titlebufflist.dbss",
    companion_files={"titlebufflistoffset.dbss": "titlebufflistoffset.dbss"},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["Text"],
    internal_path="gamecommondata/binary/titlebufflist.dbss",
    tests=[
        SchemaTest(required_keys=["level", "required_titles", "text", "offset"]),
        CountTest(expected=18),
        PosTest(
            pos=0,
            expected={
                "level": 1,
                "required_titles": 50,
                "text": "Acquire x50: Luck +1",
                "offset": 4,
            },
        ),
        TargetTest(
            col="required_titles",
            value=2000,
            expected={
                "level": 18,
                "text": (
                    "Acquire x2,000: Luck +3 / "
                    "Max Energy +8 / "
                    "EXP +12% / "
                    "Max Stamina +200"
                ),
                "offset": 5562,
            },
        ),
    ],
)

OFFSET_CASE = HandlerCase(
    handler_name="titlebufflistoffset.dbss",
    data_file="titlebufflistoffset.dbss",
    companion_files={},
    loc_file=None,
    uses_loc=False,
    loc_fields=[],
    internal_path="gamecommondata/binary/titlebufflistoffset.dbss",
    tests=[
        SchemaTest(required_keys=["buff_id", "offset"]),
        CountTest(expected=18),
        PosTest(pos=0, expected={"buff_id": 0, "offset": 4}),
        PosTest(pos=-1, expected={"buff_id": 17, "offset": 5562}),
    ],
)


@pytest.fixture(scope="module")
def buff_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_BUFF_RESULT", None)
    if result is None:
        result = run_case(replace(BUFF_CASE, tests=[]))
        request.module._BUFF_RESULT = result
    return result


@pytest.fixture(scope="module")
def offset_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_OFFSET_RESULT", None)
    if result is None:
        result = run_case(replace(OFFSET_CASE, tests=[]))
        request.module._OFFSET_RESULT = result
    return result


@pytest.mark.parametrize("spec", BUFF_CASE.tests, ids=case_id)
def test_titlebufflist_dbss(spec: Any, buff_result: HandlerResult) -> None:
    spec.check(buff_result.records)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_titlebufflistoffset_dbss(spec: Any, offset_result: HandlerResult) -> None:
    spec.check(offset_result.records)

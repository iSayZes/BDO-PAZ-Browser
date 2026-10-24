from __future__ import annotations

from dataclasses import replace
from typing import Any

import pytest

from tests.framework import (
    DeclaredCountTest,
    HandlerCase,
    HandlerResult,
    RangeTest,
    SchemaTest,
    TargetTest,
    case_id,
    header_count,
    run_case,
)

from .parser import FILE_NAME, HEAD_SCRIPTS, TAIL_SCRIPTS


_PABR_COUNT_OFFSET = 4
# The `PHM` opening cutscene in Velia, the file's first trigger.
_WARRIOR_INTRO = "cutscene(CS_Velia_00_PHM_Start_0001.pas)"
_FIRST_SHOW = "WhenShow(1);"

CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file=None,
    uses_loc=False,
    loc_fields=[],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=["row", *HEAD_SCRIPTS, "repeat", *TAIL_SCRIPTS]),
        DeclaredCountTest(declared=header_count(offset=_PABR_COUNT_OFFSET)),
        TargetTest(col="execute", value=_WARRIOR_INTRO, expected={"once_condition": _FIRST_SHOW}),
        RangeTest(col="repeat", min_val=0, max_val=1),
    ],
)


@pytest.fixture(scope="module")
def experience_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_experiencedata_bss(spec: Any, experience_result: HandlerResult) -> None:
    experience_result.check(spec)


def test_every_row_has_something_to_run(experience_result: HandlerResult) -> None:
    for r in experience_result.records:
        assert r["execute"], r["row"]

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
    UserLanguageTest,
    case_id,
    header_count,
    run_case,
)


_DATA_FILE = "pcgrowthsimply.bss"
# The rows start after the PABR magic with this count.
_COUNT_OFFSET = 4

CASE = HandlerCase(
    handler_name=_DATA_FILE,
    data_file=_DATA_FILE,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["class_name"],
    internal_path=f"gamecommondata/binary/{_DATA_FILE}",
    tests=[
        SchemaTest(required_keys=["class_type", "name_index", "name_kr", "is_playable", "class_name"]),
        DeclaredCountTest(declared=header_count(offset=_COUNT_OFFSET)),
        TargetTest(col="class_type", value=0, expected={"name_kr": "워리어", "is_playable": True}),
        TargetTest(col="class_type", value=25, expected={"class_name": "Kunoichi", "is_playable": True}),
        # Ain, an unused class slot.
        TargetTest(col="class_type", value=14, expected={"is_playable": False}),
        UserLanguageTest(fields=["class_name"]),
    ],
)


@pytest.fixture(scope="module")
def pcgrowthsimply_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_pcgrowthsimply_bss(spec: Any, pcgrowthsimply_result: HandlerResult) -> None:
    pcgrowthsimply_result.check(spec)

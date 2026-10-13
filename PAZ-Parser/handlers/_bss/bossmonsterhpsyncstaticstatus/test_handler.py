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
    case_id,
    header_count,
    run_case,
)

from .parser import FILE_NAME

_GARMOTH = 23120

CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["name"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=[
            "key", "character_id", "name", "min_x", "min_z", "max_x", "max_z",
            "unknown_14", "unknown_16",
        ]),
        DeclaredCountTest(declared=header_count(offset=4)),
        TargetTest(col="character_id", value=_GARMOTH, expected={"name": "Garmoth"}),
    ],
)


@pytest.fixture(scope="module")
def hp_sync_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_bossmonsterhpsyncstaticstatus_bss(spec: Any, hp_sync_result: HandlerResult) -> None:
    hp_sync_result.check(spec)


def test_sector_boxes_are_ordered(hp_sync_result: HandlerResult) -> None:
    for r in hp_sync_result.records:
        assert r["min_x"] <= r["max_x"] and r["min_z"] <= r["max_z"]

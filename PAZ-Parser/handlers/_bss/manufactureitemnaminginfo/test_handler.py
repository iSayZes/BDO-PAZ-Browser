from __future__ import annotations

from dataclasses import replace
from typing import Any

import pytest

from tests.framework import (
    DeclaredCountTest,
    HandlerCase,
    HandlerResult,
    SchemaTest,
    case_id,
    header_count,
    run_case,
)

from .parser import FILE_NAME


# PABR magic, then the u32 count.
_COUNT_OFFSET = 4

CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["item_name"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=["item_id", "item_name", "icon_path"]),
        DeclaredCountTest(declared=header_count(offset=_COUNT_OFFSET)),
    ],
)


@pytest.fixture(scope="module")
def naming_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_manufactureitemnaminginfo_bss(spec: Any, naming_result: HandlerResult) -> None:
    naming_result.check(spec)


def test_every_row_names_an_item(naming_result: HandlerResult) -> None:
    unnamed = [r["item_id"] for r in naming_result.records if not r["item_name"]]
    assert not unnamed, f"item IDs without a LOC type 0 name: {unnamed}"

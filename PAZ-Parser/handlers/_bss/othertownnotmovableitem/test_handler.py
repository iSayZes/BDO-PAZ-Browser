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


_ARCHAEOLOGISTS_MAP = 16019

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
        # No magic: the u32 count opens the file.
        DeclaredCountTest(declared=header_count(offset=0)),
        TargetTest(
            col="item_id",
            value=_ARCHAEOLOGISTS_MAP,
            expected={"item_name": "Archaeologist's Map"},
        ),
    ],
)


@pytest.fixture(scope="module")
def othertownnotmovableitem_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_othertownnotmovableitem_bss(spec: Any, othertownnotmovableitem_result: HandlerResult) -> None:
    othertownnotmovableitem_result.check(spec)


def test_every_row_is_a_named_item(othertownnotmovableitem_result: HandlerResult) -> None:
    unnamed = [r["item_id"] for r in othertownnotmovableitem_result.records if not r["item_name"]]
    assert not unnamed, f"item IDs with no item name: {unnamed}"

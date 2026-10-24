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


_CLASS_COUNT_AT = 4
_WARRIOR = 0

CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["class"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=["class_type", "class", "width", "height", "blank_cells", "skill_cells", "skill_nos"]),
        DeclaredCountTest(declared=header_count(offset=_CLASS_COUNT_AT)),
        TargetTest(col="class_type", value=_WARRIOR, expected={"class": "Warrior"}),
    ],
)


@pytest.fixture(scope="module")
def layout_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_uipracticeskilltreelayout_bss(spec: Any, layout_result: HandlerResult) -> None:
    layout_result.check(spec)


def test_counted_cells_fit_the_grid(layout_result: HandlerResult) -> None:
    overfull = [
        r["class_type"] for r in layout_result.records if r["blank_cells"] + r["skill_cells"] > r["width"] * r["height"]
    ]
    assert not overfull, overfull


def test_class_types_are_unique(layout_result: HandlerResult) -> None:
    class_types = [r["class_type"] for r in layout_result.records]
    assert len(class_types) == len(set(class_types))

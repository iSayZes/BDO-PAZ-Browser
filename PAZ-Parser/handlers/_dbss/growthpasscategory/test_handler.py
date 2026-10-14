from __future__ import annotations

from dataclasses import replace
from typing import Any

import pytest

from _common.pabr_offset import parse_bare_u32_offset_rows
from _common.texture_string import TEXTURE_STRING_COMBINE
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


_OFFSET_FILE = "growthpasscategoryoffset.dbss"
# Each record opens with a copy of its key; the offset row points just past it.
_COUNT_SIZE = 4
_KEY_COPY_SIZE = 4
# `_hyperBoostCategoryKeyList = {9}` in panel_window_growthpass.luac.
_HYPERBOOST_KEY = 9

CASE = HandlerCase(
    handler_name="growthpasscategory.dbss",
    data_file="growthpasscategory.dbss",
    companion_files={_OFFSET_FILE: _OFFSET_FILE, TEXTURE_STRING_COMBINE: TEXTURE_STRING_COMBINE},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["Name"],
    internal_path="gamecommondata/binary/growthpasscategory.dbss",
    tests=[
        SchemaTest(required_keys=["category_key", "name", "name_kr", "icon_texture", "quest_chain_id"]),
        DeclaredCountTest(declared=header_count(offset=0)),
        TargetTest(col="category_key", value=_HYPERBOOST_KEY, expected={"name": "HYPERBOOST"}),
    ],
)

OFFSET_CASE = HandlerCase(
    handler_name=_OFFSET_FILE,
    data_file=_OFFSET_FILE,
    companion_files={},
    loc_file=None,
    uses_loc=False,
    loc_fields=[],
    internal_path=f"gamecommondata/binary/{_OFFSET_FILE}",
    tests=[
        SchemaTest(required_keys=["category_key", "offset", "size"]),
        DeclaredCountTest(declared=header_count(offset=0)),
    ],
)


@pytest.fixture(scope="module")
def category_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.fixture(scope="module")
def offset_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_OFFSET_RESULT", None)
    if result is None:
        result = run_case(replace(OFFSET_CASE, tests=[]))
        request.module._OFFSET_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_growthpasscategory_dbss(spec: Any, category_result: HandlerResult) -> None:
    category_result.check(spec)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_growthpasscategoryoffset_dbss(spec: Any, offset_result: HandlerResult) -> None:
    offset_result.check(spec)


def test_records_fill_the_file(category_result: HandlerResult) -> None:
    """Sorted by offset, the key copies and records cover every byte after the count."""
    source = category_result.source
    rows = sorted(parse_bare_u32_offset_rows(source.file(_OFFSET_FILE)), key=lambda row: row.offset)
    position = _COUNT_SIZE
    for row in rows:
        assert row.offset == position + _KEY_COPY_SIZE, f"gap or overlap before category {row.entry_id}"
        position = row.offset + row.size
    assert position == len(source.data)


def test_icons_resolve(category_result: HandlerResult) -> None:
    missing = [r["icon_texture"] for r in category_result.records if not r["icon_path"]]
    assert not missing

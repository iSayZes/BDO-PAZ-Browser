from __future__ import annotations

import struct
from dataclasses import replace
from typing import Any

import pytest

from tests.fixtures import load_binary_fixture
from tests.framework import (
    DeclaredCountTest,
    HandlerCase,
    HandlerResult,
    SchemaTest,
    TargetTest,
    UserLanguageTest,
    case_id,
    fixed_rows,
    header_count,
    run_case,
)
from tests.offset_rows import offset_row_problems

from _dbss.dyeingpalette.parser import FILE_NAME as PALETTE_FILE
from .parser import FILE_NAME, OFFSET_FILE, parse_itempaletteoffset_rows


_COUNT_SIZE = 4
_ROW_SIZE = 6
_OFFSET_ROW_SIZE = 12
# [Basic Dye] Light Rose: palette type 1, colour 12 in the DyeingItem_Table sheet of client 1784.
_LIGHT_ROSE = 17113

CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={PALETTE_FILE: PALETTE_FILE},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["item_name"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=["item_key", "palette_type", "palette_index", "item_name", "color_hex"]),
        DeclaredCountTest(declared=header_count(offset=0)),
        DeclaredCountTest(declared=fixed_rows(_ROW_SIZE, header_size=_COUNT_SIZE)),
        TargetTest(col="item_key", value=_LIGHT_ROSE, expected={"palette_type": 1, "palette_index": 12}),
        UserLanguageTest(fields=["item_name"]),
    ],
)

OFFSET_CASE = HandlerCase(
    handler_name=OFFSET_FILE,
    data_file=OFFSET_FILE,
    companion_files={},
    loc_file=None,
    uses_loc=False,
    loc_fields=[],
    internal_path=f"gamecommondata/binary/{OFFSET_FILE}",
    tests=[
        SchemaTest(required_keys=["item_key", "data_offset", "data_size"]),
        DeclaredCountTest(declared=header_count(offset=0)),
        DeclaredCountTest(declared=fixed_rows(_OFFSET_ROW_SIZE, header_size=_COUNT_SIZE)),
        TargetTest(col="item_key", value=_LIGHT_ROSE, expected={"data_size": _ROW_SIZE}),
    ],
)


@pytest.fixture(scope="module")
def palette_result(request: Any) -> HandlerResult:
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
def test_itempalette_dbss(spec: Any, palette_result: HandlerResult) -> None:
    palette_result.check(spec)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_itempaletteoffset_dbss(spec: Any, offset_result: HandlerResult) -> None:
    offset_result.check(spec)


def test_every_dye_item_has_a_palette_color(palette_result: HandlerResult) -> None:
    """Each `palette_type` and `palette_index` is a colour of `dyeingpalette.dbss`."""
    missing = [r["item_key"] for r in palette_result.records if r["color_hex"] is None]
    assert not missing, missing


def test_offset_rows_point_at_their_rows() -> None:
    rows = parse_itempaletteoffset_rows(load_binary_fixture(OFFSET_FILE))
    problems = offset_row_problems(load_binary_fixture(FILE_NAME), rows, struct.Struct("<I"))
    assert not problems, problems

from __future__ import annotations

import struct
from dataclasses import replace
from typing import Any

import pytest

from tests.case_input import CaseInput
from tests.fixtures import load_binary_fixture
from tests.framework import (
    DeclaredCountTest,
    HandlerCase,
    HandlerResult,
    SchemaTest,
    case_id,
    fixed_rows,
    header_count,
    run_case,
)
from tests.offset_rows import offset_row_problems

from _common.pabr_offset import parse_bare_u8_offset_rows
from _dbss.itempalette.parser import FILE_NAME as ITEM_PALETTE_FILE
from .parser import COLOR_SIZE, FILE_NAME, OFFSET_FILE, parse_dyeingpalette_rows


_COUNT_SIZE = 4
_OFFSET_ROW_SIZE = 9
# The palette type before the bytes an index row covers, and the u8 and the
# u64 colour count at their start.
_KEY_SIZE = 1
_ROW_HEAD_SIZE = 9
# [Basic Dye] Light Rose: palette type 1, colour 12 in the DyeingItem_Table sheet of client 1784.
_LIGHT_ROSE = 17113


def _indexed_colors(source: CaseInput) -> int:
    """The colours the index rows hold: each row's size past its head, in 12-byte colours."""
    return sum((row.size - _ROW_HEAD_SIZE) // COLOR_SIZE for row in parse_bare_u8_offset_rows(source.file(OFFSET_FILE)))


CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={ITEM_PALETTE_FILE: ITEM_PALETTE_FILE, OFFSET_FILE: OFFSET_FILE},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["item_names"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=[
            "palette_type", "unknown_01", "palette_index", "color_b", "color_g", "color_r", "color_a",
            "environment", "specular", "color_hex", "item_keys", "item_names",
        ]),
        DeclaredCountTest(declared=_indexed_colors),
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
        SchemaTest(required_keys=["palette_type", "data_offset", "data_size"]),
        DeclaredCountTest(declared=header_count(offset=0)),
        DeclaredCountTest(declared=fixed_rows(_OFFSET_ROW_SIZE, header_size=_COUNT_SIZE)),
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
def test_dyeingpalette_dbss(spec: Any, palette_result: HandlerResult) -> None:
    palette_result.check(spec)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_dyeingpaletteoffset_dbss(spec: Any, offset_result: HandlerResult) -> None:
    offset_result.check(spec)


def test_palette_count_matches_the_header() -> None:
    data = load_binary_fixture(FILE_NAME)
    rows = parse_dyeingpalette_rows(data)
    assert len(rows) == struct.unpack_from("<I", data)[0]
    for row in rows:
        assert row["color_count"] == len(row["colors"]), row["palette_type"]


def test_dye_item_sits_on_its_color(palette_result: HandlerResult) -> None:
    found = [r for r in palette_result.records if r["palette_type"] == 1 and r["palette_index"] == 12]
    assert len(found) == 1
    assert _LIGHT_ROSE in found[0]["item_keys"]


def test_offset_rows_point_past_the_palette_type() -> None:
    rows = parse_bare_u8_offset_rows(load_binary_fixture(OFFSET_FILE))
    problems = offset_row_problems(load_binary_fixture(FILE_NAME), rows, struct.Struct("<B"), lead=_KEY_SIZE)
    assert not problems, problems

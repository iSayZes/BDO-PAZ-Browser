from __future__ import annotations

import struct
from dataclasses import replace
from typing import Any

import pytest

from tests.framework import (
    CaseInput,
    DeclaredCountTest,
    HandlerCase,
    HandlerResult,
    RangeTest,
    SchemaTest,
    case_id,
    run_case,
)

from .parser import ATTACK_TABLES, FILE_NAME, GROUND_ROWS, SPECIAL_ATTACK_TABLES


_U32 = struct.Struct("<I")
_MAGIC_SIZE = 4
_TRAILER_SIZE = 8
_STRING_HEAD_SIZE = 5
_MAX_TABLE = 9
_MAX_SPECIAL_ROW = 500
_MAX_ARMOR = 99
_GROUND_ROW_COUNT = 30
_GROUND_COLUMNS = 5


def _empty_string_indices(data: bytes, table_start: int) -> set[int]:
    """Indices of the zero-length entries, read from the string table heads."""
    (count,) = _U32.unpack_from(data, table_start)
    pos, empty = table_start + 4, set()
    for index in range(count):
        (length,) = _U32.unpack_from(data, pos + 1)
        if length == 0:
            empty.add(index)
        pos += _STRING_HEAD_SIZE + length
    return empty


def _filled_refs(source: CaseInput) -> int:
    """Refs between the magic and the string table that point at a non-empty string."""
    data = source.data
    (table_start,) = _U32.unpack_from(data, len(data) - _TRAILER_SIZE)
    ref_count = (table_start - _MAGIC_SIZE) // _U32.size
    refs = struct.unpack_from(f"<{ref_count}I", data, _MAGIC_SIZE)
    empty = _empty_string_indices(data, table_start)
    return sum(1 for ref in refs if ref not in empty)


CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=False,
    loc_fields=[],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=["grid", "table_index", "row_index", "column_index", "effect_ref", "effect"]),
        DeclaredCountTest(declared=_filled_refs),
        RangeTest(col="table_index", min_val=0, max_val=_MAX_TABLE),
        RangeTest(col="row_index", min_val=0, max_val=_MAX_SPECIAL_ROW),
        RangeTest(col="column_index", min_val=0, max_val=_MAX_ARMOR),
    ],
)


@pytest.fixture(scope="module")
def effect_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_effectfilename_bss(spec: Any, effect_result: HandlerResult) -> None:
    effect_result.check(spec)


def test_every_grid_has_filled_cells(effect_result: HandlerResult) -> None:
    grids = {r["grid"] for r in effect_result.records}
    assert grids == {ATTACK_TABLES, SPECIAL_ATTACK_TABLES, GROUND_ROWS}


def test_ground_cells_have_no_table_and_fit_the_grid(effect_result: HandlerResult) -> None:
    for r in effect_result.records:
        if r["grid"] != GROUND_ROWS:
            assert r["table_index"] is not None, r
            continue
        assert r["table_index"] is None, r
        assert r["row_index"] < _GROUND_ROW_COUNT and r["column_index"] < _GROUND_COLUMNS, r


def test_basic_attack_on_common_animals_has_an_effect(effect_result: HandlerResult) -> None:
    """Attack table 0, weapon type 0 (basic attack), armor type 0 (common animals)."""
    keys = {(r["grid"], r["table_index"], r["row_index"], r["column_index"]) for r in effect_result.records}
    assert (ATTACK_TABLES, 0, 0, 0) in keys


def test_no_record_holds_an_empty_effect(effect_result: HandlerResult) -> None:
    assert all(r["effect"] for r in effect_result.records)

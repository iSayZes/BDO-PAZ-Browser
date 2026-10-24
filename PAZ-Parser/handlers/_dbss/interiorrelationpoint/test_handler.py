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
    case_id,
    header_count,
    run_case,
)

from .parser import (
    FILE_NAME,
    OFFSET_FILE,
    RELATION_FIELDS,
    parse_interiorrelationpoint_records,
    parse_interiorrelationpointoffset_rows,
)


# PABR magic and the u32 row count.
_PABR_HEADER_SIZE = 8
_ROW_SIZE = 66
# The index points past the u16 key, at its copy.
_KEY_SIZE = 2
_MELISSANDE_TABLE = 6252
_MELISSANDE_CHAIR = 6751

CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["name"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(
            required_keys=[
                "character_key", "character_key_dup", "matching_character_key", "matching_character_point",
                *RELATION_FIELDS, "name", "matching_character_name",
            ],
        ),
        DeclaredCountTest(declared=header_count(offset=4)),
        TargetTest(
            col="character_key",
            value=_MELISSANDE_TABLE,
            expected={
                "name": "Melissande Table",
                "matching_character_key": _MELISSANDE_CHAIR,
                "matching_character_name": f"{_MELISSANDE_CHAIR} Melissande Chair",
            },
        ),
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
        SchemaTest(required_keys=["character_key", "data_offset", "data_size"]),
        DeclaredCountTest(declared=header_count(offset=4)),
        TargetTest(col="character_key", value=_MELISSANDE_TABLE, expected={"character_key": _MELISSANDE_TABLE}),
    ],
)


@pytest.fixture(scope="module")
def relation_result(request: Any) -> HandlerResult:
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
def test_interiorrelationpoint_dbss(spec: Any, relation_result: HandlerResult) -> None:
    relation_result.check(spec)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_interiorrelationpointoffset_dbss(spec: Any, offset_result: HandlerResult) -> None:
    offset_result.check(spec)


def test_each_row_repeats_its_key(relation_result: HandlerResult) -> None:
    assert all(r["character_key"] == r["character_key_dup"] for r in relation_result.records)


def test_every_matching_character_has_a_row_of_its_own(relation_result: HandlerResult) -> None:
    keys = {r["character_key"] for r in relation_result.records}
    matching = {r["matching_character_key"] for r in relation_result.records if r["matching_character_key"]}

    assert matching
    assert matching <= keys


def test_offset_rows_point_past_the_key_of_every_row() -> None:
    """The index has no row sizes (`0`), so it is checked by its offsets alone."""
    data = load_binary_fixture(FILE_NAME)
    rows = parse_interiorrelationpointoffset_rows(load_binary_fixture(OFFSET_FILE))
    row_count = len(parse_interiorrelationpoint_records(data))
    starts = {_PABR_HEADER_SIZE + index * _ROW_SIZE + _KEY_SIZE for index in range(row_count)}

    assert {row.offset for row in rows} == starts
    for row in rows:
        (key,) = struct.unpack_from("<H", data, row.offset - _KEY_SIZE)
        assert key == row.entry_id

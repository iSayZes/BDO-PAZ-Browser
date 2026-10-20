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

from _common.item_key import split_item_key
from _common.pabr_offset import parse_bare_u32_offset_rows
from .parser import FILE_NAME, OFFSET_FILE, parse_waititem_records


_BLACKSTAR_SHIELD = 735001
_PEN = 20
_BLACKSTAR_SHIELD_PEN = _PEN << 24 | _BLACKSTAR_SHIELD
_COUNT_OFFSET = 0
_KEY_SIZE = 4
_ROW_SIZE = 17


CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["item_name"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=["key", "item_key", "item_id", "enchant_level", "item_name", "icon_path", "wait_second"]),
        DeclaredCountTest(declared=header_count(offset=_COUNT_OFFSET)),
        TargetTest(
            col="item_key",
            value=_BLACKSTAR_SHIELD_PEN,
            expected={"item_id": _BLACKSTAR_SHIELD, "enchant_level": _PEN, "item_name": "Blackstar Shield (20)"},
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
        SchemaTest(required_keys=["item_key", "offset", "size"]),
        DeclaredCountTest(declared=header_count(offset=_COUNT_OFFSET)),
        TargetTest(col="item_key", value=_BLACKSTAR_SHIELD_PEN, expected={"size": _ROW_SIZE - _KEY_SIZE}),
    ],
)


@pytest.fixture(scope="module")
def wait_item_result(request: Any) -> HandlerResult:
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
def test_waititem_dbss(spec: Any, wait_item_result: HandlerResult) -> None:
    wait_item_result.check(spec)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_waititemoffset_dbss(spec: Any, offset_result: HandlerResult) -> None:
    offset_result.check(spec)


def test_item_id_and_level_split_the_item_key(wait_item_result: HandlerResult) -> None:
    for r in wait_item_result.records:
        assert r["key"] == r["item_key"]
        assert split_item_key(r["item_key"]) == (r["item_id"], r["enchant_level"])


def test_item_keys_are_unique(wait_item_result: HandlerResult) -> None:
    keys = [r["item_key"] for r in wait_item_result.records]
    assert len(keys) == len(set(keys))


def test_every_offset_row_points_at_its_item_key() -> None:
    main = load_binary_fixture(FILE_NAME)
    for row in parse_bare_u32_offset_rows(load_binary_fixture(OFFSET_FILE)):
        assert row.size == _ROW_SIZE - _KEY_SIZE
        assert struct.unpack_from("<II", main, row.offset - _KEY_SIZE) == (row.entry_id, row.entry_id)


def test_a_small_table_reads_back() -> None:
    row = struct.pack("<IIIBI", _BLACKSTAR_SHIELD_PEN, _BLACKSTAR_SHIELD_PEN, _BLACKSTAR_SHIELD, _PEN, 900)
    assert parse_waititem_records(struct.pack("<I", 1) + row) == [
        {
            "key": _BLACKSTAR_SHIELD_PEN,
            "item_key": _BLACKSTAR_SHIELD_PEN,
            "item_id": _BLACKSTAR_SHIELD,
            "enchant_level": _PEN,
            "wait_second": 900,
        },
    ]


def test_a_short_file_raises() -> None:
    row = struct.pack("<IIIBI", _BLACKSTAR_SHIELD_PEN, _BLACKSTAR_SHIELD_PEN, _BLACKSTAR_SHIELD, _PEN, 900)
    with pytest.raises(ValueError):
        parse_waititem_records(struct.pack("<I", 2) + row)

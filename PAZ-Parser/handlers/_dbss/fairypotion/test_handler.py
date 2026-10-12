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
    RangeTest,
    SchemaTest,
    TargetTest,
    case_id,
    fixed_rows,
    header_count,
    run_case,
)

from _common.pabr_offset import parse_bare_offset_rows
from .parser import parse_fairypotion_lists


_FILE_NAME = "fairypotion.dbss"
_OFFSET_FILE = "fairypotionoffset.dbss"
_HEADER_SIZE = 4
_OFFSET_ROW_SIZE = 10
# A list: u32 item count, the u32 item IDs, then a u8 potion type.
_ITEM_COUNT_SIZE = 4
_ITEM_ID_SIZE = 4
_POTION_TYPE_SIZE = 1
_HP = 0
_SP = 3

_HP_POTION_BEGINNER = 502
_MP_POTION_BEGINNER = 503


def _listed_items(source: CaseInput) -> int:
    """Item IDs in the file: what remains after the header and each list's count and type."""
    list_count = struct.unpack_from("<I", source.data, 0)[0]
    list_overhead = _ITEM_COUNT_SIZE + _POTION_TYPE_SIZE
    body = len(source.data) - _HEADER_SIZE - list_count * list_overhead
    if body < 0 or body % _ITEM_ID_SIZE:
        raise AssertionError(f"{body} bytes of item IDs are not whole u32 values")
    return body // _ITEM_ID_SIZE


CASE = HandlerCase(
    handler_name="fairypotion.dbss",
    data_file="fairypotion.dbss",
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["item_name"],
    internal_path="gamecommondata/binary/fairypotion.dbss",
    tests=[
        SchemaTest(
            required_keys=["potion_type", "resource", "item_id", "item_name", "icon_path"],
        ),
        DeclaredCountTest(declared=_listed_items),
        # One list per resource: HP, MP, WP, SP.
        RangeTest(col="potion_type", min_val=_HP, max_val=_SP),
        RangeTest(col="item_id", min_val=1, max_val=0x00FFFFFF),
        # HP potions are only in the HP list.
        TargetTest(
            col="item_id",
            value=_HP_POTION_BEGINNER,
            expected=[{
                "potion_type": _HP,
                "resource": "HP",
                "item_name": "HP Potion (Beginner)",
            }],
        ),
        TargetTest(
            col="item_id",
            value=_MP_POTION_BEGINNER,
            expected={"item_name": "MP Potion (Beginner)"},
        ),
    ],
)

OFFSET_CASE = HandlerCase(
    handler_name="fairypotionoffset.dbss",
    data_file="fairypotionoffset.dbss",
    companion_files={},
    loc_file=None,
    uses_loc=False,
    loc_fields=[],
    internal_path="gamecommondata/binary/fairypotionoffset.dbss",
    tests=[
        SchemaTest(required_keys=["potion_type", "data_offset", "data_size"]),
        DeclaredCountTest(declared=header_count()),
        DeclaredCountTest(declared=fixed_rows(_OFFSET_ROW_SIZE, header_size=_HEADER_SIZE)),
        RangeTest(col="potion_type", min_val=_HP, max_val=_SP),
        # The first list follows the main file's u32 list count.
        TargetTest(col="data_offset", value=_HEADER_SIZE, expected={}),
    ],
)


def test_every_offset_row_spans_the_list_with_its_key() -> None:
    data = load_binary_fixture(_FILE_NAME)
    rows = parse_bare_offset_rows(load_binary_fixture(_OFFSET_FILE))
    lists = {potion_list.potion_type: potion_list for potion_list in parse_fairypotion_lists(data)}

    assert sorted(row.entry_id for row in rows) == sorted(lists)
    for row in rows:
        item_count = len(lists[row.entry_id].item_ids)
        assert row.size == _ITEM_COUNT_SIZE + item_count * _ITEM_ID_SIZE + _POTION_TYPE_SIZE
        # The list's last byte is its potion type, the row's key.
        assert data[row.offset + row.size - _POTION_TYPE_SIZE] == row.entry_id


def test_a_list_past_the_end_raises() -> None:
    # One list that claims two items but holds one and no type byte.
    data = struct.pack("<III", 1, 2, 502)
    with pytest.raises(ValueError, match="runs past the end"):
        parse_fairypotion_lists(data)


def test_bytes_after_the_last_list_raise() -> None:
    data = struct.pack("<IIIBB", 1, 1, 502, 0, 0)
    with pytest.raises(ValueError, match="1 bytes after its last list"):
        parse_fairypotion_lists(data)


@pytest.fixture(scope="module")
def fairypotion_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.fixture(scope="module")
def fairypotionoffset_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_OFFSET_RESULT", None)
    if result is None:
        result = run_case(replace(OFFSET_CASE, tests=[]))
        request.module._OFFSET_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_fairypotion_dbss(spec: Any, fairypotion_result: HandlerResult) -> None:
    fairypotion_result.check(spec)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_fairypotionoffset_dbss(spec: Any, fairypotionoffset_result: HandlerResult) -> None:
    fairypotionoffset_result.check(spec)

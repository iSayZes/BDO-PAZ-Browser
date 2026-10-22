from __future__ import annotations

import struct
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

from .parser import FILE_NAME, parse_challengerewardlist_records


_ROW_COUNT_AT = 4
_U32 = struct.Struct("<I")
_ENCHANT_SHIFT = 24

CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["item_name"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=["item_key", "item_id", "enchant_level", "item_name"]),
        DeclaredCountTest(declared=header_count(offset=_ROW_COUNT_AT)),
    ],
)


@pytest.fixture(scope="module")
def challengerewardlist_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_challengerewardlist_bss(spec: Any, challengerewardlist_result: HandlerResult) -> None:
    challengerewardlist_result.check(spec)


def test_keys_ascend_without_repeats(challengerewardlist_result: HandlerResult) -> None:
    keys = [record["item_key"] for record in challengerewardlist_result.records]
    assert keys == sorted(set(keys))


def test_most_keys_name_an_item(challengerewardlist_result: HandlerResult) -> None:
    named = [record for record in challengerewardlist_result.records if record["item_name"]]
    assert len(named) * 2 > len(challengerewardlist_result.records)


def test_a_key_splits_into_item_and_level() -> None:
    key = 5 << _ENCHANT_SHIFT | 694110
    data = b"PABR" + _U32.pack(1) + _U32.pack(key) + _U32.pack(0) + _U32.pack(12) + _U32.pack(0)
    assert parse_challengerewardlist_records(data) == [{"item_key": key, "item_id": 694110, "enchant_level": 5}]

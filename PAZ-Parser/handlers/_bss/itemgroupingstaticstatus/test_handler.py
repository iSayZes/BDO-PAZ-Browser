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
    case_id,
    header_count,
    run_case,
)

from _bss.itemeffectgroupstaticstatus.parser import FILE_NAME as EFFECT_FILE, parse_itemeffectgroup_effects
from .parser import FILE_NAME, parse_itemgrouping_groups


_GROUP = struct.Struct("<BI")
_U32 = struct.Struct("<I")

CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["item_names"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=["item_group_type", "item_ids", "item_names", "item_count"]),
        DeclaredCountTest(declared=header_count(offset=0)),
    ],
)


@pytest.fixture(scope="module")
def grouping_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_itemgroupingstaticstatus_bss(spec: Any, grouping_result: HandlerResult) -> None:
    grouping_result.check(spec)


def test_group_types_are_unique(grouping_result: HandlerResult) -> None:
    types = [record["item_group_type"] for record in grouping_result.records]
    assert len(types) == len(set(types))


def test_items_are_base_item_ids(grouping_result: HandlerResult) -> None:
    # The high byte of an item key is its enhancement level; the groups list level 0 only.
    assert all(item_id >> 24 == 0 for record in grouping_result.records for item_id in record["item_ids"])


def test_every_glow_effect_group_is_an_item_group_type(grouping_result: HandlerResult) -> None:
    types = {record["item_group_type"] for record in grouping_result.records}
    effect_types = {effect["item_group_type"] for effect in parse_itemeffectgroup_effects(load_binary_fixture(EFFECT_FILE))}
    assert effect_types <= types


def test_groups_read_type_count_and_items() -> None:
    data = _U32.pack(2) + _GROUP.pack(11, 2) + _U32.pack(930601) + _U32.pack(930602) + _GROUP.pack(0, 0)
    assert parse_itemgrouping_groups(data) == [
        {"item_group_type": 11, "item_ids": [930601, 930602]},
        {"item_group_type": 0, "item_ids": []},
    ]


def test_bytes_after_the_groups_raise() -> None:
    data = _U32.pack(1) + _GROUP.pack(0, 0) + bytes(1)
    with pytest.raises(ValueError, match="rows end"):
        parse_itemgrouping_groups(data)

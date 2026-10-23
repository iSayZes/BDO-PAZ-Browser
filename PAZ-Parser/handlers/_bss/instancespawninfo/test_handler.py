from __future__ import annotations

from dataclasses import replace
from typing import Any

import pytest

from tests.framework import (
    DeclaredCountTest,
    HandlerCase,
    HandlerResult,
    RangeTest,
    SchemaTest,
    TargetTest,
    case_id,
    header_count,
    run_case,
)

from .parser import FILE_NAME, parse_instancespawninfo_records


# Zephyros Castle and the scroll its deep entry consumes (instancespawninfo_bss.md).
_ZEPHYROS_CASTLE = 43
_ZEPHYROS_CASTLE_SCROLL = 761679
# One sector of the world grid, in world units.
_SECTOR = 12_800

CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["enter_item"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=[
            "key", "max_x", "max_z", "min_x", "min_z", "unknown_12", "x", "y", "z", "radius",
            "area_name_kr", "offense_point", "unknown_area_name_kr_04", "enter_item_key",
            "unknown_area_name_kr_0a", "unknown_area_name_kr_0e", "enter_type", "unknown_item_key",
            "unknown_area_name_kr_17", "offense", "enter_item", "radius_m",
        ]),
        DeclaredCountTest(declared=header_count(offset=0)),
        RangeTest(col="enter_type", min_val=0, max_val=1),
        TargetTest(col="key", value=_ZEPHYROS_CASTLE, expected={
            "area_name_kr": "제피로스 성",
            "enter_item_key": _ZEPHYROS_CASTLE_SCROLL,
            "enter_item": "Zephyros Castle Scroll",
            "enter_type": 1,
        }),
    ],
)


@pytest.fixture(scope="module")
def spawn_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_instancespawninfo_bss(spec: Any, spawn_result: HandlerResult) -> None:
    spawn_result.check(spec)


def test_keys_are_unique_and_repeated(spawn_result: HandlerResult) -> None:
    keys = [record["key"] for record in spawn_result.records]
    assert len(keys) == len(set(keys))
    assert all(record["unknown_12"] == record["key"] for record in spawn_result.records)


def test_centre_lies_in_its_sector_box(spawn_result: HandlerResult) -> None:
    # Checks the box order: max_x / max_z first, then min_x / min_z.
    for record in spawn_result.records:
        assert record["min_x"] <= record["x"] <= record["max_x"], record["key"]
        assert record["min_z"] <= record["z"] <= record["max_z"], record["key"]
        corners = (record["max_x"], record["max_z"], record["min_x"], record["min_z"])
        assert all(corner % _SECTOR == 0 for corner in corners), record["key"]


def test_entry_flag_follows_the_entry_item(spawn_result: HandlerResult) -> None:
    for record in spawn_result.records:
        assert record["unknown_area_name_kr_0a"] == (1 if record["enter_item_key"] else 0), record["key"]


def test_short_file_raises() -> None:
    with pytest.raises(ValueError):
        parse_instancespawninfo_records((1).to_bytes(4, "little"))

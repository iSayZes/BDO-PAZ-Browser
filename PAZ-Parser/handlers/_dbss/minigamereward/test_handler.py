from __future__ import annotations

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

from _bss.itemmaingroup.drop_groups import DROP_GROUP_FILES
from _common.pabr_offset import parse_bare_offset_rows
from .parser import FILE_NAME, OFFSET_FILE, ROW_SIZE, parse_minigamereward_records


_COUNT_OFFSET = 0
_COUNT_SIZE = 4
_KEY_SIZE = 2
# Minigame 1 is the cow: vehicle type 26 (Cow), drop group 65021 (Milk),
# as in the 1784 sheet's MiniGameKey comment.
_COW_MINIGAME = 1
_COW_VEHICLE_TYPE = 26
_MILK_DROP_GROUP = 65021


CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={name: name for name in DROP_GROUP_FILES},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["drop_items"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=[
            "minigame_key", "success_wp", "fail_wp", "drop_group", "check_vehicle_type",
            "minigame_key_dup", "has_drop_group", "drop_item_keys", "drop_items", "check_vehicle_type_name",
        ]),
        DeclaredCountTest(declared=header_count(offset=_COUNT_OFFSET)),
        TargetTest(
            col="minigame_key",
            value=_COW_MINIGAME,
            expected={
                "check_vehicle_type": _COW_VEHICLE_TYPE,
                "check_vehicle_type_name": "Cow",
                "drop_group": _MILK_DROP_GROUP,
                "has_drop_group": True,
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
        SchemaTest(required_keys=["minigame_key", "data_offset", "data_size"]),
        DeclaredCountTest(declared=header_count(offset=_COUNT_OFFSET)),
    ],
)


@pytest.fixture(scope="module")
def minigamereward_result(request: Any) -> HandlerResult:
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
def test_minigamereward_dbss(spec: Any, minigamereward_result: HandlerResult) -> None:
    minigamereward_result.check(spec)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_minigamerewardoffset_dbss(spec: Any, offset_result: HandlerResult) -> None:
    offset_result.check(spec)


def test_minigame_key_is_stored_twice(minigamereward_result: HandlerResult) -> None:
    assert all(r["minigame_key_dup"] == r["minigame_key"] for r in minigamereward_result.records)


def test_every_drop_group_is_in_itemmaingroup(minigamereward_result: HandlerResult) -> None:
    assert all(r["has_drop_group"] and r["drop_item_keys"] for r in minigamereward_result.records)


def test_offset_rows_point_past_the_first_key() -> None:
    """Each index row starts at a row's `minigame_key_dup` and covers the rest of the row."""
    records = parse_minigamereward_records(load_binary_fixture(FILE_NAME))
    expected = {
        r["minigame_key"]: (_COUNT_SIZE + index * ROW_SIZE + _KEY_SIZE, ROW_SIZE - _KEY_SIZE)
        for index, r in enumerate(records)
    }
    rows = parse_bare_offset_rows(load_binary_fixture(OFFSET_FILE))
    assert {row.entry_id: (row.offset, row.size) for row in rows} == expected


def test_parser_reads_a_row_and_rejects_extra_bytes() -> None:
    row = (
        _COW_MINIGAME.to_bytes(2, "little") * 2
        + (10).to_bytes(2, "little")
        + (4).to_bytes(2, "little")
        + _MILK_DROP_GROUP.to_bytes(4, "little")
        + bytes([_COW_VEHICLE_TYPE])
    )
    data = (1).to_bytes(4, "little") + row
    record = parse_minigamereward_records(data)[0]
    assert (record["drop_group"], record["check_vehicle_type"]) == (_MILK_DROP_GROUP, _COW_VEHICLE_TYPE)
    with pytest.raises(ValueError):
        parse_minigamereward_records(data + b"\x00")

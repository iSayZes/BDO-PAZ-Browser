from __future__ import annotations

import struct
from dataclasses import replace
from typing import Any

import pytest

from _common.lookup_index import IndexKind
from tests.fixtures import load_binary_fixture
from tests.framework import (
    DeclaredCountTest,
    HandlerCase,
    HandlerResult,
    SchemaTest,
    TargetTest,
    case_id,
    fixed_rows,
    header_count,
    run_case,
)
from tests.offset_rows import offset_row_problems

from _dbss.marblegamediceitemkey.parser import (
    FILE_NAME as DICE_ITEM_KEY_FILE,
    KEY_FIELD as DICE_ITEM_KEY_FIELD,
    parse_marblegamediceitemkey_records,
)
from .parser import (
    FILE_NAME,
    OFFSET_FILE,
    groups_by_dice_item,
    parse_marblegamediceitemgroup_records,
    parse_marblegamediceitemgroupoffset_rows,
)


_COUNT_SIZE = 4
_OFFSET_ROW_SIZE = 12
# Group 1001 drops dice item 101 (Pace of Delight - 1 Square), which item
# 756440 grants; group 9 drops the six one-face dice 2 to 7
# (DiceItemGroup_Table of client 1784, contents event 98 on client 3482).
_PACE_OF_DELIGHT_GROUP = 1001
_PACE_OF_DELIGHT_DICE_ITEM = 101
_PACE_OF_DELIGHT_ITEM = 756440
_ONE_FACE_DICE_GROUP = 9
_ONE_FACE_DICE = [2, 3, 4, 5, 6, 7]


CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=[],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    lookup_indexes={IndexKind.MARBLE_DICE_GROUP_ITEMS: {_PACE_OF_DELIGHT_GROUP: (_PACE_OF_DELIGHT_ITEM,)}},
    tests=[
        SchemaTest(
            required_keys=[
                "dice_drop_group_key",
                "entries",
                "dice_item_keys",
                "dice_items_text",
                "item_ids",
                "item_names",
                "item_count",
            ],
        ),
        DeclaredCountTest(declared=header_count(offset=0)),
        TargetTest(
            col="dice_drop_group_key",
            value=_PACE_OF_DELIGHT_GROUP,
            expected={
                "dice_item_keys": [_PACE_OF_DELIGHT_DICE_ITEM],
                "item_ids": [_PACE_OF_DELIGHT_ITEM],
                "item_names": ["Pace of Delight - 1 Square"],
                "item_count": 1,
            },
        ),
        # No indexed item grants the group; None sorts last.
        TargetTest(
            col="dice_drop_group_key",
            value=_ONE_FACE_DICE_GROUP,
            expected={"dice_item_keys": _ONE_FACE_DICE, "item_ids": [], "item_count": None},
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
        SchemaTest(required_keys=["dice_drop_group_key", "data_offset", "data_size"]),
        DeclaredCountTest(declared=header_count(offset=0)),
        DeclaredCountTest(declared=fixed_rows(_OFFSET_ROW_SIZE, header_size=_COUNT_SIZE)),
    ],
)


@pytest.fixture(scope="module")
def group_result(request: Any) -> HandlerResult:
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
def test_marblegamediceitemgroup_dbss(spec: Any, group_result: HandlerResult) -> None:
    group_result.check(spec)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_marblegamediceitemgroupoffset_dbss(spec: Any, offset_result: HandlerResult) -> None:
    offset_result.check(spec)


def test_offset_rows_point_at_their_rows() -> None:
    rows = parse_marblegamediceitemgroupoffset_rows(load_binary_fixture(OFFSET_FILE))
    problems = offset_row_problems(load_binary_fixture(FILE_NAME), rows, struct.Struct("<I"))
    assert not problems, problems


def test_every_dice_item_is_in_the_key_table() -> None:
    keys = {r[DICE_ITEM_KEY_FIELD] for r in parse_marblegamediceitemkey_records(load_binary_fixture(DICE_ITEM_KEY_FILE))}
    used = set(groups_by_dice_item(load_binary_fixture(FILE_NAME)))
    assert used <= keys, f"dice items missing from {DICE_ITEM_KEY_FILE}: {sorted(used - keys)}"


def test_rates_are_zero_in_the_client() -> None:
    """The sheet's `%Rate` column is server-only; the client build writes 0."""
    records = parse_marblegamediceitemgroup_records(load_binary_fixture(FILE_NAME))
    assert all(entry["rate"] == 0 for record in records for entry in record["entries"])


def test_parse_reads_each_group_with_its_entries() -> None:
    data = struct.pack("<I", 2) + struct.pack("<II2I", 1001, 1, 101, 0) + struct.pack("<II", 2, 0)

    assert parse_marblegamediceitemgroup_records(data) == [
        {"dice_drop_group_key": 1001, "entries": [{"dice_item_key": 101, "rate": 0}]},
        {"dice_drop_group_key": 2, "entries": []},
    ]
    assert groups_by_dice_item(data) == {101: [1001]}


def test_parse_rejects_a_group_longer_than_the_file() -> None:
    data = struct.pack("<I", 1) + struct.pack("<II", 1, 3) + struct.pack("<II", 2, 0)

    with pytest.raises(ValueError, match="lists 3 dice"):
        parse_marblegamediceitemgroup_records(data)

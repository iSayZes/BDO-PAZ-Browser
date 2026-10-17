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

from _common.pabr_offset import parse_bare_u32_offset_rows
from _dbss.itemimprovement.parser import (
    FILE_NAME as REFORM_FILE,
    SOURCE_FILE as STONE_FILE,
    parse_itemimprovement_records,
    parse_itemimprovementsource_records,
)
from .parser import FILE_NAME, OFFSET_FILE, ROW, parse_extractitem_records
from .reform_group import reform_group_lookup


_COUNT_OFFSET = 0
_COUNT_SIZE = 4
_STORM_DEVOURED_DANDELION_IRON_BUSTER = 731222
_DANDELION_IRON_BUSTER = 694273
_MIRROR_OF_EQUILIBRIUM = 320060
_HEART_OF_KARANDA = 9787
_COMBATANTS_TUVALA_HWANDO = 697180
_TUVALA_HWANDO = 695180
_COMBATANTS_RESTORATION_STONE = 8172
_COMBATANTS_STONE_WEAPON = 8170


CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={REFORM_FILE: REFORM_FILE, STONE_FILE: STONE_FILE},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["item_name", "need_item_name", "result_item_name", "result_material_name"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=[
            "item_id", "item_name", "need_item_id", "need_item_name",
            "result_item_id", "result_item_name", "result_material_id", "result_material_name",
            "reform_group", "item_count", "need_item_count", "result_item_count", "result_material_count",
        ]),
        DeclaredCountTest(declared=header_count(offset=_COUNT_OFFSET)),
        # The Mirror of Equilibrium text: "Extract Heart of Karanda from Storm Devoured gear".
        TargetTest(
            col="item_id",
            value=_STORM_DEVOURED_DANDELION_IRON_BUSTER,
            expected={
                "item_name": "Storm Devoured Dandelion Iron Buster",
                "need_item_id": _MIRROR_OF_EQUILIBRIUM,
                "result_item_id": _DANDELION_IRON_BUSTER,
                "result_material_id": _HEART_OF_KARANDA,
            },
        ),
        # Combatant's Restoration Stone names the two Combatant's Stones.
        TargetTest(
            col="item_id",
            value=_COMBATANTS_TUVALA_HWANDO,
            expected={
                "need_item_id": _COMBATANTS_RESTORATION_STONE,
                "result_item_id": _TUVALA_HWANDO,
                "result_material_id": _COMBATANTS_STONE_WEAPON,
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
        SchemaTest(required_keys=["item_id", "offset", "size"]),
        DeclaredCountTest(declared=header_count(offset=_COUNT_OFFSET)),
        TargetTest(
            col="item_id",
            value=_STORM_DEVOURED_DANDELION_IRON_BUSTER,
            expected={"size": ROW.size},
        ),
    ],
)


def _row(item_id: int, need: int, result: int, material: int, need_count: int = 1) -> bytes:
    return ROW.pack(item_id, 1, need, need_count, result, 1, material, 1)


@pytest.fixture(scope="module")
def extract_result(request: Any) -> HandlerResult:
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
def test_extractitem_dbss(spec: Any, extract_result: HandlerResult) -> None:
    extract_result.check(spec)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_extractitemoffset_dbss(spec: Any, offset_result: HandlerResult) -> None:
    offset_result.check(spec)


def test_item_ids_are_unique(extract_result: HandlerResult) -> None:
    item_ids = [r["item_id"] for r in extract_result.records]
    assert len(item_ids) == len(set(item_ids))


def test_no_row_extracts_to_itself(extract_result: HandlerResult) -> None:
    assert all(r["result_item_id"] != r["item_id"] for r in extract_result.records)


def test_reform_group_is_a_reform_of_the_row_holding_its_stone(extract_result: HandlerResult) -> None:
    reforms = {
        (r["result_id"], r["input_id"], r["group"])
        for r in parse_itemimprovement_records(load_binary_fixture(REFORM_FILE))
    }
    stones = {
        (s["item_id"], s["group"])
        for s in parse_itemimprovementsource_records(load_binary_fixture(STONE_FILE))
    }
    grouped = [r for r in extract_result.records if r["reform_group"] is not None]
    assert grouped
    for r in grouped:
        assert (r["item_id"], r["result_item_id"], r["reform_group"]) in reforms
        assert (r["result_material_id"], r["reform_group"]) in stones


def test_storm_devoured_gear_has_a_reform_group(extract_result: HandlerResult) -> None:
    row = next(r for r in extract_result.records if r["item_id"] == _STORM_DEVOURED_DANDELION_IRON_BUSTER)
    assert row["reform_group"] is not None


def _reform_file(*records: tuple[int, int, int, int]) -> bytes:
    """(key, result, input, group) records in the itemimprovement.dbss shape."""
    body = b"".join(
        struct.pack("<IQ5I", key, 5, result, *[input_id] * 4) + struct.pack("<BB11s", 0, group, bytes(11))
        for key, result, input_id, group in records
    )
    return struct.pack("<I", len(records)) + body


def _stone_file(*stones: tuple[int, int]) -> bytes:
    """(item, group) records in the itemimprovementsource.dbss shape."""
    body = b"".join(
        struct.pack("<IQ5I", item_id, 5, *[0] * 5) + struct.pack("<IIH", 0, group, 0)
        for item_id, group in stones
    )
    return struct.pack("<I", len(stones)) + body


def test_the_stone_picks_one_group_of_a_pair_in_two() -> None:
    lookup = reform_group_lookup(
        _reform_file((1, 731222, 694273, 2), (2, 731222, 694273, 8)),
        _stone_file((9787, 8)),
    )
    row = {"item_id": 731222, "result_item_id": 694273, "result_material_id": 9787}
    assert lookup(row) == 8
    assert lookup({**row, "result_material_id": 9771}) is None


def test_no_reform_tables_give_no_group() -> None:
    lookup = reform_group_lookup(None, None)
    assert lookup({"item_id": 731222, "result_item_id": 694273, "result_material_id": 9787}) is None


def test_offset_rows_point_at_every_row_key() -> None:
    """Each index row points at a row's `item_id` and covers the whole row; the
    offsets are exactly the row starts."""
    main = load_binary_fixture(FILE_NAME)
    rows = parse_bare_u32_offset_rows(load_binary_fixture(OFFSET_FILE))
    for row in rows:
        assert row.size == ROW.size
        assert struct.unpack_from("<I", main, row.offset)[0] == row.entry_id
    row_starts = range(_COUNT_SIZE, len(main), ROW.size)
    assert sorted(row.offset for row in rows) == list(row_starts)


def test_a_small_table_reads_back() -> None:
    data = struct.pack("<I", 2) + _row(731222, 320060, 694273, 9787, need_count=3) + _row(10431, 4929, 10407, 4912)
    records = parse_extractitem_records(data)
    assert [
        (r["item_id"], r["need_item_id"], r["result_item_id"], r["result_material_id"]) for r in records
    ] == [(731222, 320060, 694273, 9787), (10431, 4929, 10407, 4912)]
    # Each count follows its own item ID: only the need item's count is 3.
    assert [
        (r["item_count"], r["need_item_count"], r["result_item_count"], r["result_material_count"]) for r in records
    ] == [(1, 3, 1, 1), (1, 1, 1, 1)]


def test_a_cut_row_raises() -> None:
    data = struct.pack("<I", 1) + _row(731222, 320060, 694273, 9787)
    with pytest.raises(ValueError):
        parse_extractitem_records(data[:-1])


def test_bytes_after_the_last_row_raise() -> None:
    data = struct.pack("<I", 1) + _row(731222, 320060, 694273, 9787)
    with pytest.raises(ValueError):
        parse_extractitem_records(data + b"\x00")

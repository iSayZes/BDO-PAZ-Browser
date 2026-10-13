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
from .parser import FILE_NAME, OFFSET_FILE, parse_alchemystonechange_records


_SPLENDID_DESTRUCTION = 45228
_SHINING_DESTRUCTION = 45232
_OLD_TOTEM_OF_THE_SEA = 54201
_BRIMMING_ESSENCE_OF_AETHER = 821322
_BLACK_STONE = 16001
_COUNT_OFFSET = 0
_KEY_SIZE = 4


CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["item_name", "material_name"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=[
            "key", "item_id", "item_name", "item_icon_path", "material_item_id", "material_name",
            "material_count", "condition", "result_item_id", "result_name",
            "unknown_08", "unknown_14", "unknown_tail_04", "unknown_tail_08",
        ]),
        DeclaredCountTest(declared=header_count(offset=_COUNT_OFFSET)),
        # Brimming Essence of Aether, "Usage #1: Alchemy Stone Growth".
        TargetTest(
            col="item_id",
            value=_SPLENDID_DESTRUCTION,
            expected={
                "item_name": "Splendid Alchemy Stone of Destruction",
                "material_item_id": _BRIMMING_ESSENCE_OF_AETHER,
                "material_name": "Brimming Essence of Aether",
                "result_item_id": _SHINING_DESTRUCTION,
                "result_name": "Shining Alchemy Stone of Destruction",
            },
        ),
        # The Totem tooltip: "it can be grown with Black Stone".
        TargetTest(
            col="item_id",
            value=_OLD_TOTEM_OF_THE_SEA,
            expected={"item_name": "Old Totem of the Sea", "material_item_id": _BLACK_STONE},
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
        TargetTest(col="item_id", value=_SPLENDID_DESTRUCTION, expected={"item_id": _SPLENDID_DESTRUCTION}),
    ],
)


def _row(item_id: int, material: int, count: int, condition: str, result: int, tail_04: int) -> bytes:
    head = struct.pack("<5I", item_id, item_id, 0, material, count) + bytes(16)
    text = struct.pack("<Q", len(condition)) + condition.encode("utf-16-le")
    return head + text + struct.pack("<3I", result, tail_04, 0)


@pytest.fixture(scope="module")
def change_result(request: Any) -> HandlerResult:
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
def test_alchemystonechange_dbss(spec: Any, change_result: HandlerResult) -> None:
    change_result.check(spec)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_alchemystonechangeoffset_dbss(spec: Any, offset_result: HandlerResult) -> None:
    offset_result.check(spec)


def test_every_key_is_its_item_id(change_result: HandlerResult) -> None:
    assert all(r["key"] == r["item_id"] for r in change_result.records)


def test_every_row_has_a_condition_script(change_result: HandlerResult) -> None:
    assert all(r["condition"].endswith(";") for r in change_result.records)


def test_offset_rows_tile_the_main_rows() -> None:
    """Each index row starts 4 bytes into a main row, at its `item_id`, and
    the rows end where the next key starts, the last one at the end of file."""
    main = load_binary_fixture(FILE_NAME)
    rows = sorted(parse_bare_u32_offset_rows(load_binary_fixture(OFFSET_FILE)), key=lambda row: row.offset)
    for row in rows:
        assert struct.unpack_from("<II", main, row.offset - _KEY_SIZE) == (row.entry_id, row.entry_id)
    ends = [row.offset + row.size for row in rows]
    starts = [row.offset - _KEY_SIZE for row in rows[1:]]
    assert ends[:-1] == starts
    assert ends[-1] == len(main)


def test_a_small_table_reads_back() -> None:
    data = struct.pack("<I", 2) + _row(45228, 821322, 30, "getLifeLevel(4)>10;", 45232, 3870) + _row(
        54201, 16001, 1, "getLifeLevel(1)>30;", 0, 0
    )
    records = parse_alchemystonechange_records(data)
    assert [(r["item_id"], r["material_item_id"], r["condition"], r["result_item_id"]) for r in records] == [
        (45228, 821322, "getLifeLevel(4)>10;", 45232),
        (54201, 16001, "getLifeLevel(1)>30;", 0),
    ]
    assert records[0]["unknown_14"] == "00" * 16


def test_a_cut_row_raises() -> None:
    data = struct.pack("<I", 1) + _row(45228, 821322, 30, "getLifeLevel(4)>10;", 45232, 3870)
    with pytest.raises(ValueError):
        parse_alchemystonechange_records(data[:-1])


def test_bytes_after_the_last_row_raise() -> None:
    data = struct.pack("<I", 1) + _row(45228, 821322, 30, "getLifeLevel(4)>10;", 45232, 3870)
    with pytest.raises(ValueError):
        parse_alchemystonechange_records(data + b"\x00")

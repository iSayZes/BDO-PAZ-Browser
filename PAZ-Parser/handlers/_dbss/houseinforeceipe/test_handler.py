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
    RangeTest,
    SchemaTest,
    TargetTest,
    UserLanguageTest,
    case_id,
    header_count,
    run_case,
)

from _common.pabr_offset import parse_bare_u32_offset_rows
from .house_enums import HOUSE_ICON_TYPE_NAMES, HOUSE_USE_TYPE_NAMES
from .parser import FILE_NAME, LEVEL_COUNT, OFFSET_FILE, parse_houseinforeceipe_records


_RESIDENCE = 0
_WEAPON_WORKSHOP = 11
_AREHAZA_WORKSHOP = 24
_COUNT_OFFSET = 0


CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["name"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=[
            "receipe_key", "need_item_key", "name_kr", "name", "house_use_type", "house_use_type_name",
            "icon_type", "icon_type_name", "level_exchanges", "level_count", "exchange_count",
            "unknown_tail_02", "unknown_after_level_exchanges", "unknown_end",
        ]),
        DeclaredCountTest(declared=header_count(offset=_COUNT_OFFSET)),
        RangeTest(col="house_use_type", min_val=0, max_val=len(HOUSE_USE_TYPE_NAMES) - 1),
        RangeTest(col="icon_type", min_val=0, max_val=len(HOUSE_ICON_TYPE_NAMES) - 1),
        RangeTest(col="level_count", min_val=0, max_val=LEVEL_COUNT),
        UserLanguageTest(fields=["name"]),
        TargetTest(
            col="receipe_key",
            value=_RESIDENCE,
            expected={"name": "Residence", "house_use_type_name": "Empty", "icon_type_name": "House"},
        ),
        TargetTest(
            col="receipe_key",
            value=_WEAPON_WORKSHOP,
            expected={
                "name": "Weapon Workshop",
                "house_use_type_name": "WeaponForgingWorkshop",
                "icon_type_name": "Workshop_WeaponForging",
            },
        ),
        # The town workshops keep the furniture use type and carry their own icon.
        TargetTest(
            col="receipe_key",
            value=_AREHAZA_WORKSHOP,
            expected={
                "name": "Arehaza Workshop",
                "house_use_type_name": "FurnitureWorkshop",
                "icon_type_name": "Workshop_Arehaza",
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
        SchemaTest(required_keys=["receipe_key", "offset", "size"]),
        DeclaredCountTest(declared=header_count(offset=_COUNT_OFFSET)),
        TargetTest(col="receipe_key", value=_WEAPON_WORKSHOP, expected={"receipe_key": _WEAPON_WORKSHOP}),
    ],
)


def _row(key: int, need: int, name: str, use: int, icon: int, levels: list[list[int]], end: list[int]) -> bytes:
    head = struct.pack("<IHQ", key, need, len(name)) + name.encode("utf-16-le") + bytes([use, icon, 0])
    lists = b"".join(struct.pack(f"<I{len(keys)}I", len(keys), *keys) for keys in levels)
    return head + lists + struct.pack("<II", 0, len(end)) + bytes(end)


_WEAPON_ROW = _row(11, 2, "무기 단조 공방", 4, 4, [[5026, 5027], [5028], [], [], []], [0, 1, 2, 3, 4, 5])
_RESIDENCE_ROW = _row(0, 3, "주거지", 0, 0, [[], [], [], [], []], [0, 1, 2, 3, 4, 5])


@pytest.fixture(scope="module")
def receipe_result(request: Any) -> HandlerResult:
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
def test_houseinforeceipe_dbss(spec: Any, receipe_result: HandlerResult) -> None:
    receipe_result.check(spec)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_houseinforeceipeoffset_dbss(spec: Any, offset_result: HandlerResult) -> None:
    offset_result.check(spec)


def test_every_row_has_five_level_lists(receipe_result: HandlerResult) -> None:
    assert all(len(r["level_exchanges"]) == LEVEL_COUNT for r in receipe_result.records)


def test_level_lists_fill_from_level_one(receipe_result: HandlerResult) -> None:
    """No row skips a level: the filled lists are the first `level_count` ones."""
    for r in receipe_result.records:
        filled = [bool(keys) for keys in r["level_exchanges"]]
        assert filled == [True] * r["level_count"] + [False] * (LEVEL_COUNT - r["level_count"])


def test_offset_rows_tile_the_main_rows() -> None:
    """Each index row starts at its main row's key, and the rows end where
    the next one starts, the last one at the end of the file."""
    main = load_binary_fixture(FILE_NAME)
    rows = sorted(parse_bare_u32_offset_rows(load_binary_fixture(OFFSET_FILE)), key=lambda row: row.offset)
    for row in rows:
        assert struct.unpack_from("<I", main, row.offset)[0] == row.entry_id
    ends = [row.offset + row.size for row in rows]
    assert ends[:-1] == [row.offset for row in rows[1:]]
    assert ends[-1] == len(main)


def test_a_small_table_reads_back() -> None:
    records = parse_houseinforeceipe_records(struct.pack("<I", 2) + _WEAPON_ROW + _RESIDENCE_ROW)
    assert [(r["receipe_key"], r["need_item_key"], r["name_kr"], r["house_use_type"]) for r in records] == [
        (11, 2, "무기 단조 공방", 4),
        (0, 3, "주거지", 0),
    ]
    assert records[0]["level_exchanges"] == [[5026, 5027], [5028], [], [], []]
    assert records[0]["unknown_end"] == [0, 1, 2, 3, 4, 5]


def test_a_cut_row_raises() -> None:
    with pytest.raises(ValueError):
        parse_houseinforeceipe_records((struct.pack("<I", 1) + _WEAPON_ROW)[:-1])


def test_bytes_after_the_last_row_raise() -> None:
    with pytest.raises(ValueError):
        parse_houseinforeceipe_records(struct.pack("<I", 1) + _WEAPON_ROW + b"\x00")


def test_a_list_count_past_the_file_raises() -> None:
    bad = _row(11, 2, "x", 4, 4, [[], [], [], [], []], [])
    cut = bad[: bad.index(bytes([4, 4, 0])) + 3] + struct.pack("<I", 0xFFFFFFFF)
    with pytest.raises(ValueError):
        parse_houseinforeceipe_records(struct.pack("<I", 1) + cut)

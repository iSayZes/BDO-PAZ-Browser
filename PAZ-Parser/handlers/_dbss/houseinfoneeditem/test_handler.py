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
    case_id,
    header_count,
    run_case,
)

from _common.pabr_offset import parse_bare_offset_rows
from _dbss.houseinforeceipe.parser import FILE_NAME as RECEIPE_FILE
from _dbss.houseinforeceipe.parser import parse_houseinforeceipe_records
from .parser import FILE_NAME, LEVEL_SLOTS, OFFSET_FILE, parse_houseinfoneeditem_records


_COUNT_OFFSET = 0
_RESIDENCE_GROUP = 3
_SILVER = 1


CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={RECEIPE_FILE: RECEIPE_FILE},
    loc_file="languagedata_en.loc",
    uses_loc=False,
    loc_fields=[],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=["need_item_key", "levels", "receipe_keys", "house_uses", "level_count"]),
        DeclaredCountTest(declared=header_count(offset=_COUNT_OFFSET)),
        RangeTest(col="level_count", min_val=0, max_val=LEVEL_SLOTS - 1),
        # Receipe 0 (Residence) reads its costs from group 3.
        TargetTest(col="need_item_key", value=_RESIDENCE_GROUP, expected={"house_uses": ["Residence"]}),
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
        SchemaTest(required_keys=["need_item_key", "offset", "size"]),
        DeclaredCountTest(declared=header_count(offset=_COUNT_OFFSET)),
        TargetTest(col="need_item_key", value=_RESIDENCE_GROUP, expected={"need_item_key": _RESIDENCE_GROUP}),
    ],
)


def _level(level: int, transfer_time: int, items: list[tuple[int, int]]) -> bytes:
    head = struct.pack("<iiI", level, transfer_time, len(items))
    return head + b"".join(struct.pack("<Iq", key, count) for key, count in items)


def _row(key: int, levels: list[tuple[int, list[tuple[int, int]]]]) -> bytes:
    return struct.pack("<H", key) + b"".join(
        _level(slot, transfer_time, items) for slot, (transfer_time, items) in enumerate(levels)
    )


_EMPTY_LEVEL: tuple[int, list[tuple[int, int]]] = (0, [])
_PRICED_ROW = _row(6, [_EMPTY_LEVEL, (0, [(_SILVER, 500)]), (5, [(_SILVER, 10000)]), _EMPTY_LEVEL, _EMPTY_LEVEL, _EMPTY_LEVEL])
_FREE_ROW = _row(3, [_EMPTY_LEVEL] * LEVEL_SLOTS)


@pytest.fixture(scope="module")
def need_item_result(request: Any) -> HandlerResult:
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
def test_houseinfoneeditem_dbss(spec: Any, need_item_result: HandlerResult) -> None:
    need_item_result.check(spec)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_houseinfoneeditemoffset_dbss(spec: Any, offset_result: HandlerResult) -> None:
    offset_result.check(spec)


def test_every_slot_holds_its_own_level(need_item_result: HandlerResult) -> None:
    for r in need_item_result.records:
        assert [level["level"] for level in r["levels"]] == list(range(LEVEL_SLOTS))


def test_level_zero_is_free(need_item_result: HandlerResult) -> None:
    """Slot 0 is level 0: no items and no transfer time."""
    for r in need_item_result.records:
        assert r["levels"][0] == {"level": 0, "transfer_time": 0, "items": []}


def test_every_receipe_group_has_a_row() -> None:
    """Each `need_item_key` of `houseinforeceipe.dbss` names a row here."""
    keys = {r["need_item_key"] for r in parse_houseinfoneeditem_records(load_binary_fixture(FILE_NAME))}
    receipes = parse_houseinforeceipe_records(load_binary_fixture(RECEIPE_FILE))
    assert {r["need_item_key"] for r in receipes} <= keys


def test_offset_rows_tile_the_main_rows() -> None:
    """Each index row starts at its main row's key, and the rows end where
    the next one starts, the last one at the end of the file."""
    main = load_binary_fixture(FILE_NAME)
    rows = sorted(parse_bare_offset_rows(load_binary_fixture(OFFSET_FILE)), key=lambda row: row.offset)
    for row in rows:
        assert struct.unpack_from("<H", main, row.offset)[0] == row.entry_id
    ends = [row.offset + row.size for row in rows]
    assert ends[:-1] == [row.offset for row in rows[1:]]
    assert ends[-1] == len(main)


def test_a_small_table_reads_back() -> None:
    records = parse_houseinfoneeditem_records(struct.pack("<I", 2) + _PRICED_ROW + _FREE_ROW)
    assert [r["need_item_key"] for r in records] == [6, 3]
    assert records[0]["levels"][1] == {"level": 1, "transfer_time": 0, "items": [{"item_key": _SILVER, "count": 500}]}
    assert records[0]["levels"][2]["transfer_time"] == 5
    assert all(not level["items"] for level in records[1]["levels"])


def test_a_cut_row_raises() -> None:
    with pytest.raises(ValueError):
        parse_houseinfoneeditem_records((struct.pack("<I", 1) + _PRICED_ROW)[:-1])


def test_bytes_after_the_last_row_raise() -> None:
    with pytest.raises(ValueError):
        parse_houseinfoneeditem_records(struct.pack("<I", 1) + _FREE_ROW + b"\x00")


def test_an_item_count_past_the_file_raises() -> None:
    bad = struct.pack("<IH", 1, 3) + struct.pack("<iiI", 0, 0, 0xFFFFFFFF)
    with pytest.raises(ValueError):
        parse_houseinfoneeditem_records(bad)

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

from _common.pabr_offset import parse_pabr_offset_rows
from .names import AUCTION_TYPE_NAMES
from .parser import FILE_NAME, OFFSET_FILE, parse_auction_records


_COUNT_SIZE = 4
_OFFSET_COUNT_AT = 4
# Valencia villa auction, type 6 (Villa), since client 1784.
_VILLA_AUCTION = 142
_VILLA_TYPE = 6
# Kunid's Villa, the first villa of auction 142 since client 1784.
_KUNID_VILLA = 3371
# Worker auction, type 1 (WorkerNpc), since client 1784.
_WORKER_AUCTION = 140
_WORKER_TYPE = 1
# Masterpiece auction, type 0 (Item), since client 1784.
_MASTERPIECE_AUCTION = 1001
_ITEM_TYPE = 0


CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    # The handler walks the main file alone; the index is here for its count.
    companion_files={OFFSET_FILE: OFFSET_FILE},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=[],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=[
            "auction_no", "auction_type", "auction_type_name", "start_tick_count",
            "interval_tick_count", "desc_kr", "unknown_desc_kr_01", "houses", "items",
            "unknown_items_00",
        ]),
        DeclaredCountTest(declared=header_count(offset=0)),
        DeclaredCountTest(declared=header_count(offset=_OFFSET_COUNT_AT, companion=OFFSET_FILE)),
        RangeTest(col="auction_type", min_val=0, max_val=len(AUCTION_TYPE_NAMES) - 1),
        TargetTest(col="auction_no", value=_VILLA_AUCTION, expected={"auction_type": _VILLA_TYPE, "auction_type_name": "Villa"}),
        TargetTest(col="auction_no", value=_WORKER_AUCTION, expected={"auction_type": _WORKER_TYPE, "auction_type_name": "WorkerNpc"}),
        TargetTest(col="auction_no", value=_MASTERPIECE_AUCTION, expected={"auction_type": _ITEM_TYPE}),
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
        SchemaTest(required_keys=["auction_no", "offset", "size"]),
        DeclaredCountTest(declared=header_count(offset=_OFFSET_COUNT_AT)),
    ],
)


@pytest.fixture(scope="module")
def auction_result(request: Any) -> HandlerResult:
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
def test_auction_dbss(spec: Any, auction_result: HandlerResult) -> None:
    auction_result.check(spec)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_auctionoffset_dbss(spec: Any, offset_result: HandlerResult) -> None:
    offset_result.check(spec)


def test_auction_numbers_are_unique(auction_result: HandlerResult) -> None:
    keys = [r["auction_no"] for r in auction_result.records]
    assert len(keys) == len(set(keys))


def test_villa_auction_holds_kunids_villa(auction_result: HandlerResult) -> None:
    (villa,) = [r for r in auction_result.records if r["auction_no"] == _VILLA_AUCTION]
    houses = {house["character_key"]: house["name"] for house in villa["houses"]}
    assert houses.get(_KUNID_VILLA) == "Kunid's Villa"


def test_houses_only_on_house_and_villa_auctions(auction_result: HandlerResult) -> None:
    house_types = {AUCTION_TYPE_NAMES.index("House"), AUCTION_TYPE_NAMES.index("Villa")}
    bad = [r["auction_no"] for r in auction_result.records if r["houses"] and r["auction_type"] not in house_types]
    assert not bad, f"auctions of another type with houses: {bad}"


def test_offset_rows_tile_the_main_file() -> None:
    """Each index row starts at its row's auction_no and covers the whole row, with no gap."""
    data = load_binary_fixture(FILE_NAME)
    rows = sorted(parse_pabr_offset_rows(load_binary_fixture(OFFSET_FILE)), key=lambda row: row.offset)
    position = _COUNT_SIZE
    for row in rows:
        assert row.offset == position
        assert struct.unpack_from("<H", data, row.offset)[0] == row.entry_id
        position += row.size
    assert position == len(data)


def _row(auction_no: int, desc: str, houses: list[tuple[int, int]], items: list[tuple[int, int, str, str]]) -> bytes:
    body = struct.pack("<HQQQ", auction_no, 1, 2, len(desc)) + desc.encode("utf-16-le")
    body += struct.pack("<BII", 6, 0, len(houses))
    body += b"".join(struct.pack("<Hq", key, price) for key, price in houses)
    body += struct.pack("<I", len(items))
    for item_key, price, exhibitor, description in items:
        body += struct.pack("<IqQ", item_key, price, len(exhibitor)) + exhibitor.encode("utf-16-le")
        body += struct.pack("<Q", len(description)) + description.encode("utf-16-le") + struct.pack("<I", 0)
    return body + struct.pack("<I", 0)


def test_parser_reads_houses_and_items_and_rejects_extra_or_missing_bytes() -> None:
    data = struct.pack("<I", 1) + _row(7, "빌라", [(_KUNID_VILLA, 1000)], [(320009, 5, "리베", "설명")])
    (record,) = parse_auction_records(data)
    assert record["auction_no"] == 7
    assert record["desc_kr"] == "빌라"
    assert record["houses"] == [{"character_key": _KUNID_VILLA, "lower_price": 1000}]
    assert record["items"] == [{
        "item_key": 320009, "price": 5, "exhibitor_kr": "리베", "description_kr": "설명",
        "unknown_description_kr_00": 0,
    }]
    with pytest.raises(ValueError):
        parse_auction_records(data + b"\x00")
    with pytest.raises(ValueError):
        parse_auction_records(data[:-1])

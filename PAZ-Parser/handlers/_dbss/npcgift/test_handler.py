from __future__ import annotations

import struct
from dataclasses import replace
from typing import Any

import pytest

from tests.framework import (
    CaseInput,
    DeclaredCount,
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


_OFFSET_ROW = struct.Struct("<HIHH")
_GIFT_COUNT_SIZE = 4
_GIFT_ROW_SIZE = 12


def _offset_gift_rows(companion: str) -> DeclaredCount:
    """Gift rows the offset file declares: each record's `data_size` is a u32
    gift count plus 12 bytes per gift."""

    def read(source: CaseInput) -> int:
        raw = source.file(companion)
        count = int.from_bytes(raw[:4], "little")
        total = 0
        for _npc_id, _offset, size, _unknown_08 in _OFFSET_ROW.iter_unpack(raw[4 : 4 + count * _OFFSET_ROW.size]):
            gift_bytes = size - _GIFT_COUNT_SIZE
            if gift_bytes < 0 or gift_bytes % _GIFT_ROW_SIZE:
                raise AssertionError(f"data_size {size} is not a gift count plus 12-byte gift rows")
            total += gift_bytes // _GIFT_ROW_SIZE
        return total

    return read


GIFT_CASE = HandlerCase(
    handler_name="npcgift.dbss",
    data_file="npcgift.dbss",
    companion_files={"npcgiftoffset.dbss": "npcgiftoffset.dbss"},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["NPC Name", "Item Name"],
    internal_path="gamecommondata/binary/npcgift.dbss",
    tests=[
        SchemaTest(
            required_keys=[
                "npc_id",
                "npc_name",
                "item_id",
                "item_name",
                "amity",
                "icon_path",
            ],
        ),
        DeclaredCountTest(declared=_offset_gift_rows("npcgiftoffset.dbss")),
        TargetTest(
            col="item_id",
            value=24626,
            expected={
                "npc_id": 40012,
                "npc_name": "Crio",
                "item_name": "King Clam Wall Ornament",
                "icon_path": (
                    "ui_texture/icon/new_icon/product_icon_png/00024626.png"
                ),
            },
        ),
        TargetTest(
            col="item_id",
            value=16102,
            expected={
                "npc_id": 44019,
                "npc_name": "Deve",
                "item_name": "Transparent Empty Bottle",
            },
        ),
    ],
)

GIFT_DATA_CASE = HandlerCase(
    handler_name="npcgiftdata.dbss",
    data_file="npcgiftdata.dbss",
    companion_files={"npcgiftdataoffset.dbss": "npcgiftdataoffset.dbss"},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["NPC Name", "Dialogue"],
    internal_path="gamecommondata/binary/npcgiftdata.dbss",
    tests=[
        SchemaTest(required_keys=["npc_id", "npc_name", "unknown_02", "dialogue", "dialogue_source"]),
        DeclaredCountTest(declared=header_count()),
        TargetTest(
            col="npc_id",
            value=40012,
            expected={
                "npc_name": "Crio",
                "dialogue": "Thanks. Queek!",
                "dialogue_source": "loc",
            },
        ),
        TargetTest(
            col="npc_id",
            value=44019,
            expected={"npc_name": "Deve", "dialogue_source": "loc"},
        ),
    ],
)

OFFSET_CASES = [
    HandlerCase(
        handler_name="npcgiftoffset.dbss",
        data_file="npcgiftoffset.dbss",
        companion_files={},
        loc_file=None,
        uses_loc=False,
        loc_fields=[],
        internal_path="gamecommondata/binary/npcgiftoffset.dbss",
        tests=[
            SchemaTest(required_keys=["npc_id", "data_offset", "data_size", "unknown_08"]),
            DeclaredCountTest(declared=header_count()),
            RangeTest(col="unknown_08", min_val=0, max_val=0),
            # The first record follows the 4-byte count; its offset skips the npc_id.
            TargetTest(col="npc_id", value=40012, expected={"data_offset": 6}),
        ],
    ),
    HandlerCase(
        handler_name="npcgiftdataoffset.dbss",
        data_file="npcgiftdataoffset.dbss",
        companion_files={},
        loc_file=None,
        uses_loc=False,
        loc_fields=[],
        internal_path="gamecommondata/binary/npcgiftdataoffset.dbss",
        tests=[
            SchemaTest(required_keys=["npc_id", "data_offset", "data_size", "unknown_08"]),
            DeclaredCountTest(declared=header_count()),
            RangeTest(col="unknown_08", min_val=0, max_val=0),
            TargetTest(col="npc_id", value=40012, expected={"data_offset": 6}),
        ],
    ),
]


def _cached_result(request: Any, attr: str, case: HandlerCase) -> HandlerResult:
    result = getattr(request.module, attr, None)
    if result is None:
        result = run_case(replace(case, tests=[]))
        setattr(request.module, attr, result)
    return result


@pytest.fixture(scope="module")
def gift_result(request: Any) -> HandlerResult:
    return _cached_result(request, "_GIFT_RESULT", GIFT_CASE)


@pytest.fixture(scope="module")
def gift_data_result(request: Any) -> HandlerResult:
    return _cached_result(request, "_GIFT_DATA_RESULT", GIFT_DATA_CASE)


@pytest.mark.parametrize("spec", GIFT_CASE.tests, ids=case_id)
def test_npcgift_dbss(spec: Any, gift_result: HandlerResult) -> None:
    gift_result.check(spec)


@pytest.mark.parametrize("spec", GIFT_DATA_CASE.tests, ids=case_id)
def test_npcgiftdata_dbss(spec: Any, gift_data_result: HandlerResult) -> None:
    gift_data_result.check(spec)


@pytest.mark.parametrize("case", OFFSET_CASES, ids=lambda case: case.handler_name)
def test_npcgift_offsets(case: HandlerCase) -> None:
    result = run_case(replace(case, tests=[]))
    for spec in case.tests:
        result.check(spec)


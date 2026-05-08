from __future__ import annotations

from dataclasses import replace
from typing import Any

import pytest

from tests.framework import CountTest, HandlerCase, HandlerResult, PosTest, SchemaTest, TargetTest, case_id, run_case


GIFT_CASE = HandlerCase(
    handler_name="npcgift.dbss",
    data_file="npcgift.dbss",
    companion_files={"npcgiftoffset.dbss": "npcgiftoffset.dbss"},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["NPC Name", "Item Name"],
    internal_path="gamecommondata/binary/npcgift.dbss",
    tests=[
        SchemaTest(required_keys=["npc_id", "npc_name", "item_id", "item_name", "amity"]),
        CountTest(expected=119),
        PosTest(
            pos=0,
            expected={
                "npc_id": 40012,
                "npc_name": "Crio",
                "item_id": 24626,
                "item_name": "King Clam Wall Ornament",
                "amity": 48,
            },
        ),
        PosTest(
            pos=-1,
            expected={
                "npc_id": 44019,
                "npc_name": "Deve",
                "item_id": 16102,
                "item_name": "Transparent Empty Bottle",
                "amity": 31,
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
        SchemaTest(required_keys=["npc_id", "npc_name", "unknown_param", "dialogue", "dialogue_source"]),
        CountTest(expected=24),
        PosTest(
            pos=0,
            expected={
                "npc_id": 40012,
                "npc_name": "Crio",
                "unknown_param": 70,
                "dialogue": "Thanks. Queek!",
                "dialogue_source": "loc",
            },
        ),
        TargetTest(
            col="npc_id",
            value=44019,
            expected={"npc_name": "Deve", "unknown_param": 70, "dialogue_source": "loc"},
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
            SchemaTest(required_keys=["npc_id", "data_offset", "data_size", "padding"]),
            CountTest(expected=24),
            PosTest(pos=0, expected={"npc_id": 40012, "data_offset": 6, "data_size": 64, "padding": 0}),
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
            SchemaTest(required_keys=["npc_id", "data_offset", "data_size", "padding"]),
            CountTest(expected=24),
            PosTest(pos=0, expected={"npc_id": 40012, "data_offset": 6, "data_size": 30, "padding": 0}),
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
    spec.check(gift_result.records)


@pytest.mark.parametrize("spec", GIFT_DATA_CASE.tests, ids=case_id)
def test_npcgiftdata_dbss(spec: Any, gift_data_result: HandlerResult) -> None:
    spec.check(gift_data_result.records)


@pytest.mark.parametrize("case", OFFSET_CASES, ids=lambda case: case.handler_name)
def test_npcgift_offsets(case: HandlerCase) -> None:
    result = run_case(replace(case, tests=[]))
    for spec in case.tests:
        spec.check(result.records)

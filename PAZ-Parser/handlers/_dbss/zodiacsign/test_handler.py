from __future__ import annotations

from dataclasses import replace
import struct
from typing import Any

import pytest

from handlers._dbss.zodiacsign.parser import parse_zodiacsignorderoffset_records

from tests.framework import (
    DeclaredCountTest,
    HandlerCase,
    HandlerResult,
    SchemaTest,
    TargetTest,
    UserLanguageTest,
    case_id,
    header_count,
    run_case,
)


CASE = HandlerCase(
    handler_name="zodiacsign.dbss",
    data_file="zodiacsign.dbss",
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["Name", "Traits"],
    internal_path="gamecommondata/binary/zodiacsign.dbss",
    tests=[
        SchemaTest(required_keys=["zodiac_id", "name", "float_count", "pairs_count", "constellation_name", "trait"]),
        DeclaredCountTest(declared=header_count()),
        # LOC type 7 names every sign and lists its traits.
        UserLanguageTest(fields=["name", "trait"]),
        TargetTest(
            col="zodiac_id",
            value=1,
            expected={
                "name": "Hammer",
                "constellation_name": "망치자리",
                "trait": "Brave, Conservative, Righteous, Collaborative, Hot-Blooded.",
            },
        ),
        TargetTest(
            col="zodiac_id",
            value=6,
            expected={
                "name": "Black Dragon",
                "constellation_name": "검은용자리",
                "trait": "Wealth and Fame, Noble, Delicate, Sensitive, Sociable.",
            },
        ),
        TargetTest(
            col="zodiac_id",
            value=12,
            expected={
                "name": "Goblin",
                "constellation_name": "고블린자리",
                "trait": "Linguist, Strong Beliefs, Intellectual, Materialistic, Wise.",
            },
        ),
    ],
)


ORDER_CASE = HandlerCase(
    handler_name="zodiacsignorder.dbss",
    data_file="zodiacsignorder.dbss",
    companion_files={"zodiacsignorderoffset.dbss": "zodiacsignorderoffset.dbss"},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["Zodiac"],
    internal_path="gamecommondata/binary/zodiacsignorder.dbss",
    tests=[
        SchemaTest(required_keys=["personality_type", "zodiac_name", "variant", "trigger_count", "trigger_order"]),
        DeclaredCountTest(declared=header_count(companion="zodiacsignorderoffset.dbss")),
    ],
)


@pytest.fixture(scope="module")
def zodiacsign_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_zodiacsign_dbss(spec: Any, zodiacsign_result: HandlerResult) -> None:
    zodiacsign_result.check(spec)


@pytest.fixture(scope="module")
def order_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_ORDER_RESULT", None)
    if result is None:
        result = run_case(replace(ORDER_CASE, tests=[]))
        request.module._ORDER_RESULT = result
    return result


@pytest.mark.parametrize("spec", ORDER_CASE.tests, ids=case_id)
def test_zodiacsignorder_dbss(spec: Any, order_result: HandlerResult) -> None:
    order_result.check(spec)


def test_zodiacsignorder_every_trigger_is_stored(order_result: HandlerResult) -> None:
    # u32 count, u32 zero, then `count` u16 orders and the u8 + u16 tail fill
    # each record's offset-file size. A first star implied as slot 0 would
    # put a nonzero order in the zero word.
    data = order_result.source.data
    offsets = parse_zodiacsignorderoffset_records(order_result.source.companions["zodiacsignorderoffset.dbss"])
    parsed = {r["personality_type"]: r["trigger_order"] for r in order_result.records}
    bad = []
    for entry in offsets:
        start = entry["data_offset"]
        count, reserved = struct.unpack_from("<II", data, start)
        stored = list(struct.unpack_from(f"<{count}H", data, start + 8))
        framed = reserved == 0 and 4 + 4 + 2 * count + 3 == entry["data_size"]
        if not framed or parsed.get(entry["personality_type"]) != stored:
            bad.append(entry["personality_type"])
    assert not bad, f"records not framed as count + zero + orders: {bad}"

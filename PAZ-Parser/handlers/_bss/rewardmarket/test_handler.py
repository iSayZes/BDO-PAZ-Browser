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
    UserLanguageTest,
    case_id,
    header_count,
    run_case,
)

from _dbss.pet.parser import parse_petoffset_records
from .parser import FILE_NAME, parse_rewardmarket_records


CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["pet_name", "rewards_text"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(
            required_keys=["trade_key", "pet_key", "unknown_06", "reward_count", "rewards", "pet_name", "rewards_text"],
        ),
        DeclaredCountTest(declared=header_count(offset=4)),
        UserLanguageTest(fields=["pet_name", "rewards_text"]),
    ],
)


@pytest.fixture(scope="module")
def rewardmarket_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_rewardmarket_bss(spec: Any, rewardmarket_result: HandlerResult) -> None:
    rewardmarket_result.check(spec)


def test_every_trade_takes_a_pet() -> None:
    pets = {row["pet_id"] for row in parse_petoffset_records(load_binary_fixture("petoffset.dbss"))}
    missing = [
        (record["trade_key"], record["pet_key"])
        for record in parse_rewardmarket_records(load_binary_fixture(FILE_NAME))
        if record["pet_key"] not in pets
    ]
    assert not missing, missing[:10]


def test_trade_keys_are_unique() -> None:
    keys = [record["trade_key"] for record in parse_rewardmarket_records(load_binary_fixture(FILE_NAME))]
    assert len(keys) == len(set(keys))


def test_parse_reads_the_rewards() -> None:
    row = struct.pack("<HI11s", 3, 9779, b"\0" * 11) + struct.pack("<I", 2) + struct.pack("<IQIQ", 1000131, 1, 1000692, 2)
    body = struct.pack("<I", 1) + row
    data = b"PABR" + body + struct.pack("<III", 0, 4 + len(body), 0)

    (record,) = parse_rewardmarket_records(data)

    assert record["trade_key"] == 3
    assert record["pet_key"] == 9779
    assert record["rewards"] == [{"item_key": 1000131, "item_count": 1}, {"item_key": 1000692, "item_count": 2}]

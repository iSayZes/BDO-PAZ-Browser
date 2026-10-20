from __future__ import annotations

from dataclasses import replace
from typing import Any

import pytest

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

from _bss.servant.parser import parse_servant_records
from _common.servant_kind import SERVANT_KIND_NAMES
from _dbss.vehicleskill.parser import vehicle_skill_names_kr


_FLAGS = (
    "is_male",
    "is_display_gender",
    "servant_main_model",
    "is_mating_result",
    "is_trade",
    "is_only_pcroom",
    "can_mix",
    "can_mating",
)

CASE = HandlerCase(
    handler_name="servant.bss",
    data_file="servant.bss",
    companion_files={
        "characterstaticoffset.dbss": "characterstaticoffset.dbss",
        "vehicleskill.dbss": "vehicleskill.dbss",
    },
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["name", "basic_learn_skills", "stallion_skills"],
    internal_path="gamecommondata/binary/servant.bss",
    tests=[
        SchemaTest(
            required_keys=[
                "character_id",
                "name_kr",
                "name",
                "servant_kind",
                "servant_kind_name",
                "servant_kind_sub",
                "tier",
                "grade",
                "color1",
                "color2",
                "color3",
                "mating_count",
                "lifespan",
                "base_price",
                "price_per_level",
                "link_count",
                "experience_per_one",
                "form_index",
                "basic_learn_skill_max_count",
                "basic_learn_skill_count",
                "basic_learn_skill_keys",
                "basic_learn_skills",
                "unknown_basic_learn_skill_keys_00",
                "reward_money_percent",
                "stallion_skill_count",
                "stallion_skill_keys",
                "stallion_skills",
                "unknown_stallion_skill_keys_02",
                "has_character_row",
                *_FLAGS,
            ],
        ),
        DeclaredCountTest(declared=header_count(offset=0)),
        RangeTest(col="servant_kind", min_val=0, max_val=len(SERVANT_KIND_NAMES) - 1),
        *(RangeTest(col=flag, min_val=0, max_val=1) for flag in _FLAGS),
        # Names are left out: some servants have no LOC name and show their Korean
        # one (31613 to 31618 and the boss mounts 29801 to 29804 on client 3474).
        UserLanguageTest(fields=["basic_learn_skills", "stallion_skills"]),
        TargetTest(
            col="character_id",
            value=9909,
            expected={"name_kr": "탑승용 수말9", "servant_kind": 0, "servant_kind_name": "Horse"},
        ),
        TargetTest(
            col="character_id",
            value=31001,
            expected={"name": "Epheria Sailboat", "servant_kind_name": "PersonalTradeShip"},
        ),
        TargetTest(col="character_id", value=9052, expected={"name": "Merchant Wagon", "servant_kind": 5}),
    ],
)


@pytest.fixture(scope="module")
def servant_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_servant_bss(spec: Any, servant_result: HandlerResult) -> None:
    servant_result.check(spec)


def test_skill_lists_match_their_counts(servant_result: HandlerResult) -> None:
    # Checks the two counted lists: each count sits right before its keys.
    for record in servant_result.records:
        assert len(record["basic_learn_skill_keys"]) == record["basic_learn_skill_count"], record
        assert len(record["stallion_skill_keys"]) == record["stallion_skill_count"], record


def test_every_skill_key_is_a_vehicle_skill(servant_result: HandlerResult) -> None:
    # Checks the skill lists against their target table: every key is a vehicleskill.dbss key.
    skill_keys = set(vehicle_skill_names_kr(servant_result.source.file("vehicleskill.dbss")))
    for record in servant_result.records:
        keys = set(record["basic_learn_skill_keys"]) | set(record["stallion_skill_keys"])
        assert keys <= skill_keys, (record["character_id"], keys - skill_keys)


def test_only_breedable_servants_can_mate(servant_result: HandlerResult) -> None:
    # Checks the `can_mating` name: the byte is set exactly where the breeding count is.
    for record in servant_result.records:
        assert bool(record["can_mating"]) == (record["mating_count"] > 0), record


def test_every_servant_has_a_character_row(servant_result: HandlerResult) -> None:
    # Checks `character_id`: each one is a characterstatic.dbss character.
    assert all(record["has_character_row"] for record in servant_result.records)


def test_repeated_character_id_must_match() -> None:
    # u32 count 1, then character 1 repeated as 2.
    with pytest.raises(ValueError, match="repeats character 2, expected 1"):
        parse_servant_records(b"\x01\x00\x00\x00\x01\x00\x02\x00" + bytes(80))


def test_bytes_after_the_last_row_raise() -> None:
    with pytest.raises(ValueError, match="bytes follow row 0"):
        parse_servant_records(bytes(4) + b"\x00")

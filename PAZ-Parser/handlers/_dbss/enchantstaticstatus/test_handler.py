from __future__ import annotations

from dataclasses import replace
from typing import Any

import pytest

from _common.lookup_index import IndexKind
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


# Enchant keys from itemenchant.dbss (enchantstaticstatus_dbss.md), checked
# against bdocodex (2026-10-06).
_KZARKA_GAUNTLET = 662
_SICILS_NECKLACE = 8017
_KHARAZAD_NECKLACE = 12336
_LEVEL_SHIFT = 24
_PRI = 16
_MAX_LEVEL = 0xFF
_BLACK_STONE = 16001
_CONCENTRATED_BLACK_STONE = 16004
_SICILS_NECKLACE_ITEM = 11625
_ESSENCE_OF_DAWN = 820979
_DAWN_BLACK_STONE = 820984
_KZARKA_GAUNTLET_ITEM = 11210


def _status_key(enchant_key: int, level: int) -> int:
    return level << _LEVEL_SHIFT | enchant_key


CASE = HandlerCase(
    handler_name="enchantstaticstatus.dbss",
    data_file="enchantstaticstatus.dbss",
    companion_files={"enchantstaticstatusoffset.dbss": "enchantstaticstatusoffset.dbss"},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["Material"],
    internal_path="gamecommondata/binary/enchantstaticstatus.dbss",
    # Only the link the TargetTest checks; the real index is built from itemenchant.dbss.
    lookup_indexes={IndexKind.ENCHANT_KEY_ITEMS: {_KZARKA_GAUNTLET: (_KZARKA_GAUNTLET_ITEM,)}},
    tests=[
        SchemaTest(
            required_keys=[
                "status_key",
                "enchant_key",
                "level",
                "material_item_id",
                "item_ids",
                "item_names",
                "item_count",
                "material_name",
                "material_count",
                "success_chance",
                "fail_result",
                "fail_result_name",
                "downgrade_chance",
                "fail_durability_loss",
                "perfect_count",
                "perfect_durability_loss",
                "max_durability",
                "ap_min",
                "ap_max",
                "accuracy",
                "evasion",
                "hidden_evasion",
                "damage_reduction",
                "hidden_damage_reduction",
                "max_hp",
                "aid_item_ids",
                "aid_names",
                "aid_count",
                "effects",
                "description",
            ],
        ),
        # The main file opens with the block count, which the offset table repeats.
        DeclaredCountTest(declared=header_count(offset=0)),
        DeclaredCountTest(declared=header_count(offset=4, companion="enchantstaticstatusoffset.dbss")),
        RangeTest(col="level", min_val=0, max_val=_MAX_LEVEL),
        # Stored in millionths, shown as a percentage.
        RangeTest(col="success_chance", min_val=0, max_val=100),
        RangeTest(col="downgrade_chance", min_val=0, max_val=100),
        # Safe, destroyed or downgrade; 0 on attempts that cannot fail.
        RangeTest(col="fail_result", min_val=0, max_val=3),
        # Every level of a key lists the items that enhance with it.
        TargetTest(
            col="status_key",
            value=_status_key(_KZARKA_GAUNTLET, _PRI),
            expected={"item_ids": [_KZARKA_GAUNTLET_ITEM], "item_names": ["Kzarka Gauntlet"], "item_count": 1},
        ),
        # Level 0 is the base item: nothing to pay for it.
        TargetTest(
            col="status_key",
            value=_status_key(_KZARKA_GAUNTLET, 0),
            expected={"material_item_id": None, "material_count": None, "success_chance": None},
        ),
        # +1 to +15 take a Black Stone, PRI a Concentrated Magical Black Stone.
        TargetTest(
            col="status_key",
            value=_status_key(_KZARKA_GAUNTLET, 1),
            expected={"enchant_key": _KZARKA_GAUNTLET, "level": 1, "material_item_id": _BLACK_STONE,
                      "material_name": "Black Stone"},
        ),
        TargetTest(
            col="status_key",
            value=_status_key(_KZARKA_GAUNTLET, _PRI),
            expected={"material_item_id": _CONCENTRATED_BLACK_STONE,
                      "material_name": "Concentrated Magical Black Stone"},
        ),
        # Ordinary accessories take a copy of themselves.
        TargetTest(
            col="status_key",
            value=_status_key(_SICILS_NECKLACE, 1),
            expected={"material_item_id": _SICILS_NECKLACE_ITEM},
        ),
        # Kharazad takes Essence of Dawn up to IX and a Dawn Black Stone for X.
        TargetTest(
            col="status_key",
            value=_status_key(_KHARAZAD_NECKLACE, 1),
            expected={"material_item_id": _ESSENCE_OF_DAWN},
        ),
        TargetTest(
            col="status_key",
            value=_status_key(_KHARAZAD_NECKLACE, 10),
            expected={"material_item_id": _DAWN_BLACK_STONE},
        ),
    ],
)


@pytest.fixture(scope="module")
def enchantstaticstatus_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_enchantstaticstatus(spec: Any, enchantstaticstatus_result: HandlerResult) -> None:
    enchantstaticstatus_result.check(spec)

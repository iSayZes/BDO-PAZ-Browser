from __future__ import annotations

from dataclasses import replace
from typing import Any

import pytest

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

from .parser import POSITION_FIELDS


_ICON_DIR = "ui_texture/renewal/etc/wordmap"
_BALENOS = 0
_CALPHEON = 2
# The Silver Mane and Golden Eagle crown and armor, the conquest booty.
_SILVER_MANE_BOOTY = [23381, 23386]
_GOLDEN_EAGLE_BOOTY = [23383, 23388]
# A territory supply key is the territory key times 100 plus a small index.
_SUPPLY_KEYS_PER_TERRITORY = 100

CASE = HandlerCase(
    handler_name="territoryinfo.bss",
    data_file="territoryinfo.bss",
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["name", "nation"],
    internal_path="gamecommondata/binary/territoryinfo.bss",
    tests=[
        SchemaTest(
            required_keys=[
                "territory_key",
                "name_kr",
                "nation_kr",
                "name",
                "nation",
                "is_king_territory_only",
                "is_lord_territory_only",
                "occupying_tent_position",
                "volunteer_attack_position",
                "volunteer_defense_position",
                "national_key",
                "icon_large_path",
                "icon_small_path",
                "booty_item_ids",
                "booty",
                "territory_supply_keys",
            ],
        ),
        DeclaredCountTest(declared=header_count(offset=4)),
        TargetTest(
            col="territory_key",
            value=_BALENOS,
            expected={
                "name_kr": "발레노스 자치령",
                "nation_kr": "칼페온 공화국",
                "name": "Balenos",
                "nation": "Republic of Calpheon",
                "is_king_territory_only": False,
                "is_lord_territory_only": True,
                "icon_small_path": f"{_ICON_DIR}/territorymark_valenos_small.dds",
                "booty_item_ids": _SILVER_MANE_BOOTY,
            },
        ),
        TargetTest(
            col="territory_key",
            value=_CALPHEON,
            expected={
                "name_kr": "칼페온 직할령",
                "name": "Calpheon",
                "is_king_territory_only": True,
                "is_lord_territory_only": False,
                "booty_item_ids": _GOLDEN_EAGLE_BOOTY,
            },
        ),
    ],
)


@pytest.fixture(scope="module")
def territoryinfo_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_territoryinfo_bss(spec: Any, territoryinfo_result: HandlerResult) -> None:
    territoryinfo_result.check(spec)


def test_keys_follow_row_order(territoryinfo_result: HandlerResult) -> None:
    """Each key is its row index, the LOC type 12 ID."""
    keys = [r["territory_key"] for r in territoryinfo_result.records]
    assert keys == list(range(len(keys)))


def test_every_territory_has_names_and_icons(territoryinfo_result: HandlerResult) -> None:
    for record in territoryinfo_result.records:
        assert record["name_kr"] and record["nation_kr"], record["territory_key"]
        assert record["icon_large_path"].startswith("ui_texture/"), record["territory_key"]
        assert record["icon_small_path"].startswith("ui_texture/"), record["territory_key"]
        assert all(len(record[field]) == 3 for field in POSITION_FIELDS), record["territory_key"]


def test_national_key_matches_the_nation_name(territoryinfo_result: HandlerResult) -> None:
    """Territories of one nation share its key, and no two nations do."""
    nation_by_key: dict[int, str] = {}
    for record in territoryinfo_result.records:
        assert nation_by_key.setdefault(record["national_key"], record["nation_kr"]) == record["nation_kr"]
    assert len(set(nation_by_key.values())) == len(nation_by_key)


def test_lord_territories_are_not_king_territories(territoryinfo_result: HandlerResult) -> None:
    for record in territoryinfo_result.records:
        assert not (record["is_lord_territory_only"] and record["is_king_territory_only"]), record["territory_key"]


def test_supply_keys_belong_to_their_territory(territoryinfo_result: HandlerResult) -> None:
    """`TerritoryTradeItemList_Table` numbers a territory's supply groups from its key times 100."""
    for record in territoryinfo_result.records:
        for supply_key in record["territory_supply_keys"]:
            assert supply_key // _SUPPLY_KEYS_PER_TERRITORY == record["territory_key"], supply_key

from __future__ import annotations

import struct
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

from .parser import POSITION_FIELDS, parse_territoryinfo_records


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
        assert all(len(record[field]) == 3 for field in POSITION_FIELDS if field in record), record["territory_key"]


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


# Older layouts, built in memory: the fixtures hold the live client only.
_CALPHEON_TENT = (-357067.0, 5348.0, -64503.0)
_NATIONAL_KEY = 0x71B32A3D
_STRINGS = ["칼페온 공화국", "칼페온 직할령", "Renewal/ETC/WordMap/large.dds", "Renewal/ETC/WordMap/small.dds"]


def _counted(count_format: str, value_format: str, values: list[int]) -> bytes:
    return struct.pack(f"<{count_format}{len(values)}{value_format}", len(values), *values)


def _pabr_file(rows: list[bytes]) -> bytes:
    """PABR header, the rows, a wide string table of `_STRINGS` and the trailer."""
    body = b"PABR" + struct.pack("<I", len(rows)) + b"".join(rows)
    encoded = [text.encode("utf-16-le") for text in _STRINGS]
    table = struct.pack("<I", len(encoded)) + b"".join(struct.pack("<BI", 1, len(raw)) + raw for raw in encoded)
    return body + table + struct.pack("<II", len(body), 0)


def _layout_6_row() -> bytes:
    """The client 1784 shape: five positions, u16 trade and supply keys, u32 tail."""
    coords = _CALPHEON_TENT * 5
    return (
        struct.pack("<HBB15fI4I", _CALPHEON, 1, 0, *coords, _NATIONAL_KEY, 0, 1, 2, 3)
        + _counted("Q", "I", _GOLDEN_EAGLE_BOOTY)
        + _counted("Q", "H", [205, 201])
        + _counted("Q", "H", [213, 214])
        + struct.pack("<I", 0)
    )


def _layout_1_file() -> bytes:
    """No PABR header: one position, inline UTF-16LE strings, u32 list counts."""
    strings = b"".join(struct.pack("<Q", len(text)) + text.encode("utf-16-le") for text in _STRINGS)
    row = (
        struct.pack("<HBB3fI", _CALPHEON, 1, 0, *_CALPHEON_TENT, _NATIONAL_KEY)
        + strings
        + _counted("I", "I", _GOLDEN_EAGLE_BOOTY)
        + _counted("I", "H", [205, 201])
        + _counted("I", "H", [213])
    )
    return struct.pack("<I", 1) + row


def test_layout_6_reads_trade_keys_and_plunder_positions() -> None:
    (record,) = parse_territoryinfo_records(_pabr_file([_layout_6_row()]))

    assert (record["territory_key"], record["name_kr"], record["nation_kr"]) == (_CALPHEON, _STRINGS[1], _STRINGS[0])
    assert record["booty_item_ids"] == _GOLDEN_EAGLE_BOOTY
    assert (record["territory_trade_keys"], record["territory_supply_keys"]) == ([205, 201], [213, 214])
    assert record["plunder_defense_position"] == list(_CALPHEON_TENT)
    assert record["unknown_tail"] == 0


def test_layout_1_reads_inline_strings_and_one_position() -> None:
    (record,) = parse_territoryinfo_records(_layout_1_file())

    assert (record["name_kr"], record["icon_small_path"]) == (_STRINGS[1], "ui_texture/renewal/etc/wordmap/small.dds")
    assert [field for field in POSITION_FIELDS if field in record] == ["occupying_tent_position"]
    assert (record["territory_trade_keys"], record["territory_supply_keys"]) == ([205, 201], [213])
    assert "unknown_tail" not in record


def test_a_row_no_layout_tiles_raises() -> None:
    with pytest.raises(ValueError, match="fits no known layout"):
        parse_territoryinfo_records(_pabr_file([_layout_6_row() + b"\0"]))

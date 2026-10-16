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
    case_id,
    header_count,
    run_case,
)

from _bss.specialenchantitem.parser import build_item_key_icon_index
from _common.prefixed_string import find_prefixed_ascii
from _common.ui_texture import UI_TEXTURE_ICON_ROOT
from _dbss.itemenchant.parser import parse_itemenchantoffset_records


_ITEMENCHANT_FILE = "itemenchant.dbss"
_ITEMENCHANT_OFFSET_FILE = "itemenchantoffset.dbss"
_WEAPON_DIR = "ui_texture/icon/new_icon/06_pc_equipitem/00_common/01_weapon"
# Sovereign Longsword: levels 0 to 10, drawn as PRI to DEC above level 0.
_SOVEREIGN_LONGSWORD = 747201
_DEC = 10
_DEC_DISPLAY_LEVEL = 25

CASE = HandlerCase(
    handler_name="specialenchantitem.bss",
    data_file="specialenchantitem.bss",
    # Not read by the handler; the cross-check below compares every row with them.
    companion_files={
        _ITEMENCHANT_FILE: _ITEMENCHANT_FILE,
        _ITEMENCHANT_OFFSET_FILE: _ITEMENCHANT_OFFSET_FILE,
    },
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["name"],
    internal_path="gamecommondata/binary/specialenchantitem.bss",
    tests=[
        SchemaTest(
            required_keys=[
                "item_key",
                "item_id",
                "enchant_level",
                "display_level",
                "shown_as",
                "icon_path",
                "name_kr",
                "name",
                "unknown_11",
                "unknown_12",
            ],
        ),
        DeclaredCountTest(declared=header_count(offset=4)),
        RangeTest(col="unknown_11", min_val=0, max_val=1),
        RangeTest(col="unknown_12", min_val=0, max_val=1),
        TargetTest(
            col="item_key",
            value=_DEC << 24 | _SOVEREIGN_LONGSWORD,
            expected={
                "item_id": _SOVEREIGN_LONGSWORD,
                "enchant_level": _DEC,
                "display_level": _DEC_DISPLAY_LEVEL,
                "shown_as": "DEC",
                "icon_path": f"{_WEAPON_DIR}/00747201_02.dds",
                "name": "DEC: Sovereign Longsword",
            },
        ),
        TargetTest(
            col="item_key",
            value=_SOVEREIGN_LONGSWORD,
            expected={
                "enchant_level": 0,
                "display_level": None,
                "shown_as": "",
                "icon_path": f"{_WEAPON_DIR}/00747201.dds",
                "name": "Sovereign Longsword",
            },
        ),
    ],
)


@pytest.fixture(scope="module")
def specialenchantitem_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_specialenchantitem_bss(spec: Any, specialenchantitem_result: HandlerResult) -> None:
    specialenchantitem_result.check(spec)


def test_rows_follow_itemenchant_keys_and_icons(specialenchantitem_result: HandlerResult) -> None:
    """Every row is an itemenchant.dbss key, in its order, with that level block's icon."""
    source = specialenchantitem_result.source
    data = source.file(_ITEMENCHANT_FILE)
    offset_rows = parse_itemenchantoffset_records(source.file(_ITEMENCHANT_OFFSET_FILE))
    by_key = {row["key"]: row for row in offset_rows}
    order = {row["key"]: index for index, row in enumerate(offset_rows)}

    records = specialenchantitem_result.records
    assert all(r["item_key"] in by_key for r in records)
    positions = [order[r["item_key"]] for r in records]
    assert positions == sorted(positions)

    for record in records:
        row = by_key[record["item_key"]]
        start = row["data_offset"]
        strings = find_prefixed_ascii(data, start, start + row["data_size"])
        assert f"{UI_TEXTURE_ICON_ROOT}{strings[0].lower()}" == record["icon_path"], record["item_key"]


def test_item_key_icon_index_matches_the_icon_column(
    specialenchantitem_result: HandlerResult,
) -> None:
    """IndexKind.ITEM_KEY_ICON is this table's icons by item key."""
    index = build_item_key_icon_index(specialenchantitem_result.source.data)

    assert index == {r["item_key"]: r["icon_path"] for r in specialenchantitem_result.records}


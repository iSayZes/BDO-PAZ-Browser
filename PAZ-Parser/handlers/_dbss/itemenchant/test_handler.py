from __future__ import annotations

from dataclasses import replace
from typing import Any

import pytest

from tests.framework import (
    CountTest,
    HandlerCase,
    HandlerResult,
    PosTest,
    RangeTest,
    SchemaTest,
    TargetTest,
    case_id,
    run_case,
)


_ICON_ROOT = "ui_texture/icon/new_icon"
# King Clam Wall Ornament: furniture, so its icon is named after the 3D asset
# and is unreachable from the item ID alone. It is the case this format solves.
_KING_CLAM = 24626

CASE = HandlerCase(
    handler_name="itemenchant.dbss",
    data_file="itemenchant.dbss",
    companion_files={"itemenchantoffset.dbss": "itemenchantoffset.dbss"},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["Item"],
    internal_path="gamecommondata/binary/itemenchant.dbss",
    tests=[
        SchemaTest(
            required_keys=[
                "item_id",
                "key_variant",
                "icon_path",
                "effect_tag",
                "block_size",
                "item_name",
            ],
        ),
        CountTest(expected=169_965),
        # Variant 0 is the base item: exactly one per item ID.
        RangeTest(col="key_variant", min_val=0, max_val=25),
        RangeTest(col="item_id", min_val=1, max_val=1_000_827),
        # The furniture case: icon path comes from the block, not the item ID.
        TargetTest(
            col="item_id",
            value=_KING_CLAM,
            expected={
                "key_variant": 0,
                "item_name": "King Clam Wall Ornament",
                "icon_path": (
                    f"{_ICON_ROOT}/03_etc/06_housing/"
                    "inhouse_cultivate_sea_clam_01_wall.dds"
                ),
                "effect_tag": "",
                "block_size": 870,
            },
        ),
        # First offset row is a max-enchant weapon variant.
        PosTest(
            pos=0,
            expected={
                "item_id": 697192,
                "key_variant": 24,
                "block_size": 1378,
            },
        ),
    ],
)


@pytest.fixture(scope="module")
def itemenchant_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_itemenchant_dbss(
    spec: Any,
    itemenchant_result: HandlerResult,
) -> None:
    spec.check(itemenchant_result.records)


def test_build_item_icon_index_covers_the_furniture_case() -> None:
    """The index is what lets an item ID reach an asset-named icon."""
    from _dbss.itemenchant.parser import build_item_icon_index
    from tests.fixtures import ensure_fixtures

    paths = ensure_fixtures(CASE)
    index = build_item_icon_index(
        paths["itemenchant.dbss"].read_bytes(),
        paths["itemenchantoffset.dbss"].read_bytes(),
    )

    # One entry per level-0 record, not one per enchant variant.
    assert len(index) == 69_954
    assert index[_KING_CLAM] == (
        f"{_ICON_ROOT}/03_etc/06_housing/"
        "inhouse_cultivate_sea_clam_01_wall.dds"
    )
    # Every path stays inside the icon tree.
    assert all(p.startswith("ui_texture/icon/") for p in index.values())

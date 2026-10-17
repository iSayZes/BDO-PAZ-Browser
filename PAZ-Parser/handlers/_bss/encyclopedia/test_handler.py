from __future__ import annotations

import struct
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

from _bss.encyclopedia.parser import parse_encyclopedia_records
from _common.pabr_strings import fixed_row_offsets


_DATA_FILE = "encyclopedia.bss"
# The first entry, the Mudskipper.
_MUDSKIPPER_KEY = 1
_MUDSKIPPER_ITEM = 8201
# The rows start after the PABR magic with this count.
_COUNT_OFFSET = 4
# Category is a tab of the window: 0 Others, 1 Freshwater, 2 Saltwater, 3 Crustacean.
_MAX_CATEGORY = 3
_MIN_RARENESS = 1
_MAX_RARENESS = 10
_ROW_SIZE = 104
_DICE_OFFSET = 0x28
_DICE = struct.Struct("<IIi")

CASE = HandlerCase(
    handler_name=_DATA_FILE,
    data_file=_DATA_FILE,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["item_name", "description"],
    internal_path=f"gamecommondata/binary/{_DATA_FILE}",
    tests=[
        SchemaTest(
            required_keys=[
                "key",
                "item_id",
                "type",
                "category",
                "rareness",
                "base_size",
                "fish_exp_rate",
                "fish_exp_type",
                "description_kr",
                "image_path",
                "vary_sizes",
                "unknown_10",
                "unknown_64",
                "item_name",
                "category_name",
                "average_size",
                "description",
            ],
        ),
        DeclaredCountTest(declared=header_count(offset=_COUNT_OFFSET)),
        RangeTest(col="category", min_val=0, max_val=_MAX_CATEGORY),
        RangeTest(col="rareness", min_val=_MIN_RARENESS, max_val=_MAX_RARENESS),
        RangeTest(col="type", min_val=0, max_val=0),
        UserLanguageTest(fields=["item_name", "category_name", "description"]),
        TargetTest(
            col="key",
            value=_MUDSKIPPER_KEY,
            expected={
                "item_id": _MUDSKIPPER_ITEM,
                "item_name": "Mudskipper",
                "image_path": "ui_texture/ui_artwork/encyclopedia/ic_08501.dds",
            },
        ),
    ],
)


@pytest.fixture(scope="module")
def encyclopedia_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_encyclopedia_bss(spec: Any, encyclopedia_result: HandlerResult) -> None:
    encyclopedia_result.check(spec)


def test_every_entry_has_an_image_and_a_description(encyclopedia_result: HandlerResult) -> None:
    """Each row's two string references point at an artwork path and a text."""
    without = [
        r["key"] for r in encyclopedia_result.records
        if not r["image_path"].endswith(".dds") or not r["description_kr"]
    ]
    assert not without, f"entries without image or description: {without}"


def test_dice_read_count_sides_and_bonus(encyclopedia_result: HandlerResult) -> None:
    """A roll packed as 2D6-3 into the first row's fourth die lands in vary_sizes[3]."""
    data = bytearray(encyclopedia_result.source.data)
    first_row = fixed_row_offsets(bytes(data), _ROW_SIZE, _DATA_FILE)[0]
    _DICE.pack_into(data, first_row + _DICE_OFFSET + 3 * _DICE.size, 2, 6, -3)

    vary_sizes = parse_encyclopedia_records(bytes(data))[0]["vary_sizes"]

    assert vary_sizes[3] == {"count": 2, "sides": 6, "bonus": -3}
    assert vary_sizes[2] == parse_encyclopedia_records(encyclopedia_result.source.data)[0]["vary_sizes"][2]


def test_bad_magic_raises() -> None:
    with pytest.raises(ValueError):
        parse_encyclopedia_records(b"XXXX" + bytes(16))

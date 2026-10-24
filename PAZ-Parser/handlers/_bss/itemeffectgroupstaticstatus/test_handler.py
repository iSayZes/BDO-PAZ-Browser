from __future__ import annotations

import struct
from dataclasses import replace
from typing import Any

import pytest

from tests.framework import (
    CaseInput,
    DeclaredCountTest,
    HandlerCase,
    HandlerResult,
    SchemaTest,
    TargetTest,
    UserLanguageTest,
    case_id,
    run_case,
)

from .parser import FILE_NAME, parse_itemeffectgroup_effects


_U32 = struct.Struct("<I")
_U64 = struct.Struct("<Q")
_GROUP_HEAD = struct.Struct("<II")
# The fixed part of an effect: index, unknown_04, the colour's u64 length,
# the RGB bytes, name hash and pigment item.
_EFFECT_FIXED = 4 + 1 + 8 + 3 + 4 + 4
_COLOR_LENGTH_AT = 5
_HEX_COLOR = 6
# The Sovereign main weapon group (itemgroupingstaticstatus.bss type 8).
_SOVEREIGN_MAIN = 8


def _declared_effects(source: CaseInput) -> int:
    """The sum of the group heads' effect counts."""
    data = source.data
    (group_count,) = _U32.unpack_from(data, 0)
    pos = _U32.size
    total = 0
    for _ in range(group_count):
        _, effect_count = _GROUP_HEAD.unpack_from(data, pos)
        pos += _GROUP_HEAD.size
        for _ in range(effect_count):
            (color_length,) = _U64.unpack_from(data, pos + _COLOR_LENGTH_AT)
            pos += _EFFECT_FIXED + color_length
        total += effect_count
    assert pos == len(data), (pos, len(data))
    return total


CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["name_text", "dye_item_name"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(
            required_keys=[
                "item_group_type",
                "effect_index",
                "unknown_04",
                "color",
                "color_rgb",
                "name",
                "dye_item_id",
                "name_text",
                "color_hex",
                "dye_item_name",
            ],
        ),
        DeclaredCountTest(declared=_declared_effects),
        UserLanguageTest(fields=["name_text"]),
        # The group's first effect: index 0, the default glow without a pigment.
        TargetTest(col="item_group_type", value=_SOVEREIGN_MAIN, expected={"effect_index": 0, "dye_item_id": 0}),
    ],
)


@pytest.fixture(scope="module")
def effect_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_itemeffectgroupstaticstatus_bss(spec: Any, effect_result: HandlerResult) -> None:
    effect_result.check(spec)


def test_effect_indexes_count_up_from_zero_per_group(effect_result: HandlerResult) -> None:
    indexes: dict[int, list[int]] = {}
    for record in effect_result.records:
        indexes.setdefault(record["item_group_type"], []).append(record["effect_index"])
    assert all(found == list(range(len(found))) for found in indexes.values()), indexes


def test_colours_are_hex_text(effect_result: HandlerResult) -> None:
    for record in effect_result.records:
        color = record["color"]
        assert not color or (len(color) == _HEX_COLOR and int(color, 16) >= 0), color


def test_every_pigment_has_a_name(effect_result: HandlerResult) -> None:
    for record in effect_result.records:
        if record["dye_item_id"]:
            assert record["dye_item_name"] and record["dye_item_name"] != str(record["dye_item_id"]), record


def _effect(index: int, color: str, unknown: bytes, name: int, item: int) -> bytes:
    raw = color.encode("ascii")
    return struct.pack("<IB", index, 1) + _U64.pack(len(raw)) + raw + unknown + struct.pack("<II", name, item)


def test_an_effect_reads_its_colour_text() -> None:
    data = (
        _U32.pack(1)
        + _GROUP_HEAD.pack(11, 2)
        + _effect(0, "", b"\xff\x00\x00", 1512542482, 0)
        + _effect(1, "1D3F48", bytes(3), 54624731, 767342)
    )
    assert parse_itemeffectgroup_effects(data) == [
        {
            "item_group_type": 11, "effect_index": 0, "unknown_04": 1, "color": "",
            "color_rgb": "FF0000", "name": 1512542482, "dye_item_id": 0,
        },
        {
            "item_group_type": 11, "effect_index": 1, "unknown_04": 1, "color": "1D3F48",
            "color_rgb": "000000", "name": 54624731, "dye_item_id": 767342,
        },
    ]


def test_an_effect_past_the_end_raises() -> None:
    data = _U32.pack(1) + _GROUP_HEAD.pack(11, 1) + _effect(0, "1D3F48", bytes(3), 1, 2)[:-1]
    with pytest.raises(ValueError):
        parse_itemeffectgroup_effects(data)

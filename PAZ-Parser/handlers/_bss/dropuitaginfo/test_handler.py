from __future__ import annotations

import struct
from dataclasses import replace
from typing import Any

import pytest

from tests.framework import (
    DeclaredCountTest,
    HandlerCase,
    HandlerResult,
    PaFieldTest,
    SchemaTest,
    TargetTest,
    UserLanguageTest,
    case_id,
    header_count,
    run_case,
)

from _bss.dropuihuntinggroundinfo.parser import parse_hunting_ground_records
from _bss.dropuitaginfo.parser import TagColors, guide_image_path, parse_tag_colors
from _bss.dropuitaginfo.tag_chips import tag_chip, tag_chips_cell
from _common.html import more_marker
from _common.pabr_strings import fixed_row_offsets, read_string_table


_DATA_FILE = "dropuitaginfo.bss"
_HUNTING_GROUND_FILE = "dropuihuntinggroundinfo.bss"
_LOTS_OF_MOBS = 7
# The first #FixedLanternSpot tag, with the first Dehkia's Lantern guide image.
_FIRST_LANTERN_SPOT = 20
_FIRST_GUIDE_IMAGE = "Combine_Etc_DekiaLanterns_GroundTooltip_01"
# The rows start after the PABR magic with this count.
_COUNT_OFFSET = 4
# u32 key | u32 name_ref | u32 guide_texture_ref | u32 desc_ref
# | u32 texture_color_ref | u32 font_color_ref | u32 texture_color | u32 font_color
_ROW = struct.Struct("<8I")

CASE = HandlerCase(
    handler_name=_DATA_FILE,
    data_file=_DATA_FILE,
    companion_files={_HUNTING_GROUND_FILE: _HUNTING_GROUND_FILE},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["name", "description"],
    internal_path=f"gamecommondata/binary/{_DATA_FILE}",
    tests=[
        SchemaTest(
            required_keys=[
                "key",
                "name_kr",
                "description_kr",
                "guide_texture",
                "guide_image_path",
                "texture_color",
                "font_color",
                "name",
                "description",
                "colors",
                "hunting_grounds",
            ],
        ),
        DeclaredCountTest(declared=header_count(offset=_COUNT_OFFSET)),
        PaFieldTest(field="description"),
        UserLanguageTest(fields=["name", "description"]),
        TargetTest(
            col="key",
            value=_LOTS_OF_MOBS,
            expected={"name_kr": "#다수의 몬스터와 전투", "name": "#LotsOfMobs", "guide_texture": ""},
        ),
        TargetTest(
            col="key",
            value=_FIRST_LANTERN_SPOT,
            expected={
                "name": "#FixedLanternSpot",
                "guide_texture": _FIRST_GUIDE_IMAGE,
                "guide_image_path": "ui_texture/combine/etc/combine_etc_dekialanterns_groundtooltip_01.dds",
            },
        ),
    ],
)


@pytest.fixture(scope="module")
def tag_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_dropuitaginfo_bss(spec: Any, tag_result: HandlerResult) -> None:
    tag_result.check(spec)


def test_hex_colour_strings_equal_the_argb_values(tag_result: HandlerResult) -> None:
    """The parser drops the two hex strings, since they repeat the u32 colours."""
    data = tag_result.source.data
    strings = read_string_table(data)
    differing: dict[int, tuple[str, str]] = {}
    for offset in fixed_row_offsets(data, _ROW.size, _DATA_FILE):
        key, _name, _guide, _desc, texture_ref, font_ref, texture, font = _ROW.unpack_from(data, offset)
        stored = (strings[texture_ref], strings[font_ref])
        if (int(stored[0], 16), int(stored[1], 16)) != (texture, font):
            differing[key] = stored
    assert not differing, f"hex colour strings that differ from the u32s: {differing}"


def test_hunting_grounds_list_every_ground_that_carries_the_tag(tag_result: HandlerResult) -> None:
    """Each tag lists one name per hunting ground row whose `tag_keys` hold it."""
    grounds = parse_hunting_ground_records(tag_result.source.file(_HUNTING_GROUND_FILE))
    listed = {r["key"]: len(r["hunting_grounds"]) for r in tag_result.records}
    expected = {key: sum(key in g["tag_keys"] for g in grounds) for key in listed}

    assert listed[_LOTS_OF_MOBS] > 0
    assert listed == expected


def _luminance(argb: int) -> int:
    return sum((argb >> shift) & 0xFF for shift in (16, 8, 0))


def test_tag_text_is_the_lighter_colour(tag_result: HandlerResult) -> None:
    """Where a tag's colours differ, the text (`font_color`) is the lighter one."""
    colors = parse_tag_colors(tag_result.source.data)
    darker_text = {key: c for key, c in colors.items() if _luminance(c.font) < _luminance(c.texture)}

    assert colors
    assert not darker_text, f"tags with darker text than background: {darker_text}"


def test_guide_image_path() -> None:
    assert guide_image_path(_FIRST_GUIDE_IMAGE) == (
        "ui_texture/combine/etc/combine_etc_dekialanterns_groundtooltip_01.dds"
    )
    assert guide_image_path("") == ""


def test_tag_chip_tints_the_background_and_colours_the_text() -> None:
    chip = tag_chip("#Stun & Co", TagColors(texture=0xFFD2691E, font=0xFFFFA500))

    assert chip == (
        '<span class="tag-chip" style="background: rgba(210, 105, 30, 0.2); '
        'color: rgba(255, 165, 0, 1)">#Stun &amp; Co</span>'
    )
    # Without dropuitaginfo.bss the tag is its plain name.
    assert tag_chip("#Stun & Co", None) == "#Stun &amp; Co"
    assert tag_chips_cell([], [], 3) == "-"
    # Pills sit side by side as in game, and the rest is counted.
    assert tag_chips_cell(["A", "B", "C"], [None, None, None], 2) == f"A B {more_marker(1, ['C'])}"

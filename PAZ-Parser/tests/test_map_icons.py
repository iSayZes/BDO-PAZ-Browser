from __future__ import annotations

import pytest
from PIL import Image

from api.bdo_icon_images import open_image
from map_icons import (
    ICON_HEIGHT_PX,
    LAYOUT_ICONS,
    POINTER_BOX,
    RADAR_POINTER_TEXTURE,
    RENDER_SCALE,
    UI_TEXTURE_ROOT,
    WORLDMAP_LAYOUT,
    TextureRegion,
    cut_icons,
    cut_layout_icon,
    cut_player_pointer,
    opaque_share,
    parse_layout_textures,
)
from tests.fixtures import FIXTURES_DIR, fetch_missing
from tests.map_icon_samples import LAYOUT, SHEET, sample_files

def test_layout_textures_are_the_base_texture_corners_as_a_box() -> None:
    regions = parse_layout_textures(LAYOUT)

    assert regions == {
        "Button_Node_Village": (
            TextureRegion(UI_TEXTURE_ROOT + SHEET, (0, 203, 168, 399)),
            TextureRegion(UI_TEXTURE_ROOT + SHEET, (0, 4, 168, 200)),
        )
    }


def test_a_layout_that_is_not_xml_is_refused() -> None:
    with pytest.raises(ValueError):
        parse_layout_textures(b"<UI><Control>")


def test_layout_icons_are_clipped_to_the_sheet_and_scaled_to_the_icon_height() -> None:
    sheet = Image.new("RGBA", (512, 512), (255, 0, 0, 255))

    icon = cut_layout_icon(sheet, (344, 203, 513, 399))

    assert icon.height == ICON_HEIGHT_PX * RENDER_SCALE
    assert icon.width == round(168 * icon.height / 196)


def test_a_box_outside_the_sheet_is_refused() -> None:
    with pytest.raises(ValueError):
        cut_layout_icon(Image.new("RGBA", (64, 64)), (100, 100, 120, 120))


def test_the_pointer_drops_dark_pixels_and_turns_to_face_north() -> None:
    radar = Image.new("RGBA", (512, 512), (20, 20, 20, 200))  # the view cone
    x1, y1, x2, y2 = POINTER_BOX
    radar.paste((255, 255, 255, 255), (x1, y2 - 1, x2, y2))  # the tip row, pointing down

    pointer = cut_player_pointer(radar)

    alpha = pointer.getchannel("A")
    # Scaling spreads the tip a few pixels; the bottom half stays clear.
    assert alpha.crop((0, 0, pointer.width, 2)).getbbox() is not None
    assert alpha.crop((0, pointer.height // 2, pointer.width, pointer.height)).getbbox() is None


def test_cut_icons_leaves_out_what_the_client_lacks() -> None:
    icons = cut_icons(sample_files().get)

    assert set(icons) == {"village"}
    village = icons["village"]
    width, height = village.size
    assert height == ICON_HEIGHT_PX
    assert village.anchor == (width / 2, height)
    assert not village.turns
    # The opaque On sprite, not the faint Base one.
    assert opaque_share(village.image) > 0.9


def test_every_layout_icon_is_a_control_of_the_client_layout() -> None:
    name = WORLDMAP_LAYOUT.rsplit("/", 1)[1]
    fetch_missing([name])

    regions = parse_layout_textures((FIXTURES_DIR / name).read_bytes())

    assert {control for control in LAYOUT_ICONS.values() if control not in regions} == set()


def test_the_client_pointer_has_its_tip_at_the_top() -> None:
    name = RADAR_POINTER_TEXTURE.rsplit("/", 1)[1]
    fetch_missing([name])

    pointer = cut_player_pointer(open_image((FIXTURES_DIR / name).read_bytes()))

    alpha = pointer.getchannel("A")
    bbox = alpha.getbbox()
    assert bbox is not None
    # The tip is the narrow end: the top row holds fewer opaque pixels than the head below it.
    widths = [alpha.width - alpha.crop((0, y, alpha.width, y + 1)).histogram()[0] for y in range(bbox[1], bbox[3])]
    assert widths[0] < max(widths)

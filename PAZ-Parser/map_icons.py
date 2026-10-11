"""Map pin icons: the game's own world map icons, cut from the client's UI textures.

Every icon but `player` is a control of the world map's UI layout,
`WORLDMAP_LAYOUT`: the sheet and UV rectangle of its Base or On texture. The
rectangles come from the client each time the icons are built
(`map_icons_build.py`), so a patch that moves a sprite in its sheet moves the
cut with it.

A node button has two: a dim, mostly see-through sprite for a node the map
does not highlight, and the bright one with the yellow outline that other
map sites show. The layout names the bright one On for most kinds but Base
for Craft and Excavation (client 3464), so the more opaque of the two is cut
(`opaque_share`); the position icons have a Base texture only.

`player` is the own-character pointer of the radar, `RADAR_POINTER_TEXTURE`.
The radar draws it in one image with the view cone, so the pointer is cut out
of the middle (`POINTER_BOX`) and the dark cone pixels dropped. It is turned to
face north, so the page turns it by the pin's heading like the arrow pins.
"""

from __future__ import annotations

import logging
import xml.etree.ElementTree as ET
from collections.abc import Callable, Mapping
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from PIL import Image

WORLDMAP_LAYOUT = "ui_data/window/worldmap_grand/worldmap_grand_base.xml"
# The layout's texture paths are relative to this folder.
UI_TEXTURE_ROOT = "ui_texture/"
RADAR_POINTER_TEXTURE = "ui_texture/new_ui_common_forlua/widget/rader/radar_mine00.dds"

# Icon name -> control of `WORLDMAP_LAYOUT`. The names are the map API's.
LAYOUT_ICONS: Mapping[str, str] = {
    "node": "Button_Node_Normal",
    "village": "Button_Node_Village",
    "city": "Button_Node_City",
    "gate": "Button_Node_Gate",
    "farm": "Button_Node_Farm",
    "trade": "Button_Node_Trade",
    "collect": "Button_Node_Collect",
    "quarry": "Button_Node_Quarry",
    "logging": "Button_Node_Logging",
    "dangerous": "Button_Node_Dangerous",
    "finance": "Button_Node_Finance",
    "fish_trap": "Button_Node_FishTrap",
    "minor_finance": "Button_Node_MinorFinance",
    "monopoly_farm": "Button_Node_MonopolyFarm",
    "craft": "Button_Node_Craft",
    "excavation": "Button_Node_Excavation",
    "dead": "Static_DeadPosition",
    "tent": "Static_TentPosition",
    "horse": "Static_VehiclePosition",
    "camel": "Static_CamelPosition",
    "elephant": "Static_ElephantPosition",
    "dragon": "Static_Dragon",
    "ship": "Static_ShipPosition",
    "party": "Static_PartyPosition",
    "bandit": "Static_BanditPosition",
    "whale": "Static_WhalePosition",
    "griffon": "Static_GriffonPosition",
    "bookmark": "Static_BookMarkPosition",
}
PLAYER_ICON = "player"
ICON_NAMES = frozenset((*LAYOUT_ICONS, PLAYER_ICON))

# The pointer in `RADAR_POINTER_TEXTURE` (512 x 512, the pointer's head
# centred on 255, 255, its tip pointing down): x1, y1, x2, y2 in pixels.
POINTER_BOX = (249, 249, 262, 268)
POINTER_HEAD = (6.5, 6.5)
# The texture types of a layout control an icon can come from.
LAYOUT_TEXTURE_TYPES = ("Base", "On")
# Alpha from which a pixel counts as fully opaque (`opaque_share`).
OPAQUE_ALPHA = 250
# Pixels in POINTER_BOX darker than this (Pillow's "L" luminance, 0 to 255)
# belong to the view cone.
POINTER_MIN_LUMINANCE = 64

# Size on the map in CSS px, and how many image pixels per CSS px (sharp on
# scaled displays).
ICON_HEIGHT_PX = 40
POINTER_SCALE = 1.5
RENDER_SCALE = 2

# x1, y1, x2, y2 in pixels; x2 and y2 exclusive.
Box = tuple[int, int, int, int]


@dataclass(frozen=True)
class TextureRegion:
    texture: str  # Path in the PAZ archives
    box: Box


@dataclass(frozen=True)
class CutIcon:
    """One icon: its image at RENDER_SCALE and where it sits on the pin's position."""

    image: Image.Image
    # The point on the pin's position, in CSS px from the top left.
    anchor: tuple[float, float]
    # Drawn facing north, turned by the pin's heading.
    turns: bool = False

    @property
    def size(self) -> tuple[float, float]:
        """Width and height on the map in CSS px."""
        return self.image.width / RENDER_SCALE, self.image.height / RENDER_SCALE


def parse_layout_textures(layout: bytes) -> dict[str, tuple[TextureRegion, ...]]:
    """Control name -> the sheets and rectangles of its Base and On textures, in that order.

    Controls with neither are left out. A UV attribute lists the four corners
    as x y pairs (top left, top right, bottom left, bottom right). Raises
    ValueError when `layout` is not XML.
    """
    try:
        root = ET.fromstring(layout)
    except ET.ParseError as ex:
        raise ValueError(f"{WORLDMAP_LAYOUT} is not XML: {ex}") from ex
    controls: dict[str, tuple[TextureRegion, ...]] = {}
    for control in root.iter("Control"):
        name = control.get("Name")
        textures = {texture.get("Type"): texture for texture in control.findall("Texture")}
        regions = tuple(
            region
            for kind in LAYOUT_TEXTURE_TYPES
            if (region := _texture_region(textures.get(kind))) is not None
        )
        if name and regions:
            controls[name] = regions
    return controls


def _texture_region(texture: ET.Element | None) -> TextureRegion | None:
    if texture is None or not texture.text:
        return None
    box = _uv_box(texture.get("UV", ""))
    return None if box is None else TextureRegion(texture=UI_TEXTURE_ROOT + texture.text.strip(), box=box)


def _uv_box(uv: str) -> Box | None:
    try:
        numbers = [int(value) for value in uv.split()]
    except ValueError:
        return None
    if len(numbers) != 8:
        return None
    xs, ys = numbers[0::2], numbers[1::2]
    box = (min(xs), min(ys), max(xs), max(ys))
    return box if box[0] < box[2] and box[1] < box[3] else None


def cut_layout_icon(sheet: Image.Image, box: Box) -> Image.Image:
    """The sprite at `box` of `sheet` (a Pillow image), scaled to ICON_HEIGHT_PX * RENDER_SCALE.

    UV rectangles reach one pixel past the sheet's edge at times (x2 512 on a
    512 wide sheet), so the box is clipped to the sheet.
    """
    from PIL import Image

    x1, y1, x2, y2 = box
    clipped = (x1, y1, min(x2, sheet.width), min(y2, sheet.height))
    if clipped[0] >= clipped[2] or clipped[1] >= clipped[3]:
        raise ValueError(f"Box {box} is outside the {sheet.width} x {sheet.height} sheet")
    sprite = sheet.convert("RGBA").crop(clipped)
    height = ICON_HEIGHT_PX * RENDER_SCALE
    width = max(1, round(sprite.width * height / sprite.height))
    return sprite.resize((width, height), Image.Resampling.LANCZOS)


def opaque_share(image: Image.Image) -> float:
    """The share of `image`'s pixels with alpha from OPAQUE_ALPHA: high for the
    bright node sprites, low for the dim ones."""
    histogram = image.getchannel("A").histogram()
    return sum(histogram[OPAQUE_ALPHA:]) / (image.width * image.height)


def cut_player_pointer(radar: Image.Image) -> Image.Image:
    """The pointer of the radar image `radar` (Pillow), cone pixels dropped, facing north and scaled."""
    from PIL import Image, ImageChops

    if radar.width < POINTER_BOX[2] or radar.height < POINTER_BOX[3]:
        raise ValueError(f"The radar image is {radar.width} x {radar.height}, too small for the pointer")
    pointer = radar.convert("RGBA").crop(POINTER_BOX)
    # A lookup table from luminance to the mask: 0 below the cutoff, 255 from it.
    keep = pointer.convert("L").point([0] * POINTER_MIN_LUMINANCE + [255] * (256 - POINTER_MIN_LUMINANCE))
    pointer.putalpha(ImageChops.multiply(pointer.getchannel("A"), keep))
    scale = POINTER_SCALE * RENDER_SCALE
    size = (round(pointer.width * scale), round(pointer.height * scale))
    return pointer.rotate(180).resize(size, Image.Resampling.LANCZOS)


def cut_icons(read: Callable[[str], bytes | None]) -> dict[str, CutIcon]:
    """Every icon the client has, by name.

    `read` returns a file of the PAZ archives by path in any letter case, or
    None when there is none. An icon whose layout control or sheet is missing
    or unreadable is left out and logged; the page draws its pin as a dot.
    """
    from api.bdo_icon_images import open_image

    sheets: dict[str, Image.Image | None] = {}

    def sheet(path: str) -> Image.Image | None:
        """The sheet at `path`, read once; several icons share one."""
        if path not in sheets:
            data = read(path)
            sheets[path] = None if data is None else open_image(data)
        return sheets[path]

    layout = read(WORLDMAP_LAYOUT)
    if layout is None:
        logging.warning("Map icons: %s is missing", WORLDMAP_LAYOUT)
    regions = parse_layout_textures(layout) if layout is not None else {}
    icons: dict[str, CutIcon] = {}
    for name, control in LAYOUT_ICONS.items():
        icon = _layout_icon(name, regions.get(control, ()), sheet)
        if icon is not None:
            icons[name] = icon
    pointer = _player_icon(sheet)
    if pointer is not None:
        icons[PLAYER_ICON] = pointer
    return icons


def _layout_icon(
    name: str, regions: tuple[TextureRegion, ...], sheet: Callable[[str], Image.Image | None]
) -> CutIcon | None:
    """The more opaque of the control's Base and On sprites, cut and scaled."""
    if not regions:
        logging.warning("Map icon %s: %s has no %s", name, WORLDMAP_LAYOUT, LAYOUT_ICONS[name])
        return None
    cuts: list[Image.Image] = []
    for region in regions:
        try:
            image = sheet(region.texture)
            if image is None:
                logging.warning("Map icon %s: %s is missing", name, region.texture)
                continue
            cuts.append(cut_layout_icon(image, region.box))
        except Exception:
            logging.warning("Map icon %s: cannot cut it from %s", name, region.texture, exc_info=True)
    if not cuts:
        return None
    icon = max(cuts, key=opaque_share)
    # The node and position icons are pins with their tip at the bottom middle.
    return CutIcon(icon, (icon.width / RENDER_SCALE / 2, icon.height / RENDER_SCALE))


def _player_icon(sheet: Callable[[str], Image.Image | None]) -> CutIcon | None:
    try:
        radar = sheet(RADAR_POINTER_TEXTURE)
        if radar is None:
            logging.warning("Map icon %s: %s is missing", PLAYER_ICON, RADAR_POINTER_TEXTURE)
            return None
        pointer = cut_player_pointer(radar)
    except Exception:
        logging.warning("Map icon %s: cannot cut the radar pointer", PLAYER_ICON, exc_info=True)
        return None
    # Turned half a circle, the head is as far from the bottom right as it was from the top left.
    width, height = pointer.width / RENDER_SCALE, pointer.height / RENDER_SCALE
    head = (width - POINTER_HEAD[0] * POINTER_SCALE, height - POINTER_HEAD[1] * POINTER_SCALE)
    return CutIcon(pointer, head, turns=True)

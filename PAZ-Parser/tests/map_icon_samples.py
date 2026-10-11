"""A small world map layout and sheet for the map icon tests."""

from __future__ import annotations

import struct

from PIL import Image

from map_icons import UI_TEXTURE_ROOT, WORLDMAP_LAYOUT

SHEET = "new_ui_common_forlua/widget/worldmap/worldmap_icon_00.dds"
LAYOUT = f"""<UI>
  <Control Type="Panel" Name="Worldmap_Grand_Base">
    <Control Type="Button" Name="Button_Node_Village">
      <Texture Type="Base" UV="0 203 168 203 0 399 168 399">{SHEET}</Texture>
      <Texture Type="On" UV="0 4 168 4 0 200 168 200">{SHEET}</Texture>
    </Control>
    <Control Type="Static" Name="Static_NoTexture"/>
    <Control Type="Static" Name="Static_BadUv">
      <Texture Type="Base" UV="0 0 10">{SHEET}</Texture>
    </Control>
  </Control>
</UI>""".encode()


def dds(image: Image.Image) -> bytes:
    """`image` as an uncompressed 32-bit BGRA DDS, the kind `open_image` reads straight."""
    header = bytearray(128)
    header[0:4] = b"DDS "
    struct.pack_into("<I", header, 4, 124)
    struct.pack_into("<I", header, 12, image.height)
    struct.pack_into("<I", header, 16, image.width)
    struct.pack_into("<I", header, 76, 32)
    struct.pack_into("<I", header, 80, 0x41)  # DDPF_RGB | DDPF_ALPHAPIXELS
    struct.pack_into("<I", header, 88, 32)
    struct.pack_into("<4I", header, 92, 0x00FF0000, 0x0000FF00, 0x000000FF, 0xFF000000)
    return bytes(header) + image.convert("RGBA").tobytes("raw", "BGRA")


def sample_sheet() -> Image.Image:
    """Opaque where LAYOUT's village On sprite is (the top half), faint where its Base one is."""
    sheet = Image.new("RGBA", (512, 512), (0, 0, 255, 60))
    sheet.paste((0, 0, 255, 255), (0, 0, 512, 202))
    return sheet


def sample_files() -> dict[str, bytes]:
    """A client with LAYOUT and its sheet: only the `village` icon."""
    return {WORLDMAP_LAYOUT: LAYOUT, UI_TEXTURE_ROOT + SHEET: dds(sample_sheet())}

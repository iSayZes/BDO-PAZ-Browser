"""UI texture keys, resolved through the client's texture string tables.

`ui_texture/texturestringkey/*.xml` map a texture key to a sprite sheet and a
pixel rectangle, one element per key:

    <Texture ID="Combine_Etc_WorldMap_BossList_Begg" Size="160 75"
             UV="162 382 322 457" Path="Combine/Etc/Combine_Etc_WorldMap_BossList.dds"/>

`Path` is relative to `ui_texture/`; `UV` is (x1, y1, x2, y2).
"""

from __future__ import annotations

import re
from collections.abc import Iterable
from dataclasses import dataclass

from _bss.menu.parser import sprite_sheet_path


TEXTURE_STRING_COMBINE = "texturestring_combine.xml"
TEXTURE_STRING_COMBINE_PATH = f"ui_texture/texturestringkey/{TEXTURE_STRING_COMBINE}"

_TEXTURE_RE = re.compile(r"<Texture\b([^>]*)>")
_ATTR_RE = re.compile(r'(\w+)="([^"]*)"')
_ID_RE = re.compile(r'\bID="([^"]*)"')
_UV_VALUES = 4


@dataclass(frozen=True)
class TextureRegion:
    path: str
    region: tuple[int, int, int, int]


def _region(uv: str) -> tuple[int, int, int, int] | None:
    parts = uv.split()
    if len(parts) != _UV_VALUES or not all(p.isdigit() for p in parts):
        return None
    x1, y1, x2, y2 = (int(p) for p in parts)
    return x1, y1, x2, y2


def parse_texture_regions(xml: bytes | None, keys: Iterable[str]) -> dict[str, TextureRegion]:
    """The sheet and rectangle of each wanted key the table holds.

    Keys the table lacks, or whose `UV` is not four integers, are left out, so
    a missing table gives an empty result.
    """
    wanted = set(keys)
    if xml is None or not wanted:
        return {}

    regions: dict[str, TextureRegion] = {}
    for match in _TEXTURE_RE.finditer(xml.decode("utf-8", errors="replace")):
        tag = match.group(1)
        key_match = _ID_RE.search(tag)
        if key_match is None or key_match.group(1) not in wanted:
            continue
        attrs = dict(_ATTR_RE.findall(tag))
        region = _region(attrs.get("UV", ""))
        path = sprite_sheet_path(attrs.get("Path", ""))
        if region is not None and path:
            regions[key_match.group(1)] = TextureRegion(path, region)
    return regions

"""The `regionmapinfo.bss` images a `fieldinfo.bss` row points at.

Each named `*_map_index` field holds a `regionmapinfo.bss` key; the record
gets the key's image name under the field name with `_index` replaced by
`_image` (`region_map_index` 1 -> `region_map_image` `RegionMap_New.bmp`),
or '' when the file has no row for the key (fishing, water and underground
maps on client 3482). The `unknown_*` map keys get no image field until
their names are confirmed (fieldinfo_bss.md, Open Questions).
"""

from __future__ import annotations

from collections.abc import Mapping

from _bss.regionmapinfo.parser import map_images

# Named map key fields of the newest layout, in row order.
MAP_INDEX_FIELDS: tuple[str, ...] = (
    "region_map_index",
    "fishing_map_index",
    "water_info_map_index",
    "siege_info_map_index",
    "village_siege_info_map_index",
    "village_siege_info_map_index_new",
    "underground_map_index",
    "audio_map_index",
    "great_sea_map_index",
    "horse_race_course_map_index",
)
MAPS_FIELD = "map_images"
_INDEX_SUFFIX = "_index"
_IMAGE_SUFFIX = "_image"


def image_field(index_field: str) -> str:
    """`region_map_index` -> `region_map_image`."""
    return index_field.removesuffix(_INDEX_SUFFIX) + _IMAGE_SUFFIX


def read_map_images(data: bytes | None) -> dict[int, str]:
    """Map key -> image name from the optional companion; empty when it is
    missing or unreadable, since the names are only a convenience here."""
    if data is None:
        return {}
    try:
        return map_images(data)
    except ValueError:
        return {}


def map_image_fields(record: Mapping[str, object], images: Mapping[int, str]) -> dict[str, object]:
    """One `*_map_image` text per named map key field, and their images in row order without repeats."""
    fields: dict[str, object] = {}
    shown: list[str] = []
    for index_field in MAP_INDEX_FIELDS:
        key = record[index_field]
        image = images.get(key, "") if isinstance(key, int) else ""
        fields[image_field(index_field)] = image
        if image and image not in shown:
            shown.append(image)
    fields[MAPS_FIELD] = shown
    return fields

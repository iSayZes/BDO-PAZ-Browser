"""baseobject.bss preview handler: one row per placeable object.

Each row shows the object's name and icon (from its character ID), its armor
material, its kind with the 2016 `gc::ObjectKind` name, its installation type with the client
Lua name, the collision and siege tent flags, the hull totals and where it
can be placed.
"""
from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from _common.character import character_name
from _common.html import Column, e, icon_cell
from _common.icon_index import IconKind, icon_path
from _common.lang import load_handler_strings
from _common.row_table import RowTableHandler
from _dbss.characterobject.parser import OBJECT_KIND_NAMES
from .installation_types import installation_type_name
from .parser import FILE_NAME, KEY_FIELD, PLACE_FLAG_FIELDS, parse_baseobject_records


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"
# Lang keys of the place flags, in PLACE_FLAG_FIELDS order.
_PLACE_LABEL_KEYS = ("inside", "outside", "floor", "wall", "table", "carpet")


def _object_kind_name(object_kind: int) -> str:
    """The gc::ObjectKind name, or '' for the later kinds it does not have."""
    return OBJECT_KIND_NAMES[object_kind] if object_kind < len(OBJECT_KIND_NAMES) else ""


def _number_and_name(number: int, name: str) -> str:
    return f"{number} {name}".strip()


def _placement(record: dict, labels: Mapping[str, str]) -> str | None:
    """The place flags that are set, as `labels`; None when none is (sorts last)."""
    names = [labels[key] for key, field in zip(_PLACE_LABEL_KEYS, PLACE_FLAG_FIELDS, strict=True) if record[field]]
    return ", ".join(names) or None


class BaseObjectBssHandler(RowTableHandler):
    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["characterId"], "num", sort_key=KEY_FIELD),
            Column(labels["icon"], sort_key="icon_path"),
            Column(labels["name"], sort_key="name"),
            Column(labels["armorMaterial"], "num", sort_key="armor_material"),
            # Sort by the number; the cells add the enum name where there is one.
            Column(labels["objectKind"], sort_key="object_kind"),
            Column(labels["installationType"], sort_key="installation_type"),
            Column(labels["collision"], "num", sort_key="is_collision"),
            Column(labels["siegeTent"], "num", sort_key="is_siege_tent"),
            Column(labels["layers"], "num", sort_key="layer_count"),
            Column(labels["faces"], "num", sort_key="face_count"),
            Column(labels["placement"], sort_key="placement"),
        ]

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        place_labels = load_handler_strings(self.lang, _LANG_DIR)["placement"]
        return [
            {
                **record,
                "icon_path": icon_path(IconKind.CHARACTER, record[KEY_FIELD]),
                "name": character_name(record[KEY_FIELD]) or None,
                "object_kind_name": _object_kind_name(record["object_kind"]),
                "installation_type_name": installation_type_name(record["installation_type"]),
                "placement": _placement(record, place_labels),
            }
            for record in parse_baseobject_records(data)
        ]

    def cells(self, record: dict) -> list[str]:
        return [
            e(record[KEY_FIELD]),
            icon_cell(record["icon_path"]),
            e(record["name"] or _EMPTY),
            e(record["armor_material"]),
            e(_number_and_name(record["object_kind"], record["object_kind_name"])),
            e(_number_and_name(record["installation_type"], record["installation_type_name"])),
            e(record["is_collision"]),
            e(record["is_siege_tent"]),
            e(record["layer_count"]),
            e(record["face_count"]),
            e(record["placement"] or _EMPTY),
        ]

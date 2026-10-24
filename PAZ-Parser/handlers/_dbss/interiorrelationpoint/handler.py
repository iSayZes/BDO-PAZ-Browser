"""interiorrelationpoint.dbss preview handler: the placement points of each furniture character."""
from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from bdo_models import PazEntry

from _common.character import character_name
from _common.character_link import (
    character_key_cell,
    character_row_ids,
    characterstatic_offset_companion,
    has_character_row,
)
from _common.html import Column, e
from _common.offset_table import OffsetTableHandler, keyed_offset_handler
from _common.row_table import RowTableHandler
from .parser import (
    FILE_NAME,
    KEY_FIELD,
    RELATION_FIELDS,
    parse_interiorrelationpoint_records,
    parse_interiorrelationpointoffset_rows,
)


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"
# `matching_character_key` 0 names no character.
_NO_CHARACTER = 0


def _label_key(field: str) -> str:
    """The lang key of a relation point column: `on_dresser` -> `onDresser`."""
    head, *rest = field.split("_")
    return head + "".join(word.capitalize() for word in rest)


def interior_relation_point_offset_handler() -> OffsetTableHandler:
    return keyed_offset_handler(_LANG_DIR, parse_interiorrelationpointoffset_rows, KEY_FIELD, "characterKey")


class InteriorRelationPointHandler(RowTableHandler):
    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def companions(self, entry: PazEntry) -> list[str]:
        return [characterstatic_offset_companion(entry.internal_path)]

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["characterKey"], "num", sort_key=KEY_FIELD),
            Column(labels["furniture"], sort_key="name"),
            Column(labels["matchingCharacter"], sort_key="matching_character_name"),
            Column(labels["matchingPoint"], "num", sort_key="matching_character_point"),
            *(Column(labels[_label_key(field)], "num", sort_key=field) for field in RELATION_FIELDS),
        ]

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        row_ids = character_row_ids(companions)
        return [
            {
                **record,
                "name": character_name(record[KEY_FIELD]),
                "has_character_row": has_character_row(row_ids, record[KEY_FIELD]),
                "matching_character_name": self._matching_label(record["matching_character_key"]),
            }
            for record in parse_interiorrelationpoint_records(data)
        ]

    @staticmethod
    def _matching_label(character_key: int) -> str | None:
        """`6751 Golden Hand Vase`, or None when the row names no matching character."""
        if character_key == _NO_CHARACTER:
            return None
        return f"{character_key} {character_name(character_key)}".strip()

    def cells(self, record: dict) -> list[str]:
        return [
            character_key_cell(record[KEY_FIELD], record["has_character_row"]),
            e(record["name"] or _EMPTY),
            e(record["matching_character_name"] or _EMPTY),
            e(record["matching_character_point"]),
            *(e(record[field]) for field in RELATION_FIELDS),
        ]

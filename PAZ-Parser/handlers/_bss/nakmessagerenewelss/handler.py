"""nakmessagerenewelss.bss preview handler: one row per screen-wide message type.

The text lines read LOC type 132 (`str_id1` the message type, `str_id4` the
line) in the user's language first, then the row's Korean text. Background
textures and effects stay names; they resolve through other formats.
"""

from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from _common.contents_group import contents_group_key
from _common.html import Column, e, text_list_cell
from _common.loc import loc_tagged
from _common.pa_text import pa_cell, pa_fields, strip_pa_tags
from _common.row_table import RowTableHandler
from .parser import FILE_NAME, parse_nakmessagerenewelss_records


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"
# LOC type of the message lines; `str_id4` is the line: 0 main, 1 sub, 2 and 3 the extra lines.
LOC_NAK_MESSAGE = 132
# Effect names a cell shows before it folds the rest into a "+N" marker.
_MAX_EFFECTS = 3


def nak_line_tagged(nak_message_type: int, line: int, text_kr: str) -> str:
    """One text line with its colour tags: the LOC text, else the Korean text."""
    tagged = loc_tagged(LOC_NAK_MESSAGE, nak_message_type, line)
    return tagged if strip_pa_tags(tagged).strip() else text_kr


def _derived_fields(record: dict) -> dict:
    """The main and sub line text, the contents group key, the effect names and the sound events."""
    nak_type = record["nak_message_type"]
    return {
        **pa_fields("main_message", nak_line_tagged(nak_type, 0, record["main_text"]["text_kr"])),
        **pa_fields("sub_message", nak_line_tagged(nak_type, 1, record["sub_text"]["text_kr"])),
        "contents_group": contents_group_key(record["contents_group_hash"]),
        "effect_names": [effect["effect_name"] for effect in record["effects"]],
        "sound_events": [f"{sound['audio_index']}/{sound['audio_index_b']}" for sound in record["sounds"]],
    }


class NakMessageRenewelBssHandler(RowTableHandler):
    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["nakMessageType"], "num", sort_key="nak_message_type"),
            Column(labels["mainMessage"], sort_key="main_message"),
            Column(labels["subMessage"], sort_key="sub_message"),
            Column(labels["aniTime"], "num", sort_key="ani_time"),
            Column(labels["mainBg"], sort_key="main_bg_texture"),
            Column(labels["subBg"], sort_key="sub_bg_texture"),
            Column(labels["effects"]),
            Column(labels["sounds"]),
            Column(labels["contentsGroup"], "num", sort_key="contents_group"),
        ]

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        return [
            {
                **record,
                **_derived_fields(record),
                "main_bg_texture": record["main_bg"]["texture_id"],
                "sub_bg_texture": record["sub_bg"]["texture_id"],
            }
            for record in parse_nakmessagerenewelss_records(data)
        ]

    def cells(self, record: dict) -> list[str]:
        group = record["contents_group"]
        return [
            e(record["nak_message_type"]),
            pa_cell(record, "main_message"),
            pa_cell(record, "sub_message"),
            e(f"{record['ani_time']:.6g}"),
            e(record["main_bg_texture"] or _EMPTY),
            e(record["sub_bg_texture"] or _EMPTY),
            text_list_cell(record["effect_names"], _MAX_EFFECTS) or _EMPTY,
            e(", ".join(record["sound_events"]) or _EMPTY),
            e(_EMPTY if group is None else group),
        ]


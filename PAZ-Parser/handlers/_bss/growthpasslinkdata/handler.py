"""growthpasslinkdata.bss preview handler: one row per guide link of a Growth Pass quest and service type."""
from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from _common.html import Column, e
from _common.loc import is_loc_loaded
from _common.pa_text import pa_cell, pa_fields
from _common.quest.quest import quest_title_tagged
from _common.row_table import RowTableHandler
from .parser import FILE_NAME, QuestLinks, parse_growthpasslinkdata


_LANG_DIR = Path(__file__).parent / "lang"
# `CppEnums.ServiceResourceType` of global_define_cpp_enum.luac, without the
# `eServiceResourceType_` prefix. 15 to 17 are not members, so a dict.
SERVICE_RESOURCE_TYPE_NAMES: dict[int, str] = {
    0: "Dev",
    1: "KR",
    2: "EN",
    3: "JP",
    4: "CN",
    5: "RU",
    6: "FR",
    7: "DE",
    8: "ES",
    9: "TW",
    10: "SA",
    11: "PT",
    12: "TH",
    13: "ID",
    14: "TR",
    18: "SP",
}


def service_resource_type_name(value: int) -> str:
    """`2` -> `EN`; a value outside the enum stays a number."""
    return SERVICE_RESOURCE_TYPE_NAMES.get(value, str(value))


def _link_records(record: QuestLinks, has_loc: bool) -> list[dict]:
    """One record per link: the quest, its service type and the link's index (the Lua `idx`)."""
    title = quest_title_tagged(record.quest_chain_id, record.quest_id) if has_loc else ""
    quest_fields = {
        "quest_chain_id": record.quest_chain_id,
        "quest_id": record.quest_id,
        "entry_count": len(record.entries),
        **pa_fields("title", title),
    }
    return [
        {
            **quest_fields,
            "service_resource_type": entry.service_resource_type,
            "service_resource_type_name": service_resource_type_name(entry.service_resource_type),
            "link_count": len(entry.links),
            "link_index": index,
            "link": link.link,
            "author": link.author,
        }
        for entry in record.entries
        for index, link in enumerate(entry.links)
    ]


class GrowthPassLinkDataBssHandler(RowTableHandler):
    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["mainId"], "num", sort_key="quest_chain_id"),
            Column(labels["subId"], "num", sort_key="quest_id"),
            Column(labels["title"], sort_key="title"),
            Column(labels["service"], sort_key="service_resource_type"),
            Column(labels["link"], sort_key="link"),
            Column(labels["author"], sort_key="author"),
        ]

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        has_loc = is_loc_loaded()
        return [
            link_record
            for record in parse_growthpasslinkdata(data)
            for link_record in _link_records(record, has_loc)
        ]

    def cells(self, record: dict) -> list[str]:
        return [
            e(record["quest_chain_id"]),
            e(record["quest_id"]),
            pa_cell(record, "title"),
            e(record["service_resource_type_name"]),
            e(record["link"]),
            e(record["author"]),
        ]

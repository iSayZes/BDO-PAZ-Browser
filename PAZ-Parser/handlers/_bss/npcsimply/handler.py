from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.character import character_loc_name, character_title
from _common.html import Column, e, sort_keys, table
from _common.lang import handler_text, load_handler_strings
from _common.loc import is_loc_loaded
from _dbss.characterspawntype.role_labels import role_label, role_label_overrides, role_tooltip, spawn_type_name
from _common.pa_text import pa_key, pa_list_cell, pa_list_fields
from _common.lease import lease_text_tagged
from .leases import character_leases
from .parser import parse_npcsimply_records


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"
_LIST_PREVIEW_ITEMS = 3


def _kind_cell(record: dict) -> str:
    """The role's display name, with its enum name and value on hover."""
    return f'<span title="{e(role_tooltip(record["kind"]))}">{e(record["kind_label"])}</span>'


def _lease_fields(record: dict, has_loc: bool) -> dict:
    """The stored lease (`None` without one, so it sorts last) and every known lease as text."""
    item_id = record["lease_item_id"]
    leases = character_leases(record["character_id"], item_id, record["lease_cost"])
    return {
        "lease_item_id": item_id or None,
        "lease_cost": record["lease_cost"] if item_id else None,
        **pa_list_fields("leases", [lease_text_tagged(lease, has_loc) for lease in leases]),
        # Empty sorts last.
        "lease_count": len(leases) or None,
    }


class NpcSimplyBssHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["characterId"], "num", sort_key="character_id"),
            Column(cols["name"], sort_key="name"),
            Column(cols["kind"], sort_key="kind_label"),
            Column(cols["role"], sort_key="role"),
            Column(cols["knowledgeId"], "num", sort_key="knowledge_id"),
            Column(cols["leases"], sort_key="lease_count"),
            Column(cols["script"], sort_key="script"),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        has_loc = is_loc_loaded()
        role_labels = role_label_overrides(self.lang)
        return [
            {
                **record,
                **_lease_fields(record, has_loc),
                # User language first; the inline Korean stands in without LOC.
                "name": character_loc_name(record["character_id"]) or record["name_kr"],
                "role": character_title(record["character_id"]) or record["role_kr"],
                "kind_name": spawn_type_name(record["kind"]),
                "kind_label": role_label(record["kind"], role_labels),
            }
            for record in parse_npcsimply_records(data)
        ]

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        start = page * page_size
        slice_ = records[start : start + page_size]
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records))

        rows = [
            [
                e(record["character_id"]),
                e(record["name"] or _EMPTY),
                _kind_cell(record),
                e(record["role"] or _EMPTY),
                e(_EMPTY if record["knowledge_id"] is None else record["knowledge_id"]),
                pa_list_cell(record[pa_key("leases")], _LIST_PREVIEW_ITEMS),
                e(record["script"]),
            ]
            for record in slice_
        ]

        return table(meta, self._columns(), rows)

from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.html import Column, e, record_link, sort_keys, table
from _common.lang import handler_text, load_handler_strings
from _common.lookup_builders import SKILL
from _common.offset_table import OffsetColumn, OffsetTableHandler, offset_column, offset_records, size_column
from _common.pabr_offset import parse_bare_u32_offset_rows
from _common.skill import skill_name
from .parser import parse_servantbuff_records


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"
_LINK_CLASS = "record-link"


def servant_buff_offset_handler() -> OffsetTableHandler:
    return OffsetTableHandler(
        _LANG_DIR,
        [
            OffsetColumn("key", "key"),
            offset_column("offset", "dataOffset"),
            size_column("size", "size"),
        ],
        offset_records(parse_bare_u32_offset_rows, "key"),
    )


class ServantBuffHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["key"], "num", sort_key="key"),
            Column(cols["condition"], sort_key="condition"),
            Column(cols["actionName"], sort_key="action_name"),
            Column(cols["actionHash"], "num", sort_key="action_hash"),
            Column(cols["servantActionName"], sort_key="servant_action_name"),
            Column(cols["servantActionHash"], "num", sort_key="servant_action_hash"),
            Column(cols["skillNo"], "num", sort_key="skill_no"),
            Column(cols["skill"], sort_key="skill_name"),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        return [
            {**record, "skill_name": skill_name(record["skill_no"])}
            for record in parse_servantbuff_records(data)
        ]

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        start = page * page_size
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records))
        rows = [
            [
                e(r["key"]),
                e(r["condition"] or _EMPTY),
                e(r["action_name"]),
                e(r["action_hash"]),
                e(r["servant_action_name"]),
                e(r["servant_action_hash"]),
                record_link(str(r["skill_no"]), SKILL, "skill_no", r["skill_no"], _LINK_CLASS),
                e(r["skill_name"] or _EMPTY),
            ]
            for r in records[start : start + page_size]
        ]
        return table(meta, self._columns(), rows)

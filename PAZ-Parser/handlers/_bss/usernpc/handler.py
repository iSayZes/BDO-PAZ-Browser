from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.class_type import class_name
from _common.html import Column, e, sort_keys, table
from _common.lang import handler_text, load_handler_strings
from .parser import parse_usernpc_records


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"
_DIRECTION_DECIMALS = 2


class UserNpcBssHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["characterNo"], "num", sort_key="player_character_no"),
            Column(cols["x"], "num", sort_key="pos_x"),
            Column(cols["y"], "num", sort_key="pos_y"),
            Column(cols["z"], "num", sort_key="pos_z"),
            Column(cols["direction"], "num", sort_key="direction"),
            Column(cols["action"], sort_key="action_name"),
            Column(cols["class"], sort_key="class_name"),
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
            {**record, "class_name": class_name(record["class_type"])}
            for record in parse_usernpc_records(data)
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
                e(r["player_character_no"]),
                e(f"{r['pos_x']:,.0f}"),
                e(f"{r['pos_y']:,.0f}"),
                e(f"{r['pos_z']:,.0f}"),
                e(f"{r['direction']:.{_DIRECTION_DECIMALS}f}"),
                e(r["action_name"] or _EMPTY),
                e(r["class_name"]),
            ]
            for r in records[start : start + page_size]
        ]
        return table(meta, self._columns(), rows)

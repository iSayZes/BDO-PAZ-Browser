"""uigrowthpasslayout.bss preview handler: one row per filled cell of each category's grid, with its guide links."""
from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _bss.growthpasslinkdata.parser import FILE_NAME as LINK_FILE
from _common.html import Column, e, icon_cell, sort_keys, table, text_list_cell
from _common.icon_index import IconKind, icon_path
from _common.lang import handler_text, load_handler_strings
from _common.loc import is_loc_loaded
from _common.pa_text import pa_cell, pa_fields
from _common.quest.quest import quest_title_tagged
from .links import LINKS_FIELD, cell_links, read_quest_links
from .parser import parse_uigrowthpasslayout


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"
_BLANK = 1
_QUEST = 2
# The window has three guide link buttons per quest cell.
_MAX_LINKS_SHOWN = 3
# `__eGrowthPass_CellType_*` members, matched to values by where each value
# sits in the grids (docs/file-formats/uigrowthpasslayout_bss.md). 0, 9 and 10
# do not occur, so they stay numbers.
CELL_TYPE_NAMES: dict[int, str] = {
    _BLANK: "Blank",
    _QUEST: "Value",
    3: "Vertical",
    4: "Horizon",
    5: "TR",
    6: "LT",
    7: "RB",
    8: "BL",
    11: "LTRB",
    12: "LTB",
    13: "TRB",
    14: "MiniVertical",
}


def _quest_fields(chain: int, quest: int, has_loc: bool) -> dict:
    if not chain:
        return {**pa_fields("title", ""), "packed_quest_id": None, "icon_path": ""}
    packed = (quest << 16) | chain
    title = quest_title_tagged(chain, quest) if has_loc else ""
    return {**pa_fields("title", title), "packed_quest_id": packed, "icon_path": icon_path(IconKind.QUEST, packed)}


class UiGrowthPassLayoutBssHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["categoryKey"], "num", sort_key="category_key"),
            Column(cols["row"], "num", sort_key="row"),
            Column(cols["column"], "num", sort_key="col"),
            Column(cols["cellType"], sort_key="cell_type"),
            Column(cols["mainId"], "num", sort_key="quest_chain_id"),
            Column(cols["subId"], "num", sort_key="quest_id"),
            Column(cols["icon"], sort_key="icon_path"),
            Column(cols["title"], sort_key="title"),
            Column(cols["links"]),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def companions(self, entry: PazEntry) -> list[str]:
        folder = entry.internal_path.rsplit("/", 1)[0]
        return [f"{folder}/{LINK_FILE}"]

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        has_loc = is_loc_loaded()
        links = read_quest_links(companions.get(LINK_FILE))
        records: list[dict] = []
        for layout in parse_uigrowthpasslayout(data):
            for cell in layout.cells:
                if cell.cell_type == _BLANK:
                    continue
                records.append({
                    "category_key": cell.category_key,
                    "col_count": layout.col_count,
                    "row_count": layout.row_count,
                    "row": cell.row,
                    "col": cell.col,
                    "cell_type": cell.cell_type,
                    "cell_type_name": CELL_TYPE_NAMES.get(cell.cell_type, str(cell.cell_type)),
                    "unknown_05": cell.unknown_05,
                    # Only quest cells hold a quest; None keeps the line cells' dashes sorting last.
                    "quest_chain_id": cell.quest_chain_id or None,
                    "quest_id": cell.quest_id or None,
                    **_quest_fields(cell.quest_chain_id, cell.quest_id, has_loc),
                    LINKS_FIELD: cell_links(links, cell.quest_chain_id, cell.quest_id),
                })
        return records

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        start = page * page_size
        rows = [self._row_cells(r) for r in records[start : start + page_size]]
        layouts = len({r["category_key"] for r in records})
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records), layouts=layouts)
        return table(meta, self._columns(), rows)

    def _row_cells(self, r: dict) -> list[str]:
        is_quest = r["quest_chain_id"] is not None
        return [
            e(r["category_key"]),
            e(r["row"]),
            e(r["col"]),
            e(r["cell_type_name"]),
            e(r["quest_chain_id"]) if is_quest else _EMPTY,
            e(r["quest_id"]) if is_quest else _EMPTY,
            icon_cell(r["icon_path"]) if r["icon_path"] else _EMPTY,
            pa_cell(r, "title"),
            text_list_cell(r[LINKS_FIELD], _MAX_LINKS_SHOWN) or _EMPTY,
        ]

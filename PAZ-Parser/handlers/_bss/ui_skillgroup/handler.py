from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler
from table_sort import TableSort

from _common.class_type import class_name
from _common.html import Column, e, icon_cell, sort_keys, table
from _common.icon_index import IconKind, icon_path
from _common.lang import handler_text, load_handler_strings
from _common.pa_text import pa_cell, pa_fields
from _common.skill import skill_name_tagged, split_skill_key
from _bss.skillgroup.parser import skill_keys_by_group
from _bss.stringtable.parser import GAME_SHEET, parse_key_hashes
from _bss.stringtable.text import STRINGTABLE_FILE, ui_hash_text
from .parser import ClassGrid, SkillCell, Tab, card_column, parse_ui_skillgroup


_LANG_DIR = Path(__file__).parent / "lang"
_SKILLGROUP_FILE = "skillgroup.bss"
_EMPTY = "-"


def _tab_names(tabs: tuple[Tab, ...], key_hashes: Mapping[str, int]) -> dict[int, str]:
    """English tab name by subgroup, else the tab's string key."""
    names: dict[int, str] = {}
    for tab in tabs:
        key_hash = key_hashes.get(tab.key)
        names[tab.subgroup] = (ui_hash_text(GAME_SHEET, key_hash) if key_hash is not None else "") or tab.key
    return names


def _cell_dict(
    grid: ClassGrid,
    cell: SkillCell,
    grid_class_name: str,
    tab_names: Mapping[int, str],
    group_keys: Mapping[int, tuple[int, ...]],
    column_labels: Mapping[str, str],
) -> dict:
    keys = group_keys.get(cell.group_no, ())
    # The group's first rank names the skill window entry.
    skill_no = split_skill_key(keys[0])[0] if keys else None
    column_index = card_column(cell.column, grid.width)
    return {
        "class_type": grid.class_type,
        "class": grid_class_name,
        "subgroup": cell.subgroup,
        "tab": tab_names.get(cell.subgroup, str(cell.subgroup)),
        "card_column": column_index,
        "card_column_label": column_labels.get(str(column_index), str(column_index)),
        "row": cell.row,
        "column": cell.column,
        "group_no": cell.group_no,
        "skill_no": skill_no,
        "icon_path": icon_path(IconKind.SKILL, skill_no) if skill_no is not None else "",
        **pa_fields("skill", skill_name_tagged(skill_no) if skill_no is not None else ""),
    }


def _game_key_hashes(companions: dict[str, bytes]) -> dict[str, int]:
    data = companions.get(STRINGTABLE_FILE)
    return parse_key_hashes(data, GAME_SHEET) if data is not None else {}


def _group_keys(companions: dict[str, bytes]) -> dict[int, tuple[int, ...]]:
    data = companions.get(_SKILLGROUP_FILE)
    return skill_keys_by_group(data) if data is not None else {}


def _game_order(record: dict) -> tuple[int, int, int, int, int]:
    # The skill window: sections by subgroup, then card columns, then cells.
    return (record["class_type"], record["subgroup"], record["card_column"], record["row"], record["column"])


class UiSkillGroupBssHandler(PreviewHandler):
    """`ui_skillgroup_combat.bss`, `_awakening.bss` and `_succession.bss`."""

    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["class"], sort_key="class"),
            Column(cols["tab"], sort_key="subgroup"),
            Column(cols["cardColumn"], sort_key="card_column"),
            Column(cols["row"], "num", sort_key="row"),
            Column(cols["column"], "num", sort_key="column"),
            Column(cols["group"], "num", sort_key="group_no"),
            Column(cols["icon"], sort_key="icon_path"),
            Column(cols["skill"], sort_key="skill"),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def default_sort(self) -> TableSort | None:
        # The skill window order (`_game_order`) spans five fields, so the
        # table opens in get_records() order instead of one sorted column.
        return None

    def companions(self, entry: PazEntry) -> list[str]:
        folder = entry.internal_path.rsplit("/", 1)[0]
        return [f"{folder}/{_SKILLGROUP_FILE}", f"{folder}/{STRINGTABLE_FILE}"]

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        window = parse_ui_skillgroup(data)
        key_hashes = _game_key_hashes(companions)
        group_keys = _group_keys(companions)
        column_labels = load_handler_strings(self.lang, _LANG_DIR)["cardColumn"]

        records: list[dict] = []
        for grid in window.grids:
            grid_class_name = class_name(grid.class_type)
            tab_names = _tab_names(window.tabs.get(grid.class_type, ()), key_hashes)
            records.extend(
                _cell_dict(grid, cell, grid_class_name, tab_names, group_keys, column_labels)
                for cell in grid.cells
            )
        return sorted(records, key=_game_order)

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        start = page * page_size
        slice_ = records[start : start + page_size]
        classes = len({r["class_type"] for r in records})
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records), classes=classes)
        rows = [
            [
                e(r["class"]),
                e(r["tab"]),
                e(r["card_column_label"]),
                e(r["row"]),
                e(r["column"]),
                e(r["group_no"]),
                icon_cell(r["icon_path"]),
                pa_cell(r, "skill"),
            ]
            for r in slice_
        ]
        return table(meta, self._columns(), rows)

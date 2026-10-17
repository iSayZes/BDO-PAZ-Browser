from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.class_type import ALL_CLASSES_MASK, class_name, class_types_in_mask
from _common.html import Column, e, flag_cell, icon_cell, sort_keys, table, text_list_cell
from _common.icon_index import IconKind, icon_path
from _common.lang import handler_text, load_handler_strings
from _common.pa_text import pa_cell, pa_fields
from _common.skill import skill_name, skill_name_tagged
from .parser import SkillSimplyRecord, parse_skillsimply_records


_LANG_DIR = Path(__file__).parent / "lang"
_OFFSET_FILE = "skillsimplyoffset.dbss"
_EMPTY = "-"
_LIST_PREVIEW_ITEMS = 3
# require_equip_type of every Awakening weapon skill, whatever the class.
_AWAKENING_EQUIP_TYPE = 57


def _skill_label(skill_no: int) -> str:
    return skill_name(skill_no) or str(skill_no)


def _classes(class_mask: int, all_label: str) -> str:
    if class_mask == ALL_CLASSES_MASK:
        return all_label
    return ", ".join(class_name(class_type) for class_type in class_types_in_mask(class_mask))


def _weapon(record: SkillSimplyRecord, labels: dict[str, str]) -> str:
    """Main, Sub or Awakening; empty for skills without a weapon."""
    if record.uses_main_weapon:
        return labels["main"]
    if record.uses_sub_weapon:
        return labels["sub"]
    if record.require_equip_type == _AWAKENING_EQUIP_TYPE:
        return labels["awakening"]
    return ""


def _record_dict(record: SkillSimplyRecord, strings: dict) -> dict:
    kind_labels = strings["kind"]
    branch_labels = strings["branch"]
    return {
        "skill_key": record.skill_key,
        "skill_no": record.skill_no,
        "level": record.level,
        "max_level": record.max_level,
        "icon_path": icon_path(IconKind.SKILL, record.skill_no),
        **pa_fields("name", skill_name_tagged(record.skill_no)),
        "class_mask": record.class_mask,
        "classes": _classes(record.class_mask, strings["allClasses"]),
        "kind": record.kind,
        "kind_label": kind_labels.get(str(record.kind), str(record.kind)),
        # Zero means neither branch; None sorts last.
        "branch": record.branch or None,
        "branch_label": branch_labels.get(str(record.branch), str(record.branch)) if record.branch else "",
        "require_equip_type": record.require_equip_type,
        "require_equip_slot": record.require_equip_slot,
        "weapon": _weapon(record, strings["weapon"]),
        "skill_owner_type": record.skill_owner_type,
        "is_fusion": record.is_fusion,
        "can_quick_slot": record.can_quick_slot,
        "condition": record.condition,
        "is_except_cool_time": record.is_except_cool_time,
        "need_buff_module_type": record.need_buff_module_type,
        "contents_group_keys": list(record.contents_group_keys),
        # Zero means no requirement; None sorts last.
        "need_level": record.need_level or None,
        "need_skill_point": record.need_skill_point or None,
        "need_skill_nos": list(record.need_skill_nos),
        "need_skills": [_skill_label(no) for no in record.need_skill_nos],
        "previous_rank_no": record.previous_rank_no or None,
        "previous_rank": _skill_label(record.previous_rank_no) if record.previous_rank_no else "",
        "next_rank_keys": list(record.next_rank_keys),
        "first_rank_key": record.first_rank_key,
        "exclusive_skill_nos": list(record.exclusive_skill_nos),
        "exclusive_skills": [_skill_label(no) for no in record.exclusive_skill_nos],
        "base_skill_keys": list(record.base_skill_keys),
    }


class SkillSimplyHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["skillNo"], "num", sort_key="skill_no"),
            Column(cols["level"], "num", sort_key="level"),
            Column(cols["maxLevel"], "num", sort_key="max_level"),
            Column(cols["icon"], sort_key="icon_path"),
            Column(cols["name"], sort_key="name"),
            Column(cols["classes"], sort_key="classes"),
            Column(cols["kind"], sort_key="kind"),
            Column(cols["branch"], sort_key="branch"),
            Column(cols["weapon"], sort_key="weapon"),
            Column(cols["quickSlot"], sort_key="can_quick_slot"),
            Column(cols["needLevel"], "num", sort_key="need_level"),
            Column(cols["needSkillPoint"], "num", sort_key="need_skill_point"),
            Column(cols["needSkills"]),
            Column(cols["previousRank"], sort_key="previous_rank"),
            Column(cols["exclusiveSkills"]),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def companions(self, entry: PazEntry) -> list[str]:
        folder = entry.internal_path.rsplit("/", 1)[0]
        return [f"{folder}/{_OFFSET_FILE}"]

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        offset_raw = companions.get(_OFFSET_FILE)
        if offset_raw is None:
            raise ValueError(f"{_OFFSET_FILE} companion not found.")

        strings = load_handler_strings(self.lang, _LANG_DIR)
        # The index order is arbitrary; skill number order puts class skills first.
        records = sorted(parse_skillsimply_records(data, offset_raw), key=lambda record: record.skill_key)
        return [_record_dict(record, strings) for record in records]

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        start = page * page_size
        slice_ = records[start : start + page_size]
        # Neither every class (item and event skills) nor none (ship and item effects).
        class_skills = sum(1 for r in records if r["class_mask"] not in (0, ALL_CLASSES_MASK))
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records), class_skills=class_skills)
        rows = [
            [
                e(r["skill_no"]),
                e(r["level"]),
                e(r["max_level"]),
                icon_cell(r["icon_path"]),
                pa_cell(r, "name"),
                e(r["classes"] or _EMPTY),
                e(r["kind_label"]),
                e(r["branch_label"] or _EMPTY),
                e(r["weapon"] or _EMPTY),
                flag_cell(r["can_quick_slot"]),
                e(r["need_level"] or _EMPTY),
                e(r["need_skill_point"] or _EMPTY),
                text_list_cell(r["need_skills"], _LIST_PREVIEW_ITEMS) or _EMPTY,
                e(r["previous_rank"] or _EMPTY),
                text_list_cell(r["exclusive_skills"], _LIST_PREVIEW_ITEMS) or _EMPTY,
            ]
            for r in slice_
        ]
        return table(meta, self._columns(), rows)

from __future__ import annotations

from collections.abc import Callable
from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.buff import buff_label, buff_list_cell
from _common.duration import format_duration
from _common.html import Column, e, icon_cell, sort_keys, table, truncate
from _common.icon_index import IconKind, icon_path
from _common.lang import handler_text, load_handler_strings
from _common.pabr_offset import PabrOffsetRow, parse_pabr_u32_offset_rows
from _common.pa_text import pa_cell, pa_fields, pa_key, pa_list_cell, pa_list_fields
from _common.skill import skill_description_tagged, skill_name_tagged, split_skill_key
from _common.offset_table import OffsetColumn, OffsetTableHandler, offset_column, size_column
from .parser import SkillRecord, parse_skill_records


_LANG_DIR = Path(__file__).parent / "lang"
_OFFSET_FILE = "skilloffset.dbss"
_EMPTY = "-"
_LIST_PREVIEW_ITEMS = 3
_SCRIPT_PREVIEW_CHARS = 80


def _skill_label_tagged(skill_key: int) -> str:
    """The skill's name with its PA tags (Prime skills are orange), else its number."""
    skill_no = split_skill_key(skill_key)[0]
    return skill_name_tagged(skill_no) or str(skill_no)


def _record_dict(record: SkillRecord) -> dict:
    return {
        "skill_key": record.skill_key,
        "skill_no": record.skill_no,
        "level": record.level,
        "icon_path": icon_path(IconKind.SKILL, record.skill_no),
        # English, then the Korean skilltype.dbss name, then the action name.
        **pa_fields("name", skill_name_tagged(record.skill_no) or record.action_name),
        "action_name": record.action_name,
        **pa_fields("description", skill_description_tagged(record.skill_no, record.level, record.description_kr)),
        # Zero means no cooldown; None sorts last.
        "cooldown_ms": record.cooldown_ms or None,
        "cooldown": format_duration(record.cooldown_ms),
        "resource_cost": record.resource_cost or None,
        "stamina_cost": record.stamina_cost or None,
        "buff_ids": list(record.buff_ids),
        "buffs": [buff_label(buff_id) for buff_id in record.buff_ids],
        "buff_count": len(record.buff_ids) or None,
        "next_skill_keys": list(record.next_skill_keys),
        **pa_list_fields("next_skills", [_skill_label_tagged(key) for key in record.next_skill_keys]),
        # Set only on Core skills, where it names the skill the Core enhances.
        "related_cool_time_skill_keys": list(record.related_cool_time_skill_keys),
        **pa_fields(
            "related_cool_time_skill",
            ", ".join(_skill_label_tagged(key) for key in record.related_cool_time_skill_keys),
        ),
        "description_kr": record.description_kr,
        "script": record.script,
    }


def _skill_offset_record(row: PabrOffsetRow) -> dict:
    skill_no, level = split_skill_key(row.entry_id)
    return {
        "skill_key": row.entry_id,
        "skill_no": skill_no,
        "level": level,
        "dbss_offset": row.offset,
        "size": row.size,
    }


def skill_offset_handler(
    parse_rows: Callable[[bytes], list[PabrOffsetRow]] = parse_pabr_u32_offset_rows,
) -> OffsetTableHandler:
    """Skill cluster offset tables: rows keyed by skill key.

    `skilloffset.dbss` and `skilltypeoffset.dbss` are PABR tables, the default;
    `skillsimplyoffset.dbss` passes its bare-row reader.
    """

    def read(data: bytes) -> list[dict]:
        return [_skill_offset_record(row) for row in parse_rows(data)]

    return OffsetTableHandler(
        _LANG_DIR,
        [
            OffsetColumn("skill_no", "skillNo"),
            OffsetColumn("level", "level"),
            offset_column("dbss_offset", "dbssOffset"),
            size_column("size", "size"),
        ],
        read,
    )


class SkillHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["skillNo"], "num", sort_key="skill_no"),
            Column(cols["level"], "num", sort_key="level"),
            Column(cols["icon"], sort_key="icon_path"),
            Column(cols["name"], sort_key="name"),
            Column(cols["description"], sort_key="description"),
            Column(cols["cooldown"], "num", sort_key="cooldown_ms"),
            Column(cols["resourceCost"], "num", sort_key="resource_cost"),
            Column(cols["staminaCost"], "num", sort_key="stamina_cost"),
            Column(cols["buffs"], sort_key="buff_count"),
            Column(cols["nextSkills"]),
            Column(cols["baseSkill"], sort_key="related_cool_time_skill"),
            Column(cols["script"], sort_key="script"),
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

        # The index order is arbitrary. Skill key order keeps each skill's
        # levels in order under the table's default skill number sort, and
        # gives CSV export class skills first.
        records = sorted(parse_skill_records(data, offset_raw), key=lambda record: record.skill_key)
        return [_record_dict(record) for record in records]

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        start = page * page_size
        slice_ = records[start : start + page_size]
        with_buffs = sum(1 for r in records if r["buff_ids"])
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records), with_buffs=with_buffs)
        rows = [
            [
                e(r["skill_no"]),
                e(r["level"]),
                icon_cell(r["icon_path"]),
                pa_cell(r, "name"),
                pa_cell(r, "description"),
                e(r["cooldown"] or _EMPTY),
                e(r["resource_cost"] or _EMPTY),
                e(r["stamina_cost"] or _EMPTY),
                buff_list_cell(r["buff_ids"], _LIST_PREVIEW_ITEMS) or _EMPTY,
                pa_list_cell(r[pa_key("next_skills")], _LIST_PREVIEW_ITEMS),
                pa_cell(r, "related_cool_time_skill"),
                e(truncate(r["script"], _SCRIPT_PREVIEW_CHARS) or _EMPTY),
            ]
            for r in slice_
        ]
        return table(meta, self._columns(), rows)

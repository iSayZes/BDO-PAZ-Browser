"""skilltype.dbss preview handler: each skill's name, icon, kind and its tooltip key command."""
from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.html import Column, e, icon_cell, sort_keys, table
from _common.lang import handler_text, load_handler_strings
from _common.pa_text import pa_cell, pa_fields, pa_line_cell
from _common.skill import skill_name_tagged
from _common.string_hash import key_hash
from _dbss.commandtooltip.parser import FILE_NAME as COMMAND_TOOLTIP_FILE
from _dbss.commandtooltip.parser import KEY_FIELD as COMMAND_TOOLTIP_KEY
from _dbss.commandtooltip.parser import parse_commandtooltip_records
from _dbss.commandtooltip.text import command_fields
from .parser import SkillTypeRecord, parse_skilltype_records


_LANG_DIR = Path(__file__).parent / "lang"
_OFFSET_FILE = "skilltypeoffset.dbss"
_EMPTY = "-"


def _label(labels: dict[str, str], value: int) -> str:
    return labels.get(str(value), str(value))


def _command_tooltips(data: bytes | None) -> dict[int, dict]:
    """`commandtooltip.dbss` rows by key hash; empty without the file. Raises ValueError when it does not parse."""
    if data is None:
        return {}
    return {row[COMMAND_TOOLTIP_KEY]: row for row in parse_commandtooltip_records(data)}


def _command_dict(pattern_control: str, tooltips: Mapping[int, dict]) -> dict:
    """The keyboard and console pad commands of the skill's `commandtooltip.dbss` row, else empty texts."""
    row = tooltips.get(key_hash(pattern_control)) if pattern_control else None
    if row is None:
        return {**pa_fields("pc_command", ""), **pa_fields("console_command", "")}
    return command_fields(row[COMMAND_TOOLTIP_KEY], row["pc_command_kr"], row["console_command_kr"])


def _record_dict(record: SkillTypeRecord, labels: dict, tooltips: Mapping[int, dict]) -> dict:
    return {
        "skill_key": record.skill_key,
        "skill_no": record.skill_no,
        "icon_path": record.icon_path,
        # English first, then the Korean source.
        **pa_fields("name", skill_name_tagged(record.skill_no) or record.name_kr),
        "name_kr": record.name_kr,
        "group_name_kr": record.group_name_kr,
        "kind": record.kind,
        "kind_label": _label(labels["kind"], record.kind),
        # 0, a normal skill, is None and an empty cell, so it sorts last.
        "awakening_type": record.awakening_type or None,
        "awakening_type_label": _label(labels["awakeningType"], record.awakening_type) if record.awakening_type else "",
        "pattern_control": record.pattern_control,
        **_command_dict(record.pattern_control, tooltips),
    }


class SkillTypeHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["skillNo"], "num", sort_key="skill_no"),
            Column(cols["icon"], sort_key="icon_path"),
            Column(cols["name"], sort_key="name"),
            Column(cols["kind"], sort_key="kind"),
            Column(cols["awakeningType"], sort_key="awakening_type"),
            Column(cols["pcCommand"], sort_key="pc_command"),
            Column(cols["consoleCommand"], sort_key="console_command"),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def companions(self, entry: PazEntry) -> list[str]:
        folder = entry.internal_path.rsplit("/", 1)[0]
        return [f"{folder}/{_OFFSET_FILE}", f"{folder}/{COMMAND_TOOLTIP_FILE}"]

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        offset_raw = companions.get(_OFFSET_FILE)
        if offset_raw is None:
            raise ValueError(f"{_OFFSET_FILE} companion not found.")

        labels = load_handler_strings(self.lang, _LANG_DIR)
        tooltips = _command_tooltips(companions.get(COMMAND_TOOLTIP_FILE))
        # The index order is arbitrary. Skill key order gives CSV export class
        # skills first; the table opens on its default skill number sort.
        records = sorted(parse_skilltype_records(data, offset_raw), key=lambda record: record.skill_key)
        return [_record_dict(record, labels, tooltips) for record in records]

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        start = page * page_size
        slice_ = records[start : start + page_size]
        with_icon = sum(1 for r in records if r["icon_path"])
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records), with_icon=with_icon)
        rows = [
            [
                e(r["skill_no"]),
                icon_cell(r["icon_path"]),
                pa_cell(r, "name"),
                e(r["kind_label"]),
                e(r["awakening_type_label"] or _EMPTY),
                pa_line_cell(r, "pc_command"),
                pa_line_cell(r, "console_command"),
            ]
            for r in slice_
        ]
        return table(meta, self._columns(), rows)

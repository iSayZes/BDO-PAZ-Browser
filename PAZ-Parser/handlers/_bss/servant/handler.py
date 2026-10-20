from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.character import character_name
from _common.character_link import (
    character_key_cell,
    character_row_ids,
    characterstatic_offset_companion,
    has_character_row,
)
from _common.duration import format_duration
from _common.html import Column, e, flag_cell, sort_keys, table, text_list_cell
from _common.lang import handler_text, load_handler_strings
from _common.servant_kind import servant_kind_name
from _common.vehicle_skill import VEHICLE_SKILL_FILE, vehicle_skill_companion, vehicle_skill_name
from _dbss.vehicleskill.parser import vehicle_skill_names_kr
from .parser import parse_servant_records


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"
_MS_PER_SECOND = 1000
_SKILLS_SHOWN = 4

# Record field -> label key of the yes/no columns, in doc order.
_FLAG_COLUMNS_MIDDLE = (
    ("is_male", "isMale"),
    ("is_display_gender", "isDisplayGender"),
    ("servant_main_model", "servantMainModel"),
    ("is_mating_result", "isMatingResult"),
    ("is_trade", "isTrade"),
)
_FLAG_COLUMNS_END = (
    ("can_mix", "canMix"),
    ("can_mating", "canMating"),
)


def _number(value: int) -> str:
    return f"{value:,}"


class ServantBssHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["characterId"], "num", sort_key="character_id"),
            Column(cols["name"], sort_key="name"),
            Column(cols["servantKind"], sort_key="servant_kind"),
            Column(cols["servantKindSub"], "num", sort_key="servant_kind_sub"),
            Column(cols["tier"], "num", sort_key="tier"),
            Column(cols["grade"], "num", sort_key="grade"),
            Column(cols["color1"], "num", sort_key="color1"),
            Column(cols["color2"], "num", sort_key="color2"),
            Column(cols["color3"], "num", sort_key="color3"),
            Column(cols["matingCount"], "num", sort_key="mating_count"),
            Column(cols["lifespan"], "num", sort_key="lifespan"),
            Column(cols["basePrice"], "num", sort_key="base_price"),
            Column(cols["pricePerLevel"], "num", sort_key="price_per_level"),
            *(Column(cols[label], sort_key=field) for field, label in _FLAG_COLUMNS_MIDDLE),
            Column(cols["linkCount"], "num", sort_key="link_count"),
            Column(cols["experiencePerOne"], "num", sort_key="experience_per_one"),
            Column(cols["formIndex"], "num", sort_key="form_index"),
            Column(cols["basicLearnSkillMaxCount"], "num", sort_key="basic_learn_skill_max_count"),
            Column(cols["basicLearnSkills"]),
            Column(cols["rewardMoneyPercent"], "num", sort_key="reward_money_percent"),
            Column(cols["isOnlyPcroom"], sort_key="is_only_pcroom"),
            Column(cols["stallionSkills"]),
            *(Column(cols[label], sort_key=field) for field, label in _FLAG_COLUMNS_END),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def companions(self, entry: PazEntry) -> list[str]:
        return [
            characterstatic_offset_companion(entry.internal_path),
            vehicle_skill_companion(entry.internal_path),
        ]

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        row_ids = character_row_ids(companions)
        try:
            skill_names_kr = vehicle_skill_names_kr(companions.get(VEHICLE_SKILL_FILE))
        except ValueError as ex:
            raise ValueError(f"{VEHICLE_SKILL_FILE}: {ex}") from ex

        def skill_names(keys: list[int]) -> list[str]:
            return [vehicle_skill_name(key, skill_names_kr) for key in keys]

        return [
            {
                **record,
                # The shown name: LOC in the user's language, else the Korean dev name.
                "name": character_name(record["character_id"]) or record["name_kr"],
                "servant_kind_name": servant_kind_name(record["servant_kind"]),
                # 0 is "no lifespan"; None keeps those rows last in a sort.
                "lifespan": record["lifespan"] or None,
                "basic_learn_skills": skill_names(record["basic_learn_skill_keys"]),
                "stallion_skills": skill_names(record["stallion_skill_keys"]),
                "has_character_row": has_character_row(row_ids, record["character_id"]),
            }
            for record in parse_servant_records(data)
        ]

    def _row(self, r: dict) -> list[str]:
        lifespan = r["lifespan"]
        return [
            character_key_cell(r["character_id"], r["has_character_row"]),
            e(r["name"]),
            e(r["servant_kind_name"]),
            e(r["servant_kind_sub"]),
            e(r["tier"]),
            e(r["grade"]),
            e(r["color1"]),
            e(r["color2"]),
            e(r["color3"]),
            e(r["mating_count"]),
            e(format_duration(lifespan * _MS_PER_SECOND)) if lifespan else _EMPTY,
            e(_number(r["base_price"])),
            e(_number(r["price_per_level"])),
            *(flag_cell(bool(r[field])) for field, _ in _FLAG_COLUMNS_MIDDLE),
            e(r["link_count"]),
            e(_number(r["experience_per_one"])),
            e(r["form_index"]),
            e(r["basic_learn_skill_max_count"]),
            text_list_cell(r["basic_learn_skills"], _SKILLS_SHOWN) or _EMPTY,
            e(_number(r["reward_money_percent"])),
            flag_cell(bool(r["is_only_pcroom"])),
            text_list_cell(r["stallion_skills"], _SKILLS_SHOWN) or _EMPTY,
            *(flag_cell(bool(r[field])) for field, _ in _FLAG_COLUMNS_END),
        ]

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        start = page * page_size
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records))
        rows = [self._row(r) for r in records[start : start + page_size]]
        return table(meta, self._columns(), rows)

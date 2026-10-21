"""Layouts of the Rose War tables (`rosewar*.bss`) that fit the PABR value tables.

The team columns follow the team numbers of `rosewarteamnostaticstatus.bss`:
Kamasylvia first, then O'dyllita. A fierce battle key is a sanctum, the key
of `rosewarfiercebattlemonsterstaticstatus.bss`.
"""

from __future__ import annotations

from _common.character import character_name
from _common.skill import skill_name
from _common.town import town_name
from .fields import CHARACTER_KEY, ITEM_ID, MAP_COLOR
from .layout import NameLookup, RowCount, TextRef, ValueField, ValueTable, unknown_fields
from .rosewar_names import argb_hex, game_key_text, region_text, schedule_text, skill_type_text, team_text


# The (character key, u32) pairs of rosewargimicfiercebattlebuffstaicstatus.bss.
_GIMMICK_PAIR_COUNT = 5
_GIMMICK_PAIR_SIZE = 8
_SANCTUM_KEY = ValueField("fierce_battle_key", "H", "sanctumId")


def _character(name: str, column: str, fmt: str = "H") -> ValueField:
    """A character key and its LOC type 6 name, stored as `character_name` in place of `character_key`."""
    name_field = name.replace("character_key", "character_name")
    return ValueField(name, fmt, f"{column}Id", NameLookup(name_field, column, character_name))


def _skill(name: str, column: str) -> ValueField:
    """A skill number and its LOC type 10 name."""
    name_field = name.removesuffix("_no") + "_name"
    return ValueField(name, "H", f"{column}Id", NameLookup(name_field, column, skill_name))


def _gimmick_pairs() -> tuple[ValueField, ...]:
    """The five (character key, unknown u32) pairs at the start of a gimmick row."""
    fields: list[ValueField] = []
    for index in range(_GIMMICK_PAIR_COUNT):
        number = index + 1
        fields.append(_character(f"character_key_{number}", f"character{number}", "I"))
        fields.append(ValueField(f"unknown_{index * _GIMMICK_PAIR_SIZE + 4:02x}", "I"))
    return tuple(fields)


ROSE_WAR_TABLES: tuple[ValueTable, ...] = (
    ValueTable(
        "rosewarfiercebattlemonsterstaticstatus.bss",
        (
            _SANCTUM_KEY,
            _character("kamasylvia_character_key", "kamasylviaCharacter"),
            _character("odyllita_character_key", "odyllitaCharacter"),
            _character("neutral_character_key", "neutralCharacter"),
            ValueField("unknown_08", "B"),
            ValueField("skill_no", "H", "skillId", NameLookup("skill_name", "skill", skill_name)),
            ValueField("name_ref", "I", text=TextRef("name_kr", "sanctum")),
            ValueField("unknown_0f", "B"),
        ),
        RowCount.COUNTED,
        first_fields=("fierce_battle_key", "name_ref"),
    ),
    ValueTable(
        "rosewarfiercebattlenodestaticstatus.bss",
        (
            ValueField("kamasylvia_side_keys", "H", "kamasylviaSideSanctums", is_counted_list=True, count_fmt="Q"),
            ValueField("odyllita_side_keys", "H", "odyllitaSideSanctums", is_counted_list=True, count_fmt="Q"),
            ValueField("unknown_list_3", "H", is_counted_list=True, count_fmt="Q"),
            ValueField("unknown_list_4", "H", is_counted_list=True, count_fmt="Q"),
            _SANCTUM_KEY,
        ),
        RowCount.COUNTED,
        first_fields=("fierce_battle_key",),
    ),
    ValueTable(
        "rosewargimicfiercebattlebuffstaicstatus.bss",
        (
            *_gimmick_pairs(),
            _character("gimmick_character_key", "gimmickCharacter"),
            ValueField("unknown_2a", "B"),
        ),
        RowCount.COUNTED,
        first_fields=("gimmick_character_key",),
    ),
    ValueTable(
        "rosewarinfo.bss",
        (MAP_COLOR, *unknown_fields((0x03, "B"), (0x04, "3s"), (0x07, "B"), (0x08, "B"))),
        RowCount.COUNTED,
        count_key="mapColors",
    ),
    ValueTable(
        "rosewarkillnamescoretagstaticstatus.bss",
        (
            ValueField("score", "I", "score"),
            ValueField(
                "title_key_ref",
                "I",
                text=TextRef("title_key", "titleKey", NameLookup("title", "title", game_key_text)),
            ),
            ValueField("color", "I", "color", display=argb_hex),
        ),
        RowCount.COUNTED,
    ),
    ValueTable(
        "rosewarnodemonsterinfostaicstatus.bss",
        (
            CHARACTER_KEY,
            ValueField("image_ref", "I", text=TextRef("image_path", "imagePath")),
            ValueField("tooltip_image_ref", "I", text=TextRef("tooltip_image_path", "tooltipImagePath")),
        ),
        RowCount.COUNTED,
    ),
    ValueTable(
        "rosewarskillstaticstatus.bss",
        (
            ValueField("skill_type", "I", "skillType", display=skill_type_text),
            _skill("kamasylvia_skill_no", "kamasylviaSkill"),
            _skill("odyllita_skill_no", "odyllitaSkill"),
        ),
        RowCount.COUNTED,
    ),
    ValueTable(
        "rosewarstaticstatus.bss",
        (
            *unknown_fields(
                (0x04, "Q"),
                (0x0C, "Q"),
                *((offset, "I") for offset in range(0x14, 0x44, 4)),
                (0x44, "f"),
                *((offset, "I") for offset in range(0x48, 0x58, 4)),
            ),
            _character("kamasylvia_boss_character_key", "kamasylviaBoss"),
            _character("odyllita_boss_character_key", "odyllitaBoss"),
            *unknown_fields(*((offset, "I") for offset in range(0x5C, 0x78, 4))),
            ValueField(
                "kamasylvia_region_key",
                "H",
                "kamasylviaRegionId",
                NameLookup("kamasylvia_region_name", "kamasylviaRegion", town_name),
            ),
            ValueField(
                "odyllita_region_key",
                "H",
                "odyllitaRegionId",
                NameLookup("odyllita_region_name", "odyllitaRegion", town_name),
            ),
            *unknown_fields((0x7C, "I"), (0x80, "I")),
            ValueField("region_keys", "H", "regionKeys", display=region_text, is_counted_list=True),
            ITEM_ID,
            ValueField("schedules", "B24I", "schedules", display=schedule_text, is_counted_list=True),
        ),
    ),
    ValueTable(
        "rosewarteamnostaticstatus.bss",
        (CHARACTER_KEY, ValueField("team_no", "I", "team", display=team_text)),
        RowCount.COUNTED,
    ),
)

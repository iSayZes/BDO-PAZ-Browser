"""Layouts of the PvP and matching tables that fit the PABR value tables.

The Arena of Arsha (`arsha*.bss`), the Shadow Arena duel tournament, the
world boss non-PK regions, the Red Battlefield, Atoraxxion party matching,
the matching queue thresholds and the Golden Pig Cave relay field
(`personalrelayoption.bss`). A reward list holds `(item_key, item_count)`
entries, as in the guild tables.
"""

from __future__ import annotations

from _common.character import character_name
from _common.item_key import item_name_tagged
from .fields import CHARACTER_KEY
from .guild_names import reward_item_text
from .layout import IconLookup, NameLookup, RowCount, TextRef, ValueField, ValueTable, unknown_fields
from .names import item_icon_path
from .pvp_names import action_hash_text, matching_condition_text, skill_text
from .rosewar_names import game_key_text, region_text


def _reward_items(name: str, column: str) -> ValueField:
    """A u32-counted list of (u32 item key, u64 item count)."""
    return ValueField(name, "IQ", column, display=reward_item_text, is_counted_list=True)


def _action_hash(name: str, column: str) -> ValueField:
    """The `ascii_key_hash` of an action name."""
    return ValueField(name, "I", column, display=action_hash_text)


def _character(name: str, column: str) -> ValueField:
    """A u16 character key and its LOC type 6 name, stored as `<role>_character_name`."""
    name_field = name.replace("character_key", "character_name")
    return ValueField(name, "H", f"{column}Id", NameLookup(name_field, column, character_name))


def _item(name: str, column: str) -> ValueField:
    """A u32 item ID with its icon and LOC type 0 name, stored as `<role>_item_name` and `<role>_icon_path`."""
    role = name.removesuffix("_item_id")
    return ValueField(
        name,
        "I",
        f"{column}Id",
        NameLookup(f"{role}_item_name", column, item_name_tagged, is_tagged=True),
        IconLookup(f"{role}_icon_path", "icon", item_icon_path),
    )


# (u16 instance field key, u32 minimum AP, u32 minimum DP).
_MATCHING_CONDITION_FORMAT = "HII"


PVP_TABLES: tuple[ValueTable, ...] = (
    ValueTable(
        "arshadebuff.bss",
        (ValueField("debuff_timer", "I", "debuffTimer"), *unknown_fields((0x04, "I"), (0x08, "I"))),
        RowCount.COUNTED,
    ),
    ValueTable(
        "arshasetlostregion.bss",
        (
            ValueField("index", "I", "index"),
            *unknown_fields((0x04, "I"), (0x08, "f"), (0x0C, "f"), (0x10, "f"), (0x14, "f"), (0x18, "f")),
            ValueField("skill_no", "H", "skill", display=skill_text),
        ),
        RowCount.COUNTED,
    ),
    ValueTable(
        "sha_dueltournamentoption.bss",
        (
            _action_hash("game_start_action_hash", "gameStartAction"),
            _action_hash("fight_start_action_hash", "fightStartAction"),
            _action_hash("winner_action_hash", "winnerAction"),
            ValueField("max_player_count", "I", "maxPlayerCount"),
            *unknown_fields((0x14, "I"), (0x18, "I"), (0x1C, "I"), (0x20, "I"), (0x24, "I")),
            ValueField("after_time_end_state", "I", "afterTimeEndState"),
            ValueField("unknown_2c", "I"),
        ),
    ),
    ValueTable(
        "worldbossnonpkregion.bss",
        (
            ValueField("key", "H"),
            CHARACTER_KEY,
            ValueField("region_keys", "H", "regionKeys", display=region_text, is_counted_list=True),
        ),
        RowCount.COUNTED,
    ),
    ValueTable(
        "redbattlefieldstaticstatusmanager.bss",
        (
            *unknown_fields(
                (0x04, "I"),
                (0x08, "Q"),
                (0x10, "H"),
                (0x12, "H"),
                (0x14, "f"),
                (0x18, "f"),
                (0x1C, "f"),
                (0x20, "H"),
                (0x22, "I"),
                (0x26, "f"),
                (0x2A, "f"),
                (0x2E, "f"),
                (0x32, "I"),
                (0x36, "Q"),
                (0x3E, "Q"),
                (0x46, "Q"),
                (0x4E, "I"),
                (0x52, "I"),
                (0x56, "I"),
                (0x5A, "I"),
                (0x5E, "I"),
                (0x62, "Q"),
                (0x6A, "Q"),
                (0x72, "I"),
                (0x76, "I"),
                (0x7A, "I"),
                (0x7E, "I"),
                (0x82, "I"),
            ),
            ValueField("banner_text_sheet_ref", "I", text=TextRef("banner_text_sheet")),
            ValueField(
                "banner_text_key_ref",
                "I",
                text=TextRef("banner_text_key", "bannerTextKey", NameLookup("banner_text", "bannerText", game_key_text)),
            ),
            ValueField("banner_texture_ref", "I", text=TextRef("banner_texture", "bannerTexture")),
            ValueField("map_texture_ref", "I", text=TextRef("map_texture", "mapTexture")),
            _reward_items("win_reward_items", "victoryRewards"),
            _reward_items("lose_reward_items", "defeatRewards"),
        ),
    ),
    ValueTable(
        "partymatchingcondition.bss",
        (
            ValueField(
                "matching_conditions",
                _MATCHING_CONDITION_FORMAT,
                "matchingConditions",
                display=matching_condition_text,
                is_counted_list=True,
            ),
            ValueField("unknown_conditions", _MATCHING_CONDITION_FORMAT, is_counted_list=True),
        ),
    ),
    ValueTable(
        "matchingcongestionstaticstatusmanager.bss",
        unknown_fields((0x00, "I"), (0x04, "B"), (0x05, "I"), (0x09, "I")),
        RowCount.COUNTED,
    ),
    ValueTable(
        "personalrelayoption.bss",
        (
            ValueField("name_ref", "I", text=TextRef("name_kr", "name")),
            *unknown_fields(*((offset, "f") for offset in range(0x04, 0x28, 4))),
            *unknown_fields((0x28, "Q"), (0x30, "Q")),
            _character("npc_character_key", "npc"),
            _character("monster_character_key", "monster"),
            _item("summon_item_id", "summonItem"),
            _item("token_item_id", "tokenItem"),
            *unknown_fields(
                (0x44, "I"),
                (0x48, "H"),
                (0x4A, "I"),
                (0x4E, "I"),
                (0x52, "I"),
                (0x56, "I"),
                (0x5A, "I"),
                (0x5E, "f"),
            ),
        ),
        RowCount.COUNTED,
    ),
)

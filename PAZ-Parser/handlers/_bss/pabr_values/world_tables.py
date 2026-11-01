"""Layouts of the monster and world tables that fit the PABR value tables.

Each file's doc is `docs/file-formats/bss/<stem>_bss.md`. The field names of
`bloodaltar.bss`, `treasureinfostaicstatusmanager.bss` and
`magnuseasyteleport.bss` follow the getters of the client Lua, those of
`bdobatchsummonmonsterss.bss` and `reusegroup.bss` a private server's
sheets on client 1784.
"""

from __future__ import annotations

from _common.character import character_name
from _common.item_key import item_key_icon_path, item_key_text_tagged, item_name_tagged
from _common.knowledge import knowledge_name
from _common.node import node_name
from _common.town import town_name
from .fields import CHARACTER_KEY
from .layout import IconLookup, NameLookup, RowCount, TextRef, ValueField, ValueTable, unknown_fields
from .names import item_icon_path, packed_quest_text, packed_quest_title
from .rosewar_names import game_key_text
from .world_names import item_key_entry_text, reward_entry_text


# item_enchant_key, 4 alignment bytes, item_count (bloodaltar_bss.md, Reward Entry).
_REWARD_ENTRY = "I4sQ"


def _item_enchant_key(name: str) -> ValueField:
    """An `enchant_level << 24 | item_id` key with its icon and name."""
    return ValueField(
        name,
        "I",
        "itemId",
        NameLookup("item_name", "item", item_key_text_tagged, is_tagged=True),
        IconLookup("icon_path", "icon", item_key_icon_path),
    )


def _rewards(name: str, column: str) -> ValueField:
    return ValueField(name, _REWARD_ENTRY, column, display=reward_entry_text, is_counted_list=True)


WORLD_TABLES: tuple[ValueTable, ...] = (
    ValueTable("monstermanager.bss", (CHARACTER_KEY, *unknown_fields((0x02, "I"), (0x06, "I"))), RowCount.COUNTED),
    ValueTable("monsterselfmanager.bss", (CHARACTER_KEY, *unknown_fields((0x02, "I"))), RowCount.COUNTED),
    # The BatchSummonMonsterStaticStatus members of a private server on client 1784.
    ValueTable(
        "bdobatchsummonmonsterss.bss",
        (
            ValueField("summon_key", "I", "summonKey"),
            ValueField(
                "item_key",
                "I",
                "summonItemId",
                NameLookup("item_name", "summonItem", item_name_tagged, is_tagged=True),
                IconLookup("icon_path", "icon", item_icon_path),
            ),
            ValueField("summon_level", "I", "summonLevel"),
            ValueField("added_dd", "f", "addedDd"),
            ValueField("added_pv", "f", "addedPv"),
            ValueField("added_dv", "f", "addedDv"),
            ValueField("added_hit", "f", "addedHit"),
            ValueField("added_hp", "f", "addedHp"),
            ValueField("character_key", "H", "monsterId", NameLookup("character_name", "monster", character_name)),
        ),
        RowCount.COUNTED,
    ),
    ValueTable(
        "bloodaltar.bss",
        (
            ValueField("stage_key", "I", "stageKey"),
            ValueField("unknown_str_ref_04", "I", text=TextRef("unknown_str_04_kr")),
            ValueField("unknown_str_ref_08", "I", text=TextRef("unknown_str_08_kr")),
            ValueField("boss_texture_ref", "I", text=TextRef("boss_texture", "bossTexture")),
            ValueField("match_min_offence", "f", "matchMinOffence"),
            ValueField("match_min_defence", "f", "matchMinDefence"),
            ValueField("recommended_offence", "f", "recommendedOffence"),
            ValueField("recommended_defence", "f", "recommendedDefence"),
            _rewards("first_rewards", "firstRewards"),
            _rewards("weekly_rewards", "weeklyRewards"),
        ),
        RowCount.COUNTED,
        count_key="stages",
        # The Options structure before the stage count (bloodaltar_bss.md).
        head=unknown_fields((0x00, "I"), (0x04, "I"), (0x08, "I"), (0x0C, "H")),
    ),
    ValueTable(
        "treasureinfostaicstatusmanager.bss",
        (
            _item_enchant_key("item_enchant_key"),
            ValueField("puzzle_key", "H", "puzzleKey"),
            ValueField(
                "desc_ref",
                "I",
                text=TextRef("desc_key", "descKey", NameLookup("desc", "description", game_key_text)),
            ),
            ValueField(
                "core_material_item_enchant_keys",
                "I",
                "coreMaterials",
                display=item_key_entry_text,
                is_counted_list=True,
            ),
            ValueField(
                "quest_no",
                "I",
                "questId",
                NameLookup("quest_title", "quest", packed_quest_title),
                display=packed_quest_text,
            ),
            ValueField("texture_id_ref", "I", text=TextRef("texture_id", "textureId")),
            ValueField("is_hunting", "B", "isHunting"),
        ),
        RowCount.COUNTED,
        count_key="treasures",
    ),
    ValueTable(
        "magnuseasyteleport.bss",
        (
            ValueField("waypoint_key", "H", "nodeKey", NameLookup("node_name", "node", node_name)),
            ValueField("x", "f", "x"),
            ValueField("y", "f", "y"),
            ValueField("z", "f", "z"),
            ValueField("name_ref", "I", text=TextRef("name_key", "nameKey", NameLookup("name", "name", game_key_text))),
            ValueField(
                "mental_card_key",
                "I",
                "knowledgeKey",
                NameLookup("knowledge_name", "knowledge", knowledge_name),
            ),
            ValueField("unknown_16", "Q"),
            ValueField("region_key", "H", "regionKey", NameLookup("region_name", "region", town_name)),
        ),
        RowCount.COUNTED,
        count_key="teleports",
    ),
    ValueTable(
        "reusegroup.bss",
        (
            ValueField("reuse_group", "I", "reuseGroup"),
            ValueField("is_expired_in_offline", "B", "isExpiredInOffline"),
        ),
        RowCount.COUNTED,
        count_key="reuseGroups",
    ),
)

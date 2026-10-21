"""Layouts of the small option tables, one entry per file.

The layout types are in `layout.py`. Each file's doc is
`docs/file-formats/<stem>_bss.md`; field names follow the doc, and
`unknown_*` fields get no column.
"""

from __future__ import annotations

from _common.item_key import item_name_tagged
from _common.rate import rate_percent
from _common.town import town_name
from .fields import CHARACTER_KEY, ITEM_ID, TITLE_ID
from .layout import Framing, IconLookup, NameLookup, RowCount, TextRef, ValueField, ValueTable, unknown_fields
from .names import (
    aura_name,
    calamity_number,
    cooldown_cut,
    duration_seconds,
    item_icon_path,
    packed_quest_text,
    packed_quest_title,
    rate_bonus,
    skill_key_name,
    utc_time,
    vehicle_skill_name,
)
from .rosewar_tables import ROSE_WAR_TABLES

__all__ = [
    "VALUE_TABLES",
    "SIEGE_STAGE_COUNT",
    "Framing",
    "IconLookup",
    "NameLookup",
    "RowCount",
    "TextRef",
    "ValueField",
    "ValueTable",
]


# The SiegeStage_0 to SiegeStage_6 columns of siegemercenarylimitcount.bss.
SIEGE_STAGE_COUNT = 7



VALUE_TABLES: tuple[ValueTable, ...] = (
    ValueTable(
        "barterresetoption.bss",
        (
            ValueField("general_barter", "I", "generalBarter", is_counted_list=True),
            ValueField("material_barter", "I", "materialBarter", is_counted_list=True),
        ),
    ),
    ValueTable("cashproduct_newbieproduct.bss", (ValueField("product_id", "I", "productId"),)),
    ValueTable(
        "cultivationevent.bss",
        (ValueField("cultivation_event_type", "h", "cultivationEventType"),),
        RowCount.COUNTED,
    ),
    ValueTable(
        "elementalstat.bss",
        (
            ValueField("element_type", "B", "elementType", NameLookup("aura", "aura", aura_name)),
            ValueField("ap_per_orb", "I", "apPerOrb"),
            ValueField("dp_per_orb", "I", "dpPerOrb"),
            ValueField("stat_points_per_orb", "I", "statPointsPerOrb"),
            ValueField("element_type_dup", "B"),
        ),
        RowCount.COUNTED,
        Framing.BARE,
        "blackShrineAuras",
    ),
    ValueTable("employeeloyalismitemetc.bss", unknown_fields((0x04, "I"), (0x08, "I"), (0x0C, "I"), (0x10, "I"))),
    ValueTable(
        "icefisingregionstaticstatus.bss",
        (
            ValueField("region_key", "H", "regionKey", NameLookup("region_name", "region", town_name)),
            ValueField("mini_game_group_index", "H", "miniGameGroup"),
        ),
        RowCount.TO_TABLE_START,
    ),
    ValueTable("instanceetcoption.bss", (ValueField("unknown_04", "I"), ValueField("unknown_08", "I"))),
    ValueTable(
        "interaction.bss",
        (
            ValueField("interaction_type", "I", "interactionType"),
            ValueField("unknown_04", "B"),
            # The item the interaction uses; interaction_bss.md Notes.
            ValueField(
                "execute",
                "I",
                "execute",
                NameLookup("item_name", "item", item_name_tagged, is_tagged=True),
                IconLookup("icon_path", "icon", item_icon_path),
            ),
            CHARACTER_KEY,
        ),
        RowCount.COUNTED,
    ),
    ValueTable("maidactoroption.bss", (ValueField("unknown_04", "B"), ValueField("unknown_05", "B"))),
    ValueTable(
        "morninglandoption.bss",
        (
            ValueField("stat_reset_cost", "Q", "statResetCost"),
            ValueField("light_orb_reset_cost", "Q", "lightOrbResetCost"),
            ValueField("weekly_clear_limit", "B", "weeklyClearLimit"),
        ),
        framing=Framing.BARE,
    ),
    ValueTable(
        "musicoption.bss",
        (ValueField("playable_distance", "f", "playableDistance"), ValueField("unknown_08", "8s")),
    ),
    ValueTable(
        "othertownnotmovableitem.bss",
        (
            ITEM_ID,
        ),
        RowCount.COUNTED,
        Framing.BARE,
        "notMovableItems",
    ),
    ValueTable("petfeedcount.bss", (ValueField("feed_item_count", "I", "feedItemCount"),)),
    ValueTable(
        "petleaderbuff.bss",
        (
            ValueField("pet_tier", "B", "petTier"),
            ValueField("unknown_01", "B"),
            ValueField("leader_buff_rate", "I", "lootCooldown", display=cooldown_cut),
        ),
        RowCount.COUNTED,
        Framing.BARE,
        "petTiers",
    ),
    ValueTable(
        "servantchecktitle.bss",
        (
            ValueField("unknown_04", "H"),
            TITLE_ID,
            CHARACTER_KEY,
        ),
    ),
    ValueTable("servantwhistledistance.bss", (ValueField("unknown_04", "2s"),)),
    ValueTable(
        "siegemercenarylimitcount.bss",
        tuple(ValueField(f"siege_stage_{stage}", "I", f"siegeStage{stage}") for stage in range(SIEGE_STAGE_COUNT)),
    ),
    ValueTable(
        "snowboardcourseinfo.bss",
        unknown_fields((0x00, "3s"), (0x03, "B"), (0x04, "B"), (0x05, "3s"), (0x08, "B")),
        RowCount.COUNTED,
    ),
    ValueTable(
        "solareetcoptionstaticstatus.bss",
        unknown_fields((0x00, "f"), (0x04, "f"), (0x08, "f"), (0x0C, "f"), (0x10, "f")),
        framing=Framing.BARE,
    ),
    ValueTable("timeattackranking.bss", (CHARACTER_KEY,), RowCount.COUNTED),
    ValueTable(
        "vehicletrainingskill.bss",
        (ValueField("skill_key", "B", "skillId", NameLookup("skill_name", "skill", vehicle_skill_name)),),
        RowCount.COUNTED,
    ),
    ValueTable(
        "voxelregionskillstaticstatusmanager.bss",
        (
            ValueField("unknown_00", "B"),
            ValueField("skill_key", "I", "skillId", NameLookup("skill_name", "skill", skill_key_name)),
        ),
        RowCount.COUNTED,
    ),
    ValueTable(
        "elementalserverbuff.bss",
        (
            ValueField("calamity_level", "B", "calamity", display=calamity_number),
            ValueField("calamity_level_dup", "B"),
            ValueField("sun_blessing_ap", "f", "sunBlessingAp"),
            ValueField("moon_blessing_dp", "f", "moonBlessingDp"),
            ValueField("earth_blessing_drop_rate", "I", "earthBlessingDropRate", display=rate_bonus),
            ValueField("buff_duration", "I", "buffDuration", display=duration_seconds),
            ValueField("unknown_12", "I"),
        ),
        RowCount.COUNTED,
        Framing.BARE,
    ),
    ValueTable(
        "olviaacademyseasonss.bss",
        (
            ValueField("season_no", "I", "academyClass"),
            ValueField("start_time", "Q", "startTime", display=utc_time),
            ValueField("graduation_time", "Q", "graduationTime", display=utc_time),
            ValueField("close_time", "Q", "closeTime", display=utc_time),
            ValueField("end_time", "Q", "endTime", display=utc_time),
            ValueField(
                "enter_quest",
                "I",
                "enterQuestId",
                NameLookup("enter_quest_title", "enterQuest", packed_quest_title),
                display=packed_quest_text,
            ),
            ValueField(
                "graduation_quest",
                "I",
                "graduationQuestId",
                NameLookup("graduation_quest_title", "graduationQuest", packed_quest_title),
                display=packed_quest_text,
            ),
            TITLE_ID,
        ),
        framing=Framing.BARE,
        count_key="academyClasses",
    ),
    ValueTable(
        "petupgrade.bss",
        (
            ValueField("pet_tier", "B", "petTier"),
            ITEM_ID,
            ValueField("item_count", "Q", "itemCount"),
            ValueField("success_rate", "I", "successRate", display=rate_percent),
            ValueField("unknown_11", "I"),
            ValueField("pet_tier_dup", "B"),
        ),
        RowCount.COUNTED,
        Framing.BARE,
        "petTiers",
    ),
    *ROSE_WAR_TABLES,
)

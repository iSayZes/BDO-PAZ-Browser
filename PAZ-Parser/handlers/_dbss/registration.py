from __future__ import annotations

from bdo_preview import register_handler

from _common.empty_table import EmptyTableHandler

from .title.handler import TitleDbssHandler
from .titlebuff.handler import TitleBuffListHandler, title_buff_list_offset_handler
from .titleoffset.handler import title_offset_handler
from .mentalcard.handler import MentalCardHandler, mental_card_offset_handler
from .detail_dialog.handler import DetailDialogHandler, detail_dialog_offset_handler
from .base_dialog.handler import BaseDialogHandler
from .dialogtext.handler import DialogTextHandler, dialog_text_offset_handler
from .textbind.handler import TextBindHandler, text_bind_offset_handler
from .mentaltheme.handler import MentalThemeHandler, mental_theme_offset_handler
from .knowledgelearning.handler import (
    KnowledgeLearningHandler,
    knowledge_learning_offset_handler,
)
from .npcpersonality.handler import NpcPersonalityHandler, npc_personality_offset_handler
from .quest.handler import QuestDbssHandler
from .questgroup.handler import QuestGroupDbssHandler
from .empty_tables.tables import EMPTY_TABLES
from .itemcouponreward.handler import ItemCouponRewardOffsetHandler
from .worldmapmonster.handler import WorldMapMonsterHandler, world_map_monster_offset_handler
from .cashproduct.handler import (
    CashProductHandler,
    cash_product_offset_handler,
)
from .itemenchant.handler import (
    ItemEnchantHandler,
    item_enchant_offset_handler,
)
from .guaranteeenchantss.handler import GuaranteeEnchantHandler
from .enchantstaticstatus.handler import (
    EnchantStaticStatusHandler,
    enchant_static_status_offset_handler,
)
from .journalquest.handler import JournalQuestDbssHandler, journal_quest_offset_handler
from .npcgift.handler import (
    npc_gift_offset_handler,
    NpcGiftHandler,
    NpcGiftDataHandler,
)
from .zodiacsign.handler import (
    ZodiacSignHandler,
    zodiac_sign_offset_handler,
    ZodiacSignOrderHandler,
    zodiac_sign_order_offset_handler,
)
from .plantzone.handler import plant_zone_offset_handler, PlantZoneHandler
from .itemsubgroup.handler import ItemSubgroupHandler, item_subgroup_offset_handler
from .growthpasscategory.handler import GrowthPassCategoryHandler, growth_pass_category_offset_handler
from .characterspawntype.handler import (
    character_spawn_type_offset_handler,
    CharacterSpawnTypeHandler,
)
from .characterobject.handler import (
    character_object_offset_handler,
    CharacterObjectHandler,
)
from .characterfunction.handler import (
    character_function_offset_handler,
    CharacterFunctionHandler,
)
from .characterstatic.handler import (
    character_static_offset_handler,
    CharacterStaticHandler,
)
from .pet.handler import (
    PetDbssHandler,
    PetGradeHandler,
    pet_grade_offset_handler,
    pet_offset_handler,
)
from .petaction.handler import PetActionHandler, pet_action_offset_handler
from .petexp.handler import PetExpHandler, pet_exp_offset_handler
from .servantexperience.handler import ServantExperienceHandler, servant_experience_offset_handler
from .pcgrowth.handler import PcGrowthHandler, pc_growth_offset_handler
from .fitnesslevel.handler import FitnessLevelHandler, fitness_level_offset_handler
from .lifeexp.handler import LifeExpHandler, life_exp_offset_handler
from .skillexperience.handler import LevelExpHandler, level_offset_handler
from .skillexperience.parser import LEVEL_TABLES
from .petskill.handler import PetSkillHandler, pet_skill_offset_handler
from .petequipskillaquire.handler import (
    PetEquipSkillAcquireHandler,
    pet_equip_skill_acquire_offset_handler,
)
from .fairyequipskillaquire.handler import (
    FairyEquipSkillAcquireHandler,
    fairy_equip_skill_acquire_offset_handler,
)
from .fairyfeedingitem.handler import (
    FairyFeedingItemHandler,
    fairy_feeding_item_offset_handler,
)
from .fairypotion.handler import FairyPotionHandler, fairy_potion_offset_handler
from .fairyskillchange.handler import (
    FairySkillChangeHandler,
    fairy_skill_change_offset_handler,
)
from .employeename.handler import EmployeeNameHandler, employee_name_offset_handler
from .employeespawninfo.handler import EmployeeSpawnInfoHandler, employee_spawn_info_offset_handler
from .employeespawnposition.handler import (
    EmployeeSpawnPositionHandler,
    employee_spawn_position_offset_handler,
)
from .buff.handler import BuffHandler, buff_offset_handler
from .skill.handler import SkillHandler, skill_offset_handler
from .skilltype.handler import SkillTypeHandler
from .skillsimply.handler import SkillSimplyHandler
from .skillsimply.parser import parse_skillsimply_offset_rows
from .skillpiece.handler import SkillPieceHandler, skill_piece_offset_handler
from .itemmaxlevel.handler import ItemMaxLevelHandler, item_max_level_offset_handler
from .itemtrade.handler import ItemTradeHandler, item_trade_offset_handler
from .alchemycharge.handler import AlchemyChargeHandler, alchemy_charge_offset_handler
from .itemtradegrouptonpc.handler import (
    ItemTradeGroupToNpcHandler,
    item_trade_group_to_npc_offset_handler,
)
from .alchemyupgrade.handler import AlchemyUpgradeHandler, alchemy_upgrade_offset_handler
from .alchemystonechange.handler import AlchemyStoneChangeHandler, alchemy_stone_change_offset_handler
from .waititem.handler import WaitItemHandler, wait_item_offset_handler
from .fieldboss.handler import FieldBossHandler, field_boss_offset_handler
from .weatheractor.handler import WeatherActorHandler, weather_actor_offset_handler
from .itemimprovement.handler import (
    ItemImprovementHandler,
    ItemImprovementSourceHandler,
    item_improvement_offset_handler,
    item_improvement_source_offset_handler,
)
from .extractitem.handler import ExtractItemHandler, extract_item_offset_handler
from .teleport.handler import TeleportHandler, teleport_offset_handler
from .instancefield.handler import InstanceFieldHandler, instance_field_offset_handler
from .houseinforeceipe.handler import HouseInfoReceipeHandler, house_info_receipe_offset_handler


def register_dbss_handlers() -> None:
    register_handler("titleoffset.dbss", title_offset_handler())
    register_handler("title.dbss", TitleDbssHandler())
    register_handler("titlebufflistoffset.dbss", title_buff_list_offset_handler())
    register_handler("titlebufflist.dbss", TitleBuffListHandler())
    register_handler("mentalcardoffset.dbss", mental_card_offset_handler())
    register_handler("mentalcard.dbss", MentalCardHandler())
    register_handler("detail_dialogoffset.dbss", detail_dialog_offset_handler())
    register_handler("detail_dialog.dbss", DetailDialogHandler())
    # base_dialogoffset.dbss has the layout and keys of detail_dialogoffset.dbss.
    register_handler("base_dialogoffset.dbss", detail_dialog_offset_handler())
    register_handler("base_dialog.dbss", BaseDialogHandler())
    register_handler("skilloffset.dbss", skill_offset_handler())
    register_handler("skill.dbss", SkillHandler())
    # skilltypeoffset.dbss has the layout and keys of skilloffset.dbss.
    register_handler("skilltypeoffset.dbss", skill_offset_handler())
    register_handler("skilltype.dbss", SkillTypeHandler())
    register_handler("skillsimplyoffset.dbss", skill_offset_handler(parse_skillsimply_offset_rows))
    register_handler("skillsimply.dbss", SkillSimplyHandler())
    register_handler("skillpieceoffset.dbss", skill_piece_offset_handler())
    register_handler("skillpiece.dbss", SkillPieceHandler())
    register_handler("itemmaxleveloffset.dbss", item_max_level_offset_handler())
    register_handler("itemmaxlevel.dbss", ItemMaxLevelHandler())
    register_handler("itemtradeoffset.dbss", item_trade_offset_handler())
    register_handler("itemtrade.dbss", ItemTradeHandler())
    register_handler("alchemychargeoffset.dbss", alchemy_charge_offset_handler())
    register_handler("alchemycharge.dbss", AlchemyChargeHandler())
    register_handler("itemtradegrouptonpcoffset.dbss", item_trade_group_to_npc_offset_handler())
    register_handler("itemtradegrouptonpc.dbss", ItemTradeGroupToNpcHandler())
    register_handler("alchemyupgradeoffset.dbss", alchemy_upgrade_offset_handler())
    register_handler("alchemyupgrade.dbss", AlchemyUpgradeHandler())
    register_handler("alchemystonechangeoffset.dbss", alchemy_stone_change_offset_handler())
    register_handler("alchemystonechange.dbss", AlchemyStoneChangeHandler())
    register_handler("waititemoffset.dbss", wait_item_offset_handler())
    register_handler("waititem.dbss", WaitItemHandler())
    register_handler("fieldbossoffset.dbss", field_boss_offset_handler())
    register_handler("fieldboss.dbss", FieldBossHandler())
    register_handler("weatheractoroffset.dbss", weather_actor_offset_handler())
    register_handler("weatheractor.dbss", WeatherActorHandler())
    register_handler("itemimprovementoffset.dbss", item_improvement_offset_handler())
    register_handler("itemimprovement.dbss", ItemImprovementHandler())
    register_handler("itemimprovementsourceoffset.dbss", item_improvement_source_offset_handler())
    register_handler("itemimprovementsource.dbss", ItemImprovementSourceHandler())
    register_handler("extractitemoffset.dbss", extract_item_offset_handler())
    register_handler("extractitem.dbss", ExtractItemHandler())
    register_handler("dialogtextoffset.dbss", dialog_text_offset_handler())
    register_handler("dialogtext.dbss", DialogTextHandler())
    register_handler("textbindoffset.dbss", text_bind_offset_handler())
    register_handler("textbind.dbss", TextBindHandler())
    register_handler("mentalthemeoffset.dbss", mental_theme_offset_handler())
    register_handler("mentaltheme.dbss", MentalThemeHandler())
    register_handler("knowledgelearningoffset.dbss", knowledge_learning_offset_handler())
    register_handler("knowledgelearning.dbss", KnowledgeLearningHandler())
    register_handler("npcpersonalityoffset.dbss", npc_personality_offset_handler())
    register_handler("npcpersonality.dbss", NpcPersonalityHandler())
    register_handler("quest.dbss", QuestDbssHandler())
    register_handler("questgroup.dbss", QuestGroupDbssHandler())
    for name in EMPTY_TABLES:
        register_handler(name, EmptyTableHandler(name))
    register_handler("itemcouponrewardoffset.dbss", ItemCouponRewardOffsetHandler())
    register_handler("cashproduct.dbss", CashProductHandler())
    register_handler("cashproductoffset.dbss", cash_product_offset_handler())
    register_handler("itemenchant.dbss", ItemEnchantHandler())
    register_handler("itemenchantoffset.dbss", item_enchant_offset_handler())
    register_handler("enchantstaticstatus.dbss", EnchantStaticStatusHandler())
    register_handler("enchantstaticstatusoffset.dbss", enchant_static_status_offset_handler())
    register_handler("guaranteeenchantss.dbss", GuaranteeEnchantHandler())
    register_handler("growthpasscategoryoffset.dbss", growth_pass_category_offset_handler())
    register_handler("growthpasscategory.dbss", GrowthPassCategoryHandler())
    register_handler("itemsubgroupoffset.dbss", item_subgroup_offset_handler())
    register_handler("itemsubgroup.dbss", ItemSubgroupHandler())
    register_handler("journalquestoffset.dbss", journal_quest_offset_handler())
    register_handler("journalquest.dbss", JournalQuestDbssHandler())
    register_handler("npcgiftoffset.dbss", npc_gift_offset_handler())
    register_handler("npcgift.dbss", NpcGiftHandler())
    register_handler("npcgiftdataoffset.dbss", npc_gift_offset_handler())
    register_handler("npcgiftdata.dbss", NpcGiftDataHandler())
    register_handler("zodiacsignoffset.dbss", zodiac_sign_offset_handler())
    register_handler("zodiacsign.dbss", ZodiacSignHandler())
    register_handler("zodiacsignorderoffset.dbss", zodiac_sign_order_offset_handler())
    register_handler("zodiacsignorder.dbss", ZodiacSignOrderHandler())
    register_handler("plantzoneoffset.dbss", plant_zone_offset_handler())
    register_handler("plantzone.dbss", PlantZoneHandler())
    register_handler("characterspawntypeoffset.dbss", character_spawn_type_offset_handler())
    register_handler("characterspawntype.dbss", CharacterSpawnTypeHandler())
    register_handler("characterobjectoffset.dbss", character_object_offset_handler())
    register_handler("characterobject.dbss", CharacterObjectHandler())
    register_handler("characterfunctionoffset.dbss", character_function_offset_handler())
    register_handler("characterfunction.dbss", CharacterFunctionHandler())
    register_handler("characterstaticoffset.dbss", character_static_offset_handler())
    register_handler("characterstatic.dbss", CharacterStaticHandler())
    register_handler("petoffset.dbss", pet_offset_handler())
    register_handler("petgradeoffset.dbss", pet_grade_offset_handler())
    register_handler("petgrade.dbss", PetGradeHandler())
    register_handler("pet.dbss", PetDbssHandler())
    register_handler("petactionoffset.dbss", pet_action_offset_handler())
    register_handler("petaction.dbss", PetActionHandler())
    register_handler("petexpoffset.dbss", pet_exp_offset_handler())
    register_handler("petexp.dbss", PetExpHandler())
    register_handler("servantexperienceoffset.dbss", servant_experience_offset_handler())
    register_handler("servantexperience.dbss", ServantExperienceHandler())
    register_handler("pcgrowthoffset.dbss", pc_growth_offset_handler())
    register_handler("pcgrowth.dbss", PcGrowthHandler())
    register_handler("fitnessleveloffset.dbss", fitness_level_offset_handler())
    register_handler("fitnesslevel.dbss", FitnessLevelHandler())
    register_handler("lifeexpoffset.dbss", life_exp_offset_handler())
    register_handler("lifeexp.dbss", LifeExpHandler())
    for level_table in LEVEL_TABLES:
        register_handler(level_table.offset_file, level_offset_handler())
        register_handler(level_table.file_name, LevelExpHandler(level_table))
    register_handler("petskilloffset.dbss", pet_skill_offset_handler())
    register_handler("petskill.dbss", PetSkillHandler())
    register_handler(
        "petequipskillaquireoffset.dbss",
        pet_equip_skill_acquire_offset_handler(),
    )
    register_handler("petequipskillaquire.dbss", PetEquipSkillAcquireHandler())
    register_handler(
        "fairyequipskillaquireoffset.dbss",
        fairy_equip_skill_acquire_offset_handler(),
    )
    register_handler("fairyequipskillaquire.dbss", FairyEquipSkillAcquireHandler())
    register_handler(
        "fairyfeedingitemoffset.dbss",
        fairy_feeding_item_offset_handler(),
    )
    register_handler("fairyfeedingitem.dbss", FairyFeedingItemHandler())
    register_handler("fairypotionoffset.dbss", fairy_potion_offset_handler())
    register_handler("fairypotion.dbss", FairyPotionHandler())
    register_handler(
        "fairyskillchangeoffset.dbss",
        fairy_skill_change_offset_handler(),
    )
    register_handler("fairyskillchange.dbss", FairySkillChangeHandler())
    register_handler("employeenameoffset.dbss", employee_name_offset_handler())
    register_handler("employeename.dbss", EmployeeNameHandler())
    register_handler(
        "employeespawnpositionoffset.dbss",
        employee_spawn_position_offset_handler(),
    )
    register_handler("employeespawnposition.dbss", EmployeeSpawnPositionHandler())
    register_handler("employeespawninfooffset.dbss", employee_spawn_info_offset_handler())
    register_handler("employeespawninfo.dbss", EmployeeSpawnInfoHandler())
    register_handler("buffoffset.dbss", buff_offset_handler())
    register_handler("buff.dbss", BuffHandler())
    register_handler("worldmapmonsteroffset.dbss", world_map_monster_offset_handler())
    register_handler("worldmapmonster.dbss", WorldMapMonsterHandler())
    register_handler("teleportoffset.dbss", teleport_offset_handler())
    register_handler("teleport.dbss", TeleportHandler())
    register_handler("instancefieldoffset.dbss", instance_field_offset_handler())
    register_handler("instancefield.dbss", InstanceFieldHandler())
    register_handler("houseinforeceipeoffset.dbss", house_info_receipe_offset_handler())
    register_handler("houseinforeceipe.dbss", HouseInfoReceipeHandler())

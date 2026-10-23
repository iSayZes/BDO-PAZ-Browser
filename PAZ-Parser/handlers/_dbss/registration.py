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
from .emoticon.handler import EmoticonHandler, emoticon_offset_handler
from .emoticonpackage.handler import EmoticonPackageHandler, emoticon_package_offset_handler
from .cashproductcategory.handler import CashProductCategoryHandler, cash_product_category_offset_handler
from .coupon.handler import CouponHandler, coupon_offset_handler
from .socialaction.handler import SocialActionHandler, social_action_offset_handler
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
from .itemenchantbackend.handler import ItemEnchantBackendHandler
from .itemenchantbackendtest.handler import ItemEnchantBackendTestHandler
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
from .actionexp.handler import ActionExpHandler, action_exp_offset_handler
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
from .employeecharactership.handler import (
    EmployeeCharacterShipHandler,
    employee_character_ship_offset_handler,
)
from .employeeloyalismitem.handler import (
    EmployeeLoyalismItemHandler,
    employee_loyalism_item_offset_handler,
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
from .itemtradegrouptonpc.handler import ItemTradeGroupHandler, item_trade_group_offset_handler
from .itemtradegroupfromnpc.parser import parse_itemtradegroupfromnpc_records
from .growthpasspointshop.handler import GrowthPassPointShopHandler, growth_pass_point_shop_offset_handler
from .producttool.handler import ProductToolHandler, product_tool_offset_handler
from .instancedungeoninfo.handler import InstanceDungeonInfoHandler, instance_dungeon_info_offset_handler
from .instancedungeonskillstatic.handler import (
    InstanceDungeonSkillStaticHandler,
    instance_dungeon_skill_static_offset_handler,
)
from .maincategory.handler import MainCategoryHandler, main_category_offset_handler
from .alchemyupgrade.handler import AlchemyUpgradeHandler, alchemy_upgrade_offset_handler
from .alchemystonechange.handler import AlchemyStoneChangeHandler, alchemy_stone_change_offset_handler
from .waititem.handler import WaitItemHandler, wait_item_offset_handler
from .fieldboss.handler import FieldBossHandler, field_boss_offset_handler
from .weatheractor.handler import WeatherActorHandler, weather_actor_offset_handler
from .cultivationweather.handler import CultivationWeatherHandler, cultivation_weather_offset_handler
from .floatfishing.handler import FloatFishingHandler, float_fishing_offset_handler
from .floatfishingpoint.handler import FloatFishingPointHandler, float_fishing_point_offset_handler
from .itemimprovement.handler import (
    ItemImprovementHandler,
    ItemImprovementSourceHandler,
    item_improvement_offset_handler,
    item_improvement_source_offset_handler,
)
from .extractitem.handler import ExtractItemHandler, extract_item_offset_handler
from .collect.handler import CollectHandler, collect_offset_handler
from .lifeactionexperience.handler import LifeActionExperienceHandler, life_action_experience_offset_handler
from .displayexchangeitemnpc.handler import DisplayExchangeItemNpcHandler, display_exchange_item_npc_offset_handler
from .itemexchangebynpc.handler import ItemExchangeByNpcHandler, item_exchange_by_npc_offset_handler
from .itempalette.handler import ItemPaletteHandler, item_palette_offset_handler
from .dyeingpalette.handler import DyeingPaletteHandler, dyeing_palette_offset_handler
from .itempuzzle.handler import ItemPuzzleHandler, item_puzzle_offset_handler
from .itemnakmessage.handler import ItemNakMessageHandler, item_nak_message_offset_handler
from .accessorystepup.handler import AccessoryStepUpHandler
from .employeeclientspawn.handler import EmployeeClientSpawnHandler, employee_client_spawn_offset_handler
from .exptoskillexprate.handler import ExpToSkillExpRateHandler, exp_to_skill_exp_rate_offset_handler
from .itemeffectchange.handler import ItemEffectChangeHandler, item_effect_change_offset_handler
from .itemenchantpuzzle.handler import ItemEnchantPuzzleHandler
from .itemenchantsafety.handler import ItemEnchantSafetyHandler, item_enchant_safety_offset_handler
from .servnatmarkettax.handler import ServantMarketTaxHandler, servant_market_tax_offset_handler
from .skillfusion.handler import SkillFusionHandler, skill_fusion_offset_handler
from .specialemployeeinfostaticstatus.handler import (
    SpecialEmployeeInfoHandler,
    special_employee_info_offset_handler,
)
from .restrictcontentsregion.handler import (
    RestrictContentsRegionHandler,
    restrict_contents_region_offset_handler,
)
from .instancefieldreward.handler import InstanceFieldRewardHandler, instance_field_reward_offset_handler
from .eventcategory.handler import EventCategoryHandler, event_category_offset_handler
from .greatseaevent.handler import GreatSeaEventHandler, great_sea_event_offset_handler
from .guildmanufacture.handler import GuildManufactureHandler, guild_manufacture_offset_handler
from .collectresourcename.handler import CollectResourceNameHandler, collect_resource_name_offset_handler
from .manufacturecondition.handler import ManufactureConditionHandler, manufacture_condition_offset_handler
from .teleport.handler import TeleportHandler, teleport_offset_handler
from .instancefield.handler import InstanceFieldHandler, instance_field_offset_handler
from .houseinforeceipe.handler import HouseInfoReceipeHandler, house_info_receipe_offset_handler
from .houseinfoneeditem.handler import HouseInfoNeedItemHandler, house_info_need_item_offset_handler
from .guildhousecraftskill.handler import GuildHouseCraftSkillHandler, guild_house_craft_skill_offset_handler
from .guildhousecraftstorage.handler import GuildHouseCraftStorageHandler, guild_house_craft_storage_offset_handler
from .characteraudioradius.handler import CharacterAudioRadiusHandler, character_audio_radius_offset_handler
from .itemexchangetoclass.handler import ItemExchangeToClassHandler, item_exchange_to_class_offset_handler
from .repairmaxendurance.handler import RepairMaxEnduranceHandler, repair_max_endurance_offset_handler
from .guildquest.handler import GuildQuestHandler, guild_quest_offset_handler
from .vehicleskill.handler import VehicleSkillHandler, vehicle_skill_offset_handler
from .vehicleskillcount.handler import VehicleSkillCountHandler
from .vehicleskillowner.handler import VehicleSkillOwnerHandler, vehicle_skill_owner_offset_handler
from .servantbuff.handler import ServantBuffHandler, servant_buff_offset_handler
from .servantinteraction.handler import ServantInteractionHandler, servant_interaction_offset_handler
from .servantupgrade.handler import ServantUpgradeHandler, servant_upgrade_offset_handler
from .minigamefindpattern.handler import MiniGameFindPatternHandler, minigame_find_pattern_offset_handler
from .minigamefindtool.handler import MiniGameFindToolHandler, minigame_find_tool_offset_handler
from .minigamereward.handler import MiniGameRewardHandler, minigame_reward_offset_handler
from .musiclevel.handler import MusicLevelHandler, musiclevel_offset_handler
from .purchaselimitgroup.handler import PurchaseLimitGroupHandler, purchase_limit_group_offset_handler
from .trainingvehicle.handler import TrainingVehicleHandler, training_vehicle_offset_handler
from .guildboss.handler import GuildBossHandler, guild_boss_offset_handler
from .itemcollectionscroll.handler import ItemCollectionScrollHandler, item_collection_scroll_offset_handler
from .servanttransformdata.handler import ServantTransformDataHandler, servant_transform_data_offset_handler
from .buildingbuff.handler import BuildingBuffHandler, building_buff_offset_handler
from .buildingupgrade.handler import BuildingUpgradeHandler, building_upgrade_offset_handler
from .carriagespec.handler import CarriageSpecHandler, carriage_spec_offset_handler
from .petdetectposition.handler import PetDetectPositionHandler, pet_detect_position_offset_handler
from .actionverificationindex.handler import (
    ActionVerificationIndexHandler,
    action_verification_index_offset_handler,
)
from .exceptionskillcooltimewidget.handler import (
    ExceptionSkillCoolTimeWidgetHandler,
    exception_skill_cool_time_widget_offset_handler,
)
from .personalmonster.handler import PersonalMonsterHandler, personal_monster_offset_handler
from .personalmonsterposition.handler import (
    PersonalMonsterPositionHandler,
    personal_monster_position_offset_handler,
)
from .petpcroom.handler import PetPcRoomHandler, pet_pc_room_offset_handler
from .petchangelook.handler import PetChangeLookHandler, pet_change_look_offset_handler
from .petoldfusion.handler import PetOldFusionHandler, pet_old_fusion_offset_handler
from .petfusionnew.handler import (
    PetFusionNewAddRateInfoHandler,
    PetFusionNewHandler,
    pet_fusion_new_offset_handler,
)
from .maid.handler import MaidHandler, maid_offset_handler
from .auction.handler import AuctionHandler, auction_offset_handler
from .monstergroup.handler import MonsterGroupHandler, monster_group_offset_handler
from .yachtbasecard.handler import YachtBaseCardHandler, yacht_base_card_offset_handler
from .yachtclasstypetextureinfo.handler import (
    YachtClassTypeTextureInfoHandler,
    yacht_class_type_texture_info_offset_handler,
)
from .yachtdice.handler import YachtDiceHandler, yacht_dice_offset_handler
from .yachtdicecard.handler import YachtDiceCardHandler, yacht_dice_card_offset_handler
from .yachtdicepreset.handler import YachtDicePresetHandler, yacht_dice_preset_offset_handler
from .houseinfoviewposition.handler import HouseInfoViewPositionHandler, house_info_view_position_offset_handler
from .mansiondata.handler import MansionDataHandler, mansion_data_offset_handler
from .innstaticstatus.handler import InnStaticStatusHandler, inn_static_status_offset_handler
from .houseworking.handler import HouseWorkingHandler, house_working_offset_handler
from .interiorrelationpoint.handler import InteriorRelationPointHandler, interior_relation_point_offset_handler
from .guildhouseinfo.handler import GuildHouseInfoHandler, guild_house_info_offset_handler
from .blackspirit.handler import BlackSpiritHandler, black_spirit_offset_handler
from .form.handler import FormHandler, form_offset_handler
from .marblegamediceitemgroup.handler import MarbleDiceItemGroupHandler, marble_dice_item_group_offset_handler
from .marblegamediceitemkey.handler import MarbleDiceItemKeyHandler, marble_dice_item_key_offset_handler
from .moonblessingss.handler import MoonBlessingHandler
from .seasonpass.handler import SeasonPassHandler
from .seasonreward.handler import SeasonRewardHandler
from .skillawakeningability.handler import SkillAwakeningAbilityHandler, skill_awakening_ability_offset_handler
from .attendance.handler import AttendanceHandler, attendance_offset_handler
from .customizeditem.handler import CustomizedItemHandler, customized_item_offset_handler
from .cashchoose.handler import CashChooseHandler, cash_choose_offset_handler
from .skillcommand.handler import SkillCommandHandler, skill_command_offset_handler
from .setoption.handler import SetOptionHandler, set_option_offset_handler
from .profiling.handler import ProfilingHandler, profiling_offset_handler
from .cutscene.handler import CutsceneHandler, cutscene_offset_handler
from .cashitemmarketsetting.handler import CashItemMarketSettingHandler, cash_item_market_setting_offset_handler
from .intimacyrelation.handler import IntimacyRelationHandler, intimacy_relation_offset_handler


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
    # itemtradegroupfromnpc.dbss holds the same columns in the client 1784 entry shape.
    for name in ("itemtradegrouptonpcoffset.dbss", "itemtradegroupfromnpcoffset.dbss"):
        register_handler(name, item_trade_group_offset_handler())
    register_handler("itemtradegrouptonpc.dbss", ItemTradeGroupHandler())
    register_handler("itemtradegroupfromnpc.dbss", ItemTradeGroupHandler(parse_itemtradegroupfromnpc_records))
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
    register_handler("cultivationweatheroffset.dbss", cultivation_weather_offset_handler())
    register_handler("cultivationweather.dbss", CultivationWeatherHandler())
    register_handler("floatfishingoffset.dbss", float_fishing_offset_handler())
    register_handler("floatfishing.dbss", FloatFishingHandler())
    register_handler("floatfishingpointoffset.dbss", float_fishing_point_offset_handler())
    register_handler("floatfishingpoint.dbss", FloatFishingPointHandler())
    register_handler("itemimprovementoffset.dbss", item_improvement_offset_handler())
    register_handler("itemimprovement.dbss", ItemImprovementHandler())
    register_handler("itemimprovementsourceoffset.dbss", item_improvement_source_offset_handler())
    register_handler("itemimprovementsource.dbss", ItemImprovementSourceHandler())
    register_handler("extractitemoffset.dbss", extract_item_offset_handler())
    register_handler("extractitem.dbss", ExtractItemHandler())
    register_handler("collectresourcenameoffset.dbss", collect_resource_name_offset_handler())
    register_handler("collectresourcename.dbss", CollectResourceNameHandler())
    register_handler("manufactureconditionoffset.dbss", manufacture_condition_offset_handler())
    register_handler("manufacturecondition.dbss", ManufactureConditionHandler())
    register_handler("collectoffset.dbss", collect_offset_handler())
    register_handler("collect.dbss", CollectHandler())
    register_handler("lifeactionexperienceoffset.dbss", life_action_experience_offset_handler())
    register_handler("lifeactionexperience.dbss", LifeActionExperienceHandler())
    register_handler("displayexchangeitemnpcoffset.dbss", display_exchange_item_npc_offset_handler())
    register_handler("displayexchangeitemnpc.dbss", DisplayExchangeItemNpcHandler())
    register_handler("itemexchangebynpcoffset.dbss", item_exchange_by_npc_offset_handler())
    register_handler("itemexchangebynpc.dbss", ItemExchangeByNpcHandler())
    register_handler("itempaletteoffset.dbss", item_palette_offset_handler())
    register_handler("itempalette.dbss", ItemPaletteHandler())
    register_handler("dyeingpaletteoffset.dbss", dyeing_palette_offset_handler())
    register_handler("dyeingpalette.dbss", DyeingPaletteHandler())
    register_handler("itempuzzleoffset.dbss", item_puzzle_offset_handler())
    register_handler("itempuzzle.dbss", ItemPuzzleHandler())
    register_handler("itemnakmessageoffset.dbss", item_nak_message_offset_handler())
    register_handler("itemnakmessage.dbss", ItemNakMessageHandler())
    register_handler("accessorystepup.dbss", AccessoryStepUpHandler())
    register_handler("employeeclientspawnoffset.dbss", employee_client_spawn_offset_handler())
    register_handler("employeeclientspawn.dbss", EmployeeClientSpawnHandler())
    register_handler("exptoskillexprateoffset.dbss", exp_to_skill_exp_rate_offset_handler())
    register_handler("exptoskillexprate.dbss", ExpToSkillExpRateHandler())
    register_handler("itemeffectchangeoffset.dbss", item_effect_change_offset_handler())
    register_handler("itemeffectchange.dbss", ItemEffectChangeHandler())
    register_handler("itemenchantpuzzle.dbss", ItemEnchantPuzzleHandler())
    register_handler("itemenchantsafetyoffset.dbss", item_enchant_safety_offset_handler())
    register_handler("itemenchantsafety.dbss", ItemEnchantSafetyHandler())
    register_handler("servnatmarkettaxoffset.dbss", servant_market_tax_offset_handler())
    register_handler("servnatmarkettax.dbss", ServantMarketTaxHandler())
    register_handler("skillfusionoffset.dbss", skill_fusion_offset_handler())
    register_handler("skillfusion.dbss", SkillFusionHandler())
    register_handler("specialemployeeinfostaticstatusoffset.dbss", special_employee_info_offset_handler())
    register_handler("specialemployeeinfostaticstatus.dbss", SpecialEmployeeInfoHandler())
    register_handler("restrictcontentsregionoffset.dbss", restrict_contents_region_offset_handler())
    register_handler("restrictcontentsregion.dbss", RestrictContentsRegionHandler())
    register_handler("instancefieldrewardoffset.dbss", instance_field_reward_offset_handler())
    register_handler("instancefieldreward.dbss", InstanceFieldRewardHandler())
    register_handler("eventcategoryoffset.dbss", event_category_offset_handler())
    register_handler("eventcategory.dbss", EventCategoryHandler())
    register_handler("greatseaeventoffset.dbss", great_sea_event_offset_handler())
    register_handler("greatseaevent.dbss", GreatSeaEventHandler())
    register_handler("guildmanufactureoffset.dbss", guild_manufacture_offset_handler())
    register_handler("guildmanufacture.dbss", GuildManufactureHandler())
    register_handler("dialogtextoffset.dbss", dialog_text_offset_handler())
    register_handler("dialogtext.dbss", DialogTextHandler())
    register_handler("emoticonoffset.dbss", emoticon_offset_handler())
    register_handler("emoticon.dbss", EmoticonHandler())
    register_handler("emoticonpackageoffset.dbss", emoticon_package_offset_handler())
    register_handler("emoticonpackage.dbss", EmoticonPackageHandler())
    register_handler("cashproductcategoryoffset.dbss", cash_product_category_offset_handler())
    register_handler("cashproductcategory.dbss", CashProductCategoryHandler())
    register_handler("couponoffset.dbss", coupon_offset_handler())
    register_handler("coupon.dbss", CouponHandler())
    register_handler("socialactionoffset.dbss", social_action_offset_handler())
    register_handler("socialaction.dbss", SocialActionHandler())
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
    register_handler("itemenchantbackend.dbss", ItemEnchantBackendHandler())
    # The same index layout and keys as itemenchantoffset.dbss.
    register_handler("itemenchantbackendoffset.dbss", item_enchant_offset_handler())
    register_handler("itemenchantbackendtest.dbss", ItemEnchantBackendTestHandler())
    register_handler("enchantstaticstatus.dbss", EnchantStaticStatusHandler())
    register_handler("enchantstaticstatusoffset.dbss", enchant_static_status_offset_handler())
    register_handler("guaranteeenchantss.dbss", GuaranteeEnchantHandler())
    register_handler("growthpasscategoryoffset.dbss", growth_pass_category_offset_handler())
    register_handler("growthpasscategory.dbss", GrowthPassCategoryHandler())
    register_handler("growthpasspointshopoffset.dbss", growth_pass_point_shop_offset_handler())
    register_handler("growthpasspointshop.dbss", GrowthPassPointShopHandler())
    register_handler("producttooloffset.dbss", product_tool_offset_handler())
    register_handler("producttool.dbss", ProductToolHandler())
    register_handler("instancedungeoninfooffset.dbss", instance_dungeon_info_offset_handler())
    register_handler("instancedungeoninfo.dbss", InstanceDungeonInfoHandler())
    register_handler("instancedungeonskillstaticoffset.dbss", instance_dungeon_skill_static_offset_handler())
    register_handler("instancedungeonskillstatic.dbss", InstanceDungeonSkillStaticHandler())
    register_handler("maincategoryoffset.dbss", main_category_offset_handler())
    register_handler("maincategory.dbss", MainCategoryHandler())
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
    register_handler("actionexpoffset.dbss", action_exp_offset_handler())
    register_handler("actionexp.dbss", ActionExpHandler())
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
    register_handler("employeecharactershipoffset.dbss", employee_character_ship_offset_handler())
    register_handler("employeecharactership.dbss", EmployeeCharacterShipHandler())
    register_handler("employeeloyalismitemoffset.dbss", employee_loyalism_item_offset_handler())
    register_handler("employeeloyalismitem.dbss", EmployeeLoyalismItemHandler())
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
    register_handler("houseinfoneeditemoffset.dbss", house_info_need_item_offset_handler())
    register_handler("houseinfoneeditem.dbss", HouseInfoNeedItemHandler())
    register_handler("guildhousecraftskilloffset.dbss", guild_house_craft_skill_offset_handler())
    register_handler("guildhousecraftskill.dbss", GuildHouseCraftSkillHandler())
    register_handler("guildhousecraftstorageoffset.dbss", guild_house_craft_storage_offset_handler())
    register_handler("guildhousecraftstorage.dbss", GuildHouseCraftStorageHandler())
    register_handler("characteraudioradiusoffset.dbss", character_audio_radius_offset_handler())
    register_handler("characteraudioradius.dbss", CharacterAudioRadiusHandler())
    register_handler("itemexchangetoclassoffset.dbss", item_exchange_to_class_offset_handler())
    register_handler("itemexchangetoclass.dbss", ItemExchangeToClassHandler())
    register_handler("repairmaxenduranceoffset.dbss", repair_max_endurance_offset_handler())
    register_handler("repairmaxendurance.dbss", RepairMaxEnduranceHandler())
    register_handler("guildquestoffset.dbss", guild_quest_offset_handler())
    register_handler("guildquest.dbss", GuildQuestHandler())
    register_handler("vehicleskilloffset.dbss", vehicle_skill_offset_handler())
    register_handler("vehicleskill.dbss", VehicleSkillHandler())
    register_handler("vehicleskillcount.dbss", VehicleSkillCountHandler())
    register_handler("vehicleskillowneroffset.dbss", vehicle_skill_owner_offset_handler())
    register_handler("vehicleskillowner.dbss", VehicleSkillOwnerHandler())
    register_handler("servantbuffoffset.dbss", servant_buff_offset_handler())
    register_handler("servantbuff.dbss", ServantBuffHandler())
    register_handler("servantinteractionoffset.dbss", servant_interaction_offset_handler())
    register_handler("servantinteraction.dbss", ServantInteractionHandler())
    register_handler("servantupgradeoffset.dbss", servant_upgrade_offset_handler())
    register_handler("servantupgrade.dbss", ServantUpgradeHandler())
    register_handler("minigamefindpatternoffset.dbss", minigame_find_pattern_offset_handler())
    register_handler("minigamefindpattern.dbss", MiniGameFindPatternHandler())
    register_handler("minigamefindtooloffset.dbss", minigame_find_tool_offset_handler())
    register_handler("minigamefindtool.dbss", MiniGameFindToolHandler())
    register_handler("minigamerewardoffset.dbss", minigame_reward_offset_handler())
    register_handler("minigamereward.dbss", MiniGameRewardHandler())
    register_handler("musicleveloffset.dbss", musiclevel_offset_handler())
    register_handler("musiclevel.dbss", MusicLevelHandler())
    register_handler("purchaselimitgroupoffset.dbss", purchase_limit_group_offset_handler())
    register_handler("purchaselimitgroup.dbss", PurchaseLimitGroupHandler())
    register_handler("trainingvehicleoffset.dbss", training_vehicle_offset_handler())
    register_handler("trainingvehicle.dbss", TrainingVehicleHandler())
    register_handler("guildbossoffset.dbss", guild_boss_offset_handler())
    register_handler("guildboss.dbss", GuildBossHandler())
    register_handler("itemcollectionscrolloffset.dbss", item_collection_scroll_offset_handler())
    register_handler("itemcollectionscroll.dbss", ItemCollectionScrollHandler())
    register_handler("servanttransformdataoffset.dbss", servant_transform_data_offset_handler())
    register_handler("servanttransformdata.dbss", ServantTransformDataHandler())
    register_handler("buildingbuffoffset.dbss", building_buff_offset_handler())
    register_handler("buildingbuff.dbss", BuildingBuffHandler())
    register_handler("buildingupgradeoffset.dbss", building_upgrade_offset_handler())
    register_handler("buildingupgrade.dbss", BuildingUpgradeHandler())
    register_handler("carriagespecoffset.dbss", carriage_spec_offset_handler())
    register_handler("carriagespec.dbss", CarriageSpecHandler())
    register_handler("petdetectpositionoffset.dbss", pet_detect_position_offset_handler())
    register_handler("petdetectposition.dbss", PetDetectPositionHandler())
    register_handler("actionverificationindexoffset.dbss", action_verification_index_offset_handler())
    register_handler("actionverificationindex.dbss", ActionVerificationIndexHandler())
    register_handler("exceptionskillcooltimewidgetoffset.dbss", exception_skill_cool_time_widget_offset_handler())
    register_handler("exceptionskillcooltimewidget.dbss", ExceptionSkillCoolTimeWidgetHandler())
    register_handler("personalmonsteroffset.dbss", personal_monster_offset_handler())
    register_handler("personalmonster.dbss", PersonalMonsterHandler())
    register_handler("personalmonsterpositionoffset.dbss", personal_monster_position_offset_handler())
    register_handler("personalmonsterposition.dbss", PersonalMonsterPositionHandler())
    register_handler("petpcroomoffset.dbss", pet_pc_room_offset_handler())
    register_handler("petpcroom.dbss", PetPcRoomHandler())
    register_handler("petfusionnewoffset.dbss", pet_fusion_new_offset_handler())
    register_handler("petfusionnew.dbss", PetFusionNewHandler())
    register_handler("petfusionnewaddrateinfo.dbss", PetFusionNewAddRateInfoHandler())
    register_handler("petoldfusionoffset.dbss", pet_old_fusion_offset_handler())
    register_handler("petoldfusion.dbss", PetOldFusionHandler())
    register_handler("petchangelookoffset.dbss", pet_change_look_offset_handler())
    register_handler("petchangelook.dbss", PetChangeLookHandler())
    register_handler("maidoffset.dbss", maid_offset_handler())
    register_handler("maid.dbss", MaidHandler())
    register_handler("auctionoffset.dbss", auction_offset_handler())
    register_handler("auction.dbss", AuctionHandler())
    register_handler("monstergroupoffset.dbss", monster_group_offset_handler())
    register_handler("monstergroup.dbss", MonsterGroupHandler())
    register_handler("yachtbasecardoffset.dbss", yacht_base_card_offset_handler())
    register_handler("yachtbasecard.dbss", YachtBaseCardHandler())
    register_handler("yachtclasstypetextureinfooffset.dbss", yacht_class_type_texture_info_offset_handler())
    register_handler("yachtclasstypetextureinfo.dbss", YachtClassTypeTextureInfoHandler())
    register_handler("yachtdiceoffset.dbss", yacht_dice_offset_handler())
    register_handler("yachtdice.dbss", YachtDiceHandler())
    register_handler("yachtdicecardoffset.dbss", yacht_dice_card_offset_handler())
    register_handler("yachtdicecard.dbss", YachtDiceCardHandler())
    register_handler("yachtdicepresetoffset.dbss", yacht_dice_preset_offset_handler())
    register_handler("yachtdicepreset.dbss", YachtDicePresetHandler())
    register_handler("houseinfoviewpositionoffset.dbss", house_info_view_position_offset_handler())
    register_handler("houseinfoviewposition.dbss", HouseInfoViewPositionHandler())
    register_handler("mansiondataoffset.dbss", mansion_data_offset_handler())
    register_handler("mansiondata.dbss", MansionDataHandler())
    register_handler("innstaticstatusoffset.dbss", inn_static_status_offset_handler())
    register_handler("innstaticstatus.dbss", InnStaticStatusHandler())
    register_handler("houseworkingoffset.dbss", house_working_offset_handler())
    register_handler("houseworking.dbss", HouseWorkingHandler())
    register_handler("interiorrelationpointoffset.dbss", interior_relation_point_offset_handler())
    register_handler("interiorrelationpoint.dbss", InteriorRelationPointHandler())
    register_handler("guildhouseinfooffset.dbss", guild_house_info_offset_handler())
    register_handler("guildhouseinfo.dbss", GuildHouseInfoHandler())
    register_handler("blackspiritoffset.dbss", black_spirit_offset_handler())
    register_handler("blackspirit.dbss", BlackSpiritHandler())
    register_handler("formoffset.dbss", form_offset_handler())
    register_handler("form.dbss", FormHandler())
    register_handler("marblegamediceitemgroupoffset.dbss", marble_dice_item_group_offset_handler())
    register_handler("marblegamediceitemgroup.dbss", MarbleDiceItemGroupHandler())
    register_handler("marblegamediceitemkeyoffset.dbss", marble_dice_item_key_offset_handler())
    register_handler("marblegamediceitemkey.dbss", MarbleDiceItemKeyHandler())
    register_handler("moonblessingss.dbss", MoonBlessingHandler())
    register_handler("seasonpass.dbss", SeasonPassHandler())
    register_handler("seasonreward.dbss", SeasonRewardHandler())
    register_handler("skillawakeningabilityoffset.dbss", skill_awakening_ability_offset_handler())
    register_handler("skillawakeningability.dbss", SkillAwakeningAbilityHandler())
    register_handler("attendanceoffset.dbss", attendance_offset_handler())
    register_handler("attendance.dbss", AttendanceHandler())
    register_handler("customizeditemoffset.dbss", customized_item_offset_handler())
    register_handler("customizeditem.dbss", CustomizedItemHandler())
    register_handler("cashchooseoffset.dbss", cash_choose_offset_handler())
    register_handler("cashchoose.dbss", CashChooseHandler())
    register_handler("skillcommandoffset.dbss", skill_command_offset_handler())
    register_handler("skillcommand.dbss", SkillCommandHandler())
    register_handler("setoptionoffset.dbss", set_option_offset_handler())
    register_handler("setoption.dbss", SetOptionHandler())
    register_handler("profilingoffset.dbss", profiling_offset_handler())
    register_handler("profiling.dbss", ProfilingHandler())
    register_handler("cutsceneoffset.dbss", cutscene_offset_handler())
    register_handler("cutscene.dbss", CutsceneHandler())
    register_handler("cashitemmarketsettingoffset.dbss", cash_item_market_setting_offset_handler())
    register_handler("cashitemmarketsetting.dbss", CashItemMarketSettingHandler())
    register_handler("intimacyrelationoffset.dbss", intimacy_relation_offset_handler())
    register_handler("intimacyrelation.dbss", IntimacyRelationHandler())

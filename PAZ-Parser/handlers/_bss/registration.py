from __future__ import annotations

from bdo_preview import register_handler

from _common.empty_table import EmptyTableHandler

from .actionverification.handler import ActionVerificationBssHandler
from .allquestlist.handler import AllQuestListBssHandler
from .barter_normal.handler import BarterNormalBssHandler
from .barter_npclist.handler import BarterNpcListBssHandler
from .barter_special.handler import BarterSpecialBssHandler
from .barterlifelevelinfo.handler import BarterLifeLevelInfoBssHandler
from .bartersubgroup.handler import BarterSubGroupBssHandler
from .bdoservanttitless.handler import BdoServantTitlesBssHandler
from .blizzardregioninfo.handler import BlizzardRegionInfoBssHandler
from .branchquest.handler import BranchQuestBssHandler
from .buffsimply.handler import BuffSimplyBssHandler
from .buildingsource.handler import BuildingSourceBssHandler
from .carriagechar.handler import CarriageCharBssHandler
from .charactersimply.handler import CharacterSimplyBssHandler
from .classskilllist.handler import ClassSkillListBssHandler
from .commonlifestatdata.handler import CommonLifeStatDataBssHandler
from .contentsgroupoptionstaticstatusmanager.handler import ContentsGroupOptionBssHandler
from .cronenchant.handler import CronEnchantBssHandler
from .cutscenecharacterdata.handler import CutsceneCharacterDataBssHandler
from .dropuihuntinggroundinfo.handler import DropUiHuntingGroundInfoBssHandler
from .dropuimaincategoryinfo.handler import DropUiMainCategoryInfoBssHandler
from .dropuisubcategoryinfo.handler import DropUiSubCategoryInfoBssHandler
from .dropuitaginfo.handler import DropUiTagInfoBssHandler
from .edaniaregioninfo.handler import EdaniaRegionInfoBssHandler
from .elementalmonsterreward.handler import ElementalMonsterRewardBssHandler
from .elementalmonsterstat.handler import ElementalMonsterStatBssHandler
from .empty_tables.parser import parse_empty_pabr_table
from .empty_tables.tables import EMPTY_PABR_TABLES
from .employeeexp.handler import EmployeeExpBssHandler
from .encyclopedia.handler import EncyclopediaBssHandler
from .employeestaticstatus.handler import EmployeeStaticStatusBssHandler
from .enchantfailcountexpstaticstatus.handler import EnchantFailCountExpBssHandler
from .experience.handler import ExperienceBssHandler
from .exploration.handler import ExplorationBssHandler
from .explorepointexperiencenew.handler import ExplorePointExperienceBssHandler
from .fairyequipskill.handler import FairyEquipSkillBssHandler
from .fairyfeedenchantfailcount.handler import (
    FairyFeedEnchantFailCountBssHandler,
)
from .fairyupgraderate.handler import FairyUpgradeRateBssHandler
from .feverquestdatatable.handler import FeverQuestDataTableBssHandler
from .fevertimeskill.handler import FeverTimeSkillBssHandler
from .fieldinfo.handler import FieldInfoBssHandler
from .fishcompetition.handler import FishCompetitionBssHandler
from .fitnessmaxlevel.handler import FitnessMaxLevelBssHandler
from .groupcameradata.handler import GroupCameraDataBssHandler
from .guildhousecraftskillreverselinklist.handler import GuildHouseCraftSkillReverseLinkListBssHandler
from .guildrightnewstaticstatus.handler import GuildRightNewStaticStatusBssHandler
from .hardcorecharacterstatstaticstatus.handler import HardcoreCharacterStatBssHandler
from .hardcorerandomspawncharacterstaticstatusmanager.handler import (
    HardcoreRandomSpawnCharacterStaticStatusManagerBssHandler,
)
from .houseinfo.handler import HouseInfoBssHandler
from .instancefieldmapinfo.handler import InstanceFieldMapInfoBssHandler
from .bossinfostaicstatusmanager.handler import BossInfoStaicStatusManagerBssHandler
from .boss_spawn.handler import BossSpawnBssHandler
from .boss_spawnlevel.handler import BossSpawnLevelBssHandler
from .bossmonsterhpsyncstaticstatus.handler import BossMonsterHpSyncStaticStatusBssHandler
from .itemequipgroup.handler import ItemEquipGroupBssHandler
from .itemexchangesource.handler import ItemExchangeSourceBssHandler
from .itemlinkprice.handler import ItemLinkPriceHandler
from .enchantactiveskillitem.handler import EnchantActiveSkillItemHandler
from .extractblackstone.handler import ExtractBlackStoneHandler
from .instancefieldcommonlimitentertime.handler import InstanceFieldCommonLimitEnterTimeHandler
from .monsterbuffzone.handler import MonsterBuffZoneHandler
from .simplesequence.handler import SimpleSequenceHandler
from .guildbossfieldinfo.handler import GuildBossFieldInfoHandler
from .itemexchangetoclassmapkey.handler import ItemExchangeToClassMapKeyBssHandler
from .itemimprovementdefaultdisplaylist.handler import ItemImprovementDefaultDisplayListBssHandler
from .itemmaingroup.handler import ItemMainGroupBssHandler
from .itemmarketcategory.handler import ItemMarketCategoryBssHandler
from .itemtradeetc.handler import ItemTradeEtcBssHandler
from .itemviewstackenchantgroupss.handler import ItemViewStackEnchantGroupSsBssHandler
from .jewelgroupstaticstatus.handler import JewelGroupStaticStatusBssHandler
from .jewelspecialslotsgroupstaticstatus.handler import JewelSpecialSlotsGroupStaticStatusBssHandler
from .knowledgelearningcharacterkey.handler import KnowledgeLearningCharacterKeyBssHandler
from .lifeexpmaxlevel.handler import LifeExpMaxLevelBssHandler
from .lightstoneset.handler import LightstoneSetBssHandler
from .manufacture.handler import ManufactureBssHandler
from .manufactureitemnaminginfo.handler import ManufactureItemNamingInfoBssHandler
from .mansionlandinfo.handler import MansionLandInfoBssHandler
from .mansionpartinfo.handler import MansionPartInfoBssHandler
from .masterlessservantstaticstatus.handler import MasterlessServantStaticStatusBssHandler
from .masterystatdata.handler import MasteryStatDataBssHandler
from .masterystatdata.spec import MASTERY_TABLES
from .menu.handler import MenuBssHandler
from .multiplequest.handler import MultipleQuestBssHandler
from .nodeexperience.handler import NodeExperienceBssHandler
from .npcgiftetc.handler import NpcGiftEtcBssHandler
from .npcsimply.handler import NpcSimplyBssHandler
from .oceansiegereviveposition.handler import OceanSiegeRevivePositionBssHandler
from .oceansiegereward.handler import OceanSiegeRewardBssHandler
from .pabr_values.handler import PabrValuesBssHandler
from .pabr_values.tables import VALUE_TABLES
from .pcgrowthdefaultcharacterkey.handler import PcGrowthDefaultCharacterKeyBssHandler
from .pcgrowthsimply.handler import PcGrowthSimplyBssHandler
from .pcroommaid.handler import PcRoomMaidBssHandler
from .petequipskill.handler import PetEquipSkillBssHandler
from .petupgraderesult.handler import PetUpgradeResultBssHandler
from .possiblefusionpet.handler import PossibleFusionPetBssHandler
from .plantexchangegroup.handler import PlantExchangeGroupBssHandler
from .plantworker.handler import PlantWorkerBssHandler
from .plantworkerpassiveskill.handler import PlantWorkerPassiveSkillBssHandler
from .plantworkerselect.handler import PlantWorkerSelectBssHandler
from .planttown.handler import PlantTownBssHandler
from .plantupgradeparam.handler import PlantUpgradeParamBssHandler
from .plantupgraderesource.handler import PlantUpgradeResourceBssHandler
from .questjournalvideoinfo.handler import QuestJournalVideoInfoBssHandler
from .questlist.handler import EVENT_PERIOD_LISTS, QUEST_LIST_LOC_TYPES, QuestListBssHandler
from .questnpc.handler import QuestNpcBssHandler
from .questprogressgroup.handler import QuestProgressGroupBssHandler
from .questrandomgroup.handler import QuestRandomGroupBssHandler
from .regiongroupinfo.handler import RegionGroupInfoBssHandler
from .regioninfo.handler import RegionInfoBssHandler
from .regioninfo_linkandcheckvalid2.handler import RegionLinkBssHandler
from .regionmapinfo.handler import RegionMapInfoBssHandler
from .rosewarrevivepositionstaticstatus.handler import RoseWarRevivePositionStaticStatusBssHandler
from .rosewarrewardstaticstatus.handler import RoseWarRewardStaticStatusBssHandler
from .servant.handler import ServantBssHandler
from .servantexperiencemaxlevel.handler import ServantExperienceMaxLevelBssHandler
from .servantmating.handler import ServantMatingBssHandler
from .skillexperiencemaxlevel.handler import SkillExperienceMaxLevelBssHandler
from .skillgroup.handler import SkillGroupBssHandler
from .specialenchantitem.handler import SpecialEnchantItemBssHandler
from .specialquestinfo.handler import SpecialQuestInfoBssHandler
from .stringtable.handler import StringTableBssHandler
from .submenu.handler import SubmenuBssHandler
from .territoryinfo.handler import TerritoryInfoBssHandler
from .titlecategory.handler import TitleCategoryBssHandler
from .totalquestcount.handler import TotalQuestCountBssHandler
from .totalquestcount.tables import QUEST_COUNT_TABLES
from .traininglevelskillstat.handler import TrainingLevelSkillStatBssHandler
from .ui_skillgroup.handler import UiSkillGroupBssHandler
from .uigrowthpasslayout.handler import UiGrowthPassLayoutBssHandler
from .usernpc.handler import UserNpcBssHandler
from .yachtautobubbletextinfo.handler import YachtAutoBubbleTextInfoHandler
from .yachtgameboardinfo.handler import YachtGameBoardInfoHandler
from .yachthandrank.handler import YachtHandRankHandler
from .yachtnpcdiceinfo.handler import YachtNpcDiceInfoBssHandler
from .zodiacsignindex.handler import ZodiacSignIndexHandler


def register_bss_handlers() -> None:
    register_handler("actionverification.bss", ActionVerificationBssHandler())
    # One layout: PABR, a count and packed quest IDs.
    for name in (
        "allquestlist.bss",
        "doguildquestlist.bss",
        "growthpassquestlist.bss",
        "olviaacademycurriculumquestlist.bss",
        "olviaacademypassquestlist.bss",
        "olviaacademyrewardquestlist.bss",
        "regionmonsterkillquestlist.bss",
        "seasonpassquestlist.bss",
        "seasonpassquestlistforcash.bss",
        "seasonpassquestlistfornormal.bss",
        "specialquestlist.bss",
        "supplyservantquestlist.bss",
    ):
        register_handler(name, AllQuestListBssHandler())
    register_handler("barter_normal.bss", BarterNormalBssHandler())
    register_handler("barter_npclist.bss", BarterNpcListBssHandler())
    register_handler("barter_special.bss", BarterSpecialBssHandler())
    register_handler("barterlifelevelinfo.bss", BarterLifeLevelInfoBssHandler())
    register_handler("bartersubgroup.bss", BarterSubGroupBssHandler())
    register_handler("bdoservanttitless.bss", BdoServantTitlesBssHandler())
    register_handler("blizzardregioninfo.bss", BlizzardRegionInfoBssHandler())
    register_handler("branchquest.bss", BranchQuestBssHandler())
    register_handler("buffsimply.bss", BuffSimplyBssHandler())
    register_handler("buildingsource.bss", BuildingSourceBssHandler())
    register_handler("carriagechar.bss", CarriageCharBssHandler())
    register_handler("charactersimply.bss", CharacterSimplyBssHandler())
    register_handler("classskilllist.bss", ClassSkillListBssHandler())
    register_handler("commonlifestatdata.bss", CommonLifeStatDataBssHandler())
    register_handler(
        "contentsgroupoptionstaticstatusmanager.bss",
        ContentsGroupOptionBssHandler(),
    )
    register_handler("cronenchant.bss", CronEnchantBssHandler())
    register_handler("cutscenecharacterdata.bss", CutsceneCharacterDataBssHandler())
    register_handler(
        "dropuihuntinggroundinfo.bss",
        DropUiHuntingGroundInfoBssHandler(),
    )
    register_handler("dropuimaincategoryinfo.bss", DropUiMainCategoryInfoBssHandler())
    register_handler("dropuisubcategoryinfo.bss", DropUiSubCategoryInfoBssHandler())
    register_handler("dropuitaginfo.bss", DropUiTagInfoBssHandler())
    register_handler("edaniaregioninfo.bss", EdaniaRegionInfoBssHandler())
    register_handler("elementalmonsterreward.bss", ElementalMonsterRewardBssHandler())
    register_handler("elementalmonsterstat.bss", ElementalMonsterStatBssHandler())
    register_handler("employeeexp.bss", EmployeeExpBssHandler())
    register_handler("employeestaticstatus.bss", EmployeeStaticStatusBssHandler())
    register_handler("enchantfailcountexpstaticstatus.bss", EnchantFailCountExpBssHandler())
    for name in EMPTY_PABR_TABLES:
        register_handler(name, EmptyTableHandler(name, parse_empty_pabr_table))
    register_handler("encyclopedia.bss", EncyclopediaBssHandler())
    register_handler("experience.bss", ExperienceBssHandler())
    register_handler("exploration.bss", ExplorationBssHandler())
    register_handler("explorepointexperiencenew.bss", ExplorePointExperienceBssHandler())
    register_handler("fairyequipskill.bss", FairyEquipSkillBssHandler())
    register_handler(
        "fairyfeedenchantfailcount.bss",
        FairyFeedEnchantFailCountBssHandler(),
    )
    register_handler("fairyupgraderate.bss", FairyUpgradeRateBssHandler())
    register_handler("feverquestdatatable.bss", FeverQuestDataTableBssHandler())
    register_handler("fevertimeskill.bss", FeverTimeSkillBssHandler())
    register_handler("fieldinfo.bss", FieldInfoBssHandler())
    register_handler("fishcompetition.bss", FishCompetitionBssHandler())
    register_handler("fitnessmaxlevel.bss", FitnessMaxLevelBssHandler())
    register_handler("groupcameradata.bss", GroupCameraDataBssHandler())
    register_handler(
        "guildhousecraftskillreverselinklist.bss",
        GuildHouseCraftSkillReverseLinkListBssHandler(),
    )
    register_handler("guildrightnewstaticstatus.bss", GuildRightNewStaticStatusBssHandler())
    register_handler(
        "hardcorecharacterstatstaticstatus.bss",
        HardcoreCharacterStatBssHandler(),
    )
    register_handler(
        "hardcorerandomspawncharacterstaticstatusmanager.bss",
        HardcoreRandomSpawnCharacterStaticStatusManagerBssHandler(),
    )
    register_handler("houseinfo.bss", HouseInfoBssHandler())
    register_handler("instancefieldmapinfo.bss", InstanceFieldMapInfoBssHandler())
    register_handler("bossinfostaicstatusmanager.bss", BossInfoStaicStatusManagerBssHandler())
    register_handler("boss_spawn.bss", BossSpawnBssHandler())
    register_handler("boss_spawnlevel.bss", BossSpawnLevelBssHandler())
    register_handler("bossmonsterhpsyncstaticstatus.bss", BossMonsterHpSyncStaticStatusBssHandler())
    register_handler("enchantactiveskillitem.bss", EnchantActiveSkillItemHandler())
    register_handler("extractblackstone.bss", ExtractBlackStoneHandler())
    register_handler("itemequipgroup.bss", ItemEquipGroupBssHandler())
    register_handler("itemexchangesource.bss", ItemExchangeSourceBssHandler())
    register_handler("itemexchangetoclassmapkey.bss", ItemExchangeToClassMapKeyBssHandler())
    register_handler("itemimprovementdefaultdisplaylist.bss", ItemImprovementDefaultDisplayListBssHandler())
    register_handler("itemlinkprice.bss", ItemLinkPriceHandler())
    register_handler("instancefieldcommonlimitentertime.bss", InstanceFieldCommonLimitEnterTimeHandler())
    register_handler("monsterbuffzone.bss", MonsterBuffZoneHandler())
    register_handler("simplesequence.bss", SimpleSequenceHandler())
    register_handler("guildbossfieldinfo.bss", GuildBossFieldInfoHandler())
    register_handler("itemmaingroup.bss", ItemMainGroupBssHandler())
    register_handler("itemmarketcategory.bss", ItemMarketCategoryBssHandler())
    register_handler("itemtradeetc.bss", ItemTradeEtcBssHandler())
    register_handler("itemviewstackenchantgroupss.bss", ItemViewStackEnchantGroupSsBssHandler())
    register_handler("jewelgroupstaticstatus.bss", JewelGroupStaticStatusBssHandler())
    register_handler(
        "jewelspecialslotsgroupstaticstatus.bss",
        JewelSpecialSlotsGroupStaticStatusBssHandler(),
    )
    register_handler(
        "knowledgelearningcharacterkey.bss",
        KnowledgeLearningCharacterKeyBssHandler(),
    )
    register_handler("lifeexpmaxlevel.bss", LifeExpMaxLevelBssHandler())
    register_handler("lightstoneset.bss", LightstoneSetBssHandler())
    register_handler("manufacture.bss", ManufactureBssHandler())
    register_handler("manufactureitemnaminginfo.bss", ManufactureItemNamingInfoBssHandler())
    register_handler("mansionlandinfo.bss", MansionLandInfoBssHandler())
    register_handler("mansionpartinfo.bss", MansionPartInfoBssHandler())
    register_handler("masterlessservantstaticstatus.bss", MasterlessServantStaticStatusBssHandler())
    # One layout for the eight life skill mastery tables, each with its own columns.
    for mastery_table in MASTERY_TABLES:
        register_handler(mastery_table.file_name, MasteryStatDataBssHandler(mastery_table))
    register_handler("menu.bss", MenuBssHandler())
    register_handler("multiplequest.bss", MultipleQuestBssHandler())
    register_handler("nodeexperience.bss", NodeExperienceBssHandler())
    register_handler("servant.bss", ServantBssHandler())
    register_handler("servantexperiencemaxlevel.bss", ServantExperienceMaxLevelBssHandler())
    register_handler("servantmating.bss", ServantMatingBssHandler())
    register_handler("npcgiftetc.bss", NpcGiftEtcBssHandler())
    register_handler("npcsimply.bss", NpcSimplyBssHandler())
    register_handler("oceansiegereviveposition.bss", OceanSiegeRevivePositionBssHandler())
    register_handler("oceansiegereward.bss", OceanSiegeRewardBssHandler())
    # One handler for the small option tables (PABR and bare), each with its own layout.
    for value_table in VALUE_TABLES:
        register_handler(value_table.file_name, PabrValuesBssHandler(value_table))
    register_handler("pcgrowthdefaultcharacterkey.bss", PcGrowthDefaultCharacterKeyBssHandler())
    register_handler("pcgrowthsimply.bss", PcGrowthSimplyBssHandler())
    register_handler("pcroommaid.bss", PcRoomMaidBssHandler())
    register_handler("petequipskill.bss", PetEquipSkillBssHandler())
    register_handler("petupgraderesult.bss", PetUpgradeResultBssHandler())
    register_handler("possiblefusionpet.bss", PossibleFusionPetBssHandler())
    register_handler("plantexchangegroup.bss", PlantExchangeGroupBssHandler())
    register_handler("plantworker.bss", PlantWorkerBssHandler())
    register_handler(
        "plantworkerpassiveskill.bss",
        PlantWorkerPassiveSkillBssHandler(),
    )
    register_handler("plantworkerselect.bss", PlantWorkerSelectBssHandler())
    register_handler("planttown.bss", PlantTownBssHandler())
    register_handler("plantupgradeparam.bss", PlantUpgradeParamBssHandler())
    register_handler("plantupgraderesource.bss", PlantUpgradeResourceBssHandler())
    register_handler("questjournalvideoinfo.bss", QuestJournalVideoInfoBssHandler())
    register_handler("questprogressgroup.bss", QuestProgressGroupBssHandler())
    register_handler("questrandomgroup.bss", QuestRandomGroupBssHandler())
    # One layout for the four quest lists, each with its own LOC type.
    for name, loc_type in QUEST_LIST_LOC_TYPES.items():
        register_handler(name, QuestListBssHandler(loc_type, has_event_period=name in EVENT_PERIOD_LISTS))
    # One layout for the NPC dialog that gives and that takes each quest.
    for name in ("acceptquest.bss", "completequest.bss"):
        register_handler(name, QuestNpcBssHandler(name))
    register_handler("regiongroupinfo.bss", RegionGroupInfoBssHandler())
    register_handler("regioninfo.bss", RegionInfoBssHandler())
    register_handler("regioninfo_linkandcheckvalid2.bss", RegionLinkBssHandler())
    register_handler("regionmapinfo.bss", RegionMapInfoBssHandler())
    register_handler("rosewarrevivepositionstaticstatus.bss", RoseWarRevivePositionStaticStatusBssHandler())
    register_handler("rosewarrewardstaticstatus.bss", RoseWarRewardStaticStatusBssHandler())
    # One layout for the combat skill point and guild point max levels.
    for name in ("skillexperiencemaxlevel.bss", "guildskillexperiencemaxlevel.bss"):
        register_handler(name, SkillExperienceMaxLevelBssHandler())
    register_handler("skillgroup.bss", SkillGroupBssHandler())
    register_handler("specialenchantitem.bss", SpecialEnchantItemBssHandler())
    register_handler("specialquestinfo.bss", SpecialQuestInfoBssHandler())
    register_handler("stringtable.bss", StringTableBssHandler())
    register_handler("submenu.bss", SubmenuBssHandler())
    register_handler("territoryinfo.bss", TerritoryInfoBssHandler())
    register_handler("titlecategory.bss", TitleCategoryBssHandler())
    # One layout for the quests per region and per quest type.
    for quest_table in QUEST_COUNT_TABLES:
        register_handler(quest_table.file_name, TotalQuestCountBssHandler(quest_table))
    register_handler("traininglevelskillstat.bss", TrainingLevelSkillStatBssHandler())
    # One layout for the three skill windows.
    for window in ("combat", "awakening", "succession"):
        register_handler(f"ui_skillgroup_{window}.bss", UiSkillGroupBssHandler())
    register_handler("uigrowthpasslayout.bss", UiGrowthPassLayoutBssHandler())
    register_handler("usernpc.bss", UserNpcBssHandler())
    register_handler("yachtautobubbletextinfo.bss", YachtAutoBubbleTextInfoHandler())
    register_handler("yachtgameboardinfo.bss", YachtGameBoardInfoHandler())
    register_handler("yachthandrank.bss", YachtHandRankHandler())
    register_handler("yachtnpcdiceinfo.bss", YachtNpcDiceInfoBssHandler())
    register_handler("zodiacsignindex.bss", ZodiacSignIndexHandler())

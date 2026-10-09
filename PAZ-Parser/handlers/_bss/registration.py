from __future__ import annotations

from bdo_preview import register_handler

from .allquestlist.handler import AllQuestListBssHandler
from .blizzardregioninfo.handler import BlizzardRegionInfoBssHandler
from .buffsimply.handler import BuffSimplyBssHandler
from .dropuihuntinggroundinfo.handler import DropUiHuntingGroundInfoBssHandler
from .dropuitaginfo.handler import DropUiTagInfoBssHandler
from .edaniaregioninfo.handler import EdaniaRegionInfoBssHandler
from .employeeexp.handler import EmployeeExpBssHandler
from .employeestaticstatus.handler import EmployeeStaticStatusBssHandler
from .exploration.handler import ExplorationBssHandler
from .fairyequipskill.handler import FairyEquipSkillBssHandler
from .fairyfeedenchantfailcount.handler import (
    FairyFeedEnchantFailCountBssHandler,
)
from .fairyupgraderate.handler import FairyUpgradeRateBssHandler
from .groupcameradata.handler import GroupCameraDataBssHandler
from .knowledgelearningcharacterkey.handler import KnowledgeLearningCharacterKeyBssHandler
from .lightstoneset.handler import LightstoneSetBssHandler
from .mansionpartinfo.handler import MansionPartInfoBssHandler
from .menu.handler import MenuBssHandler
from .npcgiftetc.handler import NpcGiftEtcBssHandler
from .npcsimply.handler import NpcSimplyBssHandler
from .pcgrowthsimply.handler import PcGrowthSimplyBssHandler
from .petequipskill.handler import PetEquipSkillBssHandler
from .plantexchangegroup.handler import PlantExchangeGroupBssHandler
from .plantworker.handler import PlantWorkerBssHandler
from .plantworkerpassiveskill.handler import PlantWorkerPassiveSkillBssHandler
from .plantworkerselect.handler import PlantWorkerSelectBssHandler
from .planttown.handler import PlantTownBssHandler
from .questjournalvideoinfo.handler import QuestJournalVideoInfoBssHandler
from .questlist.handler import EVENT_PERIOD_LISTS, QUEST_LIST_LOC_TYPES, QuestListBssHandler
from .regiongroupinfo.handler import RegionGroupInfoBssHandler
from .regioninfo.handler import RegionInfoBssHandler
from .regioninfo_linkandcheckvalid2.handler import RegionLinkBssHandler
from .skillgroup.handler import SkillGroupBssHandler
from .specialenchantitem.handler import SpecialEnchantItemBssHandler
from .stringtable.handler import StringTableBssHandler
from .submenu.handler import SubmenuBssHandler
from .territoryinfo.handler import TerritoryInfoBssHandler
from .titlecategory.handler import TitleCategoryBssHandler
from .ui_skillgroup.handler import UiSkillGroupBssHandler
from .zodiacsignindex.handler import ZodiacSignIndexHandler


def register_bss_handlers() -> None:
    register_handler("allquestlist.bss", AllQuestListBssHandler())
    register_handler("blizzardregioninfo.bss", BlizzardRegionInfoBssHandler())
    register_handler("buffsimply.bss", BuffSimplyBssHandler())
    register_handler(
        "dropuihuntinggroundinfo.bss",
        DropUiHuntingGroundInfoBssHandler(),
    )
    register_handler("dropuitaginfo.bss", DropUiTagInfoBssHandler())
    register_handler("edaniaregioninfo.bss", EdaniaRegionInfoBssHandler())
    register_handler("employeeexp.bss", EmployeeExpBssHandler())
    register_handler("employeestaticstatus.bss", EmployeeStaticStatusBssHandler())
    register_handler("exploration.bss", ExplorationBssHandler())
    register_handler("fairyequipskill.bss", FairyEquipSkillBssHandler())
    register_handler(
        "fairyfeedenchantfailcount.bss",
        FairyFeedEnchantFailCountBssHandler(),
    )
    register_handler("fairyupgraderate.bss", FairyUpgradeRateBssHandler())
    register_handler("groupcameradata.bss", GroupCameraDataBssHandler())
    register_handler(
        "knowledgelearningcharacterkey.bss",
        KnowledgeLearningCharacterKeyBssHandler(),
    )
    register_handler("lightstoneset.bss", LightstoneSetBssHandler())
    register_handler("mansionpartinfo.bss", MansionPartInfoBssHandler())
    register_handler("menu.bss", MenuBssHandler())
    register_handler("npcgiftetc.bss", NpcGiftEtcBssHandler())
    register_handler("npcsimply.bss", NpcSimplyBssHandler())
    register_handler("pcgrowthsimply.bss", PcGrowthSimplyBssHandler())
    register_handler("petequipskill.bss", PetEquipSkillBssHandler())
    register_handler("plantexchangegroup.bss", PlantExchangeGroupBssHandler())
    register_handler("plantworker.bss", PlantWorkerBssHandler())
    register_handler(
        "plantworkerpassiveskill.bss",
        PlantWorkerPassiveSkillBssHandler(),
    )
    register_handler("plantworkerselect.bss", PlantWorkerSelectBssHandler())
    register_handler("planttown.bss", PlantTownBssHandler())
    register_handler("questjournalvideoinfo.bss", QuestJournalVideoInfoBssHandler())
    # One layout for the four quest lists, each with its own LOC type.
    for name, loc_type in QUEST_LIST_LOC_TYPES.items():
        register_handler(name, QuestListBssHandler(loc_type, has_event_period=name in EVENT_PERIOD_LISTS))
    register_handler("regiongroupinfo.bss", RegionGroupInfoBssHandler())
    register_handler("regioninfo.bss", RegionInfoBssHandler())
    register_handler("regioninfo_linkandcheckvalid2.bss", RegionLinkBssHandler())
    register_handler("skillgroup.bss", SkillGroupBssHandler())
    register_handler("specialenchantitem.bss", SpecialEnchantItemBssHandler())
    register_handler("stringtable.bss", StringTableBssHandler())
    register_handler("submenu.bss", SubmenuBssHandler())
    register_handler("territoryinfo.bss", TerritoryInfoBssHandler())
    register_handler("titlecategory.bss", TitleCategoryBssHandler())
    # One layout for the three skill windows.
    for window in ("combat", "awakening", "succession"):
        register_handler(f"ui_skillgroup_{window}.bss", UiSkillGroupBssHandler())
    register_handler("zodiacsignindex.bss", ZodiacSignIndexHandler())

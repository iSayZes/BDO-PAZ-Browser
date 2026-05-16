from __future__ import annotations

from bdo_preview import register_handler

from .allquestlist.handler import AllQuestListBssHandler
from .newquest.handler import NewQuestBssHandler
from .npcgiftetc.handler import NpcGiftEtcBssHandler
from .plantworker.handler import PlantWorkerBssHandler
from .plantworkerpassiveskill.handler import PlantWorkerPassiveSkillBssHandler
from .plantworkerselect.handler import PlantWorkerSelectBssHandler
from .titlecategory.handler import TitleCategoryBssHandler
from .zodiacsignindex.handler import ZodiacSignIndexHandler


def register_bss_handlers() -> None:
    register_handler("allquestlist.bss", AllQuestListBssHandler())
    register_handler("newquest.bss", NewQuestBssHandler())
    register_handler("npcgiftetc.bss", NpcGiftEtcBssHandler())
    register_handler("plantworker.bss", PlantWorkerBssHandler())
    register_handler(
        "plantworkerpassiveskill.bss",
        PlantWorkerPassiveSkillBssHandler(),
    )
    register_handler("plantworkerselect.bss", PlantWorkerSelectBssHandler())
    register_handler("titlecategory.bss", TitleCategoryBssHandler())
    register_handler("zodiacsignindex.bss", ZodiacSignIndexHandler())

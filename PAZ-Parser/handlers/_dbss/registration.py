from __future__ import annotations

from bdo_preview import register_handler

from .title.handler import TitleDbssHandler
from .titlebuff.handler import TitleBuffListHandler, TitleBuffListOffsetHandler
from .titleoffset.handler import TitleOffsetHandler
from .mentalcard.handler import MentalCardHandler, MentalCardOffsetHandler
from .mentaltheme.handler import MentalThemeHandler, MentalThemeOffsetHandler
from .knowledgelearning.handler import (
    KnowledgeLearningHandler,
    KnowledgeLearningOffsetHandler,
)
from .npcpersonality.handler import NpcPersonalityHandler, NpcPersonalityOffsetHandler
from .quest.handler import QuestDbssHandler
from .questgroup.handler import QuestGroupDbssHandler
from .worldquest.handler import WorldQuestDbssHandler
from .npcgift.handler import (
    NpcGiftOffsetHandler,
    NpcGiftHandler,
    NpcGiftDataOffsetHandler,
    NpcGiftDataHandler,
)
from .zodiacsign.handler import (
    ZodiacSignHandler,
    ZodiacSignOffsetHandler,
    ZodiacSignOrderHandler,
    ZodiacSignOrderOffsetHandler,
)
from .plantzone.handler import PlantZoneOffsetHandler, PlantZoneHandler
from .characterspawntype.handler import (
    CharacterSpawnTypeOffsetHandler,
    CharacterSpawnTypeHandler,
)
from .characterstatic.handler import (
    CharacterStaticOffsetHandler,
    CharacterStaticHandler,
)


def register_dbss_handlers() -> None:
    register_handler("titleoffset.dbss", TitleOffsetHandler())
    register_handler("title.dbss", TitleDbssHandler())
    register_handler("titlebufflistoffset.dbss", TitleBuffListOffsetHandler())
    register_handler("titlebufflist.dbss", TitleBuffListHandler())
    register_handler("mentalcardoffset.dbss", MentalCardOffsetHandler())
    register_handler("mentalcard.dbss", MentalCardHandler())
    register_handler("mentalthemeoffset.dbss", MentalThemeOffsetHandler())
    register_handler("mentaltheme.dbss", MentalThemeHandler())
    register_handler("knowledgelearningoffset.dbss", KnowledgeLearningOffsetHandler())
    register_handler("knowledgelearning.dbss", KnowledgeLearningHandler())
    register_handler("npcpersonalityoffset.dbss", NpcPersonalityOffsetHandler())
    register_handler("npcpersonality.dbss", NpcPersonalityHandler())
    register_handler("quest.dbss", QuestDbssHandler())
    register_handler("questgroup.dbss", QuestGroupDbssHandler())
    register_handler("worldquest.dbss", WorldQuestDbssHandler())
    register_handler("npcgiftoffset.dbss", NpcGiftOffsetHandler())
    register_handler("npcgift.dbss", NpcGiftHandler())
    register_handler("npcgiftdataoffset.dbss", NpcGiftDataOffsetHandler())
    register_handler("npcgiftdata.dbss", NpcGiftDataHandler())
    register_handler("zodiacsignoffset.dbss", ZodiacSignOffsetHandler())
    register_handler("zodiacsign.dbss", ZodiacSignHandler())
    register_handler("zodiacsignorderoffset.dbss", ZodiacSignOrderOffsetHandler())
    register_handler("zodiacsignorder.dbss", ZodiacSignOrderHandler())
    register_handler("plantzoneoffset.dbss", PlantZoneOffsetHandler())
    register_handler("plantzone.dbss", PlantZoneHandler())
    register_handler("characterspawntypeoffset.dbss", CharacterSpawnTypeOffsetHandler())
    register_handler("characterspawntype.dbss", CharacterSpawnTypeHandler())
    register_handler("characterstaticoffset.dbss", CharacterStaticOffsetHandler())
    register_handler("characterstatic.dbss", CharacterStaticHandler())

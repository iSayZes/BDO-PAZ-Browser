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
from .zodiacsign.handler import (
    ZodiacSignHandler,
    ZodiacSignOffsetHandler,
    ZodiacSignOrderHandler,
    ZodiacSignOrderOffsetHandler,
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
    register_handler("zodiacsignoffset.dbss", ZodiacSignOffsetHandler())
    register_handler("zodiacsign.dbss", ZodiacSignHandler())
    register_handler("zodiacsignorderoffset.dbss", ZodiacSignOrderOffsetHandler())
    register_handler("zodiacsignorder.dbss", ZodiacSignOrderHandler())

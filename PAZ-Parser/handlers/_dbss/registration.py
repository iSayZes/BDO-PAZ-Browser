from __future__ import annotations

from bdo_preview import register_handler

from .title.handler import TitleDbssHandler
from .titlebuff.handler import TitleBuffListHandler, TitleBuffListOffsetHandler
from .titleoffset.handler import TitleOffsetHandler
from .mentalcard.handler import MentalCardHandler, MentalCardOffsetHandler
from .knowledgelearning.handler import (
    KnowledgeLearningHandler,
    KnowledgeLearningOffsetHandler,
)
from .npcpersonality.handler import NpcPersonalityHandler, NpcPersonalityOffsetHandler
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
    register_handler("knowledgelearningoffset.dbss", KnowledgeLearningOffsetHandler())
    register_handler("knowledgelearning.dbss", KnowledgeLearningHandler())
    register_handler("npcpersonalityoffset.dbss", NpcPersonalityOffsetHandler())
    register_handler("npcpersonality.dbss", NpcPersonalityHandler())
    register_handler("zodiacsignoffset.dbss", ZodiacSignOffsetHandler())
    register_handler("zodiacsign.dbss", ZodiacSignHandler())
    register_handler("zodiacsignorderoffset.dbss", ZodiacSignOrderOffsetHandler())
    register_handler("zodiacsignorder.dbss", ZodiacSignOrderHandler())

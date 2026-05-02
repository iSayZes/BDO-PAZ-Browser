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


def register_dbss_handlers() -> None:
    register_handler("titleoffset.dbss", TitleOffsetHandler())
    register_handler("title.dbss", TitleDbssHandler())
    register_handler("titlebufflistoffset.dbss", TitleBuffListOffsetHandler())
    register_handler("titlebufflist.dbss", TitleBuffListHandler())
    register_handler("mentalcardoffset.dbss", MentalCardOffsetHandler())
    register_handler("mentalcard.dbss", MentalCardHandler())
    register_handler("knowledgelearningoffset.dbss", KnowledgeLearningOffsetHandler())
    register_handler("knowledgelearning.dbss", KnowledgeLearningHandler())

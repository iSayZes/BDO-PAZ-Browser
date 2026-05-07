from __future__ import annotations

from bdo_preview import register_handler

from .allquestlist.handler import AllQuestListBssHandler
from .titlecategory.handler import TitleCategoryBssHandler
from .zodiacsignindex.handler import ZodiacSignIndexHandler


def register_bss_handlers() -> None:
    register_handler("allquestlist.bss", AllQuestListBssHandler())
    register_handler("titlecategory.bss", TitleCategoryBssHandler())
    register_handler("zodiacsignindex.bss", ZodiacSignIndexHandler())

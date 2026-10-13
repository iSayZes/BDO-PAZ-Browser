from __future__ import annotations

from bdo_preview import register_handler

from .aiscript.handler import AiScriptHandler


def register_ai_handlers() -> None:
    # Every `.ai` file in the client is an AI script (character/aiscript/,
    # character/ai_check/, character/pcaiscript/), so the extension is the key.
    register_handler(".ai", AiScriptHandler())

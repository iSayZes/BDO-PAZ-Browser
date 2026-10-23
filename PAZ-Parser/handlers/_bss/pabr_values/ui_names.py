"""Cell text of the quiz, photo mode and world map option tables (`ui_tables.py`)."""

from __future__ import annotations

from types import MappingProxyType

from _common.enum_name import enum_name
from _common.string_hash import ascii_key_hash


# eQuizAnswerType in value order without the prefix
# (panel_event_quizgm_all.luac, client 3482): None, OX_O, OX_X.
QUIZ_ANSWER_TYPES: tuple[str, ...] = ("None", "O", "X")
# The `ActionName` values of the Social_Quiz sheet of a private server on
# client 1784; on client 3482 every quiz action hash is the hash of one of
# them (quizactionstaticstatus_bss.md, Field Names).
QUIZ_ACTION_NAMES: tuple[str, ...] = (
    "SOCIAL_PutUP_R_Start",
    "SOCIAL_PutUP_R_Ing",
    "SOCIAL_PutUP_L_Start",
    "SOCIAL_PutUP_L_Ing",
)
_QUIZ_ACTIONS = MappingProxyType({ascii_key_hash(name): name for name in QUIZ_ACTION_NAMES})


def quiz_answer_text(answer_type: int) -> str:
    """`1 O`: an answer type and its `eQuizAnswerType` name."""
    return f"{answer_type} {enum_name(QUIZ_ANSWER_TYPES, answer_type)}"


def quiz_action_text(action_hash: int) -> str:
    """The sheet's action name of a hash, else the hash as `0x31C83250`."""
    return _QUIZ_ACTIONS.get(action_hash, f"0x{action_hash:08X}")

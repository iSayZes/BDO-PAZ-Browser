"""Display text of a `challenge.dbss` row: enum names, texts and rewards.

Kept out of `handler.py` so tests can import it without loading the handler
registry.
"""

from __future__ import annotations

from collections.abc import Sequence

from _common.challenge import DESCRIPTION_SLOT, TITLE_SLOT, challenge_tagged
from _common.enum_name import enum_name
from _common.html import e, html_list_cell
from _common.inline_text import decode_inline_text
from _common.quest.reward_entry import RewardEntry
from _common.quest.reward_text import reward_text, rewards_cell


# CppEnums.ChallengeType of client 3482 (global_define_cpp_enum.luac).
CHALLENGE_TYPE_NAMES = (
    "Benefit",
    "Event",
    "ShortTerm",
    "LongTerm",
    "PcRoom",
    "EnchantPcRoomCount",
    "EnchantValuePackCount",
    "PremiumPackage",
    "Coupon",
)
# gc::CompleteChallengeType of the 2016 client; later values have no name.
COMPLETE_CONDITION_TYPE_NAMES = (
    "PastMinute",
    "Contact",
    "AchieveLevel",
    "FirstLogin",
    "AchieveLifeLevel",
    "PlayTime",
    "PcRoomPlayTime",
)
# gc::ChallengeResetType of the 2016 client; later values have no name.
RESET_TYPE_NAMES = ("None", "Immediately", "Day", "CumulatedMinute")

# reward_type of a `coupon(n)` reward; `n` is the u16 at +0x2F of the entry,
# which the shared reader keeps as the hex text `unknown_2f`.
REWARD_COUPON = 6


def challenge_type_name(value: int) -> str:
    return enum_name(CHALLENGE_TYPE_NAMES, value)


def complete_condition_type_name(value: int) -> str:
    return enum_name(COMPLETE_CONDITION_TYPE_NAMES, value)


def reset_type_name(value: int) -> str:
    return enum_name(RESET_TYPE_NAMES, value)


def _tagged(challenge_key: int, slot: int, text_kr: str) -> str:
    """The LOC text with its PA tags, else the Korean with its `\\n` escapes decoded."""
    return challenge_tagged(challenge_key, slot) or decode_inline_text(text_kr)


def title_tagged(challenge_key: int, title_kr: str) -> str:
    return _tagged(challenge_key, TITLE_SLOT, title_kr)


def description_tagged(challenge_key: int, description_kr: str) -> str:
    return _tagged(challenge_key, DESCRIPTION_SLOT, description_kr)


def coupon_number(reward: RewardEntry) -> int:
    """The `coupon(n)` argument of a coupon reward."""
    return int.from_bytes(bytes.fromhex(reward["unknown_2f"]), "little")


def challenge_reward_texts(rewards: Sequence[RewardEntry], coupon_label: str) -> list[str]:
    """The text of every reward, in entry order; a coupon as `coupon_label` filled with its number."""
    texts = []
    for reward in rewards:
        if reward["reward_type"] == REWARD_COUPON:
            texts.append(coupon_label.format(number=coupon_number(reward)))
        elif (text := reward_text(reward)) is not None:
            texts.append(text)
    return texts


def challenge_rewards_cell(rewards: Sequence[RewardEntry], coupon_label: str) -> str:
    """The rewards with icons, then the coupons as text, comma-separated, or ''."""
    coupons = [coupon_label.format(number=coupon_number(r)) for r in rewards if r["reward_type"] == REWARD_COUPON]
    cells = [cell for cell in (rewards_cell(rewards),) if cell]
    return html_list_cell([*cells, *(e(text) for text in coupons)])

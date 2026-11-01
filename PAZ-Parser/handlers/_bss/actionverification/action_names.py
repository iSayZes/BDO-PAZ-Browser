"""Names for the `action_hash` values of `actionverification.bss`.

The file stores each action name only as its `ascii_key_hash`. These are the
29 `ActionName` values of the `ActionVerification_Table` sheet of a private
server on client 1784; on client 3474 every `action_hash` in the file is the
hash of one of them. A hash that is not one of them gets no name.
See "Action Names" in docs/file-formats/bss/actionverification_bss.md.
"""

from __future__ import annotations

from types import MappingProxyType

from _common.string_hash import ascii_key_hash


SHEET_ACTION_NAMES = (
    "BT_WAIT",
    "BT_skill_SkyFall",
    "BT_skill_ThrustAndSmash_AttQ1",
    "BT_ROLL_L",
    "BT_ROLL_R",
    "BT_ROLL_B",
    "SHADOW_ATTACK_1",
    "SHADOW_ATTACK_1_2",
    "SHADOW_ATTACK_2",
    "SHADOW_ATTACK_3",
    "SHADOW_ATTACK_4",
    "SHADOW_ATTACK_5",
    "SHADOW_ATTACK_6",
    "SHADOW_ATTACK_F_1",
    "SHADOW_ATTACK_F_2",
    "SHADOW_ATTACK_F_3",
    "SHADOW_ATTACK_F_4",
    "SHADOW_ATTACK_F_5",
    "SHADOW_ATTACK_L_1",
    "SHADOW_ATTACK_L_1_C",
    "SHADOW_ATTACK_L_2",
    "SHADOW_ATTACK_L_3",
    "SHADOW_ATTACK_R_1",
    "SHADOW_ATTACK_R_1_C",
    "SHADOW_ATTACK_R_2",
    "SHADOW_ATTACK_R_3",
    "SHADOW_DASHATTACK_1",
    "SHADOW_JUMP_ATTACK",
    "SHADOW_DASHJUMP_ATTACK",
)

ACTION_NAMES = MappingProxyType({ascii_key_hash(name): name for name in SHEET_ACTION_NAMES})


def action_name(action_hash: int) -> str:
    """The action name whose hash is `action_hash`, or '' when none of the sheet names has it."""
    return ACTION_NAMES.get(action_hash, "")

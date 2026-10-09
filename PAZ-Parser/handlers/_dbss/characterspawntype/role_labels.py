"""Display names of `CppEnums.SpawnType` roles, shared by every table that shows one.

A role is named by its `roleLabels` entry in this package's `lang/<lang>.json`
(roles without a navi label, or where it is too vague), else its English navi
label from LOC, else its client enum name.
"""

from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from _common.enum_name import enum_name
from _common.lang import load_handler_strings
from .navi_labels import navi_label
from .parser import SPAWN_TYPE_NAMES

_LANG_DIR = Path(__file__).parent / "lang"


def spawn_type_name(spawn_type: int) -> str:
    """The client enum name, or the bare value outside the enum."""
    return enum_name(SPAWN_TYPE_NAMES, spawn_type)


def role_label_overrides(lang: str) -> dict[str, str]:
    """`enum name -> label` for the roles whose label replaces the navi label."""
    return load_handler_strings(lang, _LANG_DIR)["roleLabels"]


def role_label(spawn_type: int, overrides: Mapping[str, str]) -> str:
    """The display name of a role: override, else navi label, else enum name."""
    name = spawn_type_name(spawn_type)
    return overrides.get(name) or navi_label(spawn_type) or name


def role_tooltip(spawn_type: int) -> str:
    """Tooltip text naming the role's enum name and value, e.g. `Stable, SpawnType 7`."""
    return f"{spawn_type_name(spawn_type)}, SpawnType {spawn_type}"

"""Fitness type names, shared by `fitnesslevel.dbss` and `fitnessmaxlevel.bss`.

The names live in the `fitnessTypes` strings of this package's `lang/` files,
keyed by fitness type (`0` Breath, `1` Strength, `2` Health).
"""

from __future__ import annotations

from pathlib import Path

from _common.lang import load_handler_strings


_LANG_DIR = Path(__file__).parent / "lang"


def fitness_type_names(lang: str) -> dict[str, str]:
    """Fitness type (as a string key) -> its name in `lang`."""
    return load_handler_strings(lang, _LANG_DIR)["fitnessTypes"]


def fitness_type_name(names: dict[str, str], fitness_type: int) -> str:
    """The name of `fitness_type`, or the raw number for a type with no name."""
    return names.get(str(fitness_type), str(fitness_type))

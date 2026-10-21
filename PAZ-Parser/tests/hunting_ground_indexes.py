"""The `dropuihuntinggroundinfo.bss` lookup indexes, built from the fixtures for handler cases.

A `HandlerCase` takes these functions as `lookup_indexes` sources, so the
fixture loads when the case runs. Each index is built once per process.
"""

from __future__ import annotations

from functools import cache

from _bss.dropuihuntinggroundinfo.parser import (
    build_character_hunting_ground_index,
    build_hunting_ground_name_kr_index,
)

from .fixtures import load_binary_fixture

_DROPUIHUNTINGGROUNDINFO = "dropuihuntinggroundinfo.bss"


@cache
def character_hunting_ground_index() -> dict[int, tuple[int, ...]]:
    """`IndexKind.CHARACTER_HUNTING_GROUNDS` of the fixture client."""
    return build_character_hunting_ground_index(load_binary_fixture(_DROPUIHUNTINGGROUNDINFO))


@cache
def hunting_ground_name_kr_index() -> dict[int, str]:
    """`IndexKind.HUNTING_GROUND_NAME_KR` of the fixture client."""
    return build_hunting_ground_name_kr_index(load_binary_fixture(_DROPUIHUNTINGGROUNDINFO))

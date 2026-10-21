"""The `characterstatic.dbss` lookup indexes, built from the fixtures for handler cases.

A `HandlerCase` takes these functions as `lookup_indexes` sources, so the
fixtures load when the case runs. Each index is built once per process.
"""

from __future__ import annotations

from functools import cache

from _dbss.characterstatic.parser import (
    build_character_group_index,
    build_character_name_kr_index,
    build_character_title_kr_index,
)

from .fixtures import load_binary_fixture

_CHARACTERSTATIC = "characterstatic.dbss"
_CHARACTERSTATIC_OFFSET = "characterstaticoffset.dbss"


@cache
def character_name_kr_index() -> dict[int, str]:
    """`IndexKind.CHARACTER_NAME_KR` of the fixture client."""
    return build_character_name_kr_index(
        load_binary_fixture(_CHARACTERSTATIC), load_binary_fixture(_CHARACTERSTATIC_OFFSET)
    )


@cache
def character_title_kr_index() -> dict[int, str]:
    """`IndexKind.CHARACTER_TITLE_KR` of the fixture client."""
    return build_character_title_kr_index(
        load_binary_fixture(_CHARACTERSTATIC), load_binary_fixture(_CHARACTERSTATIC_OFFSET)
    )


@cache
def character_group_index() -> dict[int, tuple[int, ...]]:
    """`IndexKind.CHARACTER_GROUP_MEMBERS` of the fixture client."""
    return build_character_group_index(
        load_binary_fixture(_CHARACTERSTATIC), load_binary_fixture(_CHARACTERSTATIC_OFFSET)
    )

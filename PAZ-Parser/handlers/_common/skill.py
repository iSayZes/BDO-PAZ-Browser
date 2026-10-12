"""Skill keys and skill names shared by the skill tables.

Every table in the skill cluster (`skill.dbss`, `skilltype.dbss`,
`skillgroup.bss`, `ui_skillgroup_*.bss`) keys a skill rank by

    skill_key = skill_no << 16 | level

and LOC type 10 names a skill by its number alone, so every rank of one skill
shares a name. LOC type 13 holds each rank's own text, keyed by skill number
and level. See docs/file-formats/skill_dbss.md.
"""

from __future__ import annotations

from collections.abc import Iterable

from _common.loc import LOC_NULL, loc_lookup, loc_tagged
from _common.pa_text import strip_pa_tags
from _common.lookup_index import IndexKind, lookup

LOC_SKILL = 10
# LOC type 10 holds the skill name at str_id4 0 and its description at 1.
_LOC_DESCRIPTION_ID4 = 1
# LOC type 13, keyed (skill_no, level): the English of a rank's skill.dbss
# `description`.
LOC_SKILL_RANK = 13
# Literals stored instead of a description: skill.dbss keeps UNKNOWN and
# <null>, and LOC type 13 keeps "0" where the Korean text is UNKNOWN.
_PLACEHOLDERS = frozenset({"UNKNOWN", LOC_NULL, "0"})
# Between the skill's text and the rank's own text in one description.
_PART_SEPARATOR = "\n\n"

_LEVEL_MASK = 0xFFFF
_SKILL_NO_SHIFT = 16


def skill_key(skill_no: int, level: int) -> int:
    """The skill key `skill_no << 16 | level` of one skill rank."""
    return skill_no << _SKILL_NO_SHIFT | level


def split_skill_key(skill_key: int) -> tuple[int, int]:
    """`(skill_no, level)` of a skill key."""
    return skill_key >> _SKILL_NO_SHIFT, skill_key & _LEVEL_MASK


def skill_name_tagged(skill_no: int) -> str:
    """`skill_name` with its PA tags kept (Prime skills are orange), for `pa_fields`."""
    name = loc_tagged(LOC_SKILL, skill_no)
    if strip_pa_tags(name).strip():
        return name
    korean = lookup(IndexKind.SKILL_NAME_KR, skill_no)
    return korean if isinstance(korean, str) else ""


def skill_name(skill_no: int) -> str:
    """LOC type 10 name of a skill, then its Korean `skilltype.dbss` name, else ''.

    The Korean names come from the `SKILL_NAME_KR` lookup index, so a table
    needs no `skilltype.dbss` companion for them.
    """
    return strip_pa_tags(skill_name_tagged(skill_no)).strip()


def _is_text(tagged: str) -> bool:
    """True unless `tagged` is blank or a placeholder once its tags are gone."""
    plain = strip_pa_tags(tagged).strip()
    return bool(plain) and plain not in _PLACEHOLDERS


def _plain_words(tagged: str) -> str:
    return " ".join(strip_pa_tags(tagged).split())


def skill_description_tagged(skill_no: int, level: int, description_kr: str) -> str:
    """A rank's description with its PA tags, for `pa_fields`, or ''.

    The skill's LOC type 10 text, then the rank's own LOC type 13 text when it
    says something else; guild skills keep a usage hint in the first and
    their effect in the second. Without either, the rank's Korean
    `skill.dbss` text, the source of type 13. See
    docs/file-formats/skill_dbss.md.
    """
    skill_text = loc_tagged(LOC_SKILL, skill_no, _LOC_DESCRIPTION_ID4)
    rank_text = loc_lookup(LOC_SKILL_RANK, skill_no, level).strip()
    parts = [text for text in (skill_text, rank_text) if _is_text(text)]
    if len(parts) == 2 and _plain_words(parts[0]) == _plain_words(parts[1]):
        parts = parts[:1]
    if parts:
        return _PART_SEPARATOR.join(parts)
    korean = description_kr.strip()
    return korean if _is_text(korean) else ""


def skill_description(skill_no: int, level: int, description_kr: str) -> str:
    """`skill_description_tagged` as plain text."""
    return strip_pa_tags(skill_description_tagged(skill_no, level, description_kr)).strip()


def _skill_buffs(skill_key: int) -> tuple[int, ...]:
    linked = lookup(IndexKind.SKILL_BUFFS, skill_key)
    return linked if isinstance(linked, tuple) else ()


def skill_buff_ids(skill_keys: Iterable[int]) -> list[int]:
    """Buffs the given skills apply, in skill then slot order, each once.

    Read from the `SKILL_BUFFS` lookup index, so empty when it is not loaded.
    """
    return list(dict.fromkeys(buff_id for key in skill_keys for buff_id in _skill_buffs(key)))

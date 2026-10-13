"""Section titles and developer notes from the comments of client XML scripts
(`.ai`, `.cl`).

A comment with `■` or a run of three `-`, `=`, `*`, `#` or `~` titles a
section (`<!-- ■■■ 비전투 상태 ■■■ -->`, `<!-- 비 전투 상태 ----- -->`); the
decoration is stripped. The last plain comment above an element is its note.
"""
from __future__ import annotations

import re

_DECORATION = re.compile(r"■|[-=*#~]{3,}")
_DECORATION_CHARS = "■□◆◇●○★☆▶▷◀◁-=*#~ "


def section_and_note(comments: tuple[str, ...], section: str) -> tuple[str, str]:
    """(section, note) of an element with these comments above it.

    `section` is the title in force before them; a title without text (a
    bare `------` line) keeps it.
    """
    note = ""
    for comment in comments:
        if _DECORATION.search(comment):
            title = comment.strip(_DECORATION_CHARS)
            if title:
                section, note = title, ""
        else:
            note = comment
    return section, note

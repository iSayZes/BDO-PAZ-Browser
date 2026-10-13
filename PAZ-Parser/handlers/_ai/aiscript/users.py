"""The characters that run a script.

`characterstatic.dbss` names each character's script by file stem, without a
folder (`Monsters_Main_Manager` for `monsters_main_manager.ai`); the
CHARACTER_AI_SCRIPT index holds that name per character ID. A stem the client
ships in two folders (`character/ai_check/before/` copies) lists the same
characters in both files.
"""
from __future__ import annotations

from pathlib import PurePosixPath

from _common.character import character_name
from _common.lookup_index import IndexKind, index_entries


def script_users(internal_path: str) -> list[tuple[int, str]]:
    """(character ID, name) of every character whose script is this file, by ID.

    The name is '' when LOC is not loaded or has none; the list is empty when
    the index is not loaded.
    """
    stem = PurePosixPath(internal_path).stem.lower()
    ids = sorted(
        character_id
        for character_id, script in index_entries(IndexKind.CHARACTER_AI_SCRIPT).items()
        if isinstance(script, str) and script.lower() == stem
    )
    return [(character_id, character_name(character_id)) for character_id in ids]

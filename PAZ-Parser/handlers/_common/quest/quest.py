from __future__ import annotations

from _common.loc import loc_lookup, strip_pa_tags


def quest_title(quest_chain_id: int, quest_id: int) -> str:
    return strip_pa_tags(loc_lookup(18, quest_chain_id, quest_id, 0, 0)).strip()

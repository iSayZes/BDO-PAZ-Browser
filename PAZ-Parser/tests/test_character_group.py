from __future__ import annotations

import pytest

from _common.character_group import character_group_cell, character_group_names, character_group_text
from _common.lookup_index import IndexKind, clear_indexes, init_index
from _common.quest.kill_monster_group import (
    KillMonsterGroup,
    kill_monster_group_texts,
    kill_monster_groups,
    kill_monster_groups_cell,
)

# Character IDs no LOC names, so the results do not depend on a loaded LOC.
_WOLF, _WOLF_COPY, _BEAR, _UNNAMED = 0xFFF0, 0xFFF1, 0xFFF2, 0xFFF3
_GROUP = 185
_EMPTY_GROUP = 186


@pytest.fixture(autouse=True)
def _indexes():
    clear_indexes()
    init_index(IndexKind.CHARACTER_GROUP_MEMBERS, {_GROUP: (_WOLF, _WOLF_COPY, _BEAR, _UNNAMED)})
    init_index(IndexKind.CHARACTER_NAME_KR, {_WOLF: "서리 늑대", _WOLF_COPY: "서리 늑대", _BEAR: "겨울 곰"})
    yield
    clear_indexes()


def test_group_names_are_distinct_with_the_id_for_an_unnamed_member() -> None:
    assert character_group_names(_GROUP) == ["서리 늑대", "겨울 곰", str(_UNNAMED)]
    assert character_group_names(_EMPTY_GROUP) == []


def test_group_text_names_every_member_after_its_label() -> None:
    assert character_group_text(_GROUP) == f"{_GROUP}: 서리 늑대, 겨울 곰, {_UNNAMED}"
    assert character_group_text(_GROUP, "label") == f"label: 서리 늑대, 겨울 곰, {_UNNAMED}"
    assert character_group_text(_EMPTY_GROUP) == str(_EMPTY_GROUP)


def test_group_cell_cuts_the_names_after_max_items() -> None:
    cell = character_group_cell(_GROUP, 1)

    assert cell.startswith(f"{_GROUP}: 서리 늑대, ")
    assert "(+2)" in cell
    assert character_group_cell(_EMPTY_GROUP, 1) == str(_EMPTY_GROUP)


def test_calls_are_read_in_any_case_once_each() -> None:
    script = f"killMonsterGroup({_GROUP},10);KillMonsterGroup(84, 5);killmonstergroup({_GROUP},10);"

    assert kill_monster_groups(script) == [KillMonsterGroup(_GROUP, 10), KillMonsterGroup(84, 5)]
    assert kill_monster_groups("killmonster(7,1);") == []


def test_calls_show_their_count_and_members() -> None:
    calls = kill_monster_groups(f"killMonsterGroup({_GROUP},1000);killMonsterGroup({_EMPTY_GROUP},3);")

    assert kill_monster_group_texts(calls) == [
        f"{_GROUP} (x1,000): 서리 늑대, 겨울 곰, {_UNNAMED}",
        f"{_EMPTY_GROUP} (x3)",
    ]
    assert kill_monster_groups_cell(calls, 3).split("<br>") == [
        f"{_GROUP} (x1,000): 서리 늑대, 겨울 곰, {_UNNAMED}",
        f"{_EMPTY_GROUP} (x3)",
    ]
    assert kill_monster_groups_cell([], 3) == ""

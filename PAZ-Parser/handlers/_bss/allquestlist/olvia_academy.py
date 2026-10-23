"""The joins between the three Olvia Academy quest lists and the two academy tables.

`olviaacademycurriculumss.bss` names the subject or reward group of each
curriculum and reward quest, `olviaacademypassstaticstatusmanager.bss` the
pass tab and step of each pass quest. A `QuestPlaces` reads one of them for
its quest list: the list view shows each quest's place as a link to its row
there, and the two academy views link each quest back to its list row
(`quest_link`).
"""

from __future__ import annotations

from collections.abc import Callable, Mapping
from dataclasses import dataclass

from _common.enum_name import enum_name
from _common.html import record_link
from _common.quest.quest import quest_title, split_packed_quest_id
from _common.string_hash import key_hash
from _bss.olviaacademycurriculumss.parser import (
    CURRICULUM_SECTION,
    FILE_NAME as CURRICULUM_FILE,
    parse_curriculum_records,
)
from _bss.olviaacademypassstaticstatusmanager.parser import (
    FILE_NAME as PASS_FILE,
    PASS_TYPE_NAMES,
    parse_pass_records,
)
from _bss.stringtable.parser import RESOURCE_SHEET
from _bss.stringtable.text import ui_hash_text


FOLDER = "gamecommondata/binary"
CURRICULUM_LIST = "olviaacademycurriculumquestlist.bss"
PASS_LIST = "olviaacademypassquestlist.bss"
REWARD_LIST = "olviaacademyrewardquestlist.bss"
# The field of a quest list record that holds its packed quest ID.
QUEST_FIELD = "packed_quest_id"
# The fields the place links open: a curriculum or reward row by its key, a pass step by its base quest.
CURRICULUM_REF_FIELD = "row_ref"
PASS_REF_FIELD = "base_quest"
_LINK_CLASS = "record-link"
_PLACE_SEPARATOR = " / "


def resource_text(key: str) -> str:
    """LOC text of a RESOURCE sheet key, else the key itself."""
    if not key:
        return ""
    return ui_hash_text(RESOURCE_SHEET, key_hash(key)) or key


def quest_text(packed_quest_id: int) -> str:
    """A packed quest ID as `chain/quest` and its LOC title: `2310/1 [Combat Course] Sign Up for Course`."""
    chain, quest = split_packed_quest_id(packed_quest_id)
    title = quest_title(chain, quest)
    return f"{chain}/{quest} {title}" if title else f"{chain}/{quest}"


def quest_link(packed_quest_id: int, list_name: str) -> str:
    """A button showing the quest that opens `list_name` on its row."""
    return record_link(quest_text(packed_quest_id), f"{FOLDER}/{list_name}", QUEST_FIELD, packed_quest_id, _LINK_CLASS)


def pass_type_name(pass_type: int) -> str:
    """The Lua name of a pass type without its prefix (`Collect`), or the bare value."""
    return enum_name(PASS_TYPE_NAMES, pass_type)


@dataclass(frozen=True)
class QuestPlace:
    """Where one quest sits: the text the list shows and the value of the target row's link field."""

    text: str
    ref: str | int


@dataclass(frozen=True)
class QuestPlaces:
    """The table that places the quests of one list, and how it reads.

    `column` is the lang column key of the place column, `target_field` the
    field of the target's records the links open by.
    """

    file_name: str
    column: str
    target_field: str
    read: Callable[[bytes], Mapping[int, QuestPlace]]

    @property
    def path(self) -> str:
        return f"{FOLDER}/{self.file_name}"


def _curriculum_place(record: dict) -> str:
    if record["section"] == CURRICULUM_SECTION:
        parent, own = record["curriculum_title"], record["subject_title"]
    else:
        parent, own = record["reward_title"], record["reward_group_title"]
    return f"{resource_text(parent)}{_PLACE_SEPARATOR}{resource_text(own)}"


def curriculum_places(data: bytes) -> dict[int, QuestPlace]:
    """Each curriculum and reward quest's subject or reward group, from `olviaacademycurriculumss.bss`."""
    places: dict[int, QuestPlace] = {}
    for record in parse_curriculum_records(data):
        place = QuestPlace(_curriculum_place(record), record[CURRICULUM_REF_FIELD])
        for quest in record["quests"]:
            places.setdefault(quest, place)
    return places


def pass_places(data: bytes) -> dict[int, QuestPlace]:
    """Each pass quest's pass type and step, from `olviaacademypassstaticstatusmanager.bss`."""
    places: dict[int, QuestPlace] = {}
    for record in parse_pass_records(data):
        text = f"{pass_type_name(record['pass_type'])}{_PLACE_SEPARATOR}{record['quest_index'] + 1}"
        place = QuestPlace(text, record[PASS_REF_FIELD])
        places.setdefault(record["base_quest"], place)
        places.setdefault(record["pass_quest"], place)
    return places


CURRICULUM_PLACES = QuestPlaces(CURRICULUM_FILE, "course", CURRICULUM_REF_FIELD, curriculum_places)
REWARD_PLACES = QuestPlaces(CURRICULUM_FILE, "familyReward", CURRICULUM_REF_FIELD, curriculum_places)
PASS_PLACES = QuestPlaces(PASS_FILE, "passStep", PASS_REF_FIELD, pass_places)
# The place source of each Olvia Academy quest list.
LIST_PLACES: dict[str, QuestPlaces] = {
    CURRICULUM_LIST: CURRICULUM_PLACES,
    PASS_LIST: PASS_PLACES,
    REWARD_LIST: REWARD_PLACES,
}

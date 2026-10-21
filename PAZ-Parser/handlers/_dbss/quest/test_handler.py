from __future__ import annotations

from dataclasses import replace
from html import escape
from typing import Any

import pytest

from bdo_models import PazEntry
from table_sort import SORT_DESC, TableSort, sort_order_by_values
from tests.framework import (
    DeclaredCountTest,
    HandlerCase,
    HandlerResult,
    RangeTest,
    SchemaTest,
    TargetTest,
    case_id,
    header_count,
    run_case,
)
from tests.character_indexes import character_group_index
from tests.runner import load_case

from _common.lookup_index import IndexKind
from _common.quest.reward_entry import (
    REWARD_EXP,
    REWARD_EXP_GRADE,
    REWARD_EXPLORE_EXP,
    REWARD_FAMILY_STAT,
    REWARD_FEVER_POINT,
    REWARD_INTIMACY,
    REWARD_ITEM,
    REWARD_KNOWLEDGE,
    REWARD_LIFE_EXP,
    REWARD_SEASON_REWARD,
    REWARD_SKILL_EXP,
)

# The head members a reward leaves at these values unless its type uses them.
_UNSET_MEMBERS = {
    "experience": 0,
    "skill_experience": 0,
    "product_experience": 0,
    "life_experience_type": 15,
    "life_experience": 0,
    "item_key": 0,
    "item_count": 0,
    "intimacy_character": 0,
    "intimacy_value": 0,
    "mental_card_key": 0,
    "exp_grade": 0,
    "max_fever_point": 0,
    "add_fever_point": 0,
    "season_no": 0,
    "explore_exp": 0,
}
# gc::RewardType -> the members that hold its reward.
_TYPE_MEMBERS_2016 = {
    REWARD_EXP: {"experience"},
    REWARD_SKILL_EXP: {"skill_experience"},
    REWARD_LIFE_EXP: {"life_experience_type", "life_experience"},
    REWARD_ITEM: {"item_key", "item_count"},
    REWARD_INTIMACY: {"intimacy_character", "intimacy_value"},
}
_TYPE_MEMBERS = {
    **_TYPE_MEMBERS_2016,
    REWARD_KNOWLEDGE: {"mental_card_key"},
    REWARD_EXP_GRADE: {"exp_grade"},
    REWARD_EXPLORE_EXP: {"explore_exp"},
    REWARD_FEVER_POINT: {"max_fever_point", "add_fever_point"},
    REWARD_SEASON_REWARD: {"season_no"},
}


def _quest_record(record: dict) -> dict:
    loc_texts = record.get("loc_texts_en", [])
    mapped = dict(record)
    mapped["title_en"] = loc_texts[0] if loc_texts else ""
    mapped["objective_en"] = loc_texts[3] if len(loc_texts) > 3 else ""
    # Which stats a quest grants, without the retunable amounts.
    mapped["family_stat_labels"] = [stat["label"] for stat in record.get("family_stats", [])]
    return mapped


CASE = HandlerCase(
    handler_name="quest.dbss",
    data_file="quest.dbss",
    companion_files={"allquestlist.bss": "allquestlist.bss", "stringtable.bss": "stringtable.bss"},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["Title", "Objective"],
    internal_path="gamecommondata/binary/quest.dbss",
    record_mapper=_quest_record,
    lookup_indexes={IndexKind.CHARACTER_GROUP_MEMBERS: character_group_index},
    tests=[
        SchemaTest(
            required_keys=[
                "row",
                "offset",
                "size",
                "packed_quest_id",
                "accept_dialog_key",
                "complete_dialog_key",
                "accept_npc",
                "complete_npc",
                "quest_chain_id",
                "quest_id",
                "quest_category",
                "quest_type_name",
                "block_kind",
                "condition_script",
                "action_script",
                "objective_text_kr",
                "title_en",
                "icon_path",
                "base_rewards",
                "select_rewards",
                "base_rewards_text",
                "select_rewards_text",
                "family_stats",
                "family_stat_text",
                "kill_groups",
            ]
        ),
        # Every record, walked in allquestlist.bss order.
        DeclaredCountTest(declared=header_count()),
        RangeTest(col="quest_category", min_val=0, max_val=19),
        # The first record follows the u32 count.
        TargetTest(col="row", value=0, expected={"offset": 0x4}),
        TargetTest(
            col="packed_quest_id",
            value=1050655,
            expected={
                "quest_chain_id": 2079,
                "quest_id": 16,
                "objective_text_kr": "<악몽의 그림자> 기가고드 처치하기;",
                "title_en": "[Elvia Weekly] Gigagord",
                "objective_en": "Defeat <Shadow of Nightmares> Gigagord;",
                "icon_path": "Icon/Quest/Hadum08.dds",
            },
        ),
        # The old icon-anchored scan read this record's scripts as icon-only.
        TargetTest(
            col="packed_quest_id",
            value=1510453,
            expected={
                "quest_chain_id": 3125,
                "quest_id": 23,
                "title_en": "Puzzling Words",
                "condition_script": "clearQuest(3125,22);",
                "action_script": "meet(50575,1);",
                "icon_path": "Icon/Quest/BalenosExplore_01.dds",
            },
        ),
        # An ordinary quest granting a Family stat from reward entry 1.
        TargetTest(col="packed_quest_id", value=72350, expected={"family_stat_labels": ["DP"]}),
        # A journal page (category 11) with its Family stat in entry 0.
        TargetTest(
            col="packed_quest_id",
            value=197406,
            expected={
                "quest_category": 11,
                "quest_type_name": "Adventurer's Tome",
                "family_stat_labels": ["Stamina"],
            },
        ),
        # An Olvia Academy Pass quest: the quest window has no name for the type, so the enum name shows.
        TargetTest(
            col="packed_quest_id",
            value=101 << 16 | 2324,
            expected={"quest_category": 17, "quest_type_name": "OlviaAcademyPass"},
        ),
        # A Growth Pass quest whose LOC title is a TextBind placeholder (LOC type 59).
        TargetTest(
            col="packed_quest_id",
            value=3 << 16 | 4470,
            expected={"title_en": "[Menu] Quick Hotkey Settings"},
        ),
        # One of the three records that store no icon path.
        TargetTest(col="packed_quest_id", value=69183, expected={"icon_path": ""}),
        # Villager 544 gives the quest as Dins (dialog 430) and takes it as a Vigilante (326).
        TargetTest(
            col="packed_quest_id",
            value=49 << 16 | 1001,
            expected={
                "accept_dialog_key": 430 << 16 | 544,
                "complete_dialog_key": 326 << 16 | 544,
                "accept_npc": "Dins",
                "complete_npc": "Vigilante",
            },
        ),
    ],
)


@pytest.fixture(scope="module")
def quest_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.fixture(scope="module")
def quest_lazy_context() -> tuple[Any, bytes, PazEntry, dict[str, bytes]]:
    # load_case restores the LOC parse the other cases already made.
    loaded = load_case(CASE)
    return loaded.handler, loaded.data, loaded.entry, loaded.companions


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_quest_dbss(spec: Any, quest_result: HandlerResult) -> None:
    quest_result.check(spec)


def _record(result: HandlerResult, packed_quest_id: int) -> dict:
    return next(record for record in result.records if record["packed_quest_id"] == packed_quest_id)


def _all_rewards(record: dict) -> list[dict]:
    return [*record["base_rewards"], *record["select_rewards"]]


def test_quest_dbss_rewards_fill_only_their_own_members(quest_result: HandlerResult) -> None:
    # A wrong member offset shows as a value in a member of another reward type.
    for record in quest_result.records:
        for reward in _all_rewards(record):
            own = _TYPE_MEMBERS.get(reward["reward_type"], set())
            stray = {name for name, unset in _UNSET_MEMBERS.items() if name not in own and reward[name] != unset}
            assert not stray, (record["packed_quest_id"], reward["reward_type"], stray)


def test_quest_dbss_uses_every_2016_reward_type(quest_result: HandlerResult) -> None:
    used = {reward["reward_type"] for record in quest_result.records for reward in record["base_rewards"]}
    assert set(_TYPE_MEMBERS_2016) <= used


def test_quest_dbss_family_stats_sit_in_one_reward_type(quest_result: HandlerResult) -> None:
    types = {
        record["base_rewards"][stat["entry"]]["reward_type"]
        for record in quest_result.records
        for stat in record["family_stats"]
    }
    assert types == {REWARD_FAMILY_STAT}, types


def test_quest_dbss_select_rewards_follow_the_base_rewards(quest_result: HandlerResult) -> None:
    # "[Processing] The Beauty of Planks": pick Pine Sap or the Pine Plank its script gathers.
    record = _record(quest_result, 138172)
    assert [reward["item_key"] for reward in record["select_rewards"]] == [5003, 4657]
    assert "gatheritem(4657," in record["action_script"]


def test_quest_dbss_amity_reward_names_its_npc(quest_result: HandlerResult) -> None:
    record = _record(quest_result, 788483)
    amity = [reward for reward in record["base_rewards"] if reward["reward_type"] == REWARD_INTIMACY]
    assert [reward["intimacy_character"] for reward in amity] == [41011]
    assert any(text.startswith("Melissa Brady ") for text in record["base_rewards_text"])


def test_quest_dbss_knowledge_rewards_name_a_knowledge_card(quest_result: HandlerResult) -> None:
    """Every knowledge reward keys a `mentalcard.dbss` card; the text names it."""
    from _dbss.mentalcard.parser import parse_mentalcard_records
    from tests.fixtures import load_binary_fixture

    cards = {
        card.card_id
        for card in parse_mentalcard_records(
            load_binary_fixture("mentalcard.dbss"), load_binary_fixture("mentalcardoffset.dbss")
        )
    }
    keys = [
        reward["mental_card_key"]
        for record in quest_result.records
        for reward in _all_rewards(record)
        if reward["reward_type"] == REWARD_KNOWLEDGE
    ]
    assert keys
    assert set(keys) <= cards
    # "Food for Hungry Pets" teaches the Pet - Dog and Pet - Cat entries.
    assert {"[Knowledge] Pet - Dog", "[Knowledge] Pet - Cat"} <= set(_record(quest_result, 788483)["base_rewards_text"])


def _is_silent(reward: dict) -> bool:
    """A Family stat shows in its own column; a fever entry without points has no widget text."""
    if reward["reward_type"] == REWARD_FAMILY_STAT:
        return True
    return reward["reward_type"] == REWARD_FEVER_POINT and not (reward["max_fever_point"] or reward["add_fever_point"])


def test_quest_dbss_every_other_reward_has_text(quest_result: HandlerResult) -> None:
    for record in quest_result.records:
        for kind in ("base_rewards", "select_rewards"):
            shown = [reward for reward in record[kind] if not _is_silent(reward)]
            assert len(record[f"{kind}_text"]) == len(shown), (record["packed_quest_id"], kind)


def test_quest_dbss_family_stats_are_gains(quest_result: HandlerResult) -> None:
    # Family stats only ever add; a wrong field width reads as zero or a negative.
    for record in quest_result.records:
        for stat in record["family_stats"]:
            assert stat["value"] is None or stat["value"] > 0, (record["packed_quest_id"], stat)


def test_quest_dbss_kill_groups_name_their_members(quest_result: HandlerResult) -> None:
    """Every killMonsterGroup call shows as `group (xcount)` and the names of the group's characters."""
    records = quest_result.records
    with_calls = [r for r in records if "killmonstergroup(" in (r["condition_script"] + r["action_script"]).lower()]

    assert with_calls
    assert sum(1 for r in records if r["kill_groups"]) == len(with_calls)
    for record in with_calls:
        calls, texts = record["_kill_groups"], record["kill_groups"]
        assert calls and len(texts) == len(calls)
        assert all(text.startswith(f"{group} (x{count:,}): ") for (group, count), text in zip(calls, texts))


def test_quest_dbss_lazy_page(
    quest_lazy_context: tuple[Any, bytes, PazEntry, dict[str, bytes]],
    quest_result: HandlerResult,
) -> None:
    handler, data, entry, companions = quest_lazy_context
    declared = header_count()(quest_result.source)
    first = quest_result.records[0]

    assert handler.supports_lazy_records()
    assert handler.get_record_count(data, entry, companions) == declared

    html = handler.render_data_page(data, entry, companions, page=0, page_size=25)

    assert f"{declared:,} quests" in html
    assert escape(first["title_en"]) in html
    assert escape(first["icon_path"]) in html


def test_quest_dbss_lazy_search(
    quest_lazy_context: tuple[Any, bytes, PazEntry, dict[str, bytes]],
    quest_result: HandlerResult,
) -> None:
    handler, data, entry, companions = quest_lazy_context
    record = _record(quest_result, 1510453)

    assert record["row"] in handler.search_records(data, entry, companions, "Puzzling Words")


def test_quest_dbss_default_sort_reads_ids_from_index(
    quest_lazy_context: tuple[Any, bytes, PazEntry, dict[str, bytes]],
    quest_result: HandlerResult,
) -> None:
    handler, data, entry, companions = quest_lazy_context
    sort = handler.default_sort()
    assert sort == TableSort("packed_quest_id", SORT_DESC)

    expected = sort_order_by_values(
        [record["packed_quest_id"] for record in quest_result.records], sort.descending
    )
    assert list(handler.sorted_order(data, entry, companions, sort)) == expected


@pytest.mark.parametrize(("file_name", "field"), [
    ("acceptquest.bss", "accept_dialog_key"),
    ("completequest.bss", "complete_dialog_key"),
])
def test_quest_dbss_dialog_keys_match_the_quest_npc_files(
    quest_result: HandlerResult, file_name: str, field: str,
) -> None:
    """Each quest's dialog key is `dialog_index << 16 | npc_id` of its row in the NPC file."""
    from _bss.questnpc.parser import parse_quest_npc_records
    from tests.fixtures import load_binary_fixture

    rows = {
        row["packed_quest_id"]: row["dialog_index"] << 16 | row["npc_id"]
        for row in parse_quest_npc_records(load_binary_fixture(file_name), file_name)
    }
    for record in quest_result.records:
        assert record[field] == rows[record["packed_quest_id"]], record["packed_quest_id"]

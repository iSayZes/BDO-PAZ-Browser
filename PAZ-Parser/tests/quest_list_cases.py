"""Shared test cases for the quest lists that use the `allquestlist.bss` layout."""
from __future__ import annotations

from .framework import (
    DeclaredCountTest,
    HandlerCase,
    HandlerResult,
    SchemaTest,
    TestSpec as Spec,
    header_count,
    run_case,
)


def quest_list_case(name: str, *extra: Spec) -> HandlerCase:
    """The schema and declared-count checks every quest list shares, plus `extra`."""
    return HandlerCase(
        handler_name=name,
        data_file=name,
        companion_files={},
        loc_file="languagedata_en.loc",
        uses_loc=True,
        loc_fields=["Title"],
        internal_path=f"gamecommondata/binary/{name}",
        tests=[
            SchemaTest(required_keys=["slot", "packed_quest_id", "quest_chain_id", "quest_id", "title"]),
            # The u32 count after the PABR magic.
            DeclaredCountTest(declared=header_count(offset=4)),
            *extra,
        ],
    )


ALL_QUESTS_CASE = HandlerCase(
    handler_name="allquestlist.bss",
    data_file="allquestlist.bss",
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=False,
    loc_fields=[],
    internal_path="gamecommondata/binary/allquestlist.bss",
    tests=[],
)


# quest.dbss, for the lists that are exactly one quest category.
QUEST_CASE = HandlerCase(
    handler_name="quest.dbss",
    data_file="quest.dbss",
    companion_files={"allquestlist.bss": "allquestlist.bss"},
    loc_file=None,
    uses_loc=False,
    loc_fields=[],
    internal_path="gamecommondata/binary/quest.dbss",
    tests=[],
)


def assert_distinct_listed_quests(result: HandlerResult) -> None:
    """Every entry is a different quest of `allquestlist.bss`."""
    listed = [record["packed_quest_id"] for record in result.records]
    all_quests = {record["packed_quest_id"] for record in run_case(ALL_QUESTS_CASE).records}
    assert len(set(listed)) == len(listed)
    assert set(listed) <= all_quests

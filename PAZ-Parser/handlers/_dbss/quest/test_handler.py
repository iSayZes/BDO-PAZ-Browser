from __future__ import annotations

from dataclasses import replace
from html import escape
from typing import Any

import pytest

from bdo_models import PazEntry
from bdo_preview import get_handler
from table_sort import SORT_DESC, TableSort, sort_order_by_values
from tests.fixtures import ensure_fixtures
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
    companion_files={"allquestlist.bss": "allquestlist.bss"},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["Title", "Objective"],
    internal_path="gamecommondata/binary/quest.dbss",
    record_mapper=_quest_record,
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
                "block_kind",
                "condition_script",
                "action_script",
                "objective_text_kr",
                "title_en",
                "icon_path",
                "family_stats",
                "family_stat_text",
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
            expected={"quest_category": 11, "family_stat_labels": ["Stamina"]},
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
    fixture_paths = ensure_fixtures(CASE)

    from _common.loc import init_loc

    init_loc(fixture_paths[str(CASE.loc_file)].read_bytes())
    entry = PazEntry(
        archive_name="",
        internal_path=CASE.internal_path,
        offset=0,
        compressed_size=0,
        uncompressed_size=0,
        compression_type=0,
        encryption_type=0,
    )
    handler = get_handler("quest.dbss", ".dbss")
    companions = {
        name: fixture_paths[name].read_bytes() for name in CASE.companion_files
    }
    return handler, fixture_paths[str(CASE.data_file)].read_bytes(), entry, companions


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_quest_dbss(spec: Any, quest_result: HandlerResult) -> None:
    quest_result.check(spec)


def _record(result: HandlerResult, packed_quest_id: int) -> dict:
    return next(record for record in result.records if record["packed_quest_id"] == packed_quest_id)


def test_quest_dbss_family_stats_are_gains(quest_result: HandlerResult) -> None:
    # Family stats only ever add; a wrong field width reads as zero or a negative.
    for record in quest_result.records:
        for stat in record["family_stats"]:
            assert stat["value"] is None or stat["value"] > 0, (record["packed_quest_id"], stat)


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

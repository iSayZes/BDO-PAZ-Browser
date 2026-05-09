from __future__ import annotations

from dataclasses import replace
from typing import Any

import pytest

from bdo_models import PazEntry
from bdo_preview import get_handler
from tests.fixtures import ensure_fixtures
from tests.framework import CountTest, HandlerCase, HandlerResult, PosTest, SchemaTest, TargetTest, case_id, run_case


def _quest_record(record: dict) -> dict:
    loc_texts = record.get("loc_texts_en", [])
    mapped = dict(record)
    mapped["title_en"] = loc_texts[0] if loc_texts else ""
    mapped["objective_en"] = loc_texts[3] if len(loc_texts) > 3 else ""
    return mapped


CASE = HandlerCase(
    handler_name="quest.dbss",
    data_file="quest.dbss",
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["Title", "Objective"],
    internal_path="gamecommondata/binary/quest.dbss",
    record_mapper=_quest_record,
    tests=[
        SchemaTest(required_keys=["row", "packed_quest_id", "quest_chain_id", "quest_id", "title_en", "icon_path"]),
        CountTest(expected=19481),
        PosTest(
            pos=0,
            expected={
                "row": 0,
                "packed_quest_id": 1050655,
                "quest_chain_id": 2079,
                "quest_id": 16,
                "title_en": "[Elvia Weekly] Gigagord",
                "objective_en": "Defeat <Shadow of Nightmares> Gigagord;",
                "icon_path": "Icon/Quest/Hadum08.dds",
            },
        ),
        TargetTest(
            col="row",
            value=100,
            expected={
                "packed_quest_id": 1510453,
                "quest_chain_id": 3125,
                "quest_id": 23,
                "title_en": "Puzzling Words",
                "icon_path": "Icon/Quest/BalenosExplore_01.dds",
                "parse_status": "Icon-only",
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
    return handler, fixture_paths[str(CASE.data_file)].read_bytes(), entry, {}


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_quest_dbss(spec: Any, quest_result: HandlerResult) -> None:
    spec.check(quest_result.records)


def test_quest_dbss_lazy_page(quest_lazy_context: tuple[Any, bytes, PazEntry, dict[str, bytes]]) -> None:
    handler, data, entry, companions = quest_lazy_context

    assert handler.supports_lazy_records()
    assert handler.get_record_count(data, entry, companions) == 19481

    html = handler.render_data_page(data, entry, companions, page=0, page_size=25)

    assert "19,481 quests" in html
    assert "[Elvia Weekly] Gigagord" in html
    assert "Icon/Quest/Hadum08.dds" in html


def test_quest_dbss_lazy_search(quest_lazy_context: tuple[Any, bytes, PazEntry, dict[str, bytes]]) -> None:
    handler, data, entry, companions = quest_lazy_context

    assert 100 in handler.search_records(data, entry, companions, "Puzzling Words")

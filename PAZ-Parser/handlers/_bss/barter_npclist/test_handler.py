from __future__ import annotations

from dataclasses import replace
from typing import Any

import pytest

from _bss.regioninfo.parser import parse_regioninfo_records
from _common.pabr_offset import parse_pabr_offset_rows
from _dbss.characterfunction.parser import parse_characterfunction_records
from tests.fixtures import load_binary_fixture
from tests.framework import (
    DeclaredCountTest,
    HandlerCase,
    HandlerResult,
    SchemaTest,
    TargetTest,
    case_id,
    header_count,
    run_case,
)

from .parser import ROW_SIZE, parse_barter_npclist_records


CASE = HandlerCase(
    handler_name="barter_npclist.bss",
    data_file="barter_npclist.bss",
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["Region", "NPC"],
    internal_path="gamecommondata/binary/barter_npclist.bss",
    tests=[
        SchemaTest(required_keys=["barter_region_key", "region_name", "character_id", "npc_name"]),
        DeclaredCountTest(declared=header_count(offset=4)),
        # Lema Island's barter NPC.
        TargetTest(col="barter_region_key", value=181, expected={"region_name": "Lema Island", "character_id": 58954}),
    ],
)


@pytest.fixture(scope="module")
def barter_npclist_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_barter_npclist_bss(spec: Any, barter_npclist_result: HandlerResult) -> None:
    barter_npclist_result.check(spec)


def test_keys_and_characters_are_unique(barter_npclist_result: HandlerResult) -> None:
    for field in ("barter_region_key", "character_id"):
        values = [record[field] for record in barter_npclist_result.records]
        assert len(values) == len(set(values)), field


def test_barter_regions_are_regions(barter_npclist_result: HandlerResult) -> None:
    region_keys = {record["region_key"] for record in parse_regioninfo_records(load_binary_fixture("regioninfo.bss"))}

    missing = [r["barter_region_key"] for r in barter_npclist_result.records if r["barter_region_key"] not in region_keys]

    assert not missing


def test_rows_match_the_maritime_trade_slot() -> None:
    """Each row's NPC stores the same region key in its characterfunction.dbss Maritime Trade slot."""
    functions = parse_characterfunction_records(
        load_binary_fixture("characterfunction.dbss"),
        parse_pabr_offset_rows(load_binary_fixture("characterfunctionoffset.dbss")),
    )
    barter_keys = {
        record.character_id: record.slot("maritime_trade").fields["barter_region_key"] for record in functions
    }
    rows = {r["character_id"]: r["barter_region_key"] for r in parse_barter_npclist_records(load_binary_fixture("barter_npclist.bss"))}

    stored = {character_id: key for character_id, key in barter_keys.items() if key}

    assert rows == stored


def test_rows_that_miss_the_string_table_are_rejected() -> None:
    # PABR, 1 row declared, but the trailer puts the string table right after the header.
    data = b"PABR" + (1).to_bytes(4, "little") + bytes(ROW_SIZE) + (0).to_bytes(4, "little")
    data += (8).to_bytes(4, "little") + bytes(4)
    with pytest.raises(ValueError, match="string table starts"):
        parse_barter_npclist_records(data)

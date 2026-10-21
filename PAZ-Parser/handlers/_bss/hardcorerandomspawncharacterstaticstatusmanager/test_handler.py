from __future__ import annotations

import struct
from dataclasses import replace
from typing import Any

import pytest

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

from .handler import BOSS_LIST, NPC_LIST
from .parser import STRING_FIELDS, parse_random_spawn_file


_U32 = struct.Struct("<I")
_ROW = struct.Struct("<H5hBIH")
_NO_STRING = -1
# Laytenn and Ancient Puturum, the two bosses; Wandering Merchant and Light of Offering, the NPCs.
_LAYTENN = 29496
_ANCIENT_PUTURUM = 29497
_WANDERING_MERCHANT = 62223
_LIGHT_OF_OFFERING = 62200

CASE = HandlerCase(
    handler_name="hardcorerandomspawncharacterstaticstatusmanager.bss",
    data_file="hardcorerandomspawncharacterstaticstatusmanager.bss",
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["character_name", "notice", "reveal_notice"],
    internal_path="gamecommondata/binary/hardcorerandomspawncharacterstaticstatusmanager.bss",
    tests=[
        SchemaTest(
            required_keys=[
                "random_spawn_key",
                "character_key",
                "character_name",
                "spawn_list",
                *(field for pair in STRING_FIELDS for field in pair),
                "notice",
                "reveal_notice",
                "unknown_0c",
                "unknown_11",
            ]
        ),
        DeclaredCountTest(declared=header_count(offset=4)),
        TargetTest(
            col="character_key",
            value=_LAYTENN,
            expected={
                "character_name": "Laytenn",
                "spawn_list": BOSS_LIST,
                "boss_icon": "Combine_Etc_HardcoreServer_Map_BossInfoIcon_Raiten",
                "notice_key": "PANEL_BIGNAK_HARDCOREMESSAGE_4",
            },
        ),
        TargetTest(
            col="character_key",
            value=_ANCIENT_PUTURUM,
            expected={"character_name": "Ancient Puturum", "spawn_list": BOSS_LIST},
        ),
        TargetTest(
            col="character_key",
            value=_WANDERING_MERCHANT,
            expected={"character_name": "Wandering Merchant", "spawn_list": NPC_LIST, "boss_icon": ""},
        ),
        TargetTest(
            col="character_key",
            value=_LIGHT_OF_OFFERING,
            expected={"character_name": "Light of Offering", "spawn_list": NPC_LIST},
        ),
    ],
)


@pytest.fixture(scope="module")
def random_spawn_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_hardcorerandomspawncharacterstaticstatusmanager_bss(spec: Any, random_spawn_result: HandlerResult) -> None:
    random_spawn_result.check(spec)


def test_every_row_is_on_one_list(random_spawn_result: HandlerResult) -> None:
    parsed = parse_random_spawn_file(random_spawn_result.source.data)
    boss, npc = set(parsed.boss_keys), set(parsed.npc_keys)
    keys = [row["random_spawn_key"] for row in parsed.rows]
    assert boss and npc and not boss & npc
    assert sorted(keys) == sorted(boss | npc)


def test_every_boss_has_a_boss_icon_and_both_notices(random_spawn_result: HandlerResult) -> None:
    bosses = [r for r in random_spawn_result.records if r["spawn_list"] == BOSS_LIST]
    assert bosses
    for record in bosses:
        assert record["boss_icon"] and record["notice"] and record["reveal_notice"], record


def test_every_notice_has_loc_text(random_spawn_result: HandlerResult) -> None:
    for record in random_spawn_result.records:
        assert record["notice"] != record["notice_key"], record


def _pabr(values: bytes, strings: list[str]) -> bytes:
    table_start = 4 + len(values)
    table = _U32.pack(len(strings))
    for text in strings:
        raw = text.encode("utf-16-le")
        table += struct.pack("<BI", 1, len(raw)) + raw
    return b"PABR" + values + table + _U32.pack(table_start) + _U32.pack(0)


def _lists(boss: list[int], npc: list[int], refs: list[int]) -> bytes:
    out = _U32.pack(len(boss)) + struct.pack(f"<{len(boss)}H", *boss)
    out += _U32.pack(len(npc)) + struct.pack(f"<{len(npc)}H", *npc)
    return out + _U32.pack(len(refs)) + struct.pack(f"<{len(refs)}I", *refs)


def test_a_minus_one_ref_has_no_string() -> None:
    row = _ROW.pack(100, 0, _NO_STRING, 1, _NO_STRING, _NO_STRING, 1, 7, 0)
    data = _pabr(_U32.pack(1) + row + _lists([], [7], [0, 1]), ["Icon", "Background"])
    (record,) = parse_random_spawn_file(data).rows
    assert record["world_map_icon"] == "Icon"
    assert record["boss_icon"] == ""
    assert record["notice_background"] == "Background"
    assert record["random_spawn_key"] == 7


def test_a_list_count_past_the_string_table_raises() -> None:
    data = _pabr(_U32.pack(0) + _U32.pack(9), [])
    with pytest.raises(ValueError, match="boss_keys count"):
        parse_random_spawn_file(data)

from __future__ import annotations

from dataclasses import replace
from typing import Any

import pytest

from _bss.allquestlist.parser import parse_allquestlist_records
from _common.lookup_builders import DETAIL_DIALOG
from _common.lookup_index import IndexKind, init_index
from _common.pabr_offset import parse_pabr_offset_rows
from _common.quest.dialog import dialog_cell
from tests.framework import (
    DeclaredCountTest,
    HandlerCase,
    HandlerResult,
    SchemaTest,
    TargetTest,
    UserLanguageTest,
    case_id,
    header_count,
    run_case,
)


_QUEST_LIST_FILE = "allquestlist.bss"
_CHARACTER_OFFSET_FILE = "characterstaticoffset.dbss"

# Velia: "Cat on the Roof" (1001/4) is given and taken by Mariano in his only dialog.
_CAT_ON_THE_ROOF = 4 << 16 | 1001
# Velia: "Dins, Spoiling for a Fight" (1001/49). The generic Villager character 544
# speaks as Dins in its dialog 430 and as a Vigilante in its dialog 326.
_DINS_QUEST = 49 << 16 | 1001
_VILLAGER = 544


def _case(file_name: str, tests: list) -> HandlerCase:
    return HandlerCase(
        handler_name=file_name,
        data_file=file_name,
        # Not read by the handler; the cross-checks below compare every row with them.
        companion_files={_QUEST_LIST_FILE: _QUEST_LIST_FILE, _CHARACTER_OFFSET_FILE: _CHARACTER_OFFSET_FILE},
        loc_file="languagedata_en.loc",
        uses_loc=True,
        loc_fields=["title", "npc_name", "dialog_name"],
        internal_path=f"gamecommondata/binary/{file_name}",
        tests=[
            SchemaTest(
                required_keys=[
                    "packed_quest_id",
                    "quest_chain_id",
                    "quest_id",
                    "title",
                    "npc_id",
                    "npc_name",
                    "dialog_index",
                    "dialog_name",
                    "dialog_key",
                ],
            ),
            # The u32 count after the PABR magic.
            DeclaredCountTest(declared=header_count(offset=4)),
            UserLanguageTest(fields=["title", "npc_name", "dialog_name"]),
            TargetTest(
                col="packed_quest_id",
                value=_CAT_ON_THE_ROOF,
                expected={
                    "quest_chain_id": 1001,
                    "quest_id": 4,
                    "title": "Cat on the Roof",
                    "npc_id": 40066,
                    "npc_name": "Mariano",
                    "dialog_index": 1,
                    "dialog_key": 1 << 16 | 40066,
                },
            ),
            *tests,
        ],
    )


ACCEPT_CASE = _case("acceptquest.bss", [
    TargetTest(
        col="packed_quest_id",
        value=_DINS_QUEST,
        expected={"npc_id": _VILLAGER, "npc_name": "Villager", "dialog_index": 430, "dialog_name": "Dins"},
    ),
])

COMPLETE_CASE = _case("completequest.bss", [
    TargetTest(
        col="packed_quest_id",
        value=_DINS_QUEST,
        expected={"npc_id": _VILLAGER, "npc_name": "Villager", "dialog_index": 326, "dialog_name": "Vigilante"},
    ),
])

CASES = [ACCEPT_CASE, COMPLETE_CASE]
_RESULTS: dict[str, HandlerResult] = {}


def _result(case: HandlerCase) -> HandlerResult:
    result = _RESULTS.get(case.handler_name)
    if result is None:
        result = run_case(replace(case, tests=[]))
        _RESULTS[case.handler_name] = result
    return result


_SPECS = [(case, spec) for case in CASES for spec in case.tests]


@pytest.mark.parametrize(
    ("case", "spec"),
    _SPECS,
    ids=[f"{case.handler_name}-{case_id(spec)}" for case, spec in _SPECS],
)
def test_quest_npc(case: HandlerCase, spec: Any) -> None:
    _result(case).check(spec)


@pytest.mark.parametrize("case", CASES, ids=lambda case: case.handler_name)
def test_every_quest_of_allquestlist_once(case: HandlerCase) -> None:
    result = _result(case)
    expected = sorted(r["packed_quest_id"] for r in parse_allquestlist_records(result.source.file(_QUEST_LIST_FILE)))

    assert sorted(r["packed_quest_id"] for r in result.records) == expected


@pytest.mark.parametrize("case", CASES, ids=lambda case: case.handler_name)
def test_every_npc_is_a_characterstatic_key(case: HandlerCase) -> None:
    result = _result(case)
    characters = {row.entry_id for row in parse_pabr_offset_rows(result.source.file(_CHARACTER_OFFSET_FILE))}

    for record in result.records:
        assert record["npc_id"] is None or record["npc_id"] in characters, record["packed_quest_id"]


@pytest.mark.parametrize("case", CASES, ids=lambda case: case.handler_name)
def test_rows_are_grouped_by_npc(case: HandlerCase) -> None:
    """Each NPC's rows, and the rows without one, form one run in file order."""
    runs = [record["npc_id"] for record in _result(case).records]
    run_starts = [npc for pos, npc in enumerate(runs) if pos == 0 or npc != runs[pos - 1]]

    assert len(run_starts) == len(set(run_starts))


@pytest.mark.parametrize("case", CASES, ids=lambda case: case.handler_name)
def test_no_npc_dialog_0_is_the_black_spirit(case: HandlerCase) -> None:
    """Rows without an NPC keep their dialog; NPC 0's dialog 0 is the Black Spirit's."""
    rows = [r for r in _result(case).records if r["npc_id"] is None and r["dialog_index"] == 0]

    assert rows
    assert {r["dialog_name"] for r in rows} == {"Black Spirit"}


def test_dialog_cell_links_only_keys_with_a_detail_dialog_row() -> None:
    key = 1 << 16 | 40066
    init_index(IndexKind.DIALOG_KEYS, {key: 40066})
    try:
        linked = dialog_cell(key, "1")
        plain = dialog_cell(2 << 16 | 40066, "<2>")
    finally:
        init_index(IndexKind.DIALOG_KEYS, None)

    assert 'data-action="open-record"' in linked
    assert f'data-path="{DETAIL_DIALOG}"' in linked
    assert f'data-field="key" data-value="{key}"' in linked
    assert plain == "&lt;2&gt;"

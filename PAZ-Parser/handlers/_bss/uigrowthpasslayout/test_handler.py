from __future__ import annotations

from dataclasses import replace
from typing import Any

import pytest

from _bss.growthpasslinkdata.parser import quest_link_addresses
from _bss.uigrowthpasslayout.links import LINKS_FIELD, cell_links, read_quest_links
from _bss.uigrowthpasslayout.parser import parse_uigrowthpasslayout
from _common.binary import u32
from _common.texture_string import TEXTURE_STRING_COMBINE
from tests.framework import (
    HandlerCase,
    HandlerResult,
    RangeTest,
    SchemaTest,
    case_id,
    run_case,
)


# `__eGrowthPass_CellType_*` has 15 members.
_MAX_CELL_TYPE = 14
_QUEST = 2
_CATEGORY_FILE = "growthpasscategory.dbss"
_CATEGORY_OFFSET_FILE = "growthpasscategoryoffset.dbss"
_LINK_FILE = "growthpasslinkdata.bss"

CASE = HandlerCase(
    handler_name="uigrowthpasslayout.bss",
    data_file="uigrowthpasslayout.bss",
    companion_files={_LINK_FILE: _LINK_FILE},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["Title"],
    internal_path="gamecommondata/binary/uigrowthpasslayout.bss",
    tests=[
        SchemaTest(required_keys=[
            "category_key", "row", "col", "cell_type", "cell_type_name", "quest_chain_id", "quest_id", LINKS_FIELD,
        ]),
        RangeTest(col="cell_type", min_val=0, max_val=_MAX_CELL_TYPE),
    ],
)

CATEGORY_CASE = HandlerCase(
    handler_name=_CATEGORY_FILE,
    data_file=_CATEGORY_FILE,
    companion_files={_CATEGORY_OFFSET_FILE: _CATEGORY_OFFSET_FILE, TEXTURE_STRING_COMBINE: TEXTURE_STRING_COMBINE},
    loc_file=None,
    uses_loc=False,
    loc_fields=[],
    internal_path=f"gamecommondata/binary/{_CATEGORY_FILE}",
    tests=[],
)


@pytest.fixture(scope="module")
def layout_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_uigrowthpasslayout_bss(spec: Any, layout_result: HandlerResult) -> None:
    layout_result.check(spec)


def test_one_grid_per_declared_layout(layout_result: HandlerResult) -> None:
    data = layout_result.source.data
    assert len(parse_uigrowthpasslayout(data)) == u32(data, 4)


def test_only_quest_cells_hold_a_quest(layout_result: HandlerResult) -> None:
    wrong = [
        (r["category_key"], r["row"], r["col"])
        for r in layout_result.records
        if (r["cell_type"] == _QUEST) != bool(r["quest_chain_id"] and r["quest_id"])
    ]
    assert not wrong


def test_quest_cells_sit_on_even_rows_and_columns(layout_result: HandlerResult) -> None:
    # The window draws even rows tall and even columns wide, sized for a quest button.
    wrong = [
        (r["category_key"], r["row"], r["col"])
        for r in layout_result.records
        if r["cell_type"] == _QUEST and (r["row"] % 2 or r["col"] % 2)
    ]
    assert not wrong


def test_each_grid_holds_its_categorys_quest_chain(layout_result: HandlerResult) -> None:
    categories = {r["category_key"]: r["quest_chain_id"] for r in run_case(CATEGORY_CASE).records}
    chains: dict[int, set[int]] = {}
    for r in layout_result.records:
        if r["cell_type"] == _QUEST:
            chains.setdefault(r["category_key"], set()).add(r["quest_chain_id"])
    assert chains == {key: {chain} for key, chain in categories.items() if key in chains}
    assert set(chains) <= set(categories)


def test_every_linked_quest_is_a_quest_cell(layout_result: HandlerResult) -> None:
    """growthpasslinkdata.bss keys its links by the quest of a grid cell."""
    links = quest_link_addresses(layout_result.source.file(_LINK_FILE))
    quest_cells = {
        (r["quest_chain_id"], r["quest_id"]) for r in layout_result.records if r["cell_type"] == _QUEST
    }
    assert links
    assert set(links) <= quest_cells


def test_quest_cells_show_their_links(layout_result: HandlerResult) -> None:
    links = quest_link_addresses(layout_result.source.file(_LINK_FILE))
    for r in layout_result.records:
        is_quest = r["cell_type"] == _QUEST
        expected = list(links.get((r["quest_chain_id"], r["quest_id"]), ())) if is_quest else []
        assert r[LINKS_FIELD] == expected, (r["category_key"], r["row"], r["col"])


def test_links_are_empty_without_the_companion() -> None:
    assert read_quest_links(None) == {}
    assert read_quest_links(b"not a PABR file") == {}
    assert cell_links({}, 4470, 1) == []

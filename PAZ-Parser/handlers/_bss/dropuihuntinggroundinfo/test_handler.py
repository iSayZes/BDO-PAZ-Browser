from __future__ import annotations

from dataclasses import replace
from typing import Any

import pytest

from tests.fixtures import load_binary_fixture
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
from tests.runner import load_case

from _bss.dropuihuntinggroundinfo import tribe_labels
from _bss.dropuihuntinggroundinfo.parser import parse_territory_keys
from _bss.dropuihuntinggroundinfo.tribe_labels import TRIBE_LABELS, tribe_label, tribe_text
from _bss.stringtable.parser import GAME_SHEET, parse_key_hashes
from _common.html import e
from _common.item_key import item_key_icon_path


_MAIN_CATEGORY_FILE = "dropuimaincategoryinfo.bss"
_TAG_INFO_FILE = "dropuitaginfo.bss"
_MANSHA_FOREST = 0
_ARESION_TEMPLE = 117
# The rows start after the PABR magic with this count.
_COUNT_OFFSET = 4

CASE = HandlerCase(
    handler_name="dropuihuntinggroundinfo.bss",
    data_file="dropuihuntinggroundinfo.bss",
    companion_files={_MAIN_CATEGORY_FILE: _MAIN_CATEGORY_FILE, _TAG_INFO_FILE: _TAG_INFO_FILE},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["name", "region", "species", "node_name"],
    internal_path="gamecommondata/binary/dropuihuntinggroundinfo.bss",
    tests=[
        SchemaTest(
            required_keys=[
                "key",
                "main_category_key",
                "sub_category_keys",
                "name_kr",
                "monster_ids",
                "repeat_quest_keys",
                "sudden_quest_keys",
                "drop_item_ids",
                "tag_keys",
                "region_keys",
                "title_keys",
                "pos_x",
                "pos_y",
                "pos_z",
                "recommended_ap",
                "recommended_dp",
                "node_key",
                "total_ap",
                "total_dp",
                "limited_ap",
                "limited_ap_apply_percent",
                "tribe_type",
                "name",
                "region",
                "categories",
                "species",
                "max_ap",
                "node_name",
                "monsters",
                "items",
                "quests",
                "tags",
                "titles",
            ],
        ),
        DeclaredCountTest(declared=header_count(offset=_COUNT_OFFSET)),
        # A new species needs a label in tribe_labels.py first.
        RangeTest(col="tribe_type", min_val=min(TRIBE_LABELS), max_val=max(TRIBE_LABELS)),
        TargetTest(
            col="key",
            value=_MANSHA_FOREST,
            expected={
                "name_kr": "만샤 숲",
                "name": "Mansha Forest",
                "region": "Calpheon",
                "node_key": 715,
                "species": "1 Demihumans",
            },
        ),
        TargetTest(
            col="key",
            value=_ARESION_TEMPLE,
            expected={
                "name_kr": "아레시온 신전",
                "name": "Aresion Temple",
                "region": "Inner Edania",
                "node_key": 2110,
                "node_name": "Aresion Temple",
                "species": "4 Edanian Monsters",
            },
        ),
    ],
)


@pytest.fixture(scope="module")
def hunting_ground_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_dropuihuntinggroundinfo_bss(spec: Any, hunting_ground_result: HandlerResult) -> None:
    hunting_ground_result.check(spec)


def test_every_region_tab_has_a_territory(hunting_ground_result: HandlerResult) -> None:
    territories = parse_territory_keys(hunting_ground_result.source.file(_MAIN_CATEGORY_FILE))
    missing = sorted({
        r["main_category_key"] for r in hunting_ground_result.records
        if r["main_category_key"] not in territories
    })
    assert not missing, f"region tabs missing from {_MAIN_CATEGORY_FILE}: {missing}"


def test_every_quest_key_names_a_quest(hunting_ground_result: HandlerResult) -> None:
    """Packed as chain | quest << 16; a wrong split shows `chain/quest` instead of a title."""
    shown = [
        title for r in hunting_ground_result.records for title in r["quests"]
        if "/" in title and title.replace("/", "").isdigit()
    ]
    assert not shown, f"quests without a LOC title: {shown[:5]}"


def test_items_column_shows_each_item_with_its_icon(hunting_ground_result: HandlerResult) -> None:
    aresion = next(r for r in hunting_ground_result.records if r["key"] == _ARESION_TEMPLE)
    first_item = aresion["drop_item_ids"][0]

    html = load_case(CASE).handler.render_records_page([aresion], 0, 1)

    assert f'data-icon-path="{e(item_key_icon_path(first_item))}"' in html
    assert f'<span class="icon-cell-label">{e(aresion["items"][0])}</span>' in html


def test_every_tag_has_its_colours(hunting_ground_result: HandlerResult) -> None:
    for record in hunting_ground_result.records:
        assert len(record["_tag_colors"]) == len(record["tags"])
        assert None not in record["_tag_colors"], f"hunting ground {record['key']} has a tag without colours"


def test_tribe_label_hashes_match_stringtable() -> None:
    hashes = parse_key_hashes(load_binary_fixture("stringtable.bss"), GAME_SHEET)
    wrong = {
        label.key: (label.key_hash, hashes.get(label.key))
        for label in TRIBE_LABELS.values()
        if hashes.get(label.key) != label.key_hash
    }
    assert not wrong, f"tribe label hashes differ from stringtable.bss (stored, file): {wrong}"


def test_tribe_labels_have_english_text() -> None:
    load_case(CASE)
    missing = [label.enum_name for value, label in TRIBE_LABELS.items() if not tribe_label(value)]
    assert not missing, f"tribe labels without LOC text: {missing}"


def test_tribe_text_without_label_shows_enum_name(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(tribe_labels, "tribe_label", lambda tribe_type: "")
    assert tribe_text(1) == "1 NonHuman"


def test_tribe_text_outside_the_enum_is_the_value() -> None:
    assert tribe_text(max(TRIBE_LABELS) + 1) == str(max(TRIBE_LABELS) + 1)

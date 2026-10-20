from __future__ import annotations

import re
from dataclasses import replace
from typing import Any

import pytest

from _common.lookup_index import IndexKind
from _common.pa_text import pa_key, strip_pa_tags
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

_OFFSET_FILE = "skilloffset.dbss"
_SKILLTYPE_OFFSET_FILE = "skilltypeoffset.dbss"
# Item 761880 casts skill 47683 level 1, which applies buffs 48723 to 48728.
_ITEM_SKILL_KEY = 47683 << 16 | 1
# Grave Digging I leads to Grave Digging II (skill 1760).
_GRAVE_DIGGING_I = 1759 << 16 | 1
_GRAVE_DIGGING_II = 1760 << 16 | 1
# Looks like a sentinel, but is the ordinary skill 57005.
_DEAD_KEY = 0xDEAD0001
# Ample Storage Lv. 8, a guild skill whose effect text is only in LOC type 13.
_AMPLE_STORAGE_KEY = 65069 << 16 | 1
_HANGUL = re.compile("[가-힣]")
_GRAVE_DIGGING_ICON = "ui_texture/icon/new_icon/04_pc_skill/01_pc_skill/01_phm_skill/phm_skill_1759.dds"

SKILL_CASE = HandlerCase(
    handler_name="skill.dbss",
    data_file="skill.dbss",
    companion_files={_OFFSET_FILE: _OFFSET_FILE},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["Name", "Description", "Buffs", "Next Skills", "Base Skill"],
    internal_path="gamecommondata/binary/skill.dbss",
    lookup_indexes={IndexKind.SKILL_ICON: {1759: _GRAVE_DIGGING_ICON}},
    tests=[
        SchemaTest(required_keys=[
            "skill_key", "skill_no", "level", "icon_path", "name", "description", "cooldown_ms", "resource_cost",
            "stamina_cost", "buff_ids", "buffs",
            "next_skill_keys", "related_cool_time_skill_keys", "script",
        ]),
        DeclaredCountTest(declared=header_count(offset=0)),
        DeclaredCountTest(declared=header_count(offset=4, companion=_OFFSET_FILE)),
        RangeTest(col="level", min_val=1, max_val=0xFFFF),
        TargetTest(
            col="skill_key",
            value=_ITEM_SKILL_KEY,
            expected={"skill_no": 47683, "level": 1, "buff_ids": [48723, 48724, 48725, 48726, 48727, 48728]},
        ),
        TargetTest(
            col="skill_key",
            value=_GRAVE_DIGGING_I,
            expected={"skill_no": 1759, "name": "Grave Digging I", "icon_path": _GRAVE_DIGGING_ICON},
        ),
        TargetTest(col="skill_key", value=_DEAD_KEY, expected={"skill_no": 57005, "level": 1}),
    ],
)

OFFSET_CASE = HandlerCase(
    handler_name=_OFFSET_FILE,
    data_file=_OFFSET_FILE,
    companion_files={},
    loc_file=None,
    uses_loc=False,
    loc_fields=[],
    internal_path=f"gamecommondata/binary/{_OFFSET_FILE}",
    tests=[
        SchemaTest(required_keys=["skill_key", "skill_no", "level", "dbss_offset", "size"]),
        DeclaredCountTest(declared=header_count(offset=4)),
        TargetTest(col="skill_key", value=_ITEM_SKILL_KEY, expected={"skill_no": 47683, "level": 1}),
    ],
)

# skilltypeoffset.dbss shares the handler; every key is level 1.
SKILLTYPE_OFFSET_CASE = replace(
    OFFSET_CASE,
    handler_name=_SKILLTYPE_OFFSET_FILE,
    data_file=_SKILLTYPE_OFFSET_FILE,
    internal_path=f"gamecommondata/binary/{_SKILLTYPE_OFFSET_FILE}",
    tests=[
        DeclaredCountTest(declared=header_count(offset=4)),
        RangeTest(col="level", min_val=1, max_val=1),
    ],
)


@pytest.fixture(scope="module")
def skill_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_SKILL_RESULT", None)
    if result is None:
        result = run_case(replace(SKILL_CASE, tests=[]))
        request.module._SKILL_RESULT = result
    return result


@pytest.fixture(scope="module")
def offset_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_OFFSET_RESULT", None)
    if result is None:
        result = run_case(replace(OFFSET_CASE, tests=[]))
        request.module._OFFSET_RESULT = result
    return result


@pytest.fixture(scope="module")
def skilltype_offset_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_SKILLTYPE_OFFSET_RESULT", None)
    if result is None:
        result = run_case(replace(SKILLTYPE_OFFSET_CASE, tests=[]))
        request.module._SKILLTYPE_OFFSET_RESULT = result
    return result


@pytest.mark.parametrize("spec", SKILL_CASE.tests, ids=case_id)
def test_skill_dbss(spec: Any, skill_result: HandlerResult) -> None:
    skill_result.check(spec)


def test_skill_rank_leads_to_next_rank(skill_result: HandlerResult) -> None:
    grave_digging = next(r for r in skill_result.records if r["skill_key"] == _GRAVE_DIGGING_I)
    assert _GRAVE_DIGGING_II in grave_digging["next_skill_keys"]


def test_every_linked_skill_is_a_skill_key(skill_result: HandlerResult) -> None:
    keys = {r["skill_key"] for r in skill_result.records}
    linked = {
        key for r in skill_result.records for key in r["next_skill_keys"] + r["related_cool_time_skill_keys"]
    }
    assert linked <= keys


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_skilloffset_dbss(spec: Any, offset_result: HandlerResult) -> None:
    offset_result.check(spec)


@pytest.mark.parametrize("spec", SKILLTYPE_OFFSET_CASE.tests, ids=case_id)
def test_skilltypeoffset_dbss(spec: Any, skilltype_offset_result: HandlerResult) -> None:
    skilltype_offset_result.check(spec)


def test_records_open_in_skill_key_order(skill_result: HandlerResult) -> None:
    keys = [r["skill_key"] for r in skill_result.records]
    assert keys == sorted(keys)


def test_descriptions_are_display_text(skill_result: HandlerResult) -> None:
    for r in skill_result.records:
        assert "<PA" not in r["description"], r["skill_key"]
        assert r["description"] not in {"<null>", "UNKNOWN"}, r["skill_key"]


def test_guild_skill_effect_comes_from_loc_type_13(skill_result: HandlerResult) -> None:
    """The rank's English text stands in for its Korean `description`."""
    ample_storage = next(r for r in skill_result.records if r["skill_key"] == _AMPLE_STORAGE_KEY)

    assert "Guild Storage" in ample_storage["description"]
    assert not _HANGUL.search(ample_storage["description"])



def test_build_skill_buff_index_keeps_slot_order() -> None:
    from _dbss.skill.parser import build_skill_buff_index
    from tests.fixtures import ensure_fixtures

    paths = ensure_fixtures(SKILL_CASE)
    index = build_skill_buff_index(paths["skill.dbss"].read_bytes(), paths[_OFFSET_FILE].read_bytes())

    assert index[_ITEM_SKILL_KEY] == (48723, 48724, 48725, 48726, 48727, 48728)
    # Skills without buffs are left out rather than stored empty.
    assert all(index.values())


def test_next_skills_keep_their_game_colours(skill_result: HandlerResult) -> None:
    """Prime skills are orange in LOC, also where another skill lists them as next."""
    tagged_key = pa_key("next_skills")
    for record in skill_result.records:
        assert record["next_skills"] == [strip_pa_tags(label).strip() for label in record[tagged_key]]
    assert any("<PAColor" in label for record in skill_result.records for label in record[tagged_key])


def test_buff_list_cell_draws_buff_icons() -> None:
    from _common.buff import buff_list_cell
    from _common.lookup_index import init_index

    icon = "ui_texture/icon/new_icon/04_pc_skill/03_buff/silverbless.dds"
    init_index(IndexKind.BUFF_ICON, {48723: icon})
    try:
        cell = buff_list_cell([48723, 48724, 48725, 48726], 3)
    finally:
        init_index(IndexKind.BUFF_ICON, None)

    assert f'data-icon-path="{icon}"' in cell
    # Buffs without an icon keep their label; the hidden rest is counted and
    # named on hover.
    shown, _, more = cell.partition('<span class="list-more"')
    assert "48724" in shown and "48726" not in shown
    assert 'title="48726' in more and more.endswith("(+1)</span>")


def test_buff_list_cell_draws_labels_in_game_colours(monkeypatch: pytest.MonkeyPatch) -> None:
    from _common import buff

    texts = {1: "<PAColor0xffe9bd23>Sap & Knot<PAOldColor>\nsecond line", 2: ""}
    monkeypatch.setattr(buff, "loc_lookup", lambda _type, buff_id: texts[buff_id])

    cell = buff.buff_list_cell([1, 2], 2)

    assert '1 <span class="pa-color" style="color: rgba(233, 189, 35, 1)">Sap &amp; Knot</span>' in cell
    assert "second line" not in cell and "PAColor" not in cell
    # The plain label for records and CSV keeps no markup.
    assert buff.buff_label(1) == "1 Sap & Knot"
    assert buff.buff_label_html(2) == "2"

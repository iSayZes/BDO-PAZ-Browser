from __future__ import annotations

import math
from dataclasses import replace
from collections.abc import Iterator
from typing import Any

import pytest

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
from tests.loc_counter import reset_loc
from tests.loc_data import LocRow, loc_bytes

import _common.loc as loc
from _common.duration import format_duration
from _common.html import e
from _common.inline_text import decode_inline_text
from _common.lookup_index import IndexKind
from _common.pa_text import pa_html

from _bss.stringtable.parser import GAME_SHEET_LOC_ID2
from _bss.stringtable.text import LOC_UI_STRING

from _dbss.buff.effect import EffectInput, effect_text, param_labels
from _dbss.buff.title import extract_title, title_leaders
from _dbss.lifeexp.labels import LIFE_SKILLS


# Backslash and `n`, how the tables store a line break in inline text.
_ESCAPED_NEWLINE = "\\n"
# Item 761880, [Blessing] Adventure's Boon (120 min), casts skill 47683 level 1,
# which applies buffs 48723 to 48728; 48723 is the headline buff with the title.
_BOON_ITEM = 761880
_BOON_SKILL_KEY = 47683 << 16 | 1
_BOON_BUFFS = (48723, 48724, 48725, 48726, 48727, 48728)
_BOON_TITLE = "[Blessing] Adventure's Boon"


BUFF_CASE = HandlerCase(
    handler_name="buff.dbss",
    data_file="buff.dbss",
    companion_files={"buffoffset.dbss": "buffoffset.dbss"},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["description"],
    internal_path="gamecommondata/binary/buff.dbss",
    lookup_indexes={
        IndexKind.SKILL_BUFFS: {_BOON_SKILL_KEY: _BOON_BUFFS},
        IndexKind.BUFF_ITEMS: {buff_id: (_BOON_ITEM,) for buff_id in _BOON_BUFFS},
    },
    tests=[
        SchemaTest(
            required_keys=[
                "buff_id",
                "name",
                "level",
                "effect_type",
                "duration_ms",
                "tick_ms",
                "duration",
                "icon_path",
                "title",
                "title_buff_id",
                "description",
                "effect",
                "applied_by_item_ids",
                "applied_by",
                "applied_by_count",
                "description_kr",
                "param_1",
                "param_10",
                "is_shown",
                "apply_rate",
                "group",
                "condition_type",
                "stacking_category",
                "is_exclusive",
            ]
        ),
        DeclaredCountTest(declared=header_count()),
        TargetTest(
            col="buff_id",
            value=48879,
            expected={"name": "중범선 대미지 저항 18.9%", "effect_type": 106, "icon_path": ""},
        ),
        TargetTest(
            col="buff_id",
            value=48830,
            expected={
                "name": "수렵 숙련도 +70 3시간",
                "effect_type": 149,
                "icon_path": "ui_texture/icon/new_icon/04_pc_skill/03_buff/huntingbuff.dds",
                "description": "Hunting Mastery +70",
                "title": "",
                "is_shown": True,
            },
        ),
        # EXP gain: param_2 selects combat (0), skill (1) or life (2) EXP.
        TargetTest(col="buff_id", value=47692, expected={"effect_type": 25, "param_2": 0}),
        # Headline buff: the coloured first line of its description is its title.
        TargetTest(
            col="buff_id",
            value=48723,
            expected={
                "title": _BOON_TITLE,
                "title_buff_id": 48723,
                "name": "모든 공격력 +8(120분)",
                "is_shown": True,
                "effect": "All AP +8",
                "applied_by_item_ids": [_BOON_ITEM],
            },
        ),
        # The rest of the same item's buffs are hidden and have no text; they
        # take the headline buff's title through the skill that applies them.
        TargetTest(
            col="buff_id",
            value=48724,
            expected={
                "title": _BOON_TITLE,
                "title_buff_id": 48723,
                "description": "",
                "effect_type": 40,
                "effect": "All Accuracy +8",
                "is_shown": False,
            },
        ),
        # Summon: Keeper Marg: in game "Marg's attack damage 579%" and
        # "Recover 250 MP every 10 sec".
        TargetTest(
            col="buff_id",
            value=8992,
            expected={"effect_type": 45, "param_4": 5790000, "effect": "Attack Damage 579%"},
        ),
        TargetTest(
            col="buff_id",
            value=8973,
            expected={
                "effect_type": 4,
                "tick_ms": 10000,
                "effect": "Recover 250 MP/WP/SP every 10 sec",
            },
        ),
        # An alchemy stone retaliation buff: type 1 under condition 4.
        TargetTest(
            col="buff_id",
            value=57123,
            expected={"effect_type": 1, "condition_type": 4, "effect": "Retaliate 15 Fixed Damage when struck"},
        ),
        # High-quality Carrot refills a mount's stamina: type 4 with no tick.
        TargetTest(col="buff_id", value=50403, expected={"effect_type": 4, "tick_ms": 0, "effect": ""}),
        # Cartian Spell (41587): "[Co-op] Eliminating the Threats to Mediah
        # will automatically be accepted".
        TargetTest(
            col="buff_id",
            value=57217,
            expected={"effect_type": 69, "effect": "Accept Quest: [Co-op] Eliminating the Threats to Mediah"},
        ),
        # Item 970013 summons character 28615.
        TargetTest(
            col="buff_id",
            value=48806,
            expected={"effect_type": 18, "param_1": 28615, "effect": "Summon Incarnation of Corruption"},
        ),
        # Item 66397 Tuntaros, used on pickup, unlocks knowledge 11216.
        TargetTest(
            col="buff_id",
            value=39562,
            expected={"effect_type": 38, "param_1": 11216, "effect": "Learn Knowledge: Tuntaros"},
        ),
        # Item 64639 reads "Employment Contract: Goblin Worker" and
        # "Affiliation: Calpheon City" on bdocodex.
        TargetTest(
            col="buff_id",
            value=64039,
            expected={
                "effect_type": 103,
                "effect": "Employment Contract: Skilled Goblin Worker (Calpheon City)",
            },
        ),
        # Summon: Keeper Marg clears the movement speed buff 8972 of group 521.
        TargetTest(col="buff_id", value=8974, expected={"effect_type": 16, "effect": "Remove Group 521"}),
        TargetTest(col="buff_id", value=59158, expected={"effect_type": 72, "effect": "Trent Stable +1"}),
        TargetTest(
            col="buff_id",
            value=58322,
            expected={"effect_type": 17, "effect": "Learn Skill: Lightning Chain I"},
        ),
        TargetTest(
            col="buff_id",
            value=51837,
            expected={"effect_type": 101, "effect": "Gain Western Camp Officer Knowledge"},
        ),
        # Applied by no item in the installed index: an empty list, None to sort last.
        TargetTest(
            col="buff_id",
            value=48830,
            expected={"applied_by_item_ids": [], "applied_by_count": None, "title_buff_id": None},
        ),
        # Food Max HP variants share one group.
        TargetTest(col="buff_id", value=59746, expected={"effect_type": 2, "group": 5616}),
        # Group keys from 40001 up are u16; an i16 read made them negative.
        RangeTest(col="group", min_val=0, max_val=0xFFFF),
        # Whale tendon elixirs have their own stacking category.
        TargetTest(col="buff_id", value=58025, expected={"stacking_category": 21}),
        # Draughts end each other: the reset every non-Harmony draught applies
        # is exclusive in the Harmony bonus category, an elixir buff is not.
        TargetTest(
            col="buff_id",
            value=47321,
            expected={"stacking_category": 26, "is_exclusive": True, "effect_type": 58},
        ),
        TargetTest(
            col="buff_id",
            value=48430,
            expected={"stacking_category": 2, "is_exclusive": False},
        ),
        # Adventurer's Luck I and V share a group, ranked by level.
        TargetTest(col="buff_id", value=57484, expected={"group": 6382, "level": 1}),
        TargetTest(col="buff_id", value=57488, expected={"group": 6382, "level": 5}),
        RangeTest(col="level", min_val=0, max_val=math.inf),
        RangeTest(col="duration_ms", min_val=0, max_val=math.inf),
    ],
)

OFFSET_CASE = HandlerCase(
    handler_name="buffoffset.dbss",
    data_file="buffoffset.dbss",
    companion_files={},
    loc_file=None,
    uses_loc=False,
    loc_fields=[],
    internal_path="gamecommondata/binary/buffoffset.dbss",
    tests=[
        SchemaTest(required_keys=["buff_id", "offset", "size"]),
        DeclaredCountTest(declared=header_count(offset=4)),
        # The first record follows buff.dbss's u32 count.
        TargetTest(col="offset", value=4, expected={}),
    ],
)


@pytest.fixture(scope="module")
def buff_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_BUFF_RESULT", None)
    if result is None:
        result = run_case(replace(BUFF_CASE, tests=[]))
        request.module._BUFF_RESULT = result
    return result


@pytest.fixture(scope="module")
def offset_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_OFFSET_RESULT", None)
    if result is None:
        result = run_case(replace(OFFSET_CASE, tests=[]))
        request.module._OFFSET_RESULT = result
    return result


@pytest.mark.parametrize("spec", BUFF_CASE.tests, ids=case_id)
def test_buff_dbss(spec: Any, buff_result: HandlerResult) -> None:
    buff_result.check(spec)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_buffoffset_dbss(spec: Any, offset_result: HandlerResult) -> None:
    offset_result.check(spec)


def test_boon_titles_keep_their_game_colour(buff_result: HandlerResult) -> None:
    """The headline buff and the buffs that inherit its title draw it in colour."""
    records = [r for r in buff_result.records if r["buff_id"] in _BOON_BUFFS[:2]]

    assert len(records) == 2
    for record in records:
        html = pa_html(record["_title_pa"])
        assert html.startswith('<span class="pa-color" style="color: rgba(')
        assert e(_BOON_TITLE) in html


def test_boon_exp_buff_reads_its_own_rate(buff_result: HandlerResult) -> None:
    """Buff 48727 of Adventure's Boon renders its stored rate (per million) as Combat EXP."""
    record = next(r for r in buff_result.records if r["buff_id"] == 48727)

    assert (record["effect_type"], record["param_2"]) == (25, 0)
    assert record["effect"] == f"Combat EXP +{record['param_1'] // 10_000}%"


def test_buff_group_levels_are_unique(buff_result: HandlerResult) -> None:
    """Within a group, each level is held by one buff."""
    seen: set[tuple[int, int]] = set()
    for record in buff_result.records:
        if not record["group"]:
            continue
        key = (record["group"], record["level"])
        assert key not in seen, f"group {key[0]} has level {key[1]} twice"
        seen.add(key)


@pytest.mark.parametrize(
    ("duration_ms", "expected"),
    [
        (0, ""),
        (1500, "1.5s"),
        (30000, "30s"),
        (1200000, "20m"),
        (5400000, "1h 30m"),
        (86400000, "24h"),
    ],
)
def test_format_duration(duration_ms: int, expected: str) -> None:
    assert format_duration(duration_ms) == expected


@pytest.mark.parametrize(
    ("raw", "expected"),
    [
        ("<PAColor0xffe9bd23>Eileen's Cheer<PAOldColor>\n\n  Alchemy Time -5 sec", "Eileen's Cheer"),
        ("<PAColor0xffe9bd23>[축복] 모험의 가호<PAOldColor>\r\n모든 공격력 +8", "[축복] 모험의 가호"),
        # One line is an effect, not a title.
        ("Hunting Mastery <PAColor0xffe9bd23>+70<PAOldColor>", ""),
        ("<PAColor0xffe9bd23>Life EXP +3%<PAOldColor>", ""),
        ("<PAColor0xffe9bd23>Trailing only<PAOldColor>\n  ", ""),
        ("", ""),
    ],
)
def test_extract_title(raw: str, expected: str) -> None:
    assert extract_title(raw) == expected


def test_inline_descriptions_hold_no_newline_escapes(buff_result: HandlerResult) -> None:
    """The stored two-character escape is decoded, so the Korean text breaks lines like LOC."""
    escaped = [r["buff_id"] for r in buff_result.records if _ESCAPED_NEWLINE in r["description_kr"]]
    assert not escaped, f"descriptions still hold a newline escape: {escaped[:5]}"


@pytest.mark.parametrize(
    ("stored", "expected"),
    [
        (f"모든 공격력 +8{_ESCAPED_NEWLINE}모든 적중력 +8", "모든 공격력 +8\n모든 적중력 +8"),
        (_ESCAPED_NEWLINE * 2, "\n\n"),
        ("no escape", "no escape"),
        ("", ""),
    ],
)
def test_decode_inline_text(stored: str, expected: str) -> None:
    assert decode_inline_text(stored) == expected


def test_korean_title_survives_without_loc() -> None:
    stored = f"<PAColor0xffe9bd23>[축복] 모험의 가호<PAOldColor>{_ESCAPED_NEWLINE * 2}모든 공격력 +8"
    assert extract_title(decode_inline_text(stored)) == "[축복] 모험의 가호"


@pytest.mark.parametrize(
    ("effect_type", "params", "expected"),
    [
        (2, [150, 0], "Max HP +150"),
        (8, [-150, 0], "Max Stamina -150"),
        # Per-million percentages keep their decimals and drop trailing zeros.
        (9, [25000, 0], "Movement Speed +2.5%"),
        # Life EXP names its life skill in param_3, 15 for all.
        (25, [150000, 2, 15], "Life EXP +15%"),
        (25, [100000, 0, 0], "Combat EXP +10%"),
        (39, [3, 8], "All AP +8"),
        (43, [3, -2], "All Damage Reduction -2"),
        (93, [4, 50000], "Critical Hit Extra Damage +5%"),
        (105, [8, 100000], "Ignore All Resistance +10%"),
        # Weight in ten-thousandths of an LT, durations in milliseconds.
        (29, [1000000, 0], "Weight Limit +100 LT"),
        (95, [15000, 0], "Underwater Breathing +15 sec"),
        # Pet skill 49134 reads "Death Penalty Resistance +3%".
        (90, [30000, 0], "Death Penalty Resistance +3%"),
        # One-off recoveries carry no sign.
        (63, [2, 0], "Recover 2 Worker Stamina"),
        (79, [10, 0], "Recover 10 Energy"),
        (67, [1, -1], "Attack Speed -1"),
        (89, [0, 2350], "Breath EXP +2,350"),
        # param_1 picks a rate or a flat amount.
        (120, [0, 60000], "Monster Damage Reduction Rate +6%"),
        (120, [2, 10], "Monster Damage Reduction +10"),
        # The amount sits in the parameter of its target.
        (136, [30, 0], "Extra AP Against Monsters +30"),
        (136, [0, 6], "Extra AP Against Adventurers +6"),
        (149, [15, 0, 100], "Life Skill Mastery +100"),
        # A [Life Skill Season] single-tool mastery.
        (149, [0, 2, 580], ""),
        # Targets other than 3 (all) have no confirmed label.
        (39, [0, 8], ""),
        # A zero amount.
        (43, [3, 0], ""),
        (46, [3, -12], "Extra AP Against Kamasylvian Monsters -12"),
        (49, [8, 100000], "All Resistance +10%"),
        # Kind 6 (bound) reads "Not in Use".
        (49, [6, 100000], ""),
        # Damage is a share of attack, printed without a sign.
        (45, [2, 0, 0, 5790000], "Attack Damage 579%"),
        # A reduction stored positive: "Fall Damage -50%".
        (52, [500000, 0], "Fall Damage -50%"),
        # Centimetres: Chenga - Sherekhan Tome of Wisdom reads +150m.
        (53, [15000, 0], "Discovery Radius +150m"),
        (59, [80, 0], "Jump Height +80"),
        (91, [100000, 0], "Durability Reduction Resistance +10%"),
        # Time cuts per million of 20 sec: Eileen's Cheer, Alchemy Time -5 sec.
        (111, [0, 250000], "Alchemy Time -5 sec"),
        (111, [1, 15000], "Cooking Time -0.3 sec"),
        (111, [2, 80000], "Processing Success Rate +8%"),
        # Farming time does not fit the scale.
        (111, [3, 400000], ""),
        # Flashbang: "Targets within the range will be stunned".
        (14, [4, 5000], "Stun for 5 sec"),
        (14, [20, 4000], "Stun (Ignores Resistance) for 4 sec"),
        # Kind 0 mixes resistances and stuns.
        (14, [0, 3000], ""),
        (24, [27500000, 2], "Skill EXP +27,500,000"),
        (24, [200000, 1], "Guild EXP +200,000"),
        (60, [0, 60, 1], "Contribution EXP +60"),
        # Package durations in minutes, worded like the item names.
        (97, [1, 43200], "Value Pack for 30 days"),
        (97, [15, 1440], "Secret Book of Old Moon for 1 day"),
        (97, [2, 25], "Shining Pearl Blessing for 25 min"),
        (97, [10, 720], "Book of Training - Combat for 12 hours"),
        # Kind 22 is shared by Premium Value Pack Plus and Blessing of Cron Stones.
        (97, [22, 10080, 2], ""),
        # Set points of a set skill; without LOC the skill shows its number.
        (48, [56050, 1], "Set Effect Points +1: 56050"),
        # Light Iron Horseshoe +0 and Epheria: Old Wind Sail on bdocodex.
        (98, [1, 20000], "Movement Speed (Mount) +2%"),
        (98, [2, 5000], "Turn +0.5%"),
        (98, [0, 10000], "Acceleration +1%"),
        (98, [3, 30000], "Brake +3%"),
        (187, [200, 0, 2], "AP +200"),
        (187, [250, 500, 1], "AP +250, DP +500"),
        (187, [0, -100, 0], "DP -100"),
        # "Remove Group 44812": a group key, written without separators.
        (16, [44812], "Remove Group 44812"),
        (66, [1], "Energy Recovery +1"),
        (106, [3, 50000], "All Damage Reduction +5%"),
        (107, [30000, 0], "Gathering Item Drop Rate +3%"),
        # A single gathering tool reads only "Gathering Luck increases."
        (107, [300000, 4], ""),
        (121, [50000], "Auto-fishing Time -5%"),
        (181, [0, 100000], "Breath EXP +10%"),
        # Kind 3 is one passive, "training EXP" in Korean.
        (181, [3, 200000], ""),
        (56, [100000], "Amity +10%"),
        # One parameter per speed: "Attack/Casting Speed +10%".
        (160, [0, 100000, 100000], "Attack Speed +10%, Casting Speed +10%"),
        # Breakthrough Crystal: Attack Speed reads "Attack Speed Limit +1".
        (68, [1, 1], "Attack Speed Limit +1"),
        (71, [8, 1], "Inventory +8"),
        # Confirmed from their items in game (Endless Ocean Draught, [Event]
        # Giddy-up Ghost Horsie!, Oceanbound Otter Fishing Rod).
        (19, [150000], "Sailor EXP +15%"),
        (47, [150000], "Horse Capture Rate +15%"),
        (51, [150000], "Mount Skill EXP +15%"),
        (62, [0, 5], "Skill Points +5"),
        (100, [1], "Character Slots +1"),
        (131, [1000000], "Trade Item Price +100%"),
        (134, [900000], "Swimming Speed +90%"),
        (196, [61], "Set Level to 61"),
        (200, [30000], "Prize Catch Fish Rate +3%"),
        # Sun Orb (red, like the Sun Aura's orb) reads "Moon's Aura" in its tooltip.
        (186, [1, 1, 0], "Sun Aura Fixed Stat +1"),
        (186, [0, 1, 0], "Selected Aura Stat +1"),
        # No amount stored: firecrackers and skills that reveal names.
        (84, [0], "Reveal Hidden Names"),
        (168, [0], "No Guard Gauge recovery"),
        (76, [100000, 0], "Karma +100,000"),
        (76, [-30000, 1], "Guild Karma -30,000"),
        # Hans' Contract: "Raises Naval Fame by 2,500".
        (76, [2500, 2], "Naval Fame +2,500"),
        (112, [500000, 0], "Item Drop Amount +50%"),
        (126, [1, 50000], "Chance to Catch Rare Fish +5%"),
        # Kind 2 is blue fish; its skills read "a high-quality fish".
        (126, [2, 50000], "Chance to Catch High-quality Fish +5%"),
        (169, [100000], "Target's Recovery -10%"),
        # Storage kinds are fixed names; 0 is every town.
        (72, [0, 16, 1, 0], "All Towns Storage +16"),
        (72, [126, 1, 0, 1], "Stable +1 in town 126"),
        (73, [0, 0], "Trade Refresh: Balenos"),
        # Territories whose English and Korean texts disagree stay unlabelled.
        (73, [0, 3], ""),
        # A character or knowledge entry with no LOC name falls back to its ID.
        (73, [1, 40010], "Trade Refresh: 40010"),
        (17, [827, 0, 1], "Learn Skill: 827"),
        (101, [30010], "Gain Knowledge of theme 30010"),
        (103, [7552, 77], "Employment Contract: 7552/77"),
        (18, [27542, 0], "Summon 27542"),
        (69, [11485, 30], "Accept Quest: 11485/30"),
        (38, [15074, 0], "Learn Knowledge: 15074"),
        (37, [2070, 0], "Register Node: 2070"),
        (142, [3176, 0], "Obtain Title: 3176"),
        # Without the TELEPORT_NEAREST_NODE index the point shows its key alone.
        (23, [0, 340], "Teleport to point 0/340"),
        # Test item A1_001 moves to the instance field named A1_001.
        (176, [17, 0, 4001], "Teleport to Instance Field 4001"),
        # Monster property keys have no name in the client; see buff_dbss.md.
        (180, [67], ""),
        # Life skill 10 is the spare slot `temp1`: no name, no line.
        (80, [10, 100], ""),
        # An effect type that is not decoded.
        (45, [1, 2], ""),
    ],
)
def test_effect_text(effect_type: int, params: list[int], expected: str) -> None:
    assert effect_text(EffectInput(effect_type, params)) == expected


@pytest.mark.parametrize(
    ("icon_path", "duration_ms", "expected"),
    [
        ("ui_texture/icon/new_icon/dot_poison.dds", 10000, "200 poison damage every 2 sec for 10 sec"),
        ("ui_texture/icon/new_icon/dot_burns.dds", 0, "200 burn damage every 2 sec"),
        # The bleeding icon also marks "burn" texts, so it names no kind.
        ("ui_texture/icon/new_icon/dot_bleeding.dds", 10000, "HP -200 every 2 sec"),
    ],
)
def test_ticking_damage_kind(icon_path: str, duration_ms: int, expected: str) -> None:
    buff = EffectInput(1, [-200], tick_ms=2000, duration_ms=duration_ms, icon_path=icon_path)
    text = effect_text(buff)
    assert text == expected


@pytest.mark.parametrize(
    ("effect_type", "amount", "tick_ms", "condition_type", "expected"),
    [
        (4, 250, 10000, 0, "Recover 250 MP/WP/SP every 10 sec"),
        (4, -50, 5000, 0, "MP/WP/SP -50 every 5 sec"),
        (4, 25, 1500, 0, "Recover 25 MP/WP/SP every 1.5 sec"),
        (4, 9, 0, 1, "Recover 9 MP/WP/SP on Hits"),
        # No tick and no condition: a one-off refill, possibly a mount's.
        (4, 500, 0, 0, ""),
        # A condition with no confirmed wording for MP/WP/SP.
        (4, 5, 0, 9, ""),
        (1, 25, 1000, 0, "Recover 25 HP every 1 sec"),
        # Poison, burn, pain and bleed differ only by icon.
        (1, -200, 1000, 0, "HP -200 every 1 sec"),
        (1, 9, 0, 1, "Recover 9 HP on Hits"),
        (1, 15, 0, 9, "Recover 15 HP on Critical Hits"),
        (1, -15, 0, 4, "Retaliate 15 Fixed Damage when struck"),
        (1, -7, 0, 6, "Deal 7 Fixed Damage on Back Attack Hits"),
        (1, -30, 0, 10, "Deal 30 Fixed Damage on Critical Hits"),
        # Infinite Fortitude: "Recover 250 HP when struck".
        (1, 250, 0, 3, "Recover 250 HP when struck"),
        # Fury of the Beast: "Recover 5 WP each time when struck".
        (4, 5, 0, 8, "Recover 5 MP/WP/SP when struck"),
        # A condition with no confirmed wording.
        (1, -100, 0, 2, ""),
    ],
)
def test_over_time_text(
    effect_type: int, amount: int, tick_ms: int, condition_type: int, expected: str
) -> None:
    buff = EffectInput(effect_type, [amount], tick_ms=tick_ms, condition_type=condition_type)
    assert effect_text(buff) == expected


@pytest.mark.parametrize(
    ("buff", "expected"),
    [
        # A kind parameter gets its kind; a flat amount needs no label.
        (EffectInput(46, [3, -12]), {1: "Kamasylvian Monsters"}),
        # A scaled amount shows the game's number.
        (EffectInput(9, [25000]), {1: "2.5%"}),
        (EffectInput(25, [150000, 0]), {1: "15%", 2: "Combat"}),
        # The parameter alone does not say which target it is.
        (EffectInput(136, [10, 0]), {1: "Monster AP"}),
        (EffectInput(136, [0, 6]), {2: "Adventurer AP"}),
        (EffectInput(120, [0, 15000]), {1: "Rate", 2: "1.5%"}),
        (EffectInput(4, [250], tick_ms=10000), {1: "every 10 sec"}),
        (EffectInput(1, [-15], condition_type=4), {1: "when struck"}),
        # No confirmed meaning: no labels at all.
        (EffectInput(39, [0, 8]), {}),
        (EffectInput(16, [521]), {1: "Group"}),
        (EffectInput(176, [17, 0, 4001]), {3: "Instance Field"}),
        (EffectInput(72, [0, 8, 1, 0]), {1: "All Towns"}),
        (EffectInput(73, [0, 5]), {2: "Southwestern Calpheon"}),
        (EffectInput(187, [0, 300, 2]), {3: "Earth"}),
        (EffectInput(53, [1000]), {1: "10m"}),
        (EffectInput(97, [15, 21600]), {1: "Secret Book of Old Moon", 2: "15 days"}),
        (EffectInput(14, [4, 5000]), {1: "Stun", 2: "5 sec"}),
        # A named effect without a name labels nothing.
        (EffectInput(23, [0, 340]), {}),
    ],
)
def test_param_labels(buff: EffectInput, expected: dict[int, str]) -> None:
    assert param_labels(buff) == expected


# Life skill names as the English LOC holds them under their GAME sheet keys.
_LIFE_SKILL_NAMES = {2: "Hunting", 4: "Alchemy", 6: "Training"}


@pytest.fixture
def life_skill_loc() -> Iterator[None]:
    rows: list[LocRow] = [
        (LOC_UI_STRING, LIFE_SKILLS[skill].key_hash or 0, GAME_SHEET_LOC_ID2, 0, 0, name)
        for skill, name in _LIFE_SKILL_NAMES.items()
    ]
    reset_loc()
    loc.init_loc(loc_bytes(rows))
    yield
    reset_loc()


@pytest.mark.usefixtures("life_skill_loc")
@pytest.mark.parametrize(
    ("effect_type", "params", "expected"),
    [
        # Hunter's Clothes (Costume) reads "Hunting EXP +10%" on bdocodex.
        (25, [100000, 2, 2], "Hunting EXP +10%"),
        (80, [4, 2560350], "Alchemy EXP +2,560,350"),
        (149, [2, 1, 70], "Hunting Mastery +70"),
    ],
)
def test_life_skill_effect_text(effect_type: int, params: list[int], expected: str) -> None:
    assert effect_text(EffectInput(effect_type, params)) == expected


@pytest.mark.usefixtures("life_skill_loc")
@pytest.mark.parametrize(
    ("buff", "expected"),
    [
        (EffectInput(149, [6, 1, 5]), {1: "Training"}),
        (EffectInput(25, [100000, 2, 2]), {1: "10%", 2: "Life", 3: "Hunting"}),
    ],
)
def test_life_skill_param_labels(buff: EffectInput, expected: dict[int, str]) -> None:
    assert param_labels(buff) == expected


def test_life_skill_without_loc_shows_its_enum_name() -> None:
    reset_loc()
    assert effect_text(EffectInput(25, [100000, 2, 2])) == "hunting EXP +10%"


def test_title_leaders_follow_the_skill_that_applies_them() -> None:
    titles = {1: "Boon", 10: "Meal", 11: "Meal", 20: "Draught A", 21: "Draught B"}
    buff_lists = [
        (1, 2, 3),
        # Two headline buffs with one title: the lower ID leads.
        (11, 10, 12),
        # Two titles: the members are ambiguous and get none.
        (20, 21, 22),
        # No headline buff at all.
        (30, 31),
    ]
    assert title_leaders(buff_lists, titles) == {2: 1, 3: 1, 12: 10}


def test_title_leaders_drop_a_buff_reached_by_two_titles() -> None:
    titles = {1: "Boon", 5: "Meal"}
    assert title_leaders([(1, 2), (5, 2)], titles) == {}


def test_teleport_buff_index_follows_section_and_key(buff_result: HandlerResult) -> None:
    from _common.teleport import teleport_point_id
    from _dbss.buff.parser import build_teleport_buff_index, build_teleport_buff_name_index

    data, offsets = buff_result.source.data, buff_result.source.file("buffoffset.dbss")
    index = build_teleport_buff_index(data, offsets)
    names = build_teleport_buff_name_index(data, offsets)

    # Buff 47341, "Footprints: Flower-sunken Swamp", goes to section 0 key 277.
    assert 47341 in index[teleport_point_id(0, 277)]
    teleports = {r["buff_id"]: r for r in buff_result.records if r["effect_type"] == 23}
    for point_id, buff_ids in index.items():
        assert list(buff_ids) == sorted(buff_ids)
        for buff_id in buff_ids:
            record = teleports[buff_id]
            assert teleport_point_id(record["param_1"], record["param_2"]) == point_id
    assert set(names) <= set(teleports)


def test_teleport_effect_names_the_nearest_node(monkeypatch: pytest.MonkeyPatch) -> None:
    import _dbss.buff.effect.named as named
    from dataclasses import replace as replace_effect

    (teleport,) = named.NAMED_EFFECTS[23]
    patched = replace_effect(teleport, name_of=lambda section, key: "Marni's Lab (12 m)")
    monkeypatch.setitem(named.NAMED_EFFECTS, 23, (patched,))
    buff = EffectInput(23, [0, 371])
    assert effect_text(buff) == "Teleport to point 0/371, near Marni's Lab (12 m)"
    assert param_labels(buff) == {2: "Marni's Lab (12 m)"}


def test_worker_contract_names_worker_and_town(monkeypatch: pytest.MonkeyPatch) -> None:
    import _dbss.buff.effect.named as named

    monkeypatch.setattr(named, "character_name", lambda key: {7552: "Skilled Goblin Worker"}.get(key, ""))
    monkeypatch.setattr(named, "town_name", lambda key: {77: "Calpheon City"}.get(key, ""))
    buff = EffectInput(103, [7552, 77])
    assert effect_text(buff) == "Employment Contract: Skilled Goblin Worker (Calpheon City)"
    assert param_labels(buff) == {2: "Skilled Goblin Worker (Calpheon City)"}
    # A town without a name leaves the worker alone.
    assert effect_text(EffectInput(103, [7552, 1])) == "Employment Contract: Skilled Goblin Worker"
    # Storage names its town the same way.
    assert effect_text(EffectInput(72, [77, 8, 0, 0])) == "Calpheon City Storage +8"


@pytest.mark.parametrize(
    ("minutes", "expected"),
    [(21600, "15 days"), (1440, "1 day"), (720, "12 hours"), (60, "1 hour"), (25, "25 min"), (0, "0 min")],
)
def test_minutes_text(minutes: int, expected: str) -> None:
    from _dbss.buff.effect.units import minutes_text

    assert minutes_text(minutes) == expected

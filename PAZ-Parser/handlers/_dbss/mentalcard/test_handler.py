from __future__ import annotations

import math
from dataclasses import replace
from typing import Any

import pytest

from _common.lookup_index import IndexKind
from _dbss.mentalcard.combo import BuffType, combo_text
from _common.contents_group import contents_group_key
from _dbss.mentalcard.parser import (
    KNOWLEDGE_TYPE_NORMAL,
    NO_MAP_STEP,
    MentalCardRecord,
    parse_mentalcard_records,
)
from tests.fixtures import load_binary_fixture
from tests.framework import (
    DeclaredCountTest,
    HandlerCase,
    HandlerResult,
    PaFieldTest,
    RangeTest,
    SchemaTest,
    TargetTest,
    case_id,
    header_count,
    run_case,
)

# Granbill grants card 304; Goyoung (47280) and a later copy (59998) both grant
# card 2043, so the name is shown once. The Helm Tribe Chief (23035) grants
# card 4678.
_KNOWLEDGE_CHARACTERS = {304: (43433,), 2043: (47280, 59998), 4678: (23035,)}
# knowledgelearning.dbss: the Rhyolite node teaches card 1643, which no action
# script grants; card 4678 adds two Steel Nux, and the shared 23035 shows once.
_KNOWLEDGE_LEARNING_CHARACTERS = {1643: (11982,), 4678: (23035, 23524, 25523)}
# The Gurnard fish teaches the Gurnard card.
_KNOWLEDGE_LEARNING_ITEMS = {8579: (8279,)}

CASE = HandlerCase(
    handler_name="mentalcard.dbss",
    data_file="mentalcard.dbss",
    companion_files={"mentalcardoffset.dbss": "mentalcardoffset.dbss"},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["Knowledge Name", "Category Name", "Description"],
    internal_path="gamecommondata/binary/mentalcard.dbss",
    lookup_indexes={
        IndexKind.KNOWLEDGE_CHARACTERS: _KNOWLEDGE_CHARACTERS,
        IndexKind.KNOWLEDGE_LEARNING_CHARACTERS: _KNOWLEDGE_LEARNING_CHARACTERS,
        IndexKind.KNOWLEDGE_LEARNING_ITEMS: _KNOWLEDGE_LEARNING_ITEMS,
    },
    tests=[
        SchemaTest(required_keys=["entry_id", "entry_name", "node_id", "node_name", "min_favor", "max_favor", "interest", "combo_text", "buff_type", "combo_value", "valid_turn", "apply_turn", "icon_path", "description", "obtain", "learned_from", "learned_from_item_ids", "learned_from_items", "position", "position_text", "knowledge_type", "map_step", "contents_groups"]),
        DeclaredCountTest(declared=header_count()),
        # Normal or Story, the two KnowledgeType values of the sheet.
        RangeTest(col="knowledge_type", min_val=0, max_val=1),
        # The first map reveal or local reputation levels 1 to 4; None for no step.
        RangeTest(col="map_step", min_val=0, max_val=4),
        # The Sausan Scout shows on the map from local reputation level 2.
        TargetTest(col="entry_id", value=4665, expected={"entry_name": "Sausan Scout", "map_step": 2}),
        # Recipe cards name their ingredients in yellow.
        PaFieldTest(field="description"),
        RangeTest(col="min_favor", min_val=0, max_val=math.inf),
        RangeTest(col="max_favor", min_val=0, max_val=math.inf),
        RangeTest(col="interest", min_val=0, max_val=math.inf),
        # Favor or Interest Level; cards without a combo store None.
        RangeTest(col="buff_type", min_val=0, max_val=1),
        TargetTest(
            col="entry_id",
            value=15055,
            expected={
                "entry_name": "Altar of Blood - The 11th Illusion",
                "node_id": 24114,
                "node_name": "Altar of Blood",
                "icon_path": "ui_texture/ui_artwork/ic_09812.dds",
                "obtain": "Altar of Blood",
                # Not in the installed index.
                "learned_from": [],
                # All zero means no position.
                "position_text": "",
            },
        ),
        TargetTest(
            col="entry_id",
            value=304,
            expected={
                "entry_name": "Granbill",
                "node_id": 155,
                "node_name": "Elionism & the Delphe Knights",
                "icon_path": "ui_texture/ui_artwork/ic_00304.dds",
                "obtain": "Delphe Knights Quartermaster",
                "learned_from": ["Granbill"],
                "position_text": "-133004, 2729, -46023",
            },
        ),
        TargetTest(col="entry_id", value=2043, expected={"learned_from": ["Goyoung"]}),
        TargetTest(col="entry_id", value=1643, expected={"learned_from": ["Rhyolite"]}),
        TargetTest(col="entry_id", value=4678, expected={"learned_from": ["Helm Tribe Chief", "Steel Nux"]}),
        TargetTest(
            col="entry_id",
            value=8579,
            expected={"learned_from": [], "learned_from_item_ids": [8279], "learned_from_items": ["Gurnard"]},
        ),
        # Lost Lamb shows "None" as its next combo effect in game.
        TargetTest(col="entry_id", value=4024, expected={"combo_text": None, "buff_type": None}),
        TargetTest(
            col="entry_id",
            value=3030,
            expected={
                "entry_name": "Iliya Island",
                "position_text": "159209, -7831, 292072",
            },
        ),
    ],
)


@pytest.fixture(scope="module")
def mentalcard_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_mentalcard_dbss(spec: Any, mentalcard_result: HandlerResult) -> None:
    mentalcard_result.check(spec)


def _card(buff_type: int, value: float = 0.0, valid_turn: int = 0, apply_turn: int = 0) -> MentalCardRecord:
    return MentalCardRecord(
        card_id=1, theme_id=1, min_favor=0.0, max_favor=0.0, interest=0.0,
        buff_type=buff_type, varied_value=value, valid_turn=valid_turn, apply_turn=apply_turn,
        name_kr="", description_kr="", knowledge_type=KNOWLEDGE_TYPE_NORMAL, knowledge_level=NO_MAP_STEP,
        icon_path="", acquisition_kr="", position=(0.0, 0.0, 0.0), contents_group_hashes=(),
    )


def test_every_contents_group_hash_names_a_key() -> None:
    records = parse_mentalcard_records(
        load_binary_fixture("mentalcard.dbss"), load_binary_fixture("mentalcardoffset.dbss")
    )

    unknown = [record.card_id for record in records if None in map(contents_group_key, record.contents_group_hashes)]
    assert not unknown, f"cards with a hash that is no contents group key: {unknown[:5]}"


@pytest.mark.parametrize(
    ("card", "expected"),
    [
        # The tooltip shows the stored delay plus one.
        (_card(BuffType.FAVOR, 4.0, 3, 1), "After 2 turns: Favor +4 for 3 turns"),
        (_card(BuffType.INTEREST, 3.0, 1, 2), "After 3 turns: Interest Level +3 for 1 turns"),
        (_card(BuffType.NONE), ""),
        (_card(7, 2.0, 1, 1), "After 2 turns: Type 7 +2 for 1 turns"),
    ],
)
def test_combo_text(card: MentalCardRecord, expected: str) -> None:
    assert combo_text(card) == expected

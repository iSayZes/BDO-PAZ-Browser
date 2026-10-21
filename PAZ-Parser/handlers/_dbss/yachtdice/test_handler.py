from __future__ import annotations

from dataclasses import replace
from typing import Any

import pytest

from _dbss.yachtbasecard.parser import FILE_NAME as CARD_FILE, KEY_FIELD as CARD_KEY, parse_yachtbasecard_records
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

from .parser import FILE_NAME


# Die 1 carries the six cards of the first symbol (the DiceList sheet of client 1784).
_DIE_1 = 1
_DIE_1_CARDS = [1, 2, 3, 4, 5, 6]

CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file=None,
    uses_loc=False,
    loc_fields=[],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=["dice_key", "dice_key_dup", "card_keys", "cards_text"]),
        DeclaredCountTest(declared=header_count(offset=0)),
        TargetTest(col="dice_key", value=_DIE_1, expected={"dice_key_dup": _DIE_1, "card_keys": _DIE_1_CARDS}),
    ],
)


@pytest.fixture(scope="module")
def yachtdice_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_yachtdice_dbss(spec: Any, yachtdice_result: HandlerResult) -> None:
    yachtdice_result.check(spec)


def test_keys_repeat_inside_each_row(yachtdice_result: HandlerResult) -> None:
    for r in yachtdice_result.records:
        assert r["dice_key_dup"] == r["dice_key"], r["dice_key"]


def test_every_face_is_a_base_card(yachtdice_result: HandlerResult) -> None:
    cards = {record[CARD_KEY] for record in parse_yachtbasecard_records(load_binary_fixture(CARD_FILE))}
    used = {key for r in yachtdice_result.records for key in r["card_keys"]}
    assert used <= cards, f"cards missing from {CARD_FILE}: {sorted(used - cards)}"

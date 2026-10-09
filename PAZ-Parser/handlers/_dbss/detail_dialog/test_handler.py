from __future__ import annotations

from dataclasses import replace
from typing import Any

import pytest

from _common.lease import Lease, lease_pairs
from _dbss.detail_dialog.lease import parse_lease
from _dbss.detail_dialog.parser import (
    CONTENTS_TYPE_NAMES,
    DIALOG_BUTTON_TYPE_NAMES,
    build_character_lease_index,
    split_key,
)
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

_OFFSET_FILE = "detail_dialogoffset.dbss"
# Options with an empty action store this value, outside DialogButtonType.
_NO_ACTION_BUTTON_TYPE = "99"
# Martina Finto's main dialog: dialog index 1 of character 40024.
_MARTINA_MAIN = 1 << 16 | 40024
_SMALL_FENCE = 58010

DIALOG_CASE = HandlerCase(
    handler_name="detail_dialog.dbss",
    data_file="detail_dialog.dbss",
    companion_files={_OFFSET_FILE: _OFFSET_FILE},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["Character"],
    internal_path="gamecommondata/binary/detail_dialog.dbss",
    tests=[
        SchemaTest(
            required_keys=[
                "key",
                "character_id",
                "dialog_index",
                "character",
                "internal_name",
                "greeting",
                "contents_types",
                "option_count",
                "dialog_button_types",
                "option_titles",
                "leases",
                "lease_item_ids",
            ]
        ),
        DeclaredCountTest(declared=header_count(offset=0)),
        DeclaredCountTest(declared=header_count(offset=4, companion=_OFFSET_FILE)),
        RangeTest(col="character_id", min_val=0, max_val=0xFFFF),
        # She leases the quest-gated [CP] Small Fence (see npcsimply_bss.md).
        TargetTest(
            col="key",
            value=_MARTINA_MAIN,
            expected={
                "character_id": 40024,
                "dialog_index": 1,
                "character": "Martina Finto",
                "internal_name": "Martina",
                "lease_item_ids": [_SMALL_FENCE],
            },
        ),
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
        SchemaTest(required_keys=["key", "character_id", "dialog_index", "dbss_offset", "size"]),
        DeclaredCountTest(declared=header_count(offset=4)),
        TargetTest(col="key", value=_MARTINA_MAIN, expected={"character_id": 40024, "dialog_index": 1}),
    ],
)


@pytest.fixture(scope="module")
def dialog_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_DIALOG_RESULT", None)
    if result is None:
        result = run_case(replace(DIALOG_CASE, tests=[]))
        request.module._DIALOG_RESULT = result
    return result


@pytest.fixture(scope="module")
def offset_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_OFFSET_RESULT", None)
    if result is None:
        result = run_case(replace(OFFSET_CASE, tests=[]))
        request.module._OFFSET_RESULT = result
    return result


@pytest.mark.parametrize("spec", DIALOG_CASE.tests, ids=case_id)
def test_detail_dialog_dbss(spec: Any, dialog_result: HandlerResult) -> None:
    dialog_result.check(spec)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_detail_dialogoffset_dbss(spec: Any, offset_result: HandlerResult) -> None:
    offset_result.check(spec)


def test_lease_index_holds_every_leasing_character(dialog_result: HandlerResult) -> None:
    """The index is the preview's lease items, grouped by character."""
    source = dialog_result.source
    index = build_character_lease_index(source.data, source.file(_OFFSET_FILE))

    expected: dict[int, set[int]] = {}
    for record in dialog_result.records:
        expected.setdefault(record["character_id"], set()).update(record["lease_item_ids"])

    assert {
        character_id: {lease.item_id for lease in lease_pairs(value)}
        for character_id, value in index.items()
    } == {character_id: items for character_id, items in expected.items() if items}
    assert _SMALL_FENCE in {lease.item_id for lease in lease_pairs(index[40024])}


@pytest.mark.parametrize(
    ("action", "expected"),
    [
        ("buyItemByPoint(58010,0,1,5,3)", Lease(58010, 3)),
        # Other scripts vary the case of their calls.
        ("buyitembypoint(3001, 0, 1, 5, 10)", Lease(3001, 10)),
        ("ExchangeItemToGroup(7003,0,3,1310)", None),
        ("", None),
    ],
)
def test_parse_lease(action: str, expected: Lease | None) -> None:
    assert parse_lease(action) == expected


def test_split_key() -> None:
    assert split_key(_MARTINA_MAIN) == (40024, 1)


def test_dialog_text_uses_the_user_language(dialog_result: HandlerResult) -> None:
    """Greetings and option titles come from LOC type 39 when it is loaded."""
    martina = next(r for r in dialog_result.records if r["key"] == _MARTINA_MAIN)
    assert "[Rent] Small Fence" in martina["option_titles"]
    assert martina["greeting"].isascii()


def test_dialog_enum_values_have_client_names(dialog_result: HandlerResult) -> None:
    """Every stored kind is a CppEnums member; only the empty-action 99 stays a number."""
    contents_types = {name for r in dialog_result.records for name in r["contents_types"]}
    button_types = {name for r in dialog_result.records for name in r["dialog_button_types"]}
    assert contents_types <= set(CONTENTS_TYPE_NAMES)
    assert "Shop" in contents_types
    assert button_types <= {*DIALOG_BUTTON_TYPE_NAMES, _NO_ACTION_BUTTON_TYPE}
    assert "Normal" in button_types

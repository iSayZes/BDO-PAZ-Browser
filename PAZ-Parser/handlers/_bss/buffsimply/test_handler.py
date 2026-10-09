from __future__ import annotations

from dataclasses import replace
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

from _bss.buffsimply.parser import build_buff_icon_index
from _common.buff import buff_icon_path
from _common.pabr_offset import parse_pabr_u32_offset_rows
from _dbss.buff.parser import parse_buff_records


_BUFF_FILE = "buff.dbss"
_BUFF_OFFSET_FILE = "buffoffset.dbss"
_HUNTING_ICON = "ui_texture/icon/new_icon/04_pc_skill/03_buff/huntingbuff.dds"

CASE = HandlerCase(
    handler_name="buffsimply.bss",
    data_file="buffsimply.bss",
    # Not read by the handler; the cross-check below compares every row with them.
    companion_files={_BUFF_FILE: _BUFF_FILE, _BUFF_OFFSET_FILE: _BUFF_OFFSET_FILE},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["description"],
    internal_path="gamecommondata/binary/buffsimply.bss",
    tests=[
        SchemaTest(
            required_keys=[
                "buff_id",
                "icon_path",
                "description",
                "is_shown",
                "unknown_str",
                "unknown_04",
                "unknown_07",
                "unknown_08",
                "unknown_09",
                "unknown_0b",
                "unknown_0c",
                "unknown_11",
                "unknown_12",
                "unknown_16",
                "unknown_18",
            ],
        ),
        DeclaredCountTest(declared=header_count(offset=4)),
        RangeTest(col="unknown_11", min_val=0, max_val=1),
        RangeTest(col="unknown_16", min_val=0, max_val=1),
        TargetTest(
            col="buff_id",
            value=48830,
            expected={
                "icon_path": _HUNTING_ICON,
                "description": "Hunting Mastery +70",
                "is_shown": True,
            },
        ),
        # Headline buff of [Blessing] Adventure's Boon; the rest of its run is
        # hidden and has no text, though it shares the icon.
        TargetTest(col="buff_id", value=48723, expected={"is_shown": True}),
        TargetTest(col="buff_id", value=48724, expected={"description": "", "is_shown": False}),
    ],
)


@pytest.fixture(scope="module")
def buffsimply_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_buffsimply_bss(spec: Any, buffsimply_result: HandlerResult) -> None:
    buffsimply_result.check(spec)


def test_rows_copy_their_buff_dbss_record(buffsimply_result: HandlerResult) -> None:
    """Same buffs in buffoffset.dbss order, with the same icon, is_shown and unknown_str."""
    source = buffsimply_result.source
    offset_rows = parse_pabr_u32_offset_rows(source.file(_BUFF_OFFSET_FILE))
    fields = ("buff_id", "icon_path", "is_shown", "unknown_str")
    expected = [
        {field: record[field] for field in fields}
        for record in parse_buff_records(source.file(_BUFF_FILE), offset_rows)
    ]

    actual = [{field: record[field] for field in fields} for record in buffsimply_result.records]
    assert actual == expected


def test_buff_icon_index_matches_the_icon_column(buffsimply_result: HandlerResult) -> None:
    """IndexKind.BUFF_ICON is this table's icons by buff ID."""
    index = build_buff_icon_index(buffsimply_result.source.data)

    assert index == {r["buff_id"]: r["icon_path"] for r in buffsimply_result.records if r["icon_path"]}


@pytest.mark.parametrize(
    ("stored", "expected"),
    [
        ("New_Icon/04_PC_Skill/03_Buff/HuntingBuff.dds", _HUNTING_ICON),
        ("New_Icon\\04_PC_Skill\\03_Buff\\HuntingBuff.dds", _HUNTING_ICON),
        (
            "New_Icon/04_PC_Skill//04_Debuff/Archer_StigmaLight.dds",
            "ui_texture/icon/new_icon/04_pc_skill/04_debuff/archer_stigmalight.dds",
        ),
        ("UNKNOWN", ""),
        ("  ", ""),
    ],
)
def test_buff_icon_path(stored: str, expected: str) -> None:
    assert buff_icon_path(stored) == expected

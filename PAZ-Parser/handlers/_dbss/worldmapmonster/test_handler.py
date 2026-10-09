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

from _dbss.worldmapmonster.parser import build_worldmap_marker_icon_index


_OFFSET_FILE = "worldmapmonsteroffset.dbss"
_BOSS_DIR = "ui_texture/combine/etc/worldmapboss"
_BASILISK_DEN = 36
_BASILISK_DEN_HUNTING_GROUND = 35
_GOBLIN = 1
# A Black Shrine boss: its unknown_ref is 0, which is no hunting ground.
_BIHYUNG = 197

MARKER_CASE = HandlerCase(
    handler_name="worldmapmonster.dbss",
    data_file="worldmapmonster.dbss",
    companion_files={_OFFSET_FILE: _OFFSET_FILE},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["name", "label", "detail", "hunting_ground"],
    internal_path="gamecommondata/binary/worldmapmonster.dbss",
    tests=[
        SchemaTest(
            required_keys=[
                "key",
                "line1_kr",
                "line2_kr",
                "name_kr",
                "pos_x",
                "pos_y",
                "pos_z",
                "icon_path",
                "condition",
                "unknown_str",
                "unknown_ref",
                "unknown_kind",
                "unknown_flag",
                "name",
                "label",
                "detail",
                "hunting_ground_key",
                "hunting_ground",
            ],
        ),
        DeclaredCountTest(declared=header_count(offset=0)),
        DeclaredCountTest(declared=header_count(offset=0, companion=_OFFSET_FILE)),
        RangeTest(col="unknown_flag", min_val=0, max_val=1),
        TargetTest(
            col="key",
            value=_BASILISK_DEN,
            expected={
                "name_kr": "바실리스크 소굴",
                "name": "Basilisk Den",
                "icon_path": f"{_BOSS_DIR}/worldmapmonster_36.dds",
                "hunting_ground_key": _BASILISK_DEN_HUNTING_GROUND,
                "hunting_ground": "Lv. 57 Basilisk Den",
            },
        ),
        TargetTest(
            col="key",
            value=_BIHYUNG,
            expected={"hunting_ground_key": None, "hunting_ground": ""},
        ),
        # Level-range zones repeat their label on the second line, and store
        # -1 for the hunting ground.
        TargetTest(
            col="key",
            value=_GOBLIN,
            expected={
                "name": "Goblin",
                "label": "Lv. 12-15",
                "detail": "",
                "hunting_ground_key": None,
                "hunting_ground": "",
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
        SchemaTest(required_keys=["key", "offset", "size"]),
        DeclaredCountTest(declared=header_count(offset=0)),
        TargetTest(col="key", value=_BASILISK_DEN, expected={}),
    ],
)


@pytest.fixture(scope="module")
def marker_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_MARKER_RESULT", None)
    if result is None:
        result = run_case(replace(MARKER_CASE, tests=[]))
        request.module._MARKER_RESULT = result
    return result


@pytest.fixture(scope="module")
def offset_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_OFFSET_RESULT", None)
    if result is None:
        result = run_case(replace(OFFSET_CASE, tests=[]))
        request.module._OFFSET_RESULT = result
    return result


@pytest.mark.parametrize("spec", MARKER_CASE.tests, ids=case_id)
def test_worldmapmonster_dbss(spec: Any, marker_result: HandlerResult) -> None:
    marker_result.check(spec)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_worldmapmonsteroffset_dbss(spec: Any, offset_result: HandlerResult) -> None:
    offset_result.check(spec)


def test_every_marker_has_a_name(marker_result: HandlerResult) -> None:
    for record in marker_result.records:
        assert record["name_kr"], record["key"]


def test_marker_icon_index_matches_the_icon_column(marker_result: HandlerResult) -> None:
    """IndexKind.WORLDMAP_MARKER_ICON is this table's icons by key, without the empty ones."""
    source = marker_result.source
    index = build_worldmap_marker_icon_index(source.data, source.file(_OFFSET_FILE))

    assert index == {r["key"]: r["icon_path"] for r in marker_result.records if r["icon_path"]}

from __future__ import annotations

import struct
from collections import defaultdict
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
    UserLanguageTest,
    case_id,
    header_count,
    run_case,
)

from _common.pabr_offset import parse_bare_offset_rows
from _common.skill import skill_key
from .parser import FILE_NAME, OFFSET_FILE, parse_skillpiece_records


# Combined Magic Crystal - Gervish, the set skill the buff.dbss doc follows.
_GERVISH = 56050
# Agony Weapon, a set skill whose tiers have no text.
_AGONY_WEAPON = 50068
# The offset index points past the u16 key prefix of each record.
_KEY_PREFIX_SIZE = 2
_U16_MAX = 0xFFFF


CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["set_name", "requires", "effects"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(
            required_keys=[
                "skill_key", "skill_no", "point", "level", "set_name", "requires",
                "effects", "buff_ids", "buffs",
                "group_title_kr", "desc_title_kr", "desc_kr", "unknown_end",
            ]
        ),
        RangeTest(col="level", min_val=1, max_val=_U16_MAX),
        TargetTest(
            col="skill_key",
            value=skill_key(_GERVISH, 2),
            expected={"skill_no": _GERVISH, "level": 2},
        ),
        TargetTest(
            col="skill_key",
            value=skill_key(_AGONY_WEAPON, 1),
            expected={"skill_no": _AGONY_WEAPON, "level": 1, "requires": ""},
        ),
        UserLanguageTest(fields=["set_name", "requires", "effects"]),
    ],
)

OFFSET_CASE = HandlerCase(
    handler_name=OFFSET_FILE,
    data_file=OFFSET_FILE,
    companion_files={},
    loc_file=None,
    uses_loc=False,
    loc_fields=[],
    internal_path=f"gamecommondata/binary/{OFFSET_FILE}",
    tests=[
        SchemaTest(required_keys=["skill_no", "offset", "size"]),
        DeclaredCountTest(declared=header_count()),
        TargetTest(col="skill_no", value=_GERVISH, expected={"skill_no": _GERVISH}),
    ],
)


@pytest.fixture(scope="module")
def skill_piece_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.fixture(scope="module")
def offset_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_OFFSET_RESULT", None)
    if result is None:
        result = run_case(replace(OFFSET_CASE, tests=[]))
        request.module._OFFSET_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_skillpiece_dbss(spec: Any, skill_piece_result: HandlerResult) -> None:
    skill_piece_result.check(spec)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_skillpieceoffset_dbss(spec: Any, offset_result: HandlerResult) -> None:
    offset_result.check(spec)


def test_the_file_count_is_the_number_of_set_skills(skill_piece_result: HandlerResult) -> None:
    (count,) = struct.unpack_from("<I", skill_piece_result.source.data, 0)
    assert len({r["skill_no"] for r in skill_piece_result.records}) == count


def test_tiers_run_from_level_1_with_rising_points(skill_piece_result: HandlerResult) -> None:
    tiers: dict[int, list[tuple[int, int]]] = defaultdict(list)
    for record in skill_piece_result.records:
        tiers[record["skill_no"]].append((record["level"], record["point"]))
    for skill_no, levels_and_points in tiers.items():
        levels = [level for level, _ in levels_and_points]
        points = [point for _, point in levels_and_points]
        assert levels == list(range(1, len(levels) + 1)), skill_no
        assert points == sorted(set(points)), skill_no


def test_every_offset_row_points_past_its_records_key_prefix() -> None:
    records = parse_skillpiece_records(load_binary_fixture(FILE_NAME))
    walked = {r["skill_no"]: (r["offset"] + _KEY_PREFIX_SIZE, r["size"] - _KEY_PREFIX_SIZE) for r in records}
    rows = parse_bare_offset_rows(load_binary_fixture(OFFSET_FILE))
    assert {row.entry_id: (row.offset, row.size) for row in rows} == walked


def _record(key_prefix: int, skill_no: int) -> bytes:
    """A record with no tiers and a zero end."""
    return struct.pack("<HIII", key_prefix, skill_no, 0, 0)


def test_a_key_prefix_that_misses_the_skill_raises() -> None:
    with pytest.raises(ValueError, match="has key 7 for skill 8"):
        parse_skillpiece_records(struct.pack("<I", 1) + _record(7, 8))


def test_bytes_after_the_last_record_raise() -> None:
    with pytest.raises(ValueError, match="bytes after its 1 records"):
        parse_skillpiece_records(struct.pack("<I", 1) + _record(8, 8) + bytes(4))


def test_a_record_past_the_file_raises() -> None:
    with pytest.raises(ValueError, match="runs past its record"):
        parse_skillpiece_records(struct.pack("<I", 2) + _record(8, 8))

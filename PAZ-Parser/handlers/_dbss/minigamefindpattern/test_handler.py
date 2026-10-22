from __future__ import annotations

import struct
from dataclasses import replace
from typing import Any

import pytest

from tests.case_input import CaseInput
from tests.fixtures import load_binary_fixture
from tests.framework import (
    DeclaredCountTest,
    HandlerCase,
    HandlerResult,
    RangeTest,
    SchemaTest,
    TargetTest,
    case_id,
    run_case,
)

from .handler import pattern_image_path
from .parser import DIRECTION_COUNT, FILE_NAME, OFFSET_FILE, parse_minigamefindpatternoffset


_U16 = struct.Struct("<H")
# The index points past the u16 key, at its copy.
_KEY_SIZE = 2
# The root tiles: slot 0, pattern 1 (clients 1784 and 3482).
_ROOT_SLOT = 0
_IMAGE_FOLDER = "ui_texture/new_ui_common_forlua/window/minigame/"


def _index_rows(source: CaseInput) -> int:
    """The rows `minigamefindpatternoffset.dbss` lists, over all its groups."""
    return len(parse_minigamefindpatternoffset(source.file(OFFSET_FILE)))


CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={OFFSET_FILE: OFFSET_FILE},
    loc_file=None,
    uses_loc=False,
    loc_fields=[],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(
            required_keys=[
                "slot_index",
                "pattern_index",
                "pattern_index_dup",
                "change_pattern",
                "root_begin_no",
                "root_size",
                "image_file",
                "image_file2",
                "slot_coordinate",
                "next_pattern_end_direction",
                "root_begin_direction",
                "next_pattern_indexes",
                "image_path",
                "end_direction_name",
            ],
        ),
        DeclaredCountTest(declared=_index_rows),
        RangeTest(col="next_pattern_end_direction", min_val=0, max_val=DIRECTION_COUNT - 1),
        TargetTest(col="slot_index", value=_ROOT_SLOT, expected={"pattern_index": 1}),
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
        SchemaTest(required_keys=["slot_index", "pattern_index", "data_offset", "data_size"]),
        TargetTest(col="slot_index", value=_ROOT_SLOT, expected={"pattern_index": 1}),
    ],
)


@pytest.fixture(scope="module")
def pattern_result(request: Any) -> HandlerResult:
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
def test_minigamefindpattern_dbss(spec: Any, pattern_result: HandlerResult) -> None:
    pattern_result.check(spec)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_minigamefindpatternoffset_dbss(spec: Any, offset_result: HandlerResult) -> None:
    offset_result.check(spec)


def test_each_row_repeats_its_key(pattern_result: HandlerResult) -> None:
    assert all(r["pattern_index"] == r["pattern_index_dup"] for r in pattern_result.records)


def test_keys_are_unique_per_slot(pattern_result: HandlerResult) -> None:
    keys = [(r["slot_index"], r["pattern_index"]) for r in pattern_result.records]
    assert len(keys) == len(set(keys))


def test_next_patterns_are_in_the_same_slot(pattern_result: HandlerResult) -> None:
    keys = {(r["slot_index"], r["pattern_index"]) for r in pattern_result.records}
    for r in pattern_result.records:
        missing = [index for index in r["next_pattern_indexes"] if (r["slot_index"], index) not in keys]
        assert not missing, (r["slot_index"], r["pattern_index"], missing)


def test_at_most_one_begin_direction(pattern_result: HandlerResult) -> None:
    assert all(sum(r["root_begin_direction"]) <= 1 for r in pattern_result.records)


def test_image_paths_sit_in_the_minigame_folder(pattern_result: HandlerResult) -> None:
    paths = {r["image_path"] for r in pattern_result.records if r["image_path"]}
    assert paths
    assert all(path.startswith(_IMAGE_FOLDER) and path.endswith(".dds") for path in paths), paths


def test_no_image_has_no_path() -> None:
    assert pattern_image_path("None") == ""
    assert pattern_image_path("") == ""


def test_offset_rows_point_at_their_rows(pattern_result: HandlerResult) -> None:
    """Every index row points 2 bytes into the row with its key; the rows of a slot follow its 5-byte head."""
    data = load_binary_fixture(FILE_NAME)
    index = parse_minigamefindpatternoffset(load_binary_fixture(OFFSET_FILE))
    assert sorted((row.slot_index, row.pattern_index) for row in index) == sorted(
        (r["slot_index"], r["pattern_index"]) for r in pattern_result.records
    )
    for row in index:
        (key,) = _U16.unpack_from(data, row.data_offset - _KEY_SIZE)
        (key_dup,) = _U16.unpack_from(data, row.data_offset)
        assert key == key_dup == row.pattern_index, row
    ends = sorted(row.data_offset + row.data_size for row in index)
    assert ends[-1] == len(data)

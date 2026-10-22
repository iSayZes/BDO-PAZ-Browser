from __future__ import annotations

import struct
from collections import defaultdict
from collections.abc import Callable
from dataclasses import replace
from typing import Any

import pytest

from tests.case_input import CaseInput
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

from .parser import FILE_NAME, OFFSET_FILE, parse_itemeffectchange_records, parse_itemeffectchangeoffset_records


_COUNT_SIZE = 4
_INDEX_GROUP_HEAD_SIZE = 8
_INDEX_ROW_SIZE = 12
_ENTRY_HEAD = struct.Struct("<IBQ")
# A one-handed sword mesh: the EffectsChange sheet of client 1784 gives it 21
# levels with this model at level 0.
_SWORD_MESH = 336000
_SWORD_MODEL = "1_pc/1_phm/weapon/1_onehandsword/phm_01_ohs_0017_r.pac"


def _index_rows(companion: str | None = None) -> Callable[[CaseInput], int]:
    """The index rows `itemeffectchangeoffset.dbss` holds: its bytes after the group heads, in 12-byte rows."""

    def read(source: CaseInput) -> int:
        raw = source.file(companion)
        (group_count,) = struct.unpack_from("<I", raw, 0)
        body = len(raw) - _COUNT_SIZE - group_count * _INDEX_GROUP_HEAD_SIZE
        if body % _INDEX_ROW_SIZE:
            raise AssertionError(f"{body} bytes after the group heads are not whole {_INDEX_ROW_SIZE}-byte rows")
        return body // _INDEX_ROW_SIZE

    return read


CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={OFFSET_FILE: OFFSET_FILE},
    loc_file=None,
    uses_loc=False,
    loc_fields=[],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=["mesh_key", "enchant_level", "entry_count", "mesh_file"]),
        DeclaredCountTest(declared=_index_rows(OFFSET_FILE)),
        TargetTest(col="mesh_key", value=_SWORD_MESH, expected={"enchant_level": 0, "mesh_file": _SWORD_MODEL}),
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
        SchemaTest(required_keys=["mesh_key", "enchant_level", "offset", "size"]),
        DeclaredCountTest(declared=_index_rows()),
        TargetTest(col="mesh_key", value=_SWORD_MESH, expected={"enchant_level": 0}),
    ],
)


@pytest.fixture(scope="module")
def change_result(request: Any) -> HandlerResult:
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
def test_itemeffectchange_dbss(spec: Any, change_result: HandlerResult) -> None:
    change_result.check(spec)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_itemeffectchangeoffset_dbss(spec: Any, offset_result: HandlerResult) -> None:
    offset_result.check(spec)


def test_each_group_holds_one_mesh_key_with_levels_from_zero(change_result: HandlerResult) -> None:
    levels: dict[int, list[int]] = defaultdict(list)
    counts: dict[int, set[int]] = defaultdict(set)
    for record in change_result.records:
        levels[record["mesh_key"]].append(record["enchant_level"])
        counts[record["mesh_key"]].add(record["entry_count"])
    bad = [key for key, found in levels.items() if found != list(range(len(found))) or counts[key] != {len(found)}]
    assert not bad, bad


def test_every_index_row_points_at_its_entry() -> None:
    data = load_binary_fixture(FILE_NAME)
    rows = parse_itemeffectchangeoffset_records(load_binary_fixture(OFFSET_FILE))
    problems = []
    for row in rows:
        mesh_key, level, path_length = _ENTRY_HEAD.unpack_from(data, row["offset"])
        if (mesh_key, level, _ENTRY_HEAD.size + path_length) != (row["mesh_key"], row["enchant_level"], row["size"]):
            problems.append(row)
    assert not problems, problems[:5]
    assert len({row["offset"] for row in rows}) == len(parse_itemeffectchange_records(data))


def test_a_small_table_reads_back() -> None:
    entry = _ENTRY_HEAD.pack(7, 0, 5) + b"a.pac"
    data = struct.pack("<II", 1, 1) + entry
    assert parse_itemeffectchange_records(data) == [
        {"mesh_key": 7, "enchant_level": 0, "entry_count": 1, "mesh_file": "a.pac"},
    ]
    with pytest.raises(ValueError):
        parse_itemeffectchange_records(data + b"\x00")

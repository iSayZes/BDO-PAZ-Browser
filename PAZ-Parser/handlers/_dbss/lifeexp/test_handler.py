from __future__ import annotations

import struct
from dataclasses import replace
from typing import Any

import pytest

from tests.fixtures import load_binary_fixture
from tests.framework import (
    CaseInput,
    DeclaredCount,
    DeclaredCountTest,
    HandlerCase,
    HandlerResult,
    RangeTest,
    SchemaTest,
    TargetTest,
    case_id,
    run_case,
)

from _bss.stringtable.parser import GAME_SHEET, parse_key_hashes
from _dbss.lifeexp.labels import KEY_HASHES, LIFE_SKILLS
from _dbss.lifeexp.parser import parse_lifeexp_records, parse_lifeexpoffset_records


_OFFSET_FILE = "lifeexpoffset.dbss"
_LEVEL_ROW_SIZE = 13
_OFFSET_ROW_SIZE = 12
_U32 = struct.Struct("<I")
_GATHERING = 0


def _block_rows(row_size: int, companion: str | None = None) -> DeclaredCount:
    """Rows the u32 block counts declare after the u32 life skill count,
    checking the blocks fill the file exactly."""

    def read(source: CaseInput) -> int:
        raw = source.file(companion)
        (skill_count,) = _U32.unpack_from(raw, 0)
        cursor = _U32.size
        total = 0
        for _ in range(skill_count):
            (count,) = _U32.unpack_from(raw, cursor)
            cursor += _U32.size + count * row_size
            total += count
        if cursor != len(raw):
            raise AssertionError(f"blocks end at {cursor}, file holds {len(raw)} bytes")
        return total

    return read


CASE = HandlerCase(
    handler_name="lifeexp.dbss",
    data_file="lifeexp.dbss",
    companion_files={_OFFSET_FILE: _OFFSET_FILE},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["life_skill_name", "rank"],
    internal_path="gamecommondata/binary/lifeexp.dbss",
    tests=[
        SchemaTest(required_keys=["life_skill", "life_skill_name", "level", "rank", "exp"]),
        DeclaredCountTest(declared=_block_rows(_LEVEL_ROW_SIZE)),
        DeclaredCountTest(declared=_block_rows(_OFFSET_ROW_SIZE, companion=_OFFSET_FILE)),
        RangeTest(col="life_skill", min_val=min(LIFE_SKILLS), max_val=max(LIFE_SKILLS)),
        RangeTest(col="exp", min_val=0, max_val=2**64 - 1),
        TargetTest(col="life_skill", value=0, expected={"life_skill_name": "Gathering"}),
        TargetTest(col="life_skill", value=5, expected={"life_skill_name": "Processing"}),
        TargetTest(col="life_skill", value=6, expected={"life_skill_name": "Training"}),
        TargetTest(col="life_skill", value=8, expected={"life_skill_name": "Farming"}),
        TargetTest(col="life_skill", value=11, expected={"life_skill_name": "Barter"}),
        # A spare slot without a name key keeps its enum name.
        TargetTest(col="life_skill", value=10, expected={"life_skill_name": "temp1"}),
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
        SchemaTest(required_keys=["life_skill", "level", "data_offset", "data_size"]),
        DeclaredCountTest(declared=_block_rows(_OFFSET_ROW_SIZE)),
        RangeTest(col="data_size", min_val=_LEVEL_ROW_SIZE, max_val=_LEVEL_ROW_SIZE),
        # The first Gathering row follows the data file's skill count and level count.
        TargetTest(col="life_skill", value=_GATHERING, expected={"level": 0, "data_offset": 8}),
    ],
)


@pytest.fixture(scope="module")
def lifeexp_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_LIFEEXP_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._LIFEEXP_RESULT = result
    return result


@pytest.fixture(scope="module")
def offset_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_OFFSET_RESULT", None)
    if result is None:
        result = run_case(replace(OFFSET_CASE, tests=[]))
        request.module._OFFSET_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_lifeexp_dbss(spec: Any, lifeexp_result: HandlerResult) -> None:
    lifeexp_result.check(spec)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_lifeexpoffset_dbss(spec: Any, offset_result: HandlerResult) -> None:
    offset_result.check(spec)


def test_label_hashes_match_stringtable() -> None:
    hashes = parse_key_hashes(load_binary_fixture("stringtable.bss"), GAME_SHEET)
    wrong = {
        key: (key_hash, hashes.get(key))
        for key, key_hash in KEY_HASHES[GAME_SHEET].items()
        if hashes.get(key) != key_hash
    }
    assert not wrong, f"life skill label hashes differ from stringtable.bss (stored, file): {wrong}"


def test_each_life_skill_runs_from_level_zero(lifeexp_result: HandlerResult) -> None:
    levels: dict[int, list[int]] = {}
    for record in lifeexp_result.records:
        levels.setdefault(record["life_skill"], []).append(record["level"])
    for life_skill, skill_levels in levels.items():
        assert skill_levels == list(range(len(skill_levels))), life_skill


def test_rank_follows_the_client_level_groups(lifeexp_result: HandlerResult) -> None:
    ranks = {
        record["level"]: record["rank"]
        for record in lifeexp_result.records
        if record["life_skill"] == _GATHERING
    }
    assert ranks[0] is None
    assert ranks[1] == "Beginner 1"
    assert ranks[10] == "Beginner 10"
    assert ranks[11] == "Apprentice 1"
    assert ranks[21] == "Skilled 1"
    assert ranks[31] == "Professional 1"
    assert ranks[50] == "Artisan 10"
    assert ranks[51] == "Master 1"
    assert ranks[80] == "Master 30"
    assert ranks[81] == "Guru 1"


def test_a_row_of_another_life_skill_raises(lifeexp_result: HandlerResult) -> None:
    offset_data = lifeexp_result.source.file(_OFFSET_FILE)
    first_row = parse_lifeexpoffset_records(offset_data)[0]
    data = bytearray(lifeexp_result.source.data)
    data[first_row["data_offset"]] += 1
    with pytest.raises(ValueError, match="row holds life skill"):
        parse_lifeexp_records(bytes(data), offset_data)


def test_different_life_skill_counts_raise(lifeexp_result: HandlerResult) -> None:
    data = bytearray(lifeexp_result.source.data)
    _U32.pack_into(data, 0, _U32.unpack_from(data, 0)[0] + 1)
    with pytest.raises(ValueError, match="counts"):
        parse_lifeexp_records(bytes(data), lifeexp_result.source.file(_OFFSET_FILE))


def test_offset_blocks_that_miss_the_file_end_raise() -> None:
    with pytest.raises(ValueError, match="blocks end"):
        parse_lifeexpoffset_records(_U32.pack(0) + bytes(4))

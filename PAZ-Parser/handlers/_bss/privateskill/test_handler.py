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

from _bss.publicskill.parser import FILE_NAME as PUBLICSKILL_FILE, parse_publicskill_keys
from _common.skill import skill_key
from _dbss.skillsimply.parser import parse_skillsimply_records
from .parser import ACTIVE_KIND, FILE_NAME, PASSIVE_KIND, parse_privateskill_records

# Ground Roar, a Warrior active skill, and Sword Training, a Musa passive.
_GROUND_ROAR = 216
_SWORD_TRAINING = 1
_SKILLSIMPLY_FILE = "skillsimply.dbss"
_SKILLSIMPLY_OFFSET_FILE = "skillsimplyoffset.dbss"
_COUNT_SIZE = 4
_ROW_SIZE = 12
_ACTIVE_COUNT_OFFSET = 4


def _both_counts(source: CaseInput) -> int:
    """`active_count` at 0x04 plus `passive_count` right after the active rows."""
    raw = source.file(None)
    active = struct.unpack_from("<I", raw, _ACTIVE_COUNT_OFFSET)[0]
    passive_offset = _ACTIVE_COUNT_OFFSET + _COUNT_SIZE + active * _ROW_SIZE
    return active + struct.unpack_from("<I", raw, passive_offset)[0]


CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["skill", "classes"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=["skill_key", "skill_no", "level", "skill", "kind", "kind_label", "class_mask", "classes"]),
        DeclaredCountTest(declared=_both_counts),
        RangeTest(col="kind", min_val=ACTIVE_KIND, max_val=PASSIVE_KIND),
        TargetTest(
            col="skill_key",
            value=skill_key(_GROUND_ROAR, 1),
            expected={"skill": "Ground Roar I", "kind": ACTIVE_KIND, "kind_label": "Active", "classes": "Warrior"},
        ),
        TargetTest(
            col="skill_key",
            value=skill_key(_SWORD_TRAINING, 1),
            expected={"skill": "Sword Training I", "kind": PASSIVE_KIND, "kind_label": "Passive", "classes": "Musa"},
        ),
    ],
)


@pytest.fixture(scope="module")
def privateskill_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_privateskill_bss(spec: Any, privateskill_result: HandlerResult) -> None:
    privateskill_result.check(spec)


def test_every_key_is_level_1_and_in_one_list(privateskill_result: HandlerResult) -> None:
    records = privateskill_result.records
    assert {r["level"] for r in records} == {1}
    assert len({r["skill_key"] for r in records}) == len(records)


def test_no_key_is_in_publicskill() -> None:
    public = set(parse_publicskill_keys(load_binary_fixture(PUBLICSKILL_FILE)))
    shared = [r["skill_key"] for r in parse_privateskill_records(load_binary_fixture(FILE_NAME)) if r["skill_key"] in public]
    assert not shared, shared


def test_kind_and_class_mask_follow_skillsimply() -> None:
    simply = {
        record.skill_key: (record.kind, record.class_mask)
        for record in parse_skillsimply_records(
            load_binary_fixture(_SKILLSIMPLY_FILE), load_binary_fixture(_SKILLSIMPLY_OFFSET_FILE)
        )
    }
    wrong = [
        r["skill_key"]
        for r in parse_privateskill_records(load_binary_fixture(FILE_NAME))
        if simply.get(r["skill_key"]) != (r["kind"], r["class_mask"])
    ]
    assert not wrong, wrong


_U32 = struct.Struct("<I")
_ROW = struct.Struct("<IQ")


def _list(*rows: tuple[int, int]) -> bytes:
    return _U32.pack(len(rows)) + b"".join(_ROW.pack(*row) for row in rows)


def _file(*lists: bytes) -> bytes:
    """PABR, the given lists and an empty string table."""
    body = b"PABR" + b"".join(lists)
    return body + _U32.pack(0) + _U32.pack(len(body)) + bytes(4)


def test_both_lists_are_read_with_their_kind() -> None:
    ground_roar = skill_key(_GROUND_ROAR, 1)
    sword_training = skill_key(_SWORD_TRAINING, 1)
    records = parse_privateskill_records(_file(_list((ground_roar, 0x1)), _list((sword_training, 0x100000))))
    assert records == [
        {"skill_key": ground_roar, "class_mask": 0x1, "kind": ACTIVE_KIND},
        {"skill_key": sword_training, "class_mask": 0x100000, "kind": PASSIVE_KIND},
    ]


def test_rows_short_of_the_string_table_are_rejected() -> None:
    with pytest.raises(ValueError, match="string table starts"):
        parse_privateskill_records(_file(_list(), _list(), _U32.pack(0)))


def test_a_count_past_the_string_table_is_rejected() -> None:
    with pytest.raises(ValueError, match="runs past the end"):
        parse_privateskill_records(_file(_U32.pack(5) + _ROW.pack(1, 1)))

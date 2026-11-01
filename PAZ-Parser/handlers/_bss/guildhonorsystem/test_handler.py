from __future__ import annotations

import struct
from dataclasses import replace
from typing import Any

import pytest

from tests.case_input import CaseInput
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

from _bss.boss_spawnlevel.parser import FILE_NAME as LEVEL_FILE
from .parser import FILE_NAME, HEAD_FIELDS, parse_guildhonorsystem
from .records import (
    BENEFIT_SECTION,
    CHANGE_REASON_SECTION,
    DAILY_INCENTIVE_SECTION,
    bonus_percent_text,
    guild_honor_records,
)


_HEAD_SIZE = 0x40
_U32 = struct.Struct("<I")
_U64 = struct.Struct("<Q")
_REASON_TAIL_SIZE = 24
_BENEFIT_TAIL_SIZE = 29
_DAILY_INCENTIVE_SIZE = 12
# `reason_type` of War Declaration: the reason the war declaration window asks with `reason_param` 0.
_DECLARE_WAR = 1004
# `reason_type` of an added guild boss summon, asked with a boss_spawn.bss key.
_ADD_BOSS_SUMMON = 1006


def _skip_rows(data: bytes, pos: int, tail_size: int) -> tuple[int, int]:
    """The count at `pos` and the offset after its rows of u32 key, str16 text and a fixed tail."""
    (count,) = _U32.unpack_from(data, pos)
    pos += _U32.size
    for _ in range(count):
        (length,) = _U64.unpack_from(data, pos + _U32.size)
        pos += _U32.size + _U64.size + 2 * length + tail_size
    return count, pos


def _declared_rows(source: CaseInput) -> int:
    """The three list counts the file stores, the last list ending at the last byte."""
    data = source.data
    reasons, pos = _skip_rows(data, _HEAD_SIZE, _REASON_TAIL_SIZE)
    benefits, pos = _skip_rows(data, pos, _BENEFIT_TAIL_SIZE)
    (steps,) = _U32.unpack_from(data, pos)
    end = pos + _U32.size + steps * _DAILY_INCENTIVE_SIZE
    if end != len(data):
        raise AssertionError(f"daily pay steps end at 0x{end:X}, the file at 0x{len(data):X}")
    return reasons + benefits + steps


CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={LEVEL_FILE: LEVEL_FILE},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["description"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=["section", "key", "point", "description", "type_value", "details_text"]),
        DeclaredCountTest(declared=_declared_rows),
        # Mission range, MissionChargeIncrease, UnlockGuildSkill, UpgradeGuildSkill.
        RangeTest(col="benefit_type", min_val=0, max_val=3),
        TargetTest(col="reason_type", value=_DECLARE_WAR, expected={"section": CHANGE_REASON_SECTION, "reason_param": 0}),
        UserLanguageTest(fields=["description"]),
    ],
)


@pytest.fixture(scope="module")
def honor_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_guildhonorsystem_bss(spec: Any, honor_result: HandlerResult) -> None:
    honor_result.check(spec)


def test_the_change_reason_count_sits_after_the_head(honor_result: HandlerResult) -> None:
    reasons = [r for r in honor_result.records if r["section"] == CHANGE_REASON_SECTION]
    assert len(reasons) == header_count(offset=_HEAD_SIZE)(honor_result.source)


def test_every_row_repeats_its_key(honor_result: HandlerResult) -> None:
    keyed = [r for r in honor_result.records if r["section"] != DAILY_INCENTIVE_SECTION]
    assert keyed
    assert all(r["key_dup"] == r["key"] for r in keyed)


def test_boss_summons_name_their_boss(honor_result: HandlerResult) -> None:
    summons = [r for r in honor_result.records if r.get("reason_type") == _ADD_BOSS_SUMMON and r["reason_param"]]
    assert summons
    assert all(r["details_text"].startswith(f"{r['reason_param']} ") for r in summons)


def test_the_benefit_rows_carry_a_type(honor_result: HandlerResult) -> None:
    benefits = [r for r in honor_result.records if r["section"] == BENEFIT_SECTION]
    assert benefits
    assert all(r["type_value"] == r["benefit_type"] for r in benefits)


def _text(value: str) -> bytes:
    raw = value.encode("utf-16-le")
    return _U64.pack(len(value)) + raw


def _built_file() -> bytes:
    """A head, one change reason (a boss summon), one skill upgrade benefit and one daily pay step."""
    head = struct.pack("<Qqq5Q", 0x7FF600000000, -2, 1, 2, 3, 4, 5, 6)
    reason = _U32.pack(7) + _text("a") + struct.pack("<qQII", -25, 8, 7, _ADD_BOSS_SUMMON)
    benefit = _U32.pack(3) + _text("bc") + struct.pack("<qQQIB", 500, 62858 << 16 | 1, 62864 << 16 | 1, 3, 3)
    step = struct.pack("<qI", 50, 500_000)
    return head + _U32.pack(1) + reason + _U32.pack(1) + benefit + _U32.pack(1) + step


def test_a_built_file_reads_back() -> None:
    system = parse_guildhonorsystem(_built_file())
    assert tuple(system.head) == HEAD_FIELDS
    assert system.head["min_guild_fame"] == -2
    assert system.change_reasons == [
        {"key": 7, "description_kr": "a", "point": -25, "reason_param": 8, "key_dup": 7, "reason_type": _ADD_BOSS_SUMMON}
    ]
    assert system.benefits[0]["param_2"] >> 16 == 62864
    assert system.benefits[0]["benefit_type"] == 3
    assert system.daily_incentives == [{"point": 50, "bonus_percent": 500_000}]


def test_built_records_join_their_labels() -> None:
    records = guild_honor_records(
        parse_guildhonorsystem(_built_file()),
        boss_label=lambda key: f"boss {key}",
        skill_label=lambda key: f"skill {key >> 16}",
    )
    assert [r["section"] for r in records] == [CHANGE_REASON_SECTION, BENEFIT_SECTION, DAILY_INCENTIVE_SECTION]
    assert records[0]["details_text"] == "boss 8"
    assert records[1]["details_text"] == "skill 62858 → skill 62864"
    assert records[2]["details_text"] == "+50%"


def test_the_bonus_is_on_the_ten_thousand_per_percent_scale() -> None:
    assert bonus_percent_text(9_000_000) == "900"
    assert bonus_percent_text(5_000) == "0.5"


@pytest.mark.parametrize(
    "data",
    [_built_file()[:-1], _built_file() + b"\0", _built_file()[:_HEAD_SIZE - 1]],
    ids=["cut_short", "trailing_byte", "head_only"],
)
def test_a_changed_file_raises(data: bytes) -> None:
    with pytest.raises(ValueError):
        parse_guildhonorsystem(data)

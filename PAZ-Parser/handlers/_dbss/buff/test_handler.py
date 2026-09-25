from __future__ import annotations

from dataclasses import replace
from typing import Any

import pytest

from tests.framework import (
    CountTest,
    HandlerCase,
    HandlerResult,
    PosTest,
    RangeTest,
    SchemaTest,
    TargetTest,
    case_id,
    run_case,
)

from .handler import extract_title, format_duration


BUFF_CASE = HandlerCase(
    handler_name="buff.dbss",
    data_file="buff.dbss",
    companion_files={"buffoffset.dbss": "buffoffset.dbss"},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["description"],
    internal_path="gamecommondata/binary/buff.dbss",
    tests=[
        SchemaTest(
            required_keys=[
                "buff_id",
                "name",
                "level",
                "effect_type",
                "duration_ms",
                "duration",
                "icon_path",
                "title",
                "description",
                "description_kr",
                "param_1",
                "param_10",
                "is_shown",
                "apply_rate",
            ]
        ),
        CountTest(expected=44609),
        PosTest(
            pos=0,
            expected={
                "buff_id": 48879,
                "name": "중범선 대미지 저항 18.9%",
                "level": 1,
                "effect_type": 106,
                "duration": "",
                "icon_path": "",
            },
        ),
        TargetTest(
            col="buff_id",
            value=48830,
            expected={
                "name": "수렵 숙련도 +70 3시간",
                "effect_type": 149,
                "duration_ms": 10800000,
                "duration": "3h",
                "icon_path": "ui_texture/icon/new_icon/04_pc_skill/03_buff/huntingbuff.dds",
                "description": "Hunting Mastery +70",
                "title": "",
                "is_shown": True,
            },
        ),
        # EXP gain stores its bonus per million: 3,000,000 is +300%.
        TargetTest(
            col="buff_id",
            value=47692,
            expected={"effect_type": 25, "param_1": 3000000, "duration": "2h"},
        ),
        # Headline buff: the coloured first line of its description is its title.
        TargetTest(
            col="buff_id",
            value=48723,
            expected={
                "title": "[Blessing] Adventure's Boon",
                "name": "모든 공격력 +8(120분)",
                "duration": "2h",
                "is_shown": True,
            },
        ),
        # The rest of the same item's buff group is hidden and has no text.
        TargetTest(
            col="buff_id",
            value=48724,
            expected={"title": "", "description": "", "effect_type": 40, "is_shown": False},
        ),
        RangeTest(col="level", min_val=0, max_val=999),
        RangeTest(col="duration_ms", min_val=0, max_val=86400000),
    ],
)

OFFSET_CASE = HandlerCase(
    handler_name="buffoffset.dbss",
    data_file="buffoffset.dbss",
    companion_files={},
    loc_file=None,
    uses_loc=False,
    loc_fields=[],
    internal_path="gamecommondata/binary/buffoffset.dbss",
    tests=[
        SchemaTest(required_keys=["buff_id", "offset", "size"]),
        CountTest(expected=44609),
        PosTest(pos=0, expected={"buff_id": 48879, "offset": 4, "size": 233}),
        PosTest(pos=-1, expected={"buff_id": 17008, "offset": 12429928, "size": 229}),
    ],
)


@pytest.fixture(scope="module")
def buff_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_BUFF_RESULT", None)
    if result is None:
        result = run_case(replace(BUFF_CASE, tests=[]))
        request.module._BUFF_RESULT = result
    return result


@pytest.fixture(scope="module")
def offset_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_OFFSET_RESULT", None)
    if result is None:
        result = run_case(replace(OFFSET_CASE, tests=[]))
        request.module._OFFSET_RESULT = result
    return result


@pytest.mark.parametrize("spec", BUFF_CASE.tests, ids=case_id)
def test_buff_dbss(spec: Any, buff_result: HandlerResult) -> None:
    spec.check(buff_result.records)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_buffoffset_dbss(spec: Any, offset_result: HandlerResult) -> None:
    spec.check(offset_result.records)


@pytest.mark.parametrize(
    ("duration_ms", "expected"),
    [
        (0, ""),
        (1500, "1.5s"),
        (30000, "30s"),
        (1200000, "20m"),
        (5400000, "1h 30m"),
        (86400000, "24h"),
    ],
)
def test_format_duration(duration_ms: int, expected: str) -> None:
    assert format_duration(duration_ms) == expected


@pytest.mark.parametrize(
    ("raw", "expected"),
    [
        ("<PAColor0xffe9bd23>Eileen's Cheer<PAOldColor>\n\n  Alchemy Time -5 sec", "Eileen's Cheer"),
        ("<PAColor0xffe9bd23>[축복] 모험의 가호<PAOldColor>\r\n모든 공격력 +8", "[축복] 모험의 가호"),
        # One line is an effect, not a title.
        ("Hunting Mastery <PAColor0xffe9bd23>+70<PAOldColor>", ""),
        ("<PAColor0xffe9bd23>Life EXP +3%<PAOldColor>", ""),
        ("<PAColor0xffe9bd23>Trailing only<PAOldColor>\n  ", ""),
        ("", ""),
    ],
)
def test_extract_title(raw: str, expected: str) -> None:
    assert extract_title(raw) == expected

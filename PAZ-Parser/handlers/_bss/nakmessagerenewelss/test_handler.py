from __future__ import annotations

from dataclasses import replace
from typing import Any

import pytest

from tests.framework import (
    DeclaredCountTest,
    HandlerCase,
    HandlerResult,
    PaFieldTest,
    SchemaTest,
    TargetTest,
    UserLanguageTest,
    case_id,
    header_count,
    run_case,
)

from .parser import EXIST_FIELDS, FILE_NAME


# Message type 0 is the Safe Zone message, `__eNakMessage_SafetyArea`'s row.
_SAFETY_AREA = 0

CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["main_message", "sub_message"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=[
            "nak_message_type", *EXIST_FIELDS, "ani_time", "contents_group_hash",
            "main_bg", "sub_bg", "main_text", "sub_text", "sub_text2", "sub_text3",
            "effects", "sounds", "icon_span_y", "main_message", "sub_message", "contents_group",
        ]),
        DeclaredCountTest(declared=header_count(offset=0)),
        TargetTest(
            col="nak_message_type",
            value=_SAFETY_AREA,
            expected={"main_bg_texture": "NakMessage_NakBG_Safety_01"},
        ),
        PaFieldTest(field="main_message"),
        UserLanguageTest(fields=["main_message", "sub_message"]),
    ],
)


@pytest.fixture(scope="module")
def nak_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_nakmessagerenewelss_bss(spec: Any, nak_result: HandlerResult) -> None:
    nak_result.check(spec)


def test_message_types_are_unique(nak_result: HandlerResult) -> None:
    keys = [r["nak_message_type"] for r in nak_result.records]
    assert len(keys) == len(set(keys))


def test_exist_flags_match_their_parts(nak_result: HandlerResult) -> None:
    """Each `is_exist_*` flag is set exactly when its part holds data (doc, Row notes)."""
    for r in nak_result.records:
        parts = {
            "is_exist_sub_bg": r["sub_bg"]["texture_id"] != "",
            "is_exist_sub_text": r["sub_text"]["text_kr"] != "",
            "is_exist_sub_text2": r["sub_text2"]["text_kr"] != "",
            "is_exist_sub_text3": r["sub_text3"]["text_kr"] != "",
            "is_exist_effect_bg": bool(r["effects"]),
            "is_exist_sound_list": bool(r["sounds"]),
        }
        for field, has_part in parts.items():
            assert r[field] == has_part, (r["nak_message_type"], field)


def test_every_contents_group_hash_is_a_key(nak_result: HandlerResult) -> None:
    for r in nak_result.records:
        assert r["contents_group"] is not None, (r["nak_message_type"], hex(r["contents_group_hash"]))


def test_every_text_line_has_loc_text(nak_result: HandlerResult) -> None:
    """A line with Korean text has an English LOC type 132 text, so no cell falls back to Korean.

    Rows `285` to `288` store a single space as their sub text.
    """
    for r in nak_result.records:
        for text, message in (("main_text", "main_message"), ("sub_text", "sub_message")):
            if r[text]["text_kr"].strip():
                assert r[message], (r["nak_message_type"], text)

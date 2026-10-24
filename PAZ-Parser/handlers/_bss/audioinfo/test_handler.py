from __future__ import annotations

import struct
from dataclasses import replace
from typing import Any

import pytest

from tests.fixtures import load_binary_fixture
from tests.framework import HandlerCase, HandlerResult, SchemaTest, case_id, run_case

from _bss.audioinfo.bgm_states import BGM_STATE_SLOTS
from _bss.audioinfo.parser import (
    FILE_NAME,
    SECTION_AREA,
    SECTION_RADIO,
    SECTION_STATE,
    STATE_ENTRY_COUNT,
    parse_audioinfo_records,
)


# PABR magic, then the u32 row count.
_COUNT_OFFSET = 4
_BGM_GROUP = "BGM"
_RADIO_EVENT_PREFIX = "BGM_Radio"

CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file=None,
    uses_loc=False,
    loc_fields=[],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(
            required_keys=[
                "section",
                "section_name",
                "color_hex",
                "state_group_text",
                "states_text",
                "bank_no_environment",
                "channel_name_text",
                "event_name_text",
            ]
        ),
    ],
)

_AREA_KEYS = {"color", "color_dup", "bgm_states", "bgm_state_names", "bgm_states_text", "bank_no_environment"}
_STATE_KEYS = {"unknown_00", "unknown_01", "state_group", "state_group_text", "state_name", "state_name_text"}
_RADIO_KEYS = {
    "unknown_00", "unknown_04", "unknown_04_text", "channel_name", "channel_name_text",
    "event_name", "event_name_text", "unknown_10",
}


@pytest.fixture(scope="module")
def audio_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_audioinfo_bss(spec: Any, audio_result: HandlerResult) -> None:
    audio_result.check(spec)


def _section(result: HandlerResult, section: str) -> list[dict]:
    return [r for r in result.records if r["section"] == section]


def test_area_rows_match_the_declared_count(audio_result: HandlerResult) -> None:
    (count,) = struct.unpack_from("<I", load_binary_fixture(FILE_NAME), _COUNT_OFFSET)
    assert len(_section(audio_result, SECTION_AREA)) == count


def test_each_section_has_its_fields(audio_result: HandlerResult) -> None:
    for section, keys in ((SECTION_AREA, _AREA_KEYS), (SECTION_STATE, _STATE_KEYS), (SECTION_RADIO, _RADIO_KEYS)):
        rows = _section(audio_result, section)
        assert rows, section
        assert all(keys <= r.keys() for r in rows), section


def test_area_colours_are_unique_and_doubled(audio_result: HandlerResult) -> None:
    areas = _section(audio_result, SECTION_AREA)
    assert len({r["color"] for r in areas}) == len(areas)
    assert all(r["color"] == r["color_dup"] for r in areas)
    assert all(len(r["bgm_states"]) == BGM_STATE_SLOTS for r in areas)


def test_state_entries_are_bgm_states_with_distinct_keys(audio_result: HandlerResult) -> None:
    states = _section(audio_result, SECTION_STATE)
    assert len(states) == STATE_ENTRY_COUNT
    assert len({r["unknown_00"] for r in states}) == len(states)
    assert all(r["state_group_text"] == _BGM_GROUP for r in states)


def test_radio_entries_name_radio_events(audio_result: HandlerResult) -> None:
    radios = _section(audio_result, SECTION_RADIO)
    assert all(r["event_name_text"].startswith(_RADIO_EVENT_PREFIX) for r in radios)


def _pstr(text: str) -> bytes:
    raw = text.encode("utf-8")
    return struct.pack("<BI", 0, len(raw)) + raw


def _file(state_count: int, tail: bytes) -> bytes:
    body = b"PABR" + struct.pack("<I", 1)
    body += struct.pack("<II4II", 0x4600, 0x4600, 0, 0, 1, 0, 110)
    body += b"".join(struct.pack("<BBII", key, 255, 2, 0) for key in range(state_count))
    body += struct.pack("<I", 1) + struct.pack("<IIIIB", 1, 0, 3, 4, 1)
    body += struct.pack("<I", len(tail)) + tail
    table_start = len(body)
    strings = ["W01_A", "W01_Boss", "BGM", "Channel", "BGM_Radio_Chanel_01"]
    body += struct.pack("<I", len(strings)) + b"".join(_pstr(text) for text in strings)
    return body + struct.pack("<II", table_start, 0)


def test_parse_reads_every_section() -> None:
    records = parse_audioinfo_records(_file(STATE_ENTRY_COUNT, bytes([0, 2, 3])))

    area, *states, radio = records
    assert area["bgm_state_names"] == ["W01_A", "W01_A", "W01_Boss", "W01_A"]
    assert area["bank_no_environment"] == 110
    assert [r["unknown_00"] for r in states] == list(range(STATE_ENTRY_COUNT))
    assert states[0]["state_group_text"] == "BGM"
    assert (radio["channel_name_text"], radio["event_name_text"]) == ("Channel", "BGM_Radio_Chanel_01")


def test_parse_rejects_another_state_entry_count() -> None:
    with pytest.raises(ValueError):
        parse_audioinfo_records(_file(STATE_ENTRY_COUNT - 1, bytes([0, 2, 3])))

from __future__ import annotations

import struct
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
    case_id,
    header_count,
    run_case,
)

from _bss.midiinstrument.parser import FILE_NAME, KEY_FIELD, parse_midiinstrument, parse_midiinstrument_records


# PABR magic, then the u32 row count.
_COUNT_OFFSET = 4
# Instrument 0 is the Acoustic Guitar in the client 1784 MidiInstrument_Table sheet and on client 3482.
_GUITAR = 0
_GUITAR_BANK = "MIDI_Instrument_00_AcousticGuitar"
_TAB_KEY_PREFIX = "AUDIO_MIDI_TAB_"
# Novice, Advanced and the electronic tab.
_ADVANCED_TYPE_MAX = 2

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
                "index",
                "bank_name",
                "event_name",
                "ingame_name",
                "articulation_count",
                "articulations",
                "start_action_hash",
                "end_action_hash",
                "advanced_type",
                "instrument_name_type",
                "is_opened",
                "ing_action_count",
                "ing_action_hashes",
                "is_provided",
                "unknown_ing_action_hashes_01",
                "unknown_ing_action_hashes_02",
                "unknown_ing_action_hashes_03",
                "bank_name_text",
                "event_name_text",
                "ingame_name_text",
                "instrument_name_type_text",
                "advanced_type_name",
            ]
        ),
        DeclaredCountTest(declared=header_count(offset=_COUNT_OFFSET)),
        RangeTest(col="advanced_type", min_val=0, max_val=_ADVANCED_TYPE_MAX),
        TargetTest(col=KEY_FIELD, value=_GUITAR, expected={"bank_name_text": _GUITAR_BANK}),
    ],
)


@pytest.fixture(scope="module")
def midi_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_midiinstrument_bss(spec: Any, midi_result: HandlerResult) -> None:
    midi_result.check(spec)


def test_keys_are_unique(midi_result: HandlerResult) -> None:
    keys = [r[KEY_FIELD] for r in midi_result.records]
    assert len(keys) == len(set(keys))


def test_every_tab_key_is_a_composer_tab(midi_result: HandlerResult) -> None:
    wrong = [r[KEY_FIELD] for r in midi_result.records if not r["instrument_name_type_text"].startswith(_TAB_KEY_PREFIX)]
    assert not wrong, wrong


def test_action_hash_list_holds_each_start_and_loop_action_once() -> None:
    records, hashes = parse_midiinstrument(load_binary_fixture(FILE_NAME))
    used = {r["start_action_hash"] for r in records} | {h for r in records for h in r["ing_action_hashes"]}
    assert len(hashes) == len(set(hashes))
    assert set(hashes) == used


def _pstr(text: str) -> bytes:
    raw = text.encode("utf-8")
    return struct.pack("<BI", 0, len(raw)) + raw


def _file(articulations: list[int], ing_hashes: list[int], action_hashes: list[int], strings: list[str]) -> bytes:
    row = (
        struct.pack("<BIIIQ", 7, 0, 0, 1, len(articulations))
        + bytes(articulations)
        + struct.pack("<IIBIBI", 0x11, 0x22, 1, 2, 1, len(ing_hashes))
        + struct.pack(f"<{len(ing_hashes)}I", *ing_hashes)
        + bytes([1, 2, 7, 0])
    )
    body = b"PABR" + struct.pack("<I", 1) + row
    body += struct.pack(f"<I{len(action_hashes)}I", len(action_hashes), *action_hashes)
    table_start = len(body)
    body += struct.pack("<I", len(strings)) + b"".join(_pstr(text) for text in strings)
    return body + struct.pack("<II", table_start, 0)


def test_parse_reads_lists_and_string_texts() -> None:
    data = _file([0, 99], [0x33, 0x44], [0x11, 0x33, 0x44], ["Bank", "Name", "AUDIO_MIDI_TAB_ADVANCED"])

    records, hashes = parse_midiinstrument(data)

    record = records[0]
    assert record["index"] == 7
    assert record["articulations"] == [0, 99]
    assert record["ing_action_hashes"] == [0x33, 0x44]
    assert (record["bank_name_text"], record["ingame_name_text"]) == ("Bank", "Name")
    assert record["instrument_name_type_text"] == "AUDIO_MIDI_TAB_ADVANCED"
    assert (record["is_provided"], record["unknown_ing_action_hashes_02"]) == (1, 7)
    assert hashes == [0x11, 0x33, 0x44]


def test_parse_rejects_a_hash_list_that_stops_before_the_string_table() -> None:
    action_hashes = [0x11, 0x33]
    data = bytearray(_file([99], [0x33], action_hashes, ["Bank", "Name", "Tab"]))
    (table_start,) = struct.unpack_from("<I", data, len(data) - 8)
    count_at = table_start - 4 * (len(action_hashes) + 1)
    struct.pack_into("<I", data, count_at, len(action_hashes) - 1)
    with pytest.raises(ValueError):
        parse_midiinstrument_records(bytes(data))

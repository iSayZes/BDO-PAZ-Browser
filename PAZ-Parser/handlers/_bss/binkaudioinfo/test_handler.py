from __future__ import annotations

import struct
from dataclasses import replace
from typing import Any

import pytest

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

from _bss.binkaudioinfo.parser import FILE_NAME, parse_binkaudioinfo_records


# PABR magic, then the u32 row count.
_COUNT_OFFSET = 4
# ui_movie/pc/cutscene/abyssstory/goyen/goyen.bk2 and its sound bank bink_goyen.bnk.
_GOYEN = "Goyen"
_GOYEN_AUDIO = "Bink_Goyen"
_AUDIO_PREFIX = "Bink_"

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
                "movie_name",
                "audio_name",
                "audio_name_dup",
                "unknown_0c",
                "unknown_0d",
                "unknown_0e",
                "movie_name_text",
                "audio_name_text",
                "audio_name_dup_text",
            ]
        ),
        DeclaredCountTest(declared=header_count(offset=_COUNT_OFFSET)),
        TargetTest(col="movie_name_text", value=_GOYEN, expected={"audio_name_text": _GOYEN_AUDIO}),
    ],
)


@pytest.fixture(scope="module")
def bink_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_binkaudioinfo_bss(spec: Any, bink_result: HandlerResult) -> None:
    bink_result.check(spec)


def test_movie_names_are_unique(bink_result: HandlerResult) -> None:
    names = [r["movie_name_text"] for r in bink_result.records]
    assert len(names) == len(set(names))


def test_every_audio_name_is_a_bink_name_twice(bink_result: HandlerResult) -> None:
    wrong = [
        r["movie_name_text"]
        for r in bink_result.records
        if not r["audio_name_text"].startswith(_AUDIO_PREFIX) or r["audio_name_text"] != r["audio_name_dup_text"]
    ]
    assert not wrong, wrong


def _file(rows: list[tuple[int, int, int]], strings: list[str]) -> bytes:
    body = b"PABR" + struct.pack("<I", len(rows))
    for movie, audio, audio_dup in rows:
        body += struct.pack("<III3B", movie, audio, audio_dup, 1, 1, 1)
    table_start = len(body)
    body += struct.pack("<I", len(strings))
    for text in strings:
        raw = text.encode("utf-8")
        body += struct.pack("<BI", 0, len(raw)) + raw
    return body + struct.pack("<II", table_start, 0)


def test_parse_reads_the_names() -> None:
    data = _file([(0, 1, 1)], ["Goyen", "Bink_Goyen"])

    (record,) = parse_binkaudioinfo_records(data)

    assert (record["movie_name_text"], record["audio_name_text"]) == ("Goyen", "Bink_Goyen")
    assert (record["unknown_0c"], record["unknown_0d"], record["unknown_0e"]) == (1, 1, 1)


def test_parse_rejects_rows_that_stop_before_the_string_table() -> None:
    data = bytearray(_file([(0, 1, 1), (0, 1, 1)], ["A", "Bink_A"]))
    struct.pack_into("<I", data, _COUNT_OFFSET, 1)
    with pytest.raises(ValueError):
        parse_binkaudioinfo_records(bytes(data))

from __future__ import annotations

from dataclasses import replace
from typing import Any

import pytest

from tests.framework import (
    DeclaredCountTest,
    HandlerCase,
    HandlerResult,
    SchemaTest,
    TargetTest,
    UserLanguageTest,
    case_id,
    header_count,
    run_case,
)

from .parser import FILE_NAME, parse_instancefieldrankingmanage_records
from .times import utc_text


_STRINGTABLE_FILE = "stringtable.bss"
# PABR magic, then the u32 record count.
_COUNT_OFFSET = 4
_ROW_SIZE = 26
# Ranking 1, the first test season of the Old Moon Grand Prix (instance type 11), as the sheet writes it.
_FIRST_RANKING = 1

CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={_STRINGTABLE_FILE: _STRINGTABLE_FILE},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["season"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=[
            "ranking_idx", "instance_type", "start_date_rank", "end_date_rank", "ranking_name",
            "ranking_name_key", "start_text", "end_text", "season",
        ]),
        DeclaredCountTest(declared=header_count(offset=_COUNT_OFFSET)),
        UserLanguageTest(fields=["season"]),
        TargetTest(col="ranking_idx", value=_FIRST_RANKING, expected={
            "instance_type": 11,
            "ranking_name_key": "LUA_INSTANCE_SEASONRANK_NAME_1",
            "start_text": "2021-02-03 08:59",
            "end_text": "2021-02-05 14:09",
            "season": "Season 1",
        }),
    ],
)


@pytest.fixture(scope="module")
def manage_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_instancefieldrankingmanage_bss(spec: Any, manage_result: HandlerResult) -> None:
    manage_result.check(spec)


def test_ranking_keys_are_unique(manage_result: HandlerResult) -> None:
    keys = [record["ranking_idx"] for record in manage_result.records]
    assert len(keys) == len(set(keys))


def test_every_ranking_ends_after_it_starts(manage_result: HandlerResult) -> None:
    assert all(r["end_date_rank"] > r["start_date_rank"] for r in manage_result.records)


def test_every_name_index_names_a_game_key(manage_result: HandlerResult) -> None:
    assert all(r["ranking_name_key"].startswith("LUA_") for r in manage_result.records)


@pytest.mark.parametrize(("seconds", "text"), [
    (0, "1970-01-01 00:00"),
    (951_782_400, "2000-02-29 00:00"),
    (1_612_342_740, "2021-02-03 08:59"),
    (4_092_530_400, "2099-09-08 06:00"),
])
def test_utc_text(seconds: int, text: str) -> None:
    assert utc_text(seconds) == text


def test_bad_magic_raises() -> None:
    with pytest.raises(ValueError):
        parse_instancefieldrankingmanage_records(b"XXXX" + bytes(16))


def test_rows_must_end_at_the_string_table() -> None:
    # One declared row, but the string table starts right after the count.
    data = b"PABR" + (1).to_bytes(4, "little") + bytes(_ROW_SIZE) + bytes(4) + (8).to_bytes(4, "little") + bytes(4)
    with pytest.raises(ValueError):
        parse_instancefieldrankingmanage_records(data)

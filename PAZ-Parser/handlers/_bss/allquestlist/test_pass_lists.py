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
    TestSpec as Spec,
    case_id,
    header_count,
    run_case,
)


_FULL = "seasonpassquestlist.bss"
_CASH = "seasonpassquestlistforcash.bss"
_NORMAL = "seasonpassquestlistfornormal.bss"
_GROWTH = "growthpassquestlist.bss"


def _case(name: str, *extra: Spec) -> HandlerCase:
    return HandlerCase(
        handler_name=name,
        data_file=name,
        companion_files={},
        loc_file="languagedata_en.loc",
        uses_loc=True,
        loc_fields=["Title"],
        internal_path=f"gamecommondata/binary/{name}",
        tests=[
            SchemaTest(required_keys=["slot", "packed_quest_id", "quest_chain_id", "quest_id", "title"]),
            # The u32 count after the PABR magic.
            DeclaredCountTest(declared=header_count(offset=4)),
            *extra,
        ],
    )


CASES = {
    _FULL: _case(_FULL),
    _CASH: _case(_CASH),
    _NORMAL: _case(_NORMAL),
    # Quest 1 of the first Growth Pass chain: (1 << 16) | 4464.
    _GROWTH: _case(
        _GROWTH,
        TargetTest(col="packed_quest_id", value=70000, expected={"quest_chain_id": 4464, "quest_id": 1}),
    ),
}


@pytest.fixture(scope="module")
def results(request: Any) -> dict[str, HandlerResult]:
    cached = getattr(request.module, "_HANDLER_RESULTS", None)
    if cached is None:
        cached = {name: run_case(replace(case, tests=[])) for name, case in CASES.items()}
        request.module._HANDLER_RESULTS = cached
    return cached


@pytest.mark.parametrize(
    ("name", "spec"),
    [(name, spec) for name, case in CASES.items() for spec in case.tests],
    ids=lambda value: value if isinstance(value, str) else case_id(value),
)
def test_pass_lists(name: str, spec: Any, results: dict[str, HandlerResult]) -> None:
    results[name].check(spec)


def _quest_keys(result: HandlerResult) -> set[tuple[int, int]]:
    return {(record["quest_chain_id"], record["quest_id"]) for record in result.records}


def test_full_list_is_normal_plus_cash(results: dict[str, HandlerResult]) -> None:
    normal = _quest_keys(results[_NORMAL])
    cash = _quest_keys(results[_CASH])
    assert not normal & cash
    assert _quest_keys(results[_FULL]) == normal | cash


def test_each_normal_quest_has_its_pass_quest_next(results: dict[str, HandlerResult]) -> None:
    # The Black Spirit Pass quest of a pass row is the free quest's sub ID + 1.
    cash = _quest_keys(results[_CASH])
    missing = [key for key in _quest_keys(results[_NORMAL]) if (key[0], key[1] + 1) not in cash]
    assert not missing

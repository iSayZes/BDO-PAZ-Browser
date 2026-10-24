from __future__ import annotations

from dataclasses import replace
from typing import Any

import pytest

from tests.fixtures import load_binary_fixture
from tests.framework import (
    DeclaredCountTest,
    HandlerCase,
    HandlerResult,
    SchemaTest,
    case_id,
    header_count,
    run_case,
)

from _bss.instancefieldrankingmanage.parser import FILE_NAME as MANAGE_FILE
from _bss.instancefieldrankingmanage.parser import parse_instancefieldrankingmanage_records
from .parser import FILE_NAME, parse_instancefieldranking_records


# PABR magic, then the u32 record count.
_COUNT_OFFSET = 4

CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=False,
    loc_fields=[],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=["instance_field_type", "ranking_count", "ranking_idxs"]),
        DeclaredCountTest(declared=header_count(offset=_COUNT_OFFSET)),
    ],
)


@pytest.fixture(scope="module")
def ranking_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_instancefieldranking_bss(spec: Any, ranking_result: HandlerResult) -> None:
    ranking_result.check(spec)


def test_one_row_per_type_in_key_order(ranking_result: HandlerResult) -> None:
    types = [record["instance_field_type"] for record in ranking_result.records]
    assert types == list(range(len(types)))


def test_list_length_follows_its_count(ranking_result: HandlerResult) -> None:
    for record in ranking_result.records:
        assert len(record["ranking_idxs"]) == record["ranking_count"]


def test_every_ranking_key_has_a_manage_row(ranking_result: HandlerResult) -> None:
    # Checks the join to instancefieldrankingmanage.bss `ranking_idx`.
    manage = parse_instancefieldrankingmanage_records(load_binary_fixture(MANAGE_FILE))
    keys = {record["ranking_idx"] for record in manage}
    for record in ranking_result.records:
        assert set(record["ranking_idxs"]) <= keys, record


def test_bad_magic_raises() -> None:
    with pytest.raises(ValueError):
        parse_instancefieldranking_records(b"XXXX" + bytes(16))

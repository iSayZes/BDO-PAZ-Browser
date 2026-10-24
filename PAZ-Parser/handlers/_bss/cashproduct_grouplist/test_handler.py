from __future__ import annotations

import struct
from dataclasses import replace
from typing import Any

import pytest

from tests.fixtures import load_binary_fixture
from tests.framework import DeclaredCountTest, HandlerCase, HandlerResult, SchemaTest, case_id, header_count, run_case

from _dbss.cashproduct.parser import parse_cashproductoffset_records
from .parser import FILE_NAME, parse_cashproduct_grouplist_records


CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["products_text"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=["offer_group", "product_count", "product_nos", "products_text"]),
        DeclaredCountTest(declared=header_count(offset=4)),
    ],
)


@pytest.fixture(scope="module")
def grouplist_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_cashproduct_grouplist_bss(spec: Any, grouplist_result: HandlerResult) -> None:
    grouplist_result.check(spec)


def test_offer_groups_are_unique() -> None:
    groups = [r["offer_group"] for r in parse_cashproduct_grouplist_records(load_binary_fixture(FILE_NAME))]
    assert len(groups) == len(set(groups))


def test_every_listed_product_is_a_cash_product() -> None:
    products = {row["product_id"] for row in parse_cashproductoffset_records(load_binary_fixture("cashproductoffset.dbss"))}
    missing = [
        (record["offer_group"], product_no)
        for record in parse_cashproduct_grouplist_records(load_binary_fixture(FILE_NAME))
        for product_no in record["product_nos"]
        if product_no not in products
    ]
    assert not missing, missing[:10]


def test_parse_reads_the_count_before_the_group() -> None:
    body = struct.pack("<I", 1) + struct.pack("<II3I", 3, 500, 500, 501, 502)
    data = b"PABR" + body + struct.pack("<III", 0, 4 + len(body), 0)

    (record,) = parse_cashproduct_grouplist_records(data)

    assert record == {"product_count": 3, "offer_group": 500, "product_nos": [500, 501, 502]}

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
    case_id,
    run_case,
)

from .parser import (
    FILE_NAME,
    ROLE_CROSSROAD_CHOICE,
    ROLE_LATER_QUEST,
    ROLE_OPENS_CROSSROAD,
    parse_branchquest_records,
)


_HEADER_SIZE = 8
_GROUP_COUNT_OFFSET = 4
_GROUP_HEAD_SIZE = 4
_ROW_SIZE = 9
_TRAILER_SIZE = 8
# Quest 21131 / 1 `[Serendia] [Crossroad] Mine Imp Subjugation`, a choice of group 39.
_MINE_IMP_SUBJUGATION = (1 << 16) | 21131


def _declared_rows(source: CaseInput) -> int:
    """Rows from the header and the trailer alone: the bytes between the header
    and the string table, less one row count per group, in 9-byte rows."""
    raw = source.file(None)
    group_count = struct.unpack_from("<I", raw, _GROUP_COUNT_OFFSET)[0]
    (groups_end,) = struct.unpack_from("<I", raw, len(raw) - _TRAILER_SIZE)
    row_bytes = groups_end - _HEADER_SIZE - group_count * _GROUP_HEAD_SIZE
    if row_bytes < 0 or row_bytes % _ROW_SIZE:
        raise AssertionError(f"{row_bytes} row bytes are not whole {_ROW_SIZE}-byte rows")
    return row_bytes // _ROW_SIZE


CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["title"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(
            required_keys=[
                "group",
                "group_key",
                "row",
                "quest_chain_id",
                "quest_id",
                "packed_quest_id",
                "is_root_quest",
                "title",
                "role",
                "icon_path",
            ]
        ),
        DeclaredCountTest(declared=_declared_rows),
        RangeTest(col="is_root_quest", min_val=ROLE_OPENS_CROSSROAD, max_val=ROLE_LATER_QUEST),
        TargetTest(
            col="packed_quest_id",
            value=_MINE_IMP_SUBJUGATION,
            expected={
                "quest_chain_id": 21131,
                "quest_id": 1,
                "group_key": 39,
                "is_root_quest": ROLE_CROSSROAD_CHOICE,
                "role": "Crossroad choice",
            },
        ),
    ],
)


@pytest.fixture(scope="module")
def branchquest_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_branchquest_bss(spec: Any, branchquest_result: HandlerResult) -> None:
    branchquest_result.check(spec)


def test_each_group_has_one_key_of_its_own(branchquest_result: HandlerResult) -> None:
    keys_by_group: dict[int, set[int]] = {}
    for r in branchquest_result.records:
        keys_by_group.setdefault(r["group"], set()).add(r["group_key"])
    assert all(len(keys) == 1 for keys in keys_by_group.values()), keys_by_group
    group_keys = [next(iter(keys)) for keys in keys_by_group.values()]
    assert len(group_keys) == len(set(group_keys))


def _file(groups: list[list[tuple[int, int, int, int]]]) -> bytes:
    body = b"".join(
        struct.pack("<I", len(rows)) + b"".join(struct.pack("<IHHB", *row) for row in rows)
        for rows in groups
    )
    head = b"PABR" + struct.pack("<I", len(groups))
    # An empty string table, then its offset and the closing zero.
    return head + body + struct.pack("<I", 0) + struct.pack("<II", len(head) + len(body), 0)


def test_parser_reads_groups_and_rejects_a_changed_row_size() -> None:
    data = _file([[(39, 21130, 4, 0), (39, 21131, 1, 1)], [(2, 21411, 14, 2)]])
    assert parse_branchquest_records(data) == [
        {"group": 0, "group_key": 39, "row": 0, "quest_chain_id": 21130, "quest_id": 4,
         "packed_quest_id": (4 << 16) | 21130, "is_root_quest": 0},
        {"group": 0, "group_key": 39, "row": 1, "quest_chain_id": 21131, "quest_id": 1,
         "packed_quest_id": (1 << 16) | 21131, "is_root_quest": 1},
        {"group": 1, "group_key": 2, "row": 0, "quest_chain_id": 21411, "quest_id": 14,
         "packed_quest_id": (14 << 16) | 21411, "is_root_quest": 2},
    ]
    # One stray byte before the string table: the groups no longer end where it starts.
    head, rest = data[:-12], data[-12:]
    groups_end = struct.unpack_from("<I", rest, 4)[0] + 1
    with pytest.raises(ValueError):
        parse_branchquest_records(head + b"\x00" + rest[:4] + struct.pack("<II", groups_end, 0))

"""Life skill mastery tables: `fishingstatdata.bss`, `cookingstatdata.bss`,
`huntingstatdata.bss`, `alchemystatdata.bss`, `sailstatdata.bss`,
`trainingstatdata.bss`, `collectingstatdata.bss` and `manufacturingstat.bss`.

    PABR | group ... | u32 0 (empty string table)
    | u32 string_table_start | u32 0
    group = u32 count | count x row
    row = f32 mastery | fields of the file's MasteryTable (4 bytes each)

The first six files hold one group. The gathering and processing tables
hold one group per type, numbered from 0, until the string table; some
groups are empty. Full layout in docs/file-formats/masterystatdata_bss.md.
"""

from __future__ import annotations

from collections.abc import Iterator

from _common.binary import u32
from _common.pabr_strings import HEADER_SIZE, check_pabr, check_rows_end, fixed_row_offsets, string_table_start
from .spec import MasteryTable

# The u32 row count in front of each group.
_GROUP_HEADER_SIZE = 4
# The PABR magic; the first group's count follows it.
_MAGIC_SIZE = HEADER_SIZE - _GROUP_HEADER_SIZE


def _group_row_offsets(data: bytes, row_size: int, file_name: str) -> Iterator[tuple[int, int]]:
    """`(group index, row start)` for every row of a file with row groups.

    Raises ValueError on a bad magic or when the groups do not end where the
    string table starts.
    """
    check_pabr(data, file_name)
    table_start = string_table_start(data)
    pos = _MAGIC_SIZE
    group = 0
    while pos + _GROUP_HEADER_SIZE <= table_start:
        rows_start = pos + _GROUP_HEADER_SIZE
        pos = rows_start + u32(data, pos) * row_size
        if pos > table_start:
            break
        for row_start in range(rows_start, pos, row_size):
            yield group, row_start
        group += 1
    check_rows_end(data, pos, f"{file_name} row groups")


def _row_offsets(data: bytes, spec: MasteryTable) -> Iterator[tuple[int | None, int]]:
    """`(group index or None, row start)` for every row in file order."""
    if spec.sub_types is None:
        for row_start in fixed_row_offsets(data, spec.row.size, spec.file_name):
            yield None, row_start
    else:
        yield from _group_row_offsets(data, spec.row.size, spec.file_name)


def parse_mastery_records(data: bytes, spec: MasteryTable) -> list[dict]:
    """Every row in file order; rows of a grouped file carry their `sub_type`.

    Raises ValueError on a missing magic or row counts that do not end where
    the trailer says the string table starts.
    """
    row = spec.row
    records: list[dict] = []
    for sub_type, pos in _row_offsets(data, spec):
        mastery, *values = row.unpack_from(data, pos)
        group = {} if sub_type is None else {"sub_type": sub_type}
        record = {**group, "mastery": mastery, **dict(zip(spec.fields, values, strict=True))}
        if spec.derive is not None:
            record = {**record, **spec.derive(record)}
        records.append(record)
    return records

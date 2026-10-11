"""Life skill mastery tables: `fishingstatdata.bss`, `cookingstatdata.bss`,
`huntingstatdata.bss`, `alchemystatdata.bss`, `sailstatdata.bss` and
`trainingstatdata.bss`.

    PABR | u32 count | count x row | u32 0 (empty string table)
    | u32 string_table_start | u32 0
    row = f32 mastery | fields of the file's MasteryTable (4 bytes each)

Rows run from the highest mastery down to 0. Full layout in
docs/file-formats/masterystatdata_bss.md.
"""

from __future__ import annotations

from _common.pabr_strings import fixed_row_offsets
from .spec import MasteryTable


def parse_mastery_records(data: bytes, spec: MasteryTable) -> list[dict]:
    """Every row in file order.

    Raises ValueError on a missing magic or a row count that does not end
    where the trailer says the string table starts.
    """
    row = spec.row
    records: list[dict] = []
    for pos in fixed_row_offsets(data, row.size, spec.file_name):
        mastery, *values = row.unpack_from(data, pos)
        record = {"mastery": mastery, **dict(zip(spec.fields, values, strict=True))}
        if spec.derive is not None:
            record.update(spec.derive(record))
        records.append(record)
    return records

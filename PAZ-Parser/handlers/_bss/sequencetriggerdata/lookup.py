"""`sequencetriggerdata.bss` as a companion file: sequence paths by file name hash.

`sequence_skill.bss` and `sequencetutorial_equipment.bss` key their rows by
the hash of a sequence file name; this table holds the name and folder of
every sequence under that hash. Both tables sit next to it in
`gamecommondata/binary/`.
"""

from __future__ import annotations

from collections.abc import Mapping

from bdo_models import PazEntry

from .parser import FILE_NAME, parse_sequencetriggerdata_records, sequence_path


def sequence_trigger_companion(entry: PazEntry) -> str:
    """Internal path of `sequencetriggerdata.bss` for a table in the same folder."""
    folder = entry.internal_path.rsplit("/", 1)[0]
    return f"{folder}/{FILE_NAME}"


def sequence_paths_by_hash(companions: Mapping[str, bytes]) -> dict[int, str]:
    """File name hash -> `IllezraTutorial/CS_Tutorial_Illezra_00`.

    Empty when the table is missing or fits no layout the parser reads, so
    the keyed rows show no name.
    """
    data = companions.get(FILE_NAME)
    if data is None:
        return {}
    try:
        records = parse_sequencetriggerdata_records(data)
    except ValueError:
        return {}
    return {record["file_name_hash"]: sequence_path(record["folder"], record["file_name"]) for record in records}

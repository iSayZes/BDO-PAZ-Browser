"""`blackspiritchangeformcondition.bss`: the condition to change the Black Spirit's form.

    str16 change_condition

The whole file is one u64-counted UTF-16LE condition script. Layout 1 in
docs/file-formats/blackspiritchangeformcondition_bss.md.
"""

from __future__ import annotations

from _common.record_reader import RecordReader


FILE_NAME = "blackspiritchangeformcondition.bss"


def parse_blackspiritchangeformcondition_records(data: bytes) -> list[dict]:
    """The one record. Raises ValueError when the text runs past the file or does not end at its last byte."""
    reader = RecordReader(data, 0, len(data), FILE_NAME)
    record = {"change_condition": reader.text(wide=True)}
    if not reader.at_end():
        raise ValueError(f"{FILE_NAME} text ends at 0x{reader.pos:X}, the file at 0x{len(data):X}")
    return [record]
